from unittest import mock
from pytest import fixture, raises
from shutil import copy
from os.path import join, dirname

from tests.base import main

from ocrd import Resolver
from ocrd_models import OcrdMetsFilter
# from ocrd_utils import setOverrideLogLevel; setOverrideLogLevel('DEBUG')

@fixture(name="sample_workspace")
def fixture_sample_workspace(tmpdir):
    resolver = Resolver()
    ws = resolver.workspace_from_nothing(str(tmpdir))
    ws.add_file('GRP1', mimetype='image/tiff', ID='GRP1_IMG1', pageId='PHYS_0001')
    ws.add_file('GRP1', mimetype='image/png', ID='GRP1_IMG2', pageId='PHYS_0002')
    ws.add_file('GRP2', mimetype='image/tiff', ID='GRP2_IMG1', pageId='PHYS_0001')
    ws.add_file('GRP2', mimetype='image/png', ID='GRP2_IMG2', pageId='PHYS_0002')
    ws.add_file('GRP3', mimetype='image/tiff', ID='GRP3_IMG1', pageId='PHYS_0001')
    ws.add_file('GRP3', mimetype='image/png', ID='GRP3_IMG2', pageId='PHYS_0002')
    return ws

def test_ocrd_mets_filter_noarg(sample_workspace):
    """Test w/o arguments"""
    mets_filter = OcrdMetsFilter()
    files = mets_filter.find_files(sample_workspace)
    assert len(files) == 6

def test_ocrd_mets_filter_bad_arg(sample_workspace):
    """Test unknown field"""
    with raises(ValueError):
        OcrdMetsFilter(foo_include='baz')

def test_ocrd_mets_filter_basic(sample_workspace):
    """Test basic filtering"""
    mets_filter = OcrdMetsFilter(mimetype_include='image/tiff', fileGrp_exclude=['GRP2'])
    files = mets_filter.find_files(sample_workspace)
    assert len(files) == 2

def test_ocrd_mets_filter_regex(sample_workspace):
    """Test filtering by regex"""
    mets_filter = OcrdMetsFilter(mimetype_include='image/tiff', fileGrp_exclude='//[GH][rR]P[2-3].*')
    files = mets_filter.find_files(sample_workspace)
    assert len(files) == 1

def test_ocrd_mets_filter_complex(sample_workspace):
    """Test complex arguments"""
    mets_filter = OcrdMetsFilter(ID_include='//GRP._IMG[0-9]', pageId_include='PHYS_0002', ID_exclude=['GRP1_IMG2'])
    files = mets_filter.find_files(sample_workspace)
    assert len(files) == 2

def test_ocrd_mets_filter_nested_regex(sample_workspace):
    """//-prefixed elements in exclude list"""
    mets_filter = OcrdMetsFilter(mimetype_include='image/tiff', ID_exclude=['//.R[pP]2.*_IMG1'])
    files = mets_filter.find_files(sample_workspace)
    assert len(files) == 2

def test_ocrd_mets_filter_lowercase(sample_workspace):
    """lowercase alternatives should be accepted"""
    mets_filter = OcrdMetsFilter(filegrp_exclude='GRP3', ID_exclude='GRP1_IMG2')
    files = mets_filter.find_files(sample_workspace)
    # print([str(f) for f  in files])
    assert len(files) == 3

def test_ocrd_mets_filter_include_aliases(sample_workspace):
    """field without _ implies field_include"""
    mets_filter = OcrdMetsFilter(pageid='PHYS_0001', ID='GRP1_IMG1')
    files = mets_filter.find_files(sample_workspace)
    assert len(files) == 1

if __name__ == '__main__':
    main(__file__)
