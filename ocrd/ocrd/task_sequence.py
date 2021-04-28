import json
import re
import sys
from shlex import split as shlex_split
from distutils.spawn import find_executable as which # pylint: disable=import-error,no-name-in-module
from subprocess import run, PIPE

# workaround venvs created for Python>=3.8
from pkg_resources import load_entry_point # pylint: disable=unused-import

from ocrd_utils import (
    getLogger,
    setOverrideLogLevel,
    parse_json_string_or_file,
    set_json_key_value_overrides
)
# from collections import Counter
from ocrd import decorators
from ocrd.processor.base import run_cli, run_api
from ocrd.resolver import Resolver
from ocrd_validators import ParameterValidator, WorkspaceValidator
from ocrd_models import ValidationReport

_processor_class = None # for exec in ProcessorTask.instantiate

class ProcessorTask():

    @classmethod
    def parse(cls, argstr):
        tokens = shlex_split(argstr)
        executable = 'ocrd-%s' % tokens.pop(0)
        input_file_grps = []
        output_file_grps = []
        parameters = {}
        while tokens:
            if tokens[0] == '-I':
                for grp in tokens[1].split(','):
                    input_file_grps.append(grp)
                tokens = tokens[2:]
            elif tokens[0] == '-O':
                for grp in tokens[1].split(','):
                    output_file_grps.append(grp)
                tokens = tokens[2:]
            elif tokens[0] == '-p':
                parameters = {**parameters, **parse_json_string_or_file(tokens[1])}
                tokens = tokens[2:]
            elif tokens[0] == '-P':
                set_json_key_value_overrides(parameters, tokens[1:3])
                tokens = tokens[3:]
            else:
                raise Exception("Failed parsing task description '%s' with tokens remaining: '%s'" % (argstr, tokens))
        return cls(executable, input_file_grps, output_file_grps, parameters)

    def __init__(self, executable, input_file_grps, output_file_grps, parameters):
        self.executable = executable
        self.input_file_grps = input_file_grps
        self.output_file_grps = output_file_grps
        self.parameters = parameters
        self._ocrd_tool_json = None
        self.instance = None # for API (instead of CLI) integration

    @property
    def ocrd_tool_json(self):
        if self._ocrd_tool_json:
            return self._ocrd_tool_json
        result = run([self.executable, '--dump-json'], stdout=PIPE, check=True, universal_newlines=True)
        self._ocrd_tool_json = json.loads(result.stdout)
        return self._ocrd_tool_json

    def validate(self):
        if not which(self.executable):
            raise Exception("Executable not found in PATH: %s" % self.executable)
        if not self.input_file_grps:
            raise Exception("Task must have input file group")
        # TODO uncomment and adapt once OCR-D/spec#121 lands
        # # make implicit input/output groups explicit by defaulting to what is
        # # provided in ocrd-tool.json
        # actual_output_grps = [*self.ocrd_tool_json['output_file_grp']]
        # for i, grp in enumerate(self.output_file_grps):
            # actual_output_grps[i] = grp
        # self.output_file_grps = actual_output_grps
        # actual_input_grps = [*self.ocrd_tool_json['input_file_grp']]
        # for i, grp in enumerate(self.input_file_grps):
            # actual_input_grps[i] = grp
        # self.input_file_grps = actual_input_grps
        param_validator = ParameterValidator(self.ocrd_tool_json)
        report = param_validator.validate(self.parameters)
        if not report.is_valid:
            raise Exception(report.errors)
        # TODO remove once OCR-D/spec#121 lands
        if 'output_file_grp' in self.ocrd_tool_json and not self.output_file_grps:
            raise Exception("Processor requires output_file_grp but none was provided.")
        return report

    def instantiate(self):
        logger = getLogger('ocrd.task_sequence.ProcessorTask')
        program = which(self.executable)
        if not program:
            logger.warning("Cannot find processor '%s' in PATH", self.executable)
            return False
        # run CLI merely to do imports and fetch class
        with open(program) as f:
            # check shebang in first line of CLI file for Python
            line = f.readline().strip()
            if not re.fullmatch('[#][!].*/python[0-9.]*', line):
                logger.info("Non-Pythonic processor '%s' breaks the chain", self.executable)
                return False
            # compile Python processor from CLI file
            try:
                code = compile(f.read(), program, 'exec')
            except (TypeError, SyntaxError, ValueError) as e:
                logger.warning("Cannot compile and instantiate processor '%s': %s",
                               self.executable, str(e))
                return False
        # temporarily monkey-patch entry point and sys.exit/sys.argv
        def ignore(anything): # pylint: disable=unused-argument
            return
        global _processor_class
        _processor_class = None
        def get_processor_class(cls, **kwargs):
            global _processor_class
            _processor_class = cls
        wrap_processor = decorators.ocrd_cli_wrap_processor
        decorators.ocrd_cli_wrap_processor = get_processor_class
        sys_exit = sys.exit
        sys.exit = ignore
        sys_argv = sys.argv
        sys.argv = [self.executable]
        # run Python processor from CLI file
        __name__ = '__main__'
        try:
            exec(code)
            logger.info("Instantiating %s for processor '%s'",
                        _processor_class.__name__, self.executable)
            # instantiate processor without workspace
            self.instance = _processor_class(None, parameter=self.parameters)
            # circumvent calling CLI to get .ocrd_tool_json
            self._ocrd_tool_json = self.instance.ocrd_tool
        except Exception as e:
            logger.warning("Cannot exec and instantiate processor '%s': %s",
                           self.executable, str(e))
        # reset modules
        sys.argv = sys_argv
        sys.exit = sys_exit
        decorators.ocrd_cli_wrap_processor = wrap_processor
        return bool(self.instance)

    def __str__(self):
        ret = '%s -I %s -O %s' % (
            self.executable.replace('ocrd-', '', 1),
            ','.join(self.input_file_grps),
            ','.join(self.output_file_grps))
        if self.parameters:
            ret += " -p '%s'" % json.dumps(self.parameters)
        return ret

