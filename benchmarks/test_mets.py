from itertools import product
from contextlib import contextmanager
from time import time

from pytest import main, fixture, mark

from ocrd import Resolver
from ocrd_utils import MIME_TO_EXT, getLogger
from ocrd_models import OcrdMets

LOG = getLogger('ocrd.benchmark.mets')

REGIONS_PER_PAGE = 10
LINES_PER_REGION = 2

GRPS_REG = ['SEG-REG', 'SEG-REPAIR', 'SEG-REG-DESKEW', 'SEG-REG-DESKEW-CLIP', 'SEG-LINE', 'SEG-REPAIR-LINE', 'SEG-LINE-RESEG-DEWARP']
GRPS_IMG = ['FULL', 'PRESENTATION', 'BIN', 'CROP', 'BIN2', 'BIN-DENOISE', 'BIN-DENOISE-DESKEW', 'OCR']
FILES_PER_PAGE = len(GRPS_IMG) * 2 + len(GRPS_REG) * REGIONS_PER_PAGE

mets_cache = {}

def _build_mets(number_of_pages, force=False):
    # LOG.info('number_of_pages=%s force=%s' % (number_of_pages, force))
    if not force and str(number_of_pages) in mets_cache:
        return mets_cache[str(number_of_pages)]
    mets = OcrdMets.empty_mets()
    mets._number_of_pages = number_of_pages
    # for page_id, mimetype in product(page_ids, mimetypes):
    for n in ['%04d' % (n + 1) for n in range(number_of_pages)]:
        _add_file = lambda n, fileGrp, mimetype, ID=None: mets.add_file(
            fileGrp,
            mimetype=mimetype,
            pageId='PHYS_%s' % n,
            ID=ID if ID else '%s_%s_%s' % (fileGrp, n, MIME_TO_EXT.get(mimetype)[1:].upper()),
            url='%s/%s%s' % (fileGrp, ID if ID else '%s_%s_%s' % (fileGrp, n, MIME_TO_EXT.get(mimetype)[1:].upper()), MIME_TO_EXT.get(mimetype))
        )
        for grp in GRPS_IMG:
            _add_file(n, grp, 'image/tiff')
            _add_file(n, grp, 'application/vnd.prima.page+xml')
        for grp in GRPS_REG:
            for region_n in range(REGIONS_PER_PAGE):
                _add_file(n, grp, 'image/png', '%s_%s_region%s' % (grp, n, region_n))
    mets_cache[str(number_of_pages)] = mets
    return mets

@contextmanager
def generated_mets(number_of_pages):
    mets = _build_mets(number_of_pages)
    def assert_len(kwargs, should):
        assert len(mets.find_files(**kwargs)) == should
    yield mets, assert_len

def benchmark_find_files(number_of_pages):
    benchmark_find_files_blank(number_of_pages)
    benchmark_find_files_filegrp(number_of_pages)
    benchmark_find_files_pageid(number_of_pages)
    # benchmark_find_files_exclude(number_of_pages)

def benchmark_find_files_blank(number_of_pages):
    with generated_mets(number_of_pages) as (_, assert_len):
        assert_len(dict(),  number_of_pages * FILES_PER_PAGE)

def benchmark_find_files_filegrp(number_of_pages):
    with generated_mets(number_of_pages) as (mets, assert_len):
        assert_len(dict(fileGrp='SEG-REG'), number_of_pages * REGIONS_PER_PAGE)
        assert_len(dict(fileGrp='SEG-REG-NOTEXIST'), 0)

def benchmark_find_files_pageid(number_of_pages):
    with generated_mets(number_of_pages) as (mets, assert_len):
        print(mets.find_files()[0].pageId)
        assert_len(dict(pageId='PHYS_0001'), FILES_PER_PAGE)

def benchmark_find_files_exclude(number_of_pages):
    with generated_mets(number_of_pages) as (mets, assert_len):
        print(mets.find_files()[0].pageId)
        assert_len(dict(pageId_exclude='PHYS_0001'), (number_of_pages - 1) * FILES_PER_PAGE)
    # def test_find_files(self):
    #     self.assertEqual(len(self.mets.find_files()), 35, '35 files total')
    #     self.assertEqual(len(self.mets.find_files(fileGrp='OCR-D-IMG')), 3, '3 files in "OCR-D-IMG"')
    #     self.assertEqual(len(self.mets.find_files(fileGrp='//OCR-D-I.*')), 13, '13 files in "//OCR-D-I.*"')
    #     self.assertEqual(len(self.mets.find_files(ID="FILE_0001_IMAGE")), 1, '1 files with ID "FILE_0001_IMAGE"')
    #     self.assertEqual(len(self.mets.find_files(ID="//FILE_0005_.*")), 1, '1 files with ID "//FILE_0005_.*"')
    #     self.assertEqual(len(self.mets.find_files(mimetype='image/tiff')), 13, '13 image/tiff')
    #     self.assertEqual(len(self.mets.find_files(mimetype='//application/.*')), 22, '22 application/.*')
    #     self.assertEqual(len(self.mets.find_files(mimetype=MIMETYPE_PAGE)), 20, '20 ' + MIMETYPE_PAGE)
    #     self.assertEqual(len(self.mets.find_files(url='OCR-D-IMG/FILE_0005_IMAGE.tif')), 1, '1 xlink:href="OCR-D-IMG/FILE_0005_IMAGE.tif"')

# @mark.benchmark(group="build")
# def test_add_1(benchmark):
#     @benchmark
#     def result(): return  _build_mets(1, force=True)

@mark.benchmark(group="add")
def test_add_5(benchmark):
    @benchmark
    def result(): _build_mets(5, force=True)

@mark.benchmark(group="add", disable_gc=True)
def test_add_5_no_gc(benchmark):
    @benchmark
    def result(): _build_mets(5, force=True)

@mark.benchmark(group="search")
def test_search_1(benchmark):
    @benchmark
    def ret(): benchmark_find_files(1)

@mark.benchmark(group="search")
def test_search_5(benchmark):
    @benchmark
    def ret(): benchmark_find_files(5)

@mark.benchmark(group="search")
def test_search_10(benchmark):
    @benchmark
    def ret(): benchmark_find_files(10)

@mark.benchmark(group="search")
def test_search_20(benchmark):
    @benchmark
    def ret(): benchmark_find_files(20)

@mark.benchmark(group="search")
def test_search_50(benchmark):
    @benchmark
    def ret(): benchmark_find_files(50)

@mark.benchmark(group="search")
def test_search_100(benchmark):
    @benchmark
    def ret(): benchmark_find_files(100)


# @mark.benchmark(group="search", max_time=1)
# def test_search_10_pageid(benchmark):
#     @benchmark
#     def result(): return benchmark_find_files(10)

# @mark.benchmark(group="search", max_time=1)
# def test_search_20(benchmark):
#     @benchmark
#     def result(): return  benchmark_find_files(20)

# @mark.benchmark(group="search", max_time=1)
# def test_search_50(benchmark):
#     @benchmark
#     def result(): return  benchmark_find_files(50)


if __name__ == '__main__':
    args = ['benchmarks']
    # args.append('--benchmark-max-time=10')
    # args.append('--benchmark-min-time=0.1')
    # args.append('--benchmark-warmup=True')
    # args.append('--benchmark-disable-gc')
    args.append('--benchmark-verbose')
    # args.append('--benchmark-min-rounds=1')
    args.append('--tb=short')
    main(args)
