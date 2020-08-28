"""
Constants for ocrd_models.
"""
from pkg_resources import resource_string
import re

__all__ = [
    'IDENTIFIER_PRIORITY',
    'METS_XML_EMPTY',
    'NAMESPACES',
    'TAG_METS_AGENT',
    'TAG_METS_DIV',
    'TAG_METS_FILE',
    'TAG_METS_FILEGRP',
    'TAG_METS_FILESEC',
    'TAG_METS_FPTR',
    'TAG_METS_FLOCAT',
    'TAG_METS_METSHDR',
    'TAG_METS_NAME',
    'TAG_METS_STRUCTMAP',
    'TAG_MODS_IDENTIFIER',
    'TAG_PAGE_ALTERNATIVEIMAGE',
    'TAG_PAGE_COORDS',
    'TAG_PAGE_READINGORDER',
    'TAG_PAGE_REGIONREFINDEXED',
    'TAG_PAGE_TEXTLINE',
    'TAG_PAGE_TEXTEQUIV',
    'TAG_PAGE_TEXTREGION',
    'REGEX_FILE_ID',
    'OCRD_WF_SHEBANG',
]

REGEX_FILE_ID = re.compile('^[A-Za-z][^:]*$')

IDENTIFIER_PRIORITY = ['purl', 'urn', 'doi', 'url']

METS_XML_EMPTY = resource_string(__name__, 'mets-empty.xml')

NAMESPACES = {
    'mets': "http://www.loc.gov/METS/",
    'mods': "http://www.loc.gov/mods/v3",
    'xlink': "http://www.w3.org/1999/xlink",
    'page': "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15",
    'xsl': 'http://www.w3.org/1999/XSL/Transform#',
}

# pylint: disable=bad-whitespace
TAG_METS_AGENT            = '{%s}agent' % NAMESPACES['mets']
TAG_METS_DIV              = '{%s}div' % NAMESPACES['mets']
TAG_METS_FILE             = '{%s}file' % NAMESPACES['mets']
TAG_METS_FILEGRP          = '{%s}fileGrp' % NAMESPACES['mets']
TAG_METS_FILESEC          = '{%s}fileSec' % NAMESPACES['mets']
TAG_METS_FPTR             = '{%s}fptr' % NAMESPACES['mets']
TAG_METS_FLOCAT           = '{%s}FLocat' % NAMESPACES['mets']
TAG_METS_METSHDR          = '{%s}metsHdr' % NAMESPACES['mets']
TAG_METS_NAME             = '{%s}name' % NAMESPACES['mets']
TAG_METS_STRUCTMAP        = '{%s}structMap' % NAMESPACES['mets']

TAG_MODS_IDENTIFIER       = '{%s}identifier' % NAMESPACES['mods']

TAG_PAGE_ALTERNATIVEIMAGE = '{%s}AlternativeImage' % NAMESPACES['page']
TAG_PAGE_COORDS           = '{%s}Coords' % NAMESPACES['page']
TAG_PAGE_READINGORDER     = '{%s}ReadingOrder' % NAMESPACES['page']
TAG_PAGE_REGIONREFINDEXED = '{%s}RegionRefIndexed' % NAMESPACES['page']
TAG_PAGE_TEXTLINE         = '{%s}TextLine' % NAMESPACES['page']
TAG_PAGE_TEXTEQUIV        = '{%s}TextEquiv' % NAMESPACES['page']
TAG_PAGE_TEXTREGION       = '{%s}TextRegion' % NAMESPACES['page']

PAGE_REGION_TYPES = [
    'Advert', 'Chart', 'Chem', 'Custom', 'Graphic', 'Image',
    'LineDrawing', 'Map', 'Maths', 'Music', 'Noise',
    'Separator', 'Table', 'Text', 'Unknown'
]

OCRD_WF_SHEBANG = '#!/usr/bin/env ocrd-wf'
