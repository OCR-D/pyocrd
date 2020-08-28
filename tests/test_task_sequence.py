import os
import json
from tempfile import mkdtemp, TemporaryDirectory
from shutil import rmtree

from pathlib import Path
from os.path import join

from tests.base import TestCase, main, assets, copy_of_directory

from ocrd_utils import pushd_popd, MIMETYPE_PAGE
from ocrd.resolver import Resolver
from ocrd_validators import OcrdWfValidator
from ocrd.task_sequence import run_tasks
from ocrd_models import OcrdWf
import ocrd_models

class OcrdWfStep(ocrd_models.OcrdWfStep):

    def validate(self):
        wf_val = OcrdWfValidator()
        report = wf_val.step_is_resolveable(self)
        if not report.is_valid:
            raise Exception(report.errors)

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

SAMPLE_NAME_REQUIRED_PARAM = 'sample-processor-required-param'
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM = json.loads(SAMPLE_OCRD_TOOL_JSON)
del SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['parameters']['param1']['default']
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['executable'] = 'ocrd-' + SAMPLE_NAME_REQUIRED_PARAM
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['parameters']['param1']['required'] = True
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM['input_file_grp'] += ['SECOND_IN']
SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM = json.dumps(SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM)

PARAM_JSON = '{"foo": 42}'

