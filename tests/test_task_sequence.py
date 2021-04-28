import json
from tempfile import TemporaryDirectory
from pathlib import Path

from tests.base import main, assets, copy_of_directory
from tests.data.wf_testcase import (
    TestCase,

    SAMPLE_NAME_REQUIRED_PARAM,
    PARAM_JSON,
)

from ocrd_utils import pushd_popd, MIMETYPE_PAGE
from ocrd.resolver import Resolver
from ocrd.task_sequence import parse_tasks, run_tasks, validate_tasks, ProcessorTask

class TestOcrdWfStep(TestCase):

    def test_parse_no_in(self):
        task = ProcessorTask.parse('sample-processor')
        with self.assertRaisesRegex(Exception, 'must have input file group'):
            task.validate()

    # XXX no longer an error since we're relying on ocrd-tool.json info for
    # output file groups
    # def test_parse_no_out(self):
    #     task = ProcessorTask.parse('sample-processor -I IN')
    #     with self.assertRaisesRegex(Exception, 'Processor requires output_file_grp but none was provided.'):
    #         task.validate()
    #     # this should validate
    #     task2 = ProcessorTask.parse('sample-processor-without-file-grp -I IN')
    #     self.assertTrue(task2.validate())

    def test_parse_implicit_after_validate(self):
        task = ProcessorTask.parse('%s -I IN -O OUT -p \'{"param1": true}\'' % SAMPLE_NAME_REQUIRED_PARAM)
        task.validate()
        # TODO uncomment and adapt once OCR-D/spec#121 lands
        # self.assertEqual(task.input_file_grps, ['IN', 'SECOND_IN'])
        # self.assertEqual(task.output_file_grps, ['OUT', 'SECOND_OUT'])
        self.assertEqual(task.input_file_grps, ['IN'])
        self.assertEqual(task.output_file_grps, ['OUT'])

    def test_parse_unknown(self):
        with self.assertRaisesRegex(Exception, 'Failed parsing task description'):
            ProcessorTask.parse('sample-processor -x wrong wrong wrong')

    def test_parse_ok(self):
        task_str = 'sample-processor -I IN -O OUT -p %s' % self.param_fname
        task = ProcessorTask.parse(task_str)
        self.assertEqual(task.executable, 'ocrd-sample-processor')
        self.assertEqual(task.input_file_grps, ['IN'])
        self.assertEqual(task.output_file_grps, ['OUT'])
        self.assertEqual(json.dumps(task.parameters), PARAM_JSON)
        self.assertEqual(str(task), task_str.replace(self.param_fname, "'%s'" % PARAM_JSON))

    def test_parse_repeated_params(self):
        task_str = 'sample-processor -I IN -O OUT -p %s -P foo 23' % self.param_fname
        task = ProcessorTask.parse(task_str)
        self.assertEqual(task.parameters, {'foo': 23})

    def test_parse_parameter_none(self):
        task_str = 'sample-processor -I IN -O OUT1,OUT2'
        task = ProcessorTask.parse(task_str)
        self.assertEqual(task.parameters, {})
        self.assertEqual(str(task), task_str)

    def test_fail_validate_param(self):
        task = ProcessorTask.parse('sample-processor -I IN -O OUT -p %s' % self.param_fname)
        with self.assertRaisesRegex(Exception, r"Additional properties are not allowed \('foo' was unexpected\)"):
            task.validate()

    def test_fail_validate_executable(self):
        task = ProcessorTask.parse('no-such-processor -I IN')
        with self.assertRaisesRegex(Exception, 'Executable not found in '):
            task.validate()

    def test_required_param(self):
        task = ProcessorTask.parse('%s -I IN -O OUT' % SAMPLE_NAME_REQUIRED_PARAM)
        with self.assertRaisesRegex(Exception, "'param1' is a required property"):
            task.validate()

    def test_validate_sequence(self):
        resolver = Resolver()
        with TemporaryDirectory() as tempdir:
            workspace = resolver.workspace_from_url(assets.path_to('kant_aufklaerung_1784/data/mets.xml'), dst_dir=tempdir)
            params_path = Path(tempdir, 'params.json')
            params_path.write_text('{"param1": true}')

            with self.assertRaisesRegex(Exception, "Input file group not contained in METS or produced by previous steps: FOO'"):
                validate_tasks([ProcessorTask.parse(x) for x in [
                    '%s -I OCR-D-IMG -O OUT1 -p %s' % (SAMPLE_NAME_REQUIRED_PARAM, params_path),
                    '%s -I FOO -O OUT2 -p %s' % (SAMPLE_NAME_REQUIRED_PARAM, params_path)
                ]], workspace)

            with self.assertRaisesRegex(Exception, "Input fileGrp.@USE='IN'. not in METS!"):
                validate_tasks([ProcessorTask.parse(x) for x in [
                    '%s -I IN -O OUT1 -p %s' % (SAMPLE_NAME_REQUIRED_PARAM, params_path),
                ]], workspace)

    def test_422(self):
        """
        # OCR-D/core#422
        """
        resolver = Resolver()
        with TemporaryDirectory() as tempdir:
            workspace = resolver.workspace_from_url(assets.path_to('kant_aufklaerung_1784/data/mets.xml'), dst_dir=tempdir)
            validate_tasks([ProcessorTask.parse(x) for x in [
                "sample-processor -I OCR-D-IMG       -O OCR-D-SEG-BLOCK",
                "sample-processor -I OCR-D-SEG-BLOCK -O OCR-D-SEG-LINE",
                "sample-processor -I OCR-D-SEG-LINE  -O OCR-D-SEG-WORD",
                "sample-processor -I OCR-D-SEG-WORD  -O OCR-D-OCR-TESS",
            ]], workspace)

    def test_overwrite(self):
        resolver = Resolver()
        with TemporaryDirectory() as tempdir:
            workspace = resolver.workspace_from_url(assets.path_to('kant_aufklaerung_1784/data/mets.xml'), dst_dir=tempdir)
            # should fail at step 3
            workspace.mets.add_file('OCR-D-SEG-WORD', url='foo/bar', ID='foo', pageId='page1', mimetype='image/tif')
            with self.assertRaisesRegex(Exception, r"Invalid task sequence input/output file groups: \[\"Output fileGrp\[@USE='OCR-D-SEG-WORD'\] already in METS!\"\]"):
                validate_tasks([ProcessorTask.parse(x) for x in [
                    "sample-processor -I OCR-D-IMG       -O OCR-D-SEG-BLOCK",
                    "sample-processor -I OCR-D-SEG-BLOCK -O OCR-D-SEG-LINE",
                    "sample-processor -I OCR-D-SEG-LINE  -O OCR-D-SEG-WORD",
                    "sample-processor -I OCR-D-SEG-WORD  -O OCR-D-OCR-TESS",
                ]], workspace)
            # should succeed b/c overwrite
            validate_tasks([ProcessorTask.parse(x) for x in [
                "sample-processor -I OCR-D-IMG       -O OCR-D-SEG-BLOCK",
                "sample-processor -I OCR-D-SEG-BLOCK -O OCR-D-SEG-LINE",
                "sample-processor -I OCR-D-SEG-LINE  -O OCR-D-SEG-WORD",
                "sample-processor -I OCR-D-SEG-WORD  -O OCR-D-OCR-TESS",
            ]], workspace, overwrite=True)


    def test_task_run(self):
        resolver = Resolver()
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784/data')) as wsdir:
            with pushd_popd(wsdir):
                ws = resolver.workspace_from_url('mets.xml')
                ws.add_file('GRP0', content='', local_filename='GRP0/foo', ID='file0', mimetype=MIMETYPE_PAGE, pageId=None)
                ws.save_mets()
                files_before = len(ws.mets.find_all_files())
                tasks = parse_tasks([
                    "dummy -I OCR-D-IMG -O GRP1",
                    "dummy -I GRP1 -O GRP2",
                ])
                run_tasks('mets.xml', 'DEBUG', None, tasks)
                ws.reload_mets()
                # step 1: 2 images in OCR-D-IMG -> 2 images 2 PAGEXML in GRP1
                # step 2: 2 images and 2 PAGEXML in GRP1 -> process just the PAGEXML
                self.assertEqual(len(ws.mets.find_all_files()), files_before + 6)


if __name__ == '__main__':
    main(__file__)
