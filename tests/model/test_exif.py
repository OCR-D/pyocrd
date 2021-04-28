from PIL import Image
from tests.base import TestCase, main, assets

from ocrd_models import OcrdExif

fixtures = {
    assets.path_to('kant_aufklaerung_1784/data/OCR-D-IMG/INPUT_0020.tif'): {
        'width': 1457, 'height': 2084, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-jp2/data/OCR-D-IMG/INPUT_0020.jp2'): {
        'width': 927, 'height': 0, 'xResolution': 0, 'yResolution': 0, 'resolution': 0, 'resolutionUnit': 'inches'},
    assets.path_to('leptonica_samples/data/OCR-D-IMG/OCR-D-IMG_1555_007.jpg'): {
        'width': 0, 'height': 0, 'xResolution': 0, 'yResolution': 0, 'resolution': 0, 'resolutionUnit': 'inches'},
    assets.path_to('leptonica_samples/data/OCR-D-IMG/OCR-D-IMG_1555_003.jpg'): {
        'width': 927, 'height': 1390, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG-1BIT/OCR-D-IMG-1BIT_0017.png'): {
        'width': 1457, 'height': 2083, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG-BIN/BIN_0020.png'): {
        'width': 0, 'height': 0, 'xResolution': 0, 'yResolution': 0, 'resolution': 0, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG-BIN/BIN_0017.png'): {
        'width': 1457, 'height': 2083, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG-NRM/OCR-D-IMG-NRM_0017.png'): {
        'width': 1457, 'height': 2083, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG-NRM/OCR-D-IMG-NRM_0020.png'): {
        'width': 1457, 'height': 2084, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG/OCR-D-IMG_0020.tif'): {
        'width': 1457, 'height': 2084, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG/OCR-D-IMG_0017.tif'): {
        'width': 1457, 'height': 2083, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},
    assets.path_to('pembroke_werke_1766/data/DEFAULT/FILE_0010_DEFAULT.tif'): {
        'width': 1158, 'height': 2138, 'xResolution': 2, 'yResolution': 2, 'resolution': 2, 'resolutionUnit': 'inches'},
    assets.path_to('dfki-testdata/data/DEWARP/DEWARP_1586.IMG-BINARIZED-DESKEWED-CROPPED-DEWARPED.png'): {
        'width': 1235, 'height': 2147, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('dfki-testdata/data/MAX/MAX_1586.tif'): {
        'width': 2323, 'height': 3214, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},
    assets.path_to('dfki-testdata/data/DESKEW/DESKEW_1586.IMG-BINARIZED-DESKEWED.png'): {
        'width': 2323, 'height': 3214, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('dfki-testdata/data/CROP/CROP_1586-IMG.png'): {
        'width': 1170, 'height': 2076, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('dfki-testdata/data/BIN-NRM/BIN-NRM_1586.IMG-GRAYSCALE_NORMALIZED.png'): {
        'width': 2323, 'height': 3214, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('dfki-testdata/data/BIN/BIN_1586.IMG-BINARIZED.png'): {
        'width': 2323, 'height': 3214, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('page_dewarp/data/OCR-D-IMG/OCR-D-IMG-linguistics_thesis_b.jpg'): {
        'width': 3456, 'height': 4608, 'xResolution': 350, 'yResolution': 350, 'resolution': 350, 'resolutionUnit': 'inches'},
    assets.path_to('page_dewarp/data/OCR-D-IMG/OCR-D-IMG-linguistics_thesis_a.jpg'): {
        'width': 3456, 'height': 4608, 'xResolution': 350, 'yResolution': 350, 'resolution': 350, 'resolutionUnit': 'inches'},
    assets.path_to('page_dewarp/data/OCR-D-IMG/OCR-D-IMG-boston_cooking_b.jpg'): {
        'width': 3264, 'height': 2448, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},
    assets.path_to('page_dewarp/data/OCR-D-IMG/OCR-D-IMG-boston_cooking_a.jpg'): {
        'width': 3264, 'height': 2448, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR1.tif'): {
        'width': 1381, 'height': 368, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR2.tif'): {
        'width': 1180, 'height': 371, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR3.tif'): {
        'width': 1203, 'height': 363, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR4.tif'): {
        'width': 1838, 'height': 798, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR5.tif'): {
        'width': 690, 'height': 682, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR6.tif'): {
        'width': 1315, 'height': 1069, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR7.tif'): {
        'width': 600, 'height': 564, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('DIBCO11-machine_printed/data/OCR-D-IMG-BIN/OCR-D-IMG-BIN_PR8.tif'): {
        'width': 859, 'height': 323, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'cm'},
    assets.path_to('grenzboten-test/data/OCR-D-IMG-BIN/p179470.tif'): {
        'width': 3340, 'height': 4872, 'xResolution': 600, 'yResolution': 600, 'resolution': 600, 'resolutionUnit': 'inches'},
    assets.path_to('column-samples/data/OCR-D-IMG/OCR-D-IMG-eiteritz_affe_1719-0206.jpg'): {
        'width': 1600, 'height': 2458, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},

    assets.path_to('column-samples/data/OCR-D-IMG/OCR-D-IMG-fleming_jaeger01_1719-0117.jpg'): {
        'width': 1600, 'height': 2642, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},
    assets.path_to('column-samples/data/OCR-D-IMG/OCR-D-IMG-corvinus_frauenzimmer_1715-0054.jpg'): {
        'width': 1600, 'height': 2756, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},
    assets.path_to('column-samples/data/OCR-D-IMG/OCR-D-IMG-bengel_abriss01_1751-0007.jpg'): {
        'width': 1600, 'height': 2867, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},
    assets.path_to('column-samples/data/OCR-D-IMG/OCR-D-IMG-dannhauer_catechismus04_1653-0585.jpg'): {
        'width': 1600, 'height': 2175, 'xResolution': 72, 'yResolution': 72, 'resolution': 72, 'resolutionUnit': 'inches'},
    assets.path_to('SBB0000F29300010000/data/OCR-D-IMG/FILE_0005_IMAGE.tif'): {
        'width': 2097, 'height': 3062, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},
    assets.path_to('SBB0000F29300010000/data/OCR-D-IMG/FILE_0001_IMAGE.tif'): {
        'width': 2875, 'height': 3749, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},

    assets.path_to('communist_manifesto/data/OCR-D-IMG/OCR-D-IMG_0015.png'): {
        'width': 2745, 'height': 4445, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('gutachten/data/IMG/IMG_1.tif'): {
        'width': 2088, 'height': 2634, 'xResolution': 300, 'yResolution': 300, 'resolution': 300, 'resolutionUnit': 'inches'},
    assets.path_to('glyph-consistency/data/00000259.sw.tif'): {
        'width': 1174, 'height': 1570, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('scribo-test/data/OCR-D-PRE-BIN-SAUVOLA/OCR-D-PRE-BIN-SAUVOLA_0001-BIN_sauvola.png'): {
        'width': 2097, 'height': 3062, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'},
    assets.path_to('kant_aufklaerung_1784-binarized/data/OCR-D-IMG-BIN/BIN_0020.png'): {
        'width': 1457, 'height': 2084, 'xResolution': 116, 'yResolution': 116, 'resolution': 116, 'resolutionUnit': 'cm'},
    assets.path_to('leptonica_samples/data/OCR-D-IMG/OCR-D-IMG_1555_007.jpg'): {
        'width': 944, 'height': 1472, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'
    },
    assets.path_to('kant_aufklaerung_1784-jp2/data/OCR-D-IMG/INPUT_0020.jp2'): {
        'width': 1457, 'height': 2084, 'xResolution': 1, 'yResolution': 1, 'resolution': 1, 'resolutionUnit': 'inches'
    }
}

# pylint: disable=no-member
class TestOcrdExif(TestCase):

    def test_images(self):
        for img_path, attrs in fixtures.items():
            print('exif-checking %s' % img_path)
            with Image.open(img_path) as img:
                exif = OcrdExif(img)
                for attr, val in attrs.items():
                    assert getattr(exif, attr) == val

if __name__ == '__main__':
    main(__file__)