def validate_tasks(tasks, workspace, page_id=None, overwrite=False):
    report = ValidationReport()
    prev_output_file_grps = workspace.mets.file_groups

    first_task = tasks[0]
    first_task.validate()

    # first task: check input/output file groups from METS
    WorkspaceValidator.check_file_grp(workspace, first_task.input_file_grps, '' if overwrite else first_task.output_file_grps, page_id, report)

    prev_output_file_grps += first_task.output_file_grps
    for task in tasks[1:]:
        task.validate()
        # check either existing fileGrp or output-file group of previous task matches current input_file_group
        for input_file_grp in task.input_file_grps:
            if not input_file_grp in prev_output_file_grps:
                report.add_error("Input file group not contained in METS or produced by previous steps: %s" % input_file_grp)
        if not overwrite:
            WorkspaceValidator.check_file_grp(workspace, [], task.output_file_grps, page_id, report)
        # TODO disable output_file_grps checks once CLI parameter 'overwrite' is implemented
        # XXX Thu Jan 16 20:14:17 CET 2020 still not sufficiently clever.
        #  if len(prev_output_file_grps) != len(set(prev_output_file_grps)):
        #      report.add_error("Output file group specified multiple times: %s" % 
        #          [grp for grp, count in Counter(prev_output_file_grps).items() if count >= 2])
        prev_output_file_grps += task.output_file_grps
    if not report.is_valid:
        raise Exception("Invalid task sequence input/output file groups: %s" % report.errors)
    return report


def parse_tasks(task_strs):
    return [ProcessorTask.parse(task_str) for task_str in task_strs]

def run_tasks(mets, log_level, page_id, tasks, overwrite=False):
    resolver = Resolver()
    workspace = resolver.workspace_from_url(mets)
    if overwrite:
        workspace.overwrite_mode = True
    log = getLogger('ocrd.task_sequence.run_tasks')
    if log_level:
        setOverrideLogLevel(log_level)

    validate_tasks(tasks, workspace, page_id, overwrite)

    # Run the tasks
    is_first = True
    last_is_instance = False
    for task in tasks:

        is_instance = bool(task.instance)
        log.info("Start processing %s task '%s'",
                 "API" if is_instance else "CLI", task)

        if (not is_first and
            not is_instance and
            last_is_instance):
            workspace.save_mets()

        if is_instance:
            # execute API
            error = run_api(
                task.instance,
                workspace,
                page_id=page_id,
                input_file_grp=','.join(task.input_file_grps),
                output_file_grp=','.join(task.output_file_grps)
            )

            if error:
                raise error
        else:
            # execute cli
            returncode = run_cli(
                task.executable,
                mets,
                resolver,
                workspace,
                log_level=log_level,
                page_id=page_id,
                overwrite=overwrite,
                input_file_grp=','.join(task.input_file_grps),
                output_file_grp=','.join(task.output_file_grps),
                parameter=json.dumps(task.parameters)
            )

            # check return code
            if returncode != 0:
                raise Exception("%s exited with non-zero return value %s." % (task.executable, returncode))

            workspace.reload_mets()

        # check output file groups are in mets
        for output_file_grp in task.output_file_grps:
            if not output_file_grp in workspace.mets.file_groups:
                raise Exception("Invalid state: expected output file group '%s' not in METS (despite processor success)" % output_file_grp)

        log.info("Finished processing task '%s'", task)

        is_first = False
        last_is_instance = is_instance

    if last_is_instance:
        workspace.save_mets()
