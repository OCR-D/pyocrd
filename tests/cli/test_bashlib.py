from tests.base import CapturingTestCase as TestCase, main, assets, copy_of_directory

import yaml

from ocrd.cli.bashlib import bashlib_cli

from ocrd.constants import BASHLIB_FILENAME
from ocrd_utils.constants import VERSION, MIME_TO_EXT
from ocrd_validators.constants import BAGIT_TXT
from ocrd_models.constants import TAG_MODS_IDENTIFIER, OCRD_WF_SHEBANG

class TestBashlibCli(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_filename(self):
        exit_code, out, err = self.invoke_cli(bashlib_cli, ['filename'])
        print("out=%s\berr=%s" % (out, err))
        self.assertTrue(out.endswith('ocrd/lib.bash\n'))

    def test_constants(self):
        def _test_constant(name, val):
            _, out, err = self.invoke_cli(bashlib_cli, ['constants', name])
            print("err=%s" % err)
            self.assertEqual(out, '%s\n' % val)
        _test_constant('BASHLIB_FILENAME', BASHLIB_FILENAME)
        _test_constant('VERSION', VERSION)
        _test_constant('BAGIT_TXT', BAGIT_TXT)
        _test_constant('TAG_MODS_IDENTIFIER', TAG_MODS_IDENTIFIER)
        _test_constant('OCRD_WF_SHEBANG', OCRD_WF_SHEBANG)

    def test_constants_dict(self):
        _, out, err = self.invoke_cli(bashlib_cli, ['constants', 'MIME_TO_EXT'])
        self.assertIn('[image/tiff]=.tif', out)

    def test_constants_all(self):
        _, out, err = self.invoke_cli(bashlib_cli, ['constants', '*'])
        out = yaml.safe_load(out)
        self.assertIn('VERSION', out)
        self.assertTrue(len(out) >= 40)

    def test_constants_fail(self):
        exit_code, _, err = self.invoke_cli(bashlib_cli, ['constants', '1234!@#$--'])
        self.assertEqual(exit_code, 1)
        self.assertEqual(err, "ERROR: name '1234!@#$--' is not a known constant\n")

if __name__ == "__main__":
    main(__file__)

