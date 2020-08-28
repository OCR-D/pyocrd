import json
from shlex import split as shlex_split, quote
# only in 3.8+ :(
# from shlex import join as shlex_join
from subprocess import run, PIPE

from ocrd_utils import getLogger, parse_json_string_or_file, set_json_key_value_overrides

LOG = getLogger('ocrd.wf.step')

class OcrdWfStep():

    @classmethod
    def parse(cls, argstr):
        tokens = shlex_split(argstr)
        executable = tokens.pop(0)
        if not executable.startswith('ocrd-'):
            executable = 'ocrd-%s' % executable
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
        return OcrdWfStep(executable, input_file_grps, output_file_grps, parameters)

    def __init__(self, executable, input_file_grps, output_file_grps, parameters):
        self.executable = executable
        self.input_file_grps = input_file_grps
        self.output_file_grps = output_file_grps
        self.parameters = parameters
        self._ocrd_tool_json = None

    @property
    def ocrd_tool_json(self):
        if self._ocrd_tool_json:
            return self._ocrd_tool_json
        result = run([self.executable, '--dump-json'], stdout=PIPE, check=True, universal_newlines=True)
        self._ocrd_tool_json = json.loads(result.stdout)
        return self._ocrd_tool_json

    def __str__(self):
        ret = [self.executable]
        if self.input_file_grps:
            ret += ['-I', ','.join(self.input_file_grps)]
        if self.output_file_grps:
            ret += ['-O', ','.join(self.output_file_grps)]
        for k in self.parameters:
            ret += ['-P', k, json.dumps(self.parameters[k])]
        return ' '.join([quote(s) for s in ret])

