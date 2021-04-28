from tests.base import TestCase, main, assets
from tests.data.mock_file import MockOcrdFile as OcrdFile

from ocrd_modelfactory import page_from_image
from ocrd_models.ocrd_page_generateds import TextTypeSimpleType
from ocrd_models.ocrd_page import (
    AlternativeImageType,
    PcGtsType,
    PageType,
    TextRegionType,
    TextLineType,
    OrderedGroupIndexedType,
    UnorderedGroupIndexedType,
    ReadingOrderType,
    RegionRefIndexedType,
    WordType,
    GlyphType,

    parseString,
    parse,
    to_xml
)

simple_page = """\
<PcGts xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15 http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd">
    <Metadata>
        <Creator>OCR-D</Creator>
        <Created>2016-09-20T11:09:27.041+02:00</Created>
        <LastChange>2018-04-25T17:44:49.605+01:00</LastChange>
    </Metadata>
    <Page
        imageFilename="https://github.com/OCR-D/assets/raw/master/data/kant_aufklaerung_1784/data/OCR-D-IMG/INPUT_0017.tif"
        imageWidth="1457"
        imageHeight="2083"
        type="content">
        <TextRegion type="heading" id="r_1_1" custom="readingOrder {index:0;} structure {type:heading;}">
            <Coords points="113,365 919,365 919,439 113,439"/>
            <TextLine id="tl_1" primaryLanguage="German" custom="readingOrder {index:0;} textStyle {offset:0; length:26;fontFamily:Arial; fontSize:17.0; bold:true;}">
                <Coords points="114,366 918,366 918,438 114,438"/>
                <Baseline points="114,429 918,429"/>
                <Word id="w_w1aab1b1b2b1b1ab1" language="German" custom="readingOrder {index:0;} textStyle {offset:0; length:11;fontFamily:Arial; fontSize:17.0; bold:true;}">
                    <Coords points="114,368 442,368 442,437 114,437"/>
                    <TextEquiv conf="1">
                        <Unicode>Berliniſche</Unicode>
                    </TextEquiv>
                </Word>
            </TextLine>
        </TextRegion>
    </Page>
</PcGts>
"""

# pylint: disable=protected-access

