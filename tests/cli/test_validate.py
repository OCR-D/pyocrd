from json import loads
from os.path import join, exists
from pathlib import Path
from filecmp import dircmp
from shutil import copytree
from tempfile import TemporaryDirectory

from click.testing import CliRunner

# pylint: disable=import-error, no-name-in-module
from tests.base import TestCase, main, assets, copy_of_directory

from ocrd_utils import initLogging, pushd_popd
from ocrd.resolver import Resolver

from ocrd.cli.validate import validate_cli

OCRD_TOOL = '''
{
    "git_url": "https://github.com/ocr-d/foo",
    "version": "0.0.1",
    "tools": {
        "ocrd-xyz": {
            "executable": "ocrd-xyz",
            "description": "bars all the foos",
            "input_file_grp": ["OCR-D-FOO"],
            "output_file_grp": ["OCR-D-BAR"],
            "categories": ["Layout analysis"],
            "steps": ["layout/analysis"]
        }
    }
}
'''

class TestCli(TestCase):


    def setUp(self):
        self.resolver = Resolver()
        initLogging()
        self.runner = CliRunner()

    def test_validate_ocrd_tool(self):
        with TemporaryDirectory() as tempdir:
            json_path = Path(tempdir, 'ocrd-tool.json')
            json_path.write_text(OCRD_TOOL)

            # normal call
            result = self.runner.invoke(validate_cli, ['tool-json', str(json_path)])
            print(result.stdout)
            self.assertEqual(result.exit_code, 0)
            # relative path
            with pushd_popd(tempdir):
                result = self.runner.invoke(validate_cli, ['tool-json', 'ocrd-tool.json'])
                self.assertEqual(result.exit_code, 0)
            # default path
            with pushd_popd(tempdir):
                result = self.runner.invoke(validate_cli, ['tool-json'])
                print(result)
                print(result.stdout)
                self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    main()
