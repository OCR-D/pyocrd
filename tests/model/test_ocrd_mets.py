from datetime import datetime
from os.path import join
from tests.base import TestCase, main, assets, copy_of_directory

from ocrd_utils import (
    initLogging,
    VERSION,
    MIMETYPE_PAGE
)
from ocrd_models import OcrdMets

# pylint: disable=protected-access,deprecated-method,too-many-public-methods
class TestOcrdMets(TestCase):

    def setUp(self):
        self.mets = OcrdMets(filename=assets.url_of('SBB0000F29300010000/data/mets.xml'))
        initLogging()

    def test_unique_identifier(self):
        self.assertEqual(self.mets.unique_identifier, 'http://resolver.staatsbibliothek-berlin.de/SBB0000F29300010000', 'Right identifier')
        self.mets.unique_identifier = 'foo'
        self.assertEqual(self.mets.unique_identifier, 'foo', 'Right identifier after change')

    # pylint: disable=no-member
    def test_unique_identifier_from_nothing(self):
        mets = OcrdMets.empty_mets(datetime.now().isoformat())
        self.assertEqual(mets.unique_identifier, None, 'no identifier')
        mets.unique_identifier = 'foo'
        self.assertEqual(mets.unique_identifier, 'foo', 'Right identifier after change')
        as_string = mets.to_xml().decode('utf-8')
        self.assertIn('ocrd/core v%s' % VERSION, as_string)
        self.assertIn('CREATEDATE="%04u-%02u-%02uT' % (
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
        ), as_string)

    def test_str(self):
        mets = OcrdMets(content='<mets/>')
        self.assertEqual(str(mets), 'OcrdMets[fileGrps=[],files=[]]')

    #  def test_override_constructor_args(self):
    #      id2file = {'foo': {}}
    #      mets = OcrdMets(id2file, content='<mets/>')
    #      self.assertEqual(mets._file_by_id, id2file)

    def test_file_groups(self):
        self.assertEqual(len(self.mets.file_groups), 17, '17 file groups')

    def test_find_files_basic(self):
        self.assertEqual(len(self.mets.find_files()), 35, '35 files total')
        self.assertEqual(len(self.mets.find_files(fileGrp='OCR-D-IMG')), 3, '3 files in "OCR-D-IMG"')
        self.assertEqual(len(self.mets.find_files(fileGrp='//OCR-D-I.*')), 13, '13 files in "//OCR-D-I.*"')
        self.assertEqual(len(self.mets.find_files(ID="FILE_0001_IMAGE")), 1, '1 files with ID "FILE_0001_IMAGE"')
        self.assertEqual(len(self.mets.find_files(ID="//FILE_0005_.*")), 1, '1 files with ID "//FILE_0005_.*"')
        self.assertEqual(len(self.mets.find_files(mimetype='image/tiff')), 13, '13 image/tiff')
        self.assertEqual(len(self.mets.find_files(mimetype='//application/.*')), 22, '22 application/.*')
        self.assertEqual(len(self.mets.find_files(mimetype=MIMETYPE_PAGE)), 20, '20 ' + MIMETYPE_PAGE)
        self.assertEqual(len(self.mets.find_files(url='OCR-D-IMG/FILE_0005_IMAGE.tif')), 1, '1 xlink:href="OCR-D-IMG/FILE_0005_IMAGE.tif"')

    def test_find_files_pageid(self):
        self.assertEqual(len(self.mets.find_files(pageId='PHYS_0001')), 17, '17 files for page "PHYS_0001"')

    def test_find_files_pageid_notexist(self):
        self.assertEqual(len(self.mets.find_files(pageId='PHYS_0001-NOTEXIST')), 0, '0 pages for "PHYS_0001-NOTEXIST"')

    def test_find_files_no_regex_for_pageid(self):
        with self.assertRaisesRegex(Exception, "not support regex search for pageId"):
            self.mets.find_files(pageId='//foo')

    def test_find_files_local_only(self):
        self.assertEqual(len(self.mets.find_files(pageId='PHYS_0001', local_only=True)), 3, '3 local files for page "PHYS_0001"')

    def test_physical_pages(self):
        self.assertEqual(len(self.mets.physical_pages), 3, '3 physical pages')

    def test_physical_pages_from_empty_mets(self):
        mets = OcrdMets(content="<mets></mets>")
        self.assertEqual(len(mets.physical_pages), 0, 'no physical page')
        mets.add_file('OUTPUT', ID="foo123", pageId="foobar")
        self.assertEqual(len(mets.physical_pages), 1, '1 physical page')

    def test_physical_pages_for_fileids(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(mets.get_physical_pages(for_fileIds=['FILE_0002_IMAGE']), ['PHYS_0002'])

    def test_add_group(self):
        mets = OcrdMets.empty_mets()
        self.assertEqual(len(mets.file_groups), 0, '0 file groups')
        mets.add_file_group('TEST')
        self.assertEqual(len(mets.file_groups), 1, '1 file groups')
        mets.add_file_group('TEST')
        self.assertEqual(len(mets.file_groups), 1, '1 file groups')

    def test_add_file(self):
        mets = OcrdMets.empty_mets()
        self.assertEqual(len(mets.file_groups), 0, '0 file groups')
        self.assertEqual(len(mets.find_files(fileGrp='OUTPUT')), 0, '0 files in "OUTPUT"')
        f = mets.add_file('OUTPUT', ID="foo123", mimetype="bla/quux", pageId="foobar")
        f2 = mets.add_file('OUTPUT', ID="foo1232", mimetype="bla/quux", pageId="foobar")
        self.assertEqual(f.pageId, 'foobar', 'pageId set')
        self.assertEqual(len(mets.file_groups), 1, '1 file groups')
        self.assertEqual(len(mets.find_files(fileGrp='OUTPUT')), 2, '2 files in "OUTPUT"')
        mets.set_physical_page_for_file('barfoo', f, order='300', orderlabel="page 300")
        self.assertEqual(f.pageId, 'barfoo', 'pageId changed')
        mets.set_physical_page_for_file('quux', f2, order='302', orderlabel="page 302")
        self.assertEqual(f2.pageId, 'quux', 'pageId changed')
        mets.set_physical_page_for_file('barfoo', f2, order='301', orderlabel="page 301")
        self.assertEqual(f2.pageId, 'barfoo', 'pageId changed')
        self.assertEqual(len(mets.file_groups), 1, '1 file group')

    def test_add_file_ID_already_exists(self):
        f = self.mets.add_file('OUTPUT', ID='best-id-ever', mimetype="beep/boop")
        self.assertEqual(f.ID, 'best-id-ever', "ID kept")
        with self.assertRaisesRegex(Exception, "File with ID='best-id-ever' already exists"):
            self.mets.add_file('OUTPUT', ID='best-id-ever', mimetype="boop/beep")
        f2 = self.mets.add_file('OUTPUT', ID='best-id-ever', mimetype="boop/beep", force=True)
        self.assertEqual(f._el, f2._el)

    def test_add_file_ignore(self):
        self.mets.add_file('OUTPUT', ID='best-id-ever', mimetype="beep/boop")
        self.mets.add_file('OUTPUT', ID='best-id-ever', mimetype="boop/beep", ignore=True)

    def test_add_file_ID_invalid(self):
        with self.assertRaisesRegex(Exception, "Invalid syntax for mets:file/@ID 1234:::"):
            self.mets.add_file('OUTPUT', ID='1234:::', mimetype="beep/boop")

    def test_filegrp_from_file(self):
        f = self.mets.find_files(fileGrp='OCR-D-IMG')[0]
        self.assertEqual(f.fileGrp, 'OCR-D-IMG')

    def test_add_file_no_id(self):
        with self.assertRaisesRegex(Exception, "Must set ID of the mets:file"):
            self.mets.add_file('FOO')

    def test_add_file_no_pageid(self):
        f = self.mets.add_file('OUTPUT', mimetype="bla/quux", ID="foo3")
        self.assertEqual(f.pageId, None, 'No pageId')

    def test_file_pageid(self):
        f = self.mets.find_files()[0]
        self.assertEqual(f.pageId, 'PHYS_0001')
        f.pageId = 'foo'
        self.assertEqual(f.pageId, 'foo')

    def test_agent(self):
        #  Processor(workspace=self.workspace)
        mets = self.mets
        beforelen = len(mets.agents)
        mets.add_agent('foo bar v0.0.1', 'OTHER', 'OTHER', 'YETOTHERSTILL')
        #  print(['%s'%x for x in mets.agents])
        self.assertEqual(len(mets.agents), beforelen + 1)

    def test_metshdr(self):
        """
        Test whether metsHdr is created on-demand
        """
        mets = OcrdMets(content="<mets></mets>")
        self.assertFalse(mets._tree.getroot().getchildren())
        mets.add_agent()
        self.assertEqual(len(mets._tree.getroot().getchildren()), 1)

    def test_nocontent_nofilename(self):
        with self.assertRaisesRegex(Exception, "Must pass 'filename' or 'content' to"):
            OcrdMets()

    def test_encoding_entities(self):
        mets = OcrdMets(content="""
        <mets>
          <metsHdr>
            <agent>
              <name>Őh śéé Áŕ</name>
              <note>OCR-D</note>
            </agent>
          </metsHdr>
        </mets>
        """)
        self.assertIn('Őh śéé Áŕ', mets.to_xml().decode('utf-8'))

    def test_remove_page(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002', 'PHYS_0005'])
            mets.remove_physical_page('PHYS_0001')
            self.assertEqual(mets.physical_pages, ['PHYS_0002', 'PHYS_0005'])

    def test_remove_page_after_remove_file(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002', 'PHYS_0005'])
            mets.remove_one_file('FILE_0005_IMAGE')
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002'])

    def test_remove_file_ocrdfile(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002', 'PHYS_0005'])
            ocrd_file = mets.find_files(ID='FILE_0005_IMAGE')[0]
            mets.remove_one_file(ocrd_file)
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002'])

    def test_remove_file_regex(self):
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002', 'PHYS_0005'])
            mets.remove_file('//FILE_0005.*')
            self.assertEqual(mets.physical_pages, ['PHYS_0001', 'PHYS_0002'])

    def test_remove_file_group0(self):
        """
        Test removal of filegrp
        """
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(len(mets.file_groups), 17)
            self.assertEqual(len(mets.find_files()), 35)
            #  print()
            #  before = sorted([x.ID for x in mets.find_files()])
            with self.assertRaisesRegex(Exception, "not empty"):
                mets.remove_file_group('OCR-D-GT-ALTO')
            mets.remove_file_group('OCR-D-GT-PAGE', recursive=True)
            #  print([x for x in before if x not in sorted([x.ID for x in mets.find_files()])])
            self.assertEqual(len(mets.file_groups), 16)
            self.assertEqual(len(mets.find_files()), 33)

    def test_remove_file_group_regex(self):
        """
        Test removal of filegrp
        """
        with copy_of_directory(assets.path_to('SBB0000F29300010000/data')) as tempdir:
            mets = OcrdMets(filename=join(tempdir, 'mets.xml'))
            self.assertEqual(len(mets.file_groups), 17)
            self.assertEqual(len(mets.find_files()), 35)
            mets.remove_file_group('//OCR-D-GT-.*', recursive=True)
            self.assertEqual(len(mets.file_groups), 15)
            self.assertEqual(len(mets.find_files()), 31)

if __name__ == '__main__':
    main(__file__)