class TestOcrdPage(TestCase):

    def setUp(self):
        super().setUp()
        self.maxDiff = 5000
        with open(assets.path_to('glyph-consistency/data/OCR-D-GT-PAGE/FAULTY_GLYPHS.xml'), 'rb') as f:
            self.xml_as_str = f.read()
            self.pcgts = parseString(self.xml_as_str, silence=True)

    def test_to_xml(self):
        # with open('/tmp/test.xml', 'w') as f:
        #     f.write(to_xml(self.pcgts))
        as_xml = to_xml(self.pcgts)
        self.assertIn(' xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', as_xml[:1000])
        self.assertIn(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15 http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15/pagecontent.xsd"', as_xml[:1000])
        self.assertIn('<pc:PcGts', as_xml[0:100])
        self.assertIn('<pc:TextRegion', as_xml[1000:3000])

    # https://github.com/OCR-D/core/pull/474#issuecomment-621477590 for context
    def test_to_xml_unicode_nsprefix(self):
        with open(assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-GT-WORD/INPUT_0020.xml'), 'rb') as f:
            from_xml = f.read()
            self.assertIn('<Unicode>', from_xml.decode('utf-8'), 'without NS prefix')
            self.assertIn('<Created', from_xml.decode('utf-8'), 'without NS prefix')
            pcgts = parseString(from_xml, silence=True)
            as_xml = to_xml(pcgts)
            self.assertIn('<pc:Unicode>', as_xml, 'with NS prefix')
            self.assertIn('<pc:Created>', as_xml, 'with NS prefix')

    def test_issue_269(self):
        """
        @conf is parsed as str but should be float
        https://github.com/OCR-D/core/issues/269
        """
        # GIGO
        self.pcgts.get_Page().get_TextRegion()[0].get_TextEquiv()[0].set_conf(1.0)
        self.assertEqual(type(self.pcgts.get_Page().get_TextRegion()[0].get_TextEquiv()[0].get_conf()), float)
        self.pcgts.get_Page().get_TextRegion()[0].get_TextEquiv()[0].set_conf('1.0')
        self.assertEqual(type(self.pcgts.get_Page().get_TextRegion()[0].get_TextEquiv()[0].get_conf()), str)
        # test with parseString that @conf in TextEquiv won't throw an error
        parseString(simple_page, silence=True)
        #  self.assertTrue(True)

    def test_pcGtsId(self):
        self.assertEqual(self.pcgts.pcGtsId, 'FAULTY_GLYPHS_FILE')

    def test_delete_region(self):
        pcgts = parseString(simple_page, silence=True)
        self.assertEqual(len(pcgts.get_Page().get_TextRegion()), 1)
        del pcgts.get_Page().get_TextRegion()[0]
        self.assertEqual(len(pcgts.get_Page().get_TextRegion()), 0)

    def test_imageFileName(self):
        #  print(self.pcgts.export(sys.stdout, 0))
        self.assertEqual(self.pcgts.get_Page().imageFilename, '00000259.sw.tif')
        self.pcgts.get_Page().imageFilename = 'foo'
        self.assertEqual(self.pcgts.get_Page().imageFilename, 'foo')

    def test_alternativeImage(self):
        pcgts = PcGtsType(pcGtsId="foo")
        self.assertEqual(pcgts.pcGtsId, 'foo')
        # Page/AlternativeImage
        page = PageType()
        pcgts.set_Page(page)
        page.add_AlternativeImage(AlternativeImageType())
        # TextRegion/AlternativeImage
        region = TextRegionType()
        page.add_TextRegion(region)
        region.add_AlternativeImage(AlternativeImageType())
        # TextLine/AlternativeImage
        line = TextLineType()
        region.add_TextLine(line)
        line.add_AlternativeImage(AlternativeImageType())
        # Word/AlternativeImage
        word = WordType()
        line.add_Word(word)
        word.add_AlternativeImage(AlternativeImageType())
        # Glyph/AlternativeImage
        glyph = GlyphType()
        word.add_Glyph(glyph)
        glyph.add_AlternativeImage(AlternativeImageType())

    def test_simple_types(self):
        regions = self.pcgts.get_Page().get_TextRegion()
        reg = regions[0]
        # print([l.get_type() for l in regions])
        self.assertTrue(isinstance(reg.get_type(), str))
        self.assertEqual(reg.get_type(), TextTypeSimpleType.CREDIT)
        self.assertTrue(isinstance(TextTypeSimpleType.CREDIT, str))
        self.assertEqual(reg.get_type(), 'credit')
        self.assertTrue(isinstance(TextTypeSimpleType.CREDIT, str))
        reg.set_type(TextTypeSimpleType.PAGENUMBER)
        self.assertEqual(reg.get_type(), 'page-number')
        self.assertTrue(isinstance(reg.get_type(), str))

    def test_orderedgroup_export_order(self):
        """
        See https://github.com/OCR-D/core/issues/475
        """
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            pcgts = parseString(f.read().encode('utf8'), silence=True)
            og = pcgts.get_Page().get_ReadingOrder().get_OrderedGroup()
            xml_before = to_xml(og)
            children = og.get_AllIndexed()
            self.assertEqual(len(children), 22)
            self.assertEqual([c.index for c in children], list(range(0, 22)))
            # mix up the indexes
            children[0].index = 11
            children[11].index = 3
            children[3].index = 0
            self.assertEqual([c.index for c in children], [11, 1, 2, 0, 4, 5, 6, 7, 8, 9, 10, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
            self.assertEqual([c.index for c in og.get_AllIndexed()], list(range(0, 22)))
            self.assertEqual(og.get_AllIndexed()[1].__class__, OrderedGroupIndexedType)
            # serialize and make sure the correct order was serialized
            new_pcgts = parseString(to_xml(pcgts).encode('utf8'), silence=True)
            new_og = new_pcgts.get_Page().get_ReadingOrder().get_OrderedGroup()
            self.assertEqual([c.index for c in new_og.get_AllIndexed()], list(range(0, 22)))
            # xml_after = to_xml(new_og)
            # self.assertEqual(xml_after, xml_before)

    def test_empty_groups_to_regionrefindexed(self):
        """
        Corrolary See https://github.com/OCR-D/core/issues/475
        """
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            pcgts = parseString(f.read().encode('utf8'), silence=True)
            og = pcgts.get_Page().get_ReadingOrder().get_OrderedGroup()
            children = og.get_AllIndexed()
            self.assertTrue(isinstance(children[1], OrderedGroupIndexedType))
            self.assertTrue(isinstance(children[21], UnorderedGroupIndexedType))
            # empty all the elements in the first orederdGroupIndexed
            children[1].set_RegionRefIndexed([])
            # serialize apnd parse to see empty group converted
            pcgts = parseString(to_xml(pcgts).encode('utf8'), silence=True)
            og = pcgts.get_Page().get_ReadingOrder().get_OrderedGroup()
            children = og.get_AllIndexed()
            self.assertTrue(isinstance(children[1], RegionRefIndexedType))
            self.assertTrue(isinstance(children[21], RegionRefIndexedType))

    def test_all_regions_without_reading_order(self):
        """
        https://github.com/OCR-D/core/pull/479
        https://github.com/OCR-D/core/issues/240#issuecomment-493135797
        """
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            pcgts = parseString(f.read().encode('utf8'), silence=True)
            pg = pcgts.get_Page()
            self.assertEqual(len(pg.get_AllRegions()), 65)
            self.assertEqual(len(pg.get_AllRegions(depth=0)), 65)
            self.assertEqual(len(pg.get_AllRegions(depth=1)), 45)
            self.assertEqual(len(pg.get_AllRegions(depth=2)), 65)
            self.assertEqual(len(pg.get_AllRegions(depth=3)), 65)
            self.assertEqual(len(pg.get_AllRegions(classes=['Separator'])), 25)
            self.assertEqual(len(pg.get_AllRegions(classes=['Table'])), 3)
            self.assertEqual(len(pg.get_AllRegions(classes=['Text'])), 37)
            self.assertEqual(len(pg.get_AllRegions(classes=['Text'], depth=1)), 17)
            self.assertEqual(len(pg.get_AllRegions(classes=['Text'], depth=2)), 37)

    def test_all_regions_with_reading_order(self):
        """
        https://github.com/OCR-D/core/pull/479
        https://github.com/OCR-D/core/issues/240#issuecomment-493135797
        """
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            pg = parseString(f.read().encode('utf8'), silence=True).get_Page()
            with self.assertRaisesRegex(Exception, "Argument 'order' must be either 'document', 'reading-order' or 'reading-order-only', not 'random'"):
                pg.get_AllRegions(order='random')
            with self.assertRaisesRegex(Exception, "Argument 'depth' must be an integer greater-or-equal 0, not '-1'"):
                pg.get_AllRegions(depth=-1)
            self.assertEqual(len(pg.get_AllRegions(order='reading-order-only')), 40)
            self.assertEqual(len(pg.get_AllRegions(order='reading-order-only', depth=1)), 20)
            self.assertEqual(len(pg.get_AllRegions(order='reading-order-only', depth=2)), 40)
            self.assertEqual(len(pg.get_AllRegions(order='reading-order', depth=0)), 65)
            self.assertEqual(len(pg.get_AllRegions(order='reading-order', depth=1)), 45)
            self.assertEqual(len(pg.get_AllRegions(order='reading-order', depth=2)), 65)
            self.assertEqual(len(pg.get_AllRegions(classes=['Table'], order='reading-order')), 3)
            self.assertEqual(len(pg.get_AllRegions(classes=['Text'], order='reading-order')), 37)
            self.assertEqual(len(pg.get_AllRegions(classes=['Text'], order='reading-order', depth=1)), 17)

    def test_get_UnorderdGroupChildren(self):
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            pcgts = parseString(f.read().encode('utf8'), silence=True)
            ug = pcgts.get_Page().get_ReadingOrder().get_OrderedGroup().get_UnorderedGroupIndexed()[0]
            self.assertEqual(len(ug.get_UnorderedGroupChildren()), 1)

    def test_get_AllIndexed_classes(self):
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            og = parseString(f.read().encode('utf8'), silence=True).get_Page().get_ReadingOrder().get_OrderedGroup()
            self.assertEqual(len(og.get_AllIndexed(classes=['RegionRef'])), 17)
            self.assertEqual(len(og.get_AllIndexed(classes=['OrderedGroup'])), 3)
            self.assertEqual(len(og.get_AllIndexed(classes=['UnorderedGroup'])), 2)

    def test_get_AllIndexed_index_sort(self):
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            og = parseString(f.read().encode('utf8'), silence=True).get_Page().get_ReadingOrder().get_OrderedGroup()
            unogs = og.get_UnorderedGroupIndexed()
            self.assertEqual([x.index for x in unogs], [20, 21])
            unogs[0].index = 21
            unogs[1].index = 20
            self.assertEqual([x.index for x in og.get_AllIndexed(classes=['UnorderedGroup'], index_sort=True)], [20, 21])
            self.assertEqual([x.index for x in og.get_AllIndexed(classes=['UnorderedGroup'], index_sort=False)], [21, 20])
            og.sort_AllIndexed()
            self.assertEqual([x.index for x in og.get_AllIndexed(classes=['UnorderedGroup'], index_sort=False)], [20, 21])

    def test_extend_AllIndexed_no_validation(self):
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            og = parseString(f.read().encode('utf8'), silence=True).get_Page().get_ReadingOrder().get_OrderedGroup()
            og.extend_AllIndexed([
                RegionRefIndexedType(index=3, id='r3'),
                RegionRefIndexedType(index=2, id='r2'),
                RegionRefIndexedType(index=1, id='r1'),
            ])
            rrs = og.get_RegionRefIndexed()
            self.assertEqual([x.index for x in rrs][-3:], [22, 23, 24])

    def test_get_AllTextLine(self):
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            page = parseString(f.read().encode('utf8'), silence=True).get_Page()
            assert len(page.get_AllTextLines()) == 55

    def test_extend_AllIndexed_validate_continuity(self):
        with open(assets.path_to('gutachten/data/TEMP1/PAGE_TEMP1.xml'), 'r') as f:
            og = parseString(f.read().encode('utf8'), silence=True).get_Page().get_ReadingOrder().get_OrderedGroup()
            with self.assertRaisesRegex(Exception, "@index already used: 1"):
                og.extend_AllIndexed([
                    RegionRefIndexedType(index=3, id='r3'),
                    RegionRefIndexedType(index=2, id='r2'),
                    RegionRefIndexedType(index=1, id='r1'),
                ], validate_continuity=True)

    def test_get_AllAlternativeImagePaths(self):
        with open(assets.path_to('kant_aufklaerung_1784-complex/data/OCR-D-OCR-OCRO-fraktur-SEG-LINE-tesseract-ocropy-DEWARP/OCR-D-OCR-OCRO-fraktur-SEG-LINE-tesseract-ocropy-DEWARP_0001.xml'), 'r') as f:
            pcgts = parseString(f.read().encode('utf8'), silence=True)
            self.assertEqual(pcgts.get_AllAlternativeImagePaths(page=False, region=False, line=False), [])
            self.assertEqual(pcgts.get_AllAlternativeImagePaths(page=True, region=False, line=False), [
                'OCR-D-IMG-BIN/OCR-D-IMG-BINPAGE-sauvola_0001-BIN_sauvola-ms-split.png',
                'OCR-D-IMG-CROP/OCR-D-IMG-CROP_0001.png',
                'OCR-D-IMG-BIN/INPUT_0017-BIN_sauvola-ms-split.png',
                'OCR-D-IMG-DESPECK/OCR-D-IMG-DESPECK_0001.png',
                'OCR-D-IMG-DESKEW/OCR-D-IMG-DESKEW_0001.png',
                'OCR-D-IMG-DESKEW/OCR-D-IMG-DESKEW_0001.png'])
            self.assertEqual(len(pcgts.get_AllAlternativeImagePaths(page=True, region=True, line=False)), 12)
            self.assertEqual(len(pcgts.get_AllAlternativeImagePaths(page=True, region=True, line=False)), 12)
            self.assertEqual(len(pcgts.get_AllAlternativeImagePaths(page=True, region=True, line=True)), 36)
            # TODO: Test with word/glyph-level AlternativeImages
            # self.assertEqual(len(pcgts.get_AllAlternativeImagePaths(word=False)), 37)

    def test_get_AllAlternativeImages(self):
        with open(assets.path_to('kant_aufklaerung_1784-complex/data/OCR-D-OCR-OCRO-fraktur-SEG-LINE-tesseract-ocropy-DEWARP/OCR-D-OCR-OCRO-fraktur-SEG-LINE-tesseract-ocropy-DEWARP_0001.xml'), 'r') as f:
            pcgts = parseString(f.read().encode('utf8'), silence=True)
            page = pcgts.get_Page()
            self.assertEqual(page.get_AllAlternativeImages(page=False, region=False, line=False), [])
            self.assertEqual([x.filename for x in page.get_AllAlternativeImages(page=True, region=False, line=False)], [
                'OCR-D-IMG-BIN/OCR-D-IMG-BINPAGE-sauvola_0001-BIN_sauvola-ms-split.png',
                'OCR-D-IMG-CROP/OCR-D-IMG-CROP_0001.png',
                'OCR-D-IMG-BIN/INPUT_0017-BIN_sauvola-ms-split.png',
                'OCR-D-IMG-DESPECK/OCR-D-IMG-DESPECK_0001.png',
                'OCR-D-IMG-DESKEW/OCR-D-IMG-DESKEW_0001.png',
                'OCR-D-IMG-DESKEW/OCR-D-IMG-DESKEW_0001.png'])
            assert isinstance(page.get_AllAlternativeImages()[0], AlternativeImageType)

    def test_serialize_no_empty_readingorder(self):
        """
        https://github.com/OCR-D/core/issues/602
        """
        pcgts = page_from_image(OcrdFile(None, url=assets.path_to('kant_aufklaerung_1784/data/OCR-D-IMG/INPUT_0017.tif')))
        pcgts.get_Page().set_ReadingOrder(ReadingOrderType())
        assert pcgts.get_Page().get_ReadingOrder()
        pcgts = parseString(to_xml(pcgts, skip_declaration=True))
        assert not pcgts.get_Page().get_ReadingOrder()

    def test_hashable(self):
        """
        https://github.com/OCR-D/ocrd_segment/issues/45
        """
        pcgts = page_from_image(OcrdFile(None, url=assets.path_to('kant_aufklaerung_1784/data/OCR-D-IMG/INPUT_0017.tif')))
        page = pcgts.get_Page()
        testset = set()
        testset.add(pcgts)
        testset.add(page)

    def test_id(self):
        """
        https://github.com/OCR-D/core/issues/682
        """
        fpath_page = assets.path_to('kant_aufklaerung_1784/data/OCR-D-GT-PAGE/PAGE_0017_PAGE.xml')
        pcgts = parse(fpath_page)
        assert pcgts.id == 'PAGE_0017_PAGE'
        assert pcgts.get_Page().id == 'OCR-D-IMG/INPUT_0017.tif'

if __name__ == '__main__':
    main(__file__)
