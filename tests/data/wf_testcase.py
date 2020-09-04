import os
import json
from tempfile import mkdtemp
from os.path import join
from shutil import rmtree
from pathlib import Path

from tests.base import TestCase as BaseTestCase

SAMPLE_NAME = 'ocrd-sample-processor'
SAMPLE_OCRD_TOOL_JSON = '''{
    "executable": "ocrd-sample-processor",
    "description": "Do stuff and things",
    "categories": ["Image foobaring"],
    "steps": ["preprocessing/optimization/foobarization"],
    "input_file_grp": ["OCR-D-IMG"],
    "output_file_grp": ["OCR-D-IMG-BIN", "SECOND_OUT"],
    "parameters": {
        "param1": {
            "type": "boolean",
            "default": false,
            "description": "param1 description"
        }
    }
}'''

SAMPLE_NAME_REQUIRED_PARAM = SAMPLE_NAME + '-required-param'
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM = json.loads(SAMPLE_OCRD_TOOL_JSON)
del SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['parameters']['param1']['default']
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['executable'] = SAMPLE_NAME_REQUIRED_PARAM
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['parameters']['param1']['required'] = True
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['input_file_grp'] += ['SECOND_IN']
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM = json.dumps(SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM)
print(SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM)

SAMPLE_NAME_TOO_VERBOSE = SAMPLE_NAME + '-too-verbose'
SAMPLE_OCRD_TOOL_JSON_TOO_VERBOSE = json.loads(SAMPLE_OCRD_TOOL_JSON)
SAMPLE_OCRD_TOOL_JSON_TOO_VERBOSE['executable'] = SAMPLE_NAME_TOO_VERBOSE
SAMPLE_OCRD_TOOL_JSON_TOO_VERBOSE = json.dumps(SAMPLE_OCRD_TOOL_JSON_TOO_VERBOSE)

PARAM_JSON = '{"foo": 42}'

class TestCase(BaseTestCase):

    def tearDown(self):
        rmtree(self.tempdir)

    def setUp(self):
        self.tempdir = mkdtemp(prefix='ocrd-task-sequence-')
        self.param_fname = join(self.tempdir, 'params.json')
        with open(self.param_fname, 'w') as f:
            f.write(PARAM_JSON)

        p = Path(self.tempdir, SAMPLE_NAME)
        p.write_text("""\
#!/usr/bin/env python
print('''%s''')
        """ % SAMPLE_OCRD_TOOL_JSON)
        p.chmod(0o777)

        p = Path(self.tempdir, SAMPLE_NAME_REQUIRED_PARAM)
        p.write_text("""\
#!/usr/bin/env python
print('''%s''')
        """ % SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM)
        p.chmod(0o777)

        p = Path(self.tempdir, SAMPLE_NAME_TOO_VERBOSE)
        p.write_text("""\
#!/usr/bin/env python
print("00 HAHA I'M MESSING WITH YOUR OUTPUT")
print('''%s''')
print("11 GOOD LUCK PARSING THIS AS JSON")
        """ % SAMPLE_OCRD_TOOL_JSON_TOO_VERBOSE)
        p.chmod(0o777)

        os.environ['PATH'] = os.pathsep.join([self.tempdir, os.environ['PATH']])
        #  from distutils.spawn import find_executable as which # pylint: disable=import-error,no-name-in-module
        #  self.assertTrue(which('ocrd-sample-processor'))