class TestTaskSequence(TestCase):

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

        p = Path(self.tempdir, 'ocrd-' + SAMPLE_NAME_REQUIRED_PARAM)
        p.write_text("""\
#!/usr/bin/env python
print('''%s''')
        """ % SAMPLE_OCRD_TOOL_JSON_REQUIRED_PARAM)
        p.chmod(0o777)

        os.environ['PATH'] = os.pathsep.join([self.tempdir, os.environ['PATH']])
        #  from distutils.spawn import find_executable as which # pylint: disable=import-error,no-name-in-module
        #  self.assertTrue(which('ocrd-sample-processor'))

    def test_parse_no_in(self):
        task = OcrdWfStep.parse('sample-processor')
        self.assertIn('must have input file group', OcrdWfValidator().step_is_consistent(task).errors[0])

    # XXX no longer an error since we're relying on ocrd-tool.json info for
    # output file groups
    # def test_parse_no_out(self):
    #     task = OcrdWfStep.parse('sample-processor -I IN')
    #     with self.assertRaisesRegex(Exception, 'Processor requires output_file_grp but none was provided.'):
    #         task.validate()
    #     # this should validate
    #     task2 = OcrdWfStep.parse('sample-processor-without-file-grp -I IN')
    #     self.assertTrue(task2.validate())

    def test_parse_implicit_after_validate(self):
        task = OcrdWfStep.parse('%s -I IN -O OUT -p \'{"param1": true}\'' % SAMPLE_NAME_REQUIRED_PARAM)
        self.assertTrue(OcrdWfValidator().step_is_resolveable(task).is_valid)
        # TODO uncomment and adapt once OCR-D/spec#121 lands
        # self.assertEqual(task.input_file_grps, ['IN', 'SECOND_IN'])
        # self.assertEqual(task.output_file_grps, ['OUT', 'SECOND_OUT'])
        self.assertEqual(task.input_file_grps, ['IN'])
        self.assertEqual(task.output_file_grps, ['OUT'])

    def test_parse_unknown(self):
        with self.assertRaisesRegex(Exception, 'Failed parsing task description'):
            OcrdWfStep.parse('sample-processor -x wrong wrong wrong')

    def test_parse_ok(self):
        task_str = 'ocrd-sample-processor -I IN -O OUT -p %s' % self.param_fname
        task = OcrdWfStep.parse(task_str)
        self.assertEqual(task.executable, 'ocrd-sample-processor')
        self.assertEqual(task.input_file_grps, ['IN'])
        self.assertEqual(task.output_file_grps, ['OUT'])
        self.assertEqual(json.dumps(task.parameters), PARAM_JSON)
        self.assertEqual(str(task), task_str.replace('-p %s' % self.param_fname, "-P foo 42"))

    def test_parse_repeated_params(self):
        task_str = 'sample-processor -I IN -O OUT -p %s -P foo 23' % self.param_fname
        task = OcrdWfStep.parse(task_str)
        self.assertEqual(task.parameters, {'foo': 23})

    def test_parse_parameter_none(self):
        task_str = 'ocrd-sample-processor -I IN -O OUT1,OUT2'
        task = OcrdWfStep.parse(task_str)
        self.assertEqual(task.parameters, {})
        self.assertEqual(str(task), task_str)

    def test_fail_validate_param(self):
        task = OcrdWfStep.parse('sample-processor -I IN -O OUT -p %s' % self.param_fname)
        report = OcrdWfValidator().step_is_resolveable(task)
        self.assertIn("Additional properties are not allowed ('foo' was unexpected)", str(report.errors))

    def test_fail_validate_executable(self):
        task = OcrdWfStep.parse('no-such-processor -I IN')
        report = OcrdWfValidator().step_is_resolveable(task)
        self.assertIn('Executable not found in ', str(report.errors))

    def test_required_param(self):
        task = OcrdWfStep.parse('%s -I IN -O OUT' % SAMPLE_NAME_REQUIRED_PARAM)
        report = OcrdWfValidator().step_is_resolveable(task)
        self.assertIn("'param1' is a required property", str(report.errors))

    def test_validate_sequence(self):
        resolver = Resolver()
        with TemporaryDirectory() as tempdir:
            workspace = resolver.workspace_from_url(assets.path_to('kant_aufklaerung_1784/data/mets.xml'), dst_dir=tempdir)
            params_path = Path(tempdir, 'params.json')
            params_path.write_text('{"param1": true}')

            with self.assertRaisesRegex(Exception, "Input file group not contained in METS or produced by previous steps: FOO'"):
                wf = OcrdWf(steps=[OcrdWfStep.parse(x) for x in [
                        '%s -I OCR-D-IMG -O OUT1 -p %s' % (SAMPLE_NAME_REQUIRED_PARAM, params_path),
                        '%s -I FOO -O OUT2 -p %s' % (SAMPLE_NAME_REQUIRED_PARAM, params_path)
                    ]])
                OcrdWfValidator().validate(wf, workspace)

            with self.assertRaisesRegex(Exception, "Input fileGrp.@USE='IN'. not in METS!"):
                wf = OcrdWf(steps=[OcrdWfStep.parse(x) for x in [
                    '%s -I IN -O OUT1 -p %s' % (SAMPLE_NAME_REQUIRED_PARAM, params_path),
                ]])
                OcrdWfValidator().validate(wf, workspace)

    def test_422(self):
        """
        # OCR-D/core#422
        """
        resolver = Resolver()
        with TemporaryDirectory() as tempdir:
            workspace = resolver.workspace_from_url(assets.path_to('kant_aufklaerung_1784/data/mets.xml'), dst_dir=tempdir)
            wf = OcrdWf([OcrdWfStep.parse(x) for x in [
                "sample-processor -I OCR-D-IMG       -O OCR-D-SEG-BLOCK",
                "sample-processor -I OCR-D-SEG-BLOCK -O OCR-D-SEG-LINE",
                "sample-processor -I OCR-D-SEG-LINE  -O OCR-D-SEG-WORD",
                "sample-processor -I OCR-D-SEG-WORD  -O OCR-D-OCR-TESS",
            ]])
            OcrdWfValidator().validate(wf, workspace)

    def test_overwrite(self):
        resolver = Resolver()
        with TemporaryDirectory() as tempdir:
            workspace = resolver.workspace_from_url(assets.path_to('kant_aufklaerung_1784/data/mets.xml'), dst_dir=tempdir)
            # should fail at step 3
            workspace.mets.add_file('OCR-D-SEG-WORD', url='foo/bar', ID='foo', pageId='page1', mimetype='image/tif')
            with self.assertRaisesRegex(Exception, r"Invalid task sequence input/output file groups: \[\"Output fileGrp\[@USE='OCR-D-SEG-WORD'\] already in METS!\"\]"):
                OcrdWfValidator().validate(OcrdWf(steps=[OcrdWfStep.parse(x) for x in [
                    "sample-processor -I OCR-D-IMG       -O OCR-D-SEG-BLOCK",
                    "sample-processor -I OCR-D-SEG-BLOCK -O OCR-D-SEG-LINE",
                    "sample-processor -I OCR-D-SEG-LINE  -O OCR-D-SEG-WORD",
                    "sample-processor -I OCR-D-SEG-WORD  -O OCR-D-OCR-TESS",
                ]]), workspace)
            # should succeed b/c overwrite
            OcrdWfValidator().validate(OcrdWf(steps=[OcrdWfStep.parse(x) for x in [
                "sample-processor -I OCR-D-IMG       -O OCR-D-SEG-BLOCK",
                "sample-processor -I OCR-D-SEG-BLOCK -O OCR-D-SEG-LINE",
                "sample-processor -I OCR-D-SEG-LINE  -O OCR-D-SEG-WORD",
                "sample-processor -I OCR-D-SEG-WORD  -O OCR-D-OCR-TESS",
            ]]), workspace, overwrite=True)

    def test_task_run(self):
        resolver = Resolver()
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784/data')) as wsdir:
            with pushd_popd(wsdir):
                ws = resolver.workspace_from_url('mets.xml')
                files_before = len(ws.mets.find_files())
                run_tasks('mets.xml', 'DEBUG', None, [
                    "dummy -I OCR-D-IMG -O GRP1",
                    "dummy -I GRP1 -O GRP2",
                ])
                ws.reload_mets()
                # step 1: 2 images in OCR-D-IMG -> 2 images 2 PAGEXML in GRP1
                # step 2: 2 images and 2 PAGEXML in GRP1 -> process just the PAGEXML
                self.assertEqual(len(ws.mets.find_files()), files_before + 6)


if __name__ == '__main__':
    main(__file__)
