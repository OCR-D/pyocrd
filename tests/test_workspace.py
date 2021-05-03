from os import walk, stat, chmod, umask
from stat import filemode
from subprocess import run, PIPE
from os.path import join, exists, abspath, basename, dirname
from tempfile import TemporaryDirectory, mkdtemp
from shutil import copyfile
from pathlib import Path
from gzip import open as gzip_open

from PIL import Image

from tests.base import TestCase, assets, main, copy_of_directory

from ocrd_models.ocrd_page import parseString
from ocrd_utils import pushd_popd, initLogging, MIMETYPE_PAGE
from ocrd_modelfactory import page_from_file
from ocrd.resolver import Resolver
from ocrd.workspace import Workspace


TMP_FOLDER = '/tmp/test-core-workspace'
SRC_METS = assets.path_to('kant_aufklaerung_1784/data/mets.xml')

SAMPLE_FILE_FILEGRP = 'OCR-D-IMG'
SAMPLE_FILE_ID = 'INPUT_0017'
SAMPLE_FILE_URL = join(SAMPLE_FILE_FILEGRP, '%s.tif' % SAMPLE_FILE_ID)

def count_files():
    result = run(['find'], stdout=PIPE)
    return len(result.stdout.decode('utf-8').split('\n'))

class TestWorkspace(TestCase):

    def setUp(self):
        super().setUp()
        self.resolver = Resolver()

    def test_workspace_add_file(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            fpath = join(tempdir, 'ID1.tif')
            ws1.add_file(
                'GRP',
                ID='ID1',
                mimetype='image/tiff',
                content='CONTENT',
                pageId=None,
                local_filename=fpath
            )
            f = ws1.mets.find_all_files()[0]
            self.assertEqual(f.ID, 'ID1')
            self.assertEqual(f.mimetype, 'image/tiff')
            self.assertEqual(f.url, fpath)
            self.assertEqual(f.local_filename, fpath)
            self.assertTrue(exists(fpath))

    def test_workspace_add_file_basename_no_content(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            ws1.add_file('GRP', ID='ID1', mimetype='image/tiff', pageId=None)
            f = next(ws1.mets.find_files())
            self.assertEqual(f.url, None)

    def test_workspace_add_file_binary_content(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            fpath = join(tempdir, 'subdir', 'ID1.tif')
            ws1.add_file('GRP', ID='ID1', content=b'CONTENT', local_filename=fpath, url='http://foo/bar', pageId=None)
            self.assertTrue(exists(fpath))

    def test_workspacec_add_file_content_wo_local_filename(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            with self.assertRaisesRegex(Exception, "'content' was set but no 'local_filename'"):
                ws1.add_file('GRP', ID='ID1', content=b'CONTENT', pageId='foo1234')

    def test_workspacec_add_file_content_wo_pageid(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            with self.assertRaisesRegex(ValueError, "workspace.add_file must be passed a 'pageId' kwarg, even if it is None."):
                ws1.add_file('GRP', ID='ID1', content=b'CONTENT', local_filename='foo')

    def test_workspace_str(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            ws1.save_mets()
            ws1.reload_mets()
            self.assertEqual(str(ws1), 'Workspace[directory=%s, baseurl=None, file_groups=[], files=[]]' % tempdir)

    def test_workspace_backup(self):
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)
            ws1.automatic_backup = True
            ws1.save_mets()
            ws1.reload_mets()
            self.assertEqual(str(ws1), 'Workspace[directory=%s, baseurl=None, file_groups=[], files=[]]' % tempdir)

    def test_download_url0(self):
        with TemporaryDirectory() as directory:
            ws1 = self.resolver.workspace_from_nothing(directory)
            fn = ws1.download_url(abspath(__file__))
            self.assertEqual(fn, join('TEMP', basename(__file__)))

    def test_download_url_without_baseurl(self):
        with TemporaryDirectory() as tempdir:
            dst_mets = join(tempdir, 'mets.xml')
            copyfile(SRC_METS, dst_mets)
            ws1 = self.resolver.workspace_from_url(dst_mets)
            with self.assertRaisesRegex(Exception, "Already tried prepending baseurl '%s'" % tempdir):
                ws1.download_url(SAMPLE_FILE_URL)

    def test_download_url_with_baseurl(self):
        with TemporaryDirectory() as tempdir:
            dst_mets = join(tempdir, 'mets.xml')
            copyfile(SRC_METS, dst_mets)
            ws1 = self.resolver.workspace_from_url(dst_mets, src_baseurl=dirname(SRC_METS))
            f = Path(ws1.download_url(SAMPLE_FILE_URL))
            self.assertEqual(f, Path('TEMP', '%s.tif' % SAMPLE_FILE_ID))
            self.assertTrue(Path(ws1.directory, f).exists())

    def test_from_url_dst_dir_download(self):
        """
        https://github.com/OCR-D/core/issues/319
        """
        with TemporaryDirectory() as tempdir:
            ws_dir = join(tempdir, 'non-existing-for-good-measure')
            # Create a relative path to trigger #319
            src_path = str(Path(assets.path_to('kant_aufklaerung_1784/data/mets.xml')).relative_to(Path.cwd()))
            self.resolver.workspace_from_url(src_path, dst_dir=ws_dir, download=True)
            self.assertTrue(Path(ws_dir, 'mets.xml').exists())  # sanity check, mets.xml must exist
            self.assertTrue(Path(ws_dir, 'OCR-D-GT-PAGE/PAGE_0017_PAGE.xml').exists())

    def test_superfluous_copies_in_ws_dir(self):
        """
        https://github.com/OCR-D/core/issues/227
        """
        def find_recursive(root):
            ret = []
            for _, _, f in walk(root):
                for file in f:
                    ret.append(file)
            return ret
        with TemporaryDirectory() as wsdir:
            with open(assets.path_to('SBB0000F29300010000/data/mets_one_file.xml'), 'r') as f_in:
                with open(join(wsdir, 'mets.xml'), 'w') as f_out:
                    f_out.write(f_in.read())
            self.assertEqual(len(find_recursive(wsdir)), 1)
            ws1 = Workspace(self.resolver, wsdir)
            for file in ws1.mets.find_all_files():
                ws1.download_file(file)
            self.assertEqual(len(find_recursive(wsdir)), 2)
            self.assertTrue(exists(join(wsdir, 'OCR-D-IMG/FILE_0005_IMAGE.tif')))

    def test_remove_file_force(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            workspace = Workspace(self.resolver, directory=tempdir)
            with self.assertRaisesRegex(FileNotFoundError, "not found"):
                # should fail
                workspace.remove_file('non-existing-id')
            # should succeed
            workspace.remove_file('non-existing-id', force=True)
            # should also succeed
            workspace.overwrite_mode = True
            workspace.remove_file('non-existing-id', force=False)

    def test_remove_file_remote(self):
        with TemporaryDirectory() as tempdir:
            ws = self.resolver.workspace_from_nothing(directory=tempdir)
            ws.add_file('IMG', ID='page1_img', mimetype='image/tiff', url='http://remote', pageId=None)
            with self.assertRaisesRegex(Exception, "not locally available"):
                # should fail
                ws.remove_file('page1_img')
            # should succeed
            ws.remove_file('page1_img', force=True)
            # should also succeed
            ws.overwrite_mode = True
            ws.remove_file('page1_img', force=False)

    def test_rename_file_group(self):
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784-page-region-line-word_glyph/data')) as tempdir:
            workspace = Workspace(self.resolver, directory=tempdir)
            with pushd_popd(tempdir):
                pcgts_before = page_from_file(next(workspace.mets.find_files(ID='OCR-D-GT-SEG-WORD_0001')))
                assert pcgts_before.get_Page().imageFilename == 'OCR-D-IMG/OCR-D-IMG_0001.tif'
                # from os import system
                # print(system('find'))
                workspace.rename_file_group('OCR-D-IMG', 'FOOBAR')
                # print(system('find'))
                pcgts_after = page_from_file(next(workspace.mets.find_files(ID='OCR-D-GT-SEG-WORD_0001')))
                assert pcgts_after.get_Page().imageFilename == 'FOOBAR/OCR-D-IMG_0001.tif'
                assert Path('FOOBAR/OCR-D-IMG_0001.tif').exists()
                assert not Path('OCR-D-IMG/OCR-D-IMG_0001.tif').exists()

    def test_remove_file_group_force(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            workspace = Workspace(self.resolver, directory=tempdir)
            with self.assertRaisesRegex(Exception, "No such fileGrp"):
                # should fail
                workspace.remove_file_group('I DO NOT EXIST')
            # should succeed
            workspace.remove_file_group('I DO NOT EXIST', force=True)
            # should also succeed
            workspace.overwrite_mode = True
            workspace.remove_file_group('I DO NOT EXIST', force=False)

    def test_remove_file_group_rmdir(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            workspace = Workspace(self.resolver, directory=tempdir)
            self.assertTrue(exists(join(tempdir, 'OCR-D-IMG')))
            workspace.remove_file_group('OCR-D-IMG', recursive=True)
            self.assertFalse(exists(join(tempdir, 'OCR-D-IMG')))

    def test_remove_file_page_recursive(self):
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784-complex/data')) as tempdir:
            with pushd_popd(tempdir):
                ws = Workspace(self.resolver, directory=tempdir)
                self.assertEqual(len(ws.mets.find_all_files()), 119)
                ws.remove_file('OCR-D-OCR-OCRO-fraktur-SEG-LINE-tesseract-ocropy-DEWARP_0001', page_recursive=True, page_same_group=False, keep_file=True)
                self.assertEqual(len(ws.mets.find_all_files()), 83)
                ws.remove_file('PAGE_0017_ALTO', page_recursive=True)

    def test_remove_file_page_recursive_keep_file(self):
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784-complex/data')) as tempdir:
            with pushd_popd(tempdir):
                ws = Workspace(self.resolver, directory=tempdir)
                before = count_files()
                ws.remove_file('OCR-D-IMG-BINPAGE-sauvola_0001', page_recursive=True, page_same_group=False, force=True)
                after = count_files()
                self.assertEqual(after, before - 2, '2 files deleted')

    def test_remove_file_page_recursive_same_group(self):
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784-complex/data')) as tempdir:
            with pushd_popd(tempdir):
                ws = Workspace(self.resolver, directory=tempdir)
                before = count_files()
                ws.remove_file('OCR-D-IMG-BINPAGE-sauvola_0001', page_recursive=True, page_same_group=True, force=False)
                after = count_files()
                self.assertEqual(after, before - 1, '2 file deleted')

    def test_download_to_directory_from_workspace_download_file(self):
        """
        https://github.com/OCR-D/core/issues/342
        """
        #  tempdir = mkdtemp()
        with TemporaryDirectory() as tempdir:
            ws1 = self.resolver.workspace_from_nothing(directory=tempdir)

            f1 = ws1.add_file('IMG', ID='page1_img', mimetype='image/tiff', local_filename='test.tif', content='', pageId=None)
            f2 = ws1.add_file('GT', ID='page1_gt', mimetype='text/xml', local_filename='test.xml', content='', pageId=None)

            self.assertEqual(f1.url, 'test.tif')
            self.assertEqual(f2.url, 'test.xml')

            # these should be no-ops
            ws1.download_file(f1)
            ws1.download_file(f2)

            self.assertEqual(f1.url, 'test.tif')
            self.assertEqual(f2.url, 'test.xml')

    def test_save_image_file(self):
        img = Image.new('RGB', (1000, 1000))
        with TemporaryDirectory() as tempdir:
            ws = self.resolver.workspace_from_nothing(directory=tempdir)
            with self.assertRaisesRegex(KeyError, ''):
                ws.save_image_file(img, 'page1_img', 'IMG', 'page1', 'ceci/nest/pas/une/mimetype')
            ws.save_image_file(img, 'page1_img', 'IMG', 'page1', 'image/jpeg')
            self.assertTrue(exists(join(tempdir, 'IMG', 'page1_img.jpg')))
            # should succeed
            ws.save_image_file(img, 'page1_img', 'IMG', 'page1', 'image/jpeg', force=True)
            # should also succeed
            ws.overwrite_mode = True
            ws.save_image_file(img, 'page1_img', 'IMG', 'page1', 'image/jpeg')

    def test_resolve_image_exif(self):
        with pushd_popd(assets.path_to('kant_aufklaerung_1784/data/')):
            ws = self.resolver.workspace_from_url('mets.xml')
            exif = ws.resolve_image_exif('OCR-D-IMG/INPUT_0017.tif')
            self.assertEqual(exif.compression, 'jpeg')
            self.assertEqual(exif.width, 1457)

    def test_resolve_image_as_pil(self):
        with pushd_popd(assets.path_to('kant_aufklaerung_1784/data/')):
            ws = self.resolver.workspace_from_url('mets.xml')
            img = ws.resolve_image_as_pil('OCR-D-IMG/INPUT_0017.tif')
            self.assertEqual(img.width, 1457)
            img = ws.resolve_image_as_pil('OCR-D-IMG/INPUT_0017.tif', coords=([100, 100], [50, 50]))
            self.assertEqual(img.width, 50)

    def test_image_from_page_basic(self):
        with pushd_popd(assets.path_to('gutachten/data')):
            ws = self.resolver.workspace_from_url('mets.xml')
            with open('TEMP1/PAGE_TEMP1.xml', 'r') as f:
                pcgts = parseString(f.read().encode('utf8'), silence=True)
            img, info, exif = ws.image_from_page(pcgts.get_Page(), page_id='PHYS_0017', feature_selector='clipped', feature_filter='cropped')
            self.assertEquals(info['features'], 'binarized,clipped')
            img, info, exif = ws.image_from_page(pcgts.get_Page(), page_id='PHYS_0017')
            self.assertEquals(info['features'], 'binarized,clipped')

    def test_image_feature_selectoro(self):
        with pushd_popd('tests/data/sample-features'):
            ws = self.resolver.workspace_from_url('mets.xml')
            with open('image_features.page.xml', 'r') as f:
                pcgts = parseString(f.read().encode('utf8'), silence=True)
            # richest feature set is not last:
            img, info, exif = ws.image_from_page(pcgts.get_Page(), page_id='page1', feature_selector='dewarped')
            # recropped because foo4 contains cropped+deskewed but not recropped yet:
            self.assertEquals(info['features'], 'cropped,dewarped,binarized,despeckled,deskewed,recropped')
            # richest feature set is also last:
            img, info, exif = ws.image_from_page(pcgts.get_Page(), page_id='page1', feature_selector='dewarped', feature_filter='binarized')
            # no deskewing here, thus no recropping:
            self.assertEquals(info['features'], 'cropped,dewarped,despeckled')

    def test_downsample_16bit_image(self):
        with pushd_popd(tempdir=True) as tempdir:
            with gzip_open(join(dirname(__file__), 'data/OCR-D-IMG_APBB_Mitteilungen_62.0002.tif.gz'), 'rb') as gzip_in:
                with open('16bit.tif', 'wb') as tif_out:
                    tif_out.write(gzip_in.read())
            ws = self.resolver.workspace_from_nothing(directory=tempdir)
            ws.add_file('IMG', ID='foo', url='16bit.tif', mimetype='image/tiff', pageId=None)
            pil_before = Image.open('16bit.tif')
            assert pil_before.mode == 'I;16'
            pil_after = ws._resolve_image_as_pil('16bit.tif')
            assert pil_after.mode == 'L'

    def test_mets_permissions(self):
        with TemporaryDirectory() as tempdir:
            ws = self.resolver.workspace_from_nothing(tempdir)
            ws.save_mets()
            mets_path = join(ws.directory, 'mets.xml')
            mask = umask(0)
            umask(mask)
            assert (stat(mets_path).st_mode) == 0o100664 & ~mask
            chmod(mets_path, 0o777)
            ws.save_mets()
            assert filemode(stat(mets_path).st_mode) == '-rwxrwxrwx'

    def test_merge(self):
        with copy_of_directory(assets.path_to('kant_aufklaerung_1784/data')) as ws1dir, \
            copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as ws2dir:
            ws1 = Workspace(self.resolver, ws1dir)
            ws2 = Workspace(self.resolver, ws2dir)
            assert len(ws1.mets.find_all_files()) == 6
            ws1.merge(ws2)
            assert len(ws1.mets.find_all_files()) == 41
            assert exists(join(ws1dir, 'OCR-D-IMG/FILE_0001_IMAGE.tif'))


if __name__ == '__main__':
    main(__file__)
