"""
Helper methods for running and documenting processors
"""
from time import perf_counter, process_time
import json
import inspect
from subprocess import run, PIPE
from memory_profiler import memory_usage
from sparklines import sparklines

from click import wrap_text
from ocrd_utils import getLogger

__all__ = [
    'generate_processor_help',
    'run_cli',
    'run_processor'
]

def _get_workspace(workspace=None, resolver=None, mets_url=None, working_dir=None):
    if workspace is None:
        if resolver is None:
            raise Exception("Need to pass a resolver to create a workspace")
        if mets_url is None:
            raise Exception("Need to pass mets_url to create a workspace")
        workspace = resolver.workspace_from_url(mets_url, dst_dir=working_dir)
    return workspace

def run_processor(
        processorClass,
        ocrd_tool=None,
        mets_url=None,
        resolver=None,
        workspace=None,
        page_id=None,
        log_level=None,         # TODO actually use this!
        input_file_grp=None,
        output_file_grp=None,
        show_resource=None,
        list_resources=False,
        parameter=None,
        parameter_override=None,
        working_dir=None,
): # pylint: disable=too-many-locals
    """
    Create a workspace for mets_url and run processor through it

    Args:
        parameter (string): URL to the parameter
    """
    workspace = _get_workspace(
        workspace,
        resolver,
        mets_url,
        working_dir
    )
    log = getLogger('ocrd.processor.helpers.run_processor')
    log.debug("Running processor %s", processorClass)
    processor = processorClass(
        workspace,
        ocrd_tool=ocrd_tool,
        page_id=page_id,
        input_file_grp=input_file_grp,
        output_file_grp=output_file_grp,
        parameter=parameter
    )
    ocrd_tool = processor.ocrd_tool
    name = '%s v%s' % (ocrd_tool['executable'], processor.version)
    otherrole = ocrd_tool['steps'][0]
    logProfile = getLogger('ocrd.process.profile')
    log.debug("Processor instance %s (%s doing %s)", processor, name, otherrole)
    t0_wall = perf_counter()
    t0_cpu = process_time()
    mem_usage = memory_usage(proc=processor.process, interval=.1, timeout=None, timestamps=True, multiprocess=True, include_children=True)
    mem_usage_values = [mem for mem, _ in mem_usage]
    mem_output = 'memory consumption: '
    mem_output += ''.join(sparklines(mem_usage_values))
    mem_output += ' max: %.2f MiB min: %.2f MiB' % (max(mem_usage_values), min(mem_usage_values))
    logProfile.info(mem_output)
    t1_wall = perf_counter() - t0_wall
    t1_cpu = process_time() - t0_cpu
    logProfile.info("Executing processor '%s' took %fs (wall) %fs (CPU)( [--input-file-grp='%s' --output-file-grp='%s' --parameter='%s']" % (
        ocrd_tool['executable'],
        t1_wall,
        t1_cpu,
        input_file_grp if input_file_grp else '',
        output_file_grp if output_file_grp else '',
        json.dumps(parameter) if parameter else {}
    ))
    workspace.mets.add_agent(
        name=name,
        _type='OTHER',
        othertype='SOFTWARE',
        role='OTHER',
        otherrole=otherrole
    )
    workspace.save_mets()
    return processor

def run_cli(
        executable,
        mets_url=None,
        resolver=None,
        workspace=None,
        page_id=None,
        overwrite=None,
        log_level=None,
        input_file_grp=None,
        output_file_grp=None,
        parameter=None,
        working_dir=None,
):
    """
    Create a workspace for mets_url and run MP CLI through it
    """
    workspace = _get_workspace(workspace, resolver, mets_url, working_dir)
    args = [executable, '--working-dir', workspace.directory]
    args += ['--mets', mets_url]
    if log_level:
        args += ['--log-level', log_level]
    if page_id:
        args += ['--page-id', page_id]
    if input_file_grp:
        args += ['--input-file-grp', input_file_grp]
    if output_file_grp:
        args += ['--output-file-grp', output_file_grp]
    if parameter:
        args += ['--parameter', parameter]
    if overwrite:
        args += ['--overwrite']
    log = getLogger('ocrd.processor.helpers.run_cli')
    log.debug("Running subprocess '%s'", ' '.join(args))
    result = run(args, check=False)
    return result.returncode

def generate_processor_help(ocrd_tool, processor_instance=None):
    """Generate a string describing the full CLI of this processor including params.
    
    Args:
         ocrd_tool (dict): this processor's ``tools`` section of the module's ``ocrd-tool.json``
         processor_instance (object, optional): the processor implementation
             (for adding any module/class/function docstrings)
    """
    parameter_help = ''
    if 'parameters' not in ocrd_tool or not ocrd_tool['parameters']:
        parameter_help = '  NONE\n'
    else:
        def wrap(s):
            return wrap_text(s, initial_indent=' '*3,
                             subsequent_indent=' '*4,
                             width=72, preserve_paragraphs=True)
        for param_name, param in ocrd_tool['parameters'].items():
            parameter_help += wrap('"%s" [%s%s]' % (
                param_name,
                param['type'],
                ' - REQUIRED' if 'required' in param and param['required'] else
                ' - %s' % json.dumps(param['default']) if 'default' in param else ''))
            parameter_help += '\n ' + wrap(param['description'])
            if 'enum' in param:
                parameter_help += '\n ' + wrap('Possible values: %s' % json.dumps(param['enum']))
            parameter_help += "\n"
    doc_help = ''
    if processor_instance:
        module = inspect.getmodule(processor_instance)
        if module and module.__doc__:
            doc_help += '\n' + inspect.cleandoc(module.__doc__)
        if processor_instance.__doc__:
            doc_help += '\n' + inspect.cleandoc(processor_instance.__doc__)
        if processor_instance.process.__doc__:
            doc_help += '\n' + inspect.cleandoc(processor_instance.process.__doc__)
        if doc_help:
            doc_help = '\n\n' + wrap_text(doc_help, width=72,
                                          initial_indent='  > ',
                                          subsequent_indent='  > ',
                                          preserve_paragraphs=True)
    return '''
Usage: %s [OPTIONS]

  %s%s

Options:
  -I, --input-file-grp USE        File group(s) used as input
  -O, --output-file-grp USE       File group(s) used as output
  -g, --page-id ID                Physical page ID(s) to process
  --overwrite                     Remove existing output pages/images
                                  (with --page-id, remove only those)
  -p, --parameter JSON-PATH       Parameters, either verbatim JSON string
                                  or JSON file path
  -P, --param-override KEY VAL    Override a single JSON object key-value pair,
                                  taking precedence over --parameter
  -m, --mets URL-PATH             URL or file path of METS to process
  -w, --working-dir PATH          Working directory of local workspace
  -l, --log-level [OFF|ERROR|WARN|INFO|DEBUG|TRACE]
                                  Log level
  -C, --show-resource RESNAME     Dump the content of processor resource RESNAME
  -L, --list-resources            List names of processor resources
  -J, --dump-json                 Dump tool description as JSON and exit
  -h, --help                      This help message
  -V, --version                   Show version

Parameters:
%s
Default Wiring:
  %s -> %s

''' % (
    ocrd_tool['executable'],
    ocrd_tool['description'],
    doc_help,
    parameter_help,
    ocrd_tool.get('input_file_grp', 'NONE'),
    ocrd_tool.get('output_file_grp', 'NONE')
)
