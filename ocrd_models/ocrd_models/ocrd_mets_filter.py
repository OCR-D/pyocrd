from re import fullmatch
from ocrd_utils import REGEX_PREFIX, getLogger, is_local_filename, equals_or_regex_matches
from .constants import NAMESPACES as NS
from .ocrd_file import OcrdFile

LOG = getLogger('ocrd.models.ocrd_mets_filter')

FIELDS = ['fileGrp', 'pageId', 'mimetype', 'ID', 'url']
FIELDS_INCLUDE = ['%s_include' % f for f in FIELDS]
FIELDS_EXCLUDE = ['%s_exclude' % f for f in FIELDS]
SYNONYMS = {
    'filegrp': 'fileGrp',
    'file_grp': 'fileGrp',
    'pageid': 'pageId',
    'page_id': 'pageId',
    'id': 'ID',
    'file_id': 'ID',
}
SELECTORS = {
    'ID': lambda el: el.get('ID'),
    'fileGrp': lambda el: el.getparent().get('USE'),
    'mimetype': lambda el: el.get('MIMETYPE') or '',
    'ID': lambda el: el.get('ID'),
    'url': lambda el: el.find('mets:FLocat', namespaces=NS).get('{%s}href' % NS['xlink']),
}

class OcrdMetsFilter():
    """
    Define file restrictions on mets:files

    The ``ID``, ``fileGrp``, ``url`` and ``mimetype`` parameters as well as
    thei ``${field}_exclude`` counterparts can be either a literal string or a
    regular expression (regex) or a list of either. A regex starts with ``//``
    (double slash). If it is a regex, the leading ``//`` is removed and
    candidates are matched against the regex with ``re.fullmatch``. If it is a
    literal string, comparison is done with string equality. 
    """

    def __init__(self, local_only=False, **kwargs):
        """

        Args:
            ID (string|list) : ID(s) to include
            fileGrp (string|list) : fileGrp USE(s) to include
            pageId (string|list) : ID(s) of physical page(s) to include
            url (string|list) : FLocat/@xlink:href(s) to include
            mimetype (string|list) : MIMETYPE(s) to include
            ID_exclude (string|list) : ID(s) to exclude
            fileGrp_exclude (string|list) : fileGrp USE(s) to exclude
            pageId_exclude (string|list) : ID(s) of physical page(s) to exclude
            url_exclude (string|list) : FLocat/@xlink:href(s) to exclude
            mimetype_exclude (string|list) : MIMETYPE(s) to exclude
            local_only (boolean) : Whether to restrict results to local files
        """
        self.local_only = local_only
        for attr in FIELDS_INCLUDE + FIELDS_EXCLUDE:
            setattr(self, attr, None)
        for k, val in kwargs.items():
            field, op = k.rsplit('_', 2) if k.endswith('clude') else (k, 'include')
            field = SYNONYMS.get(field, field)
            LOG.debug('k=%s field=%s op=%s val=%s', k, field, op, val)
            if field not in FIELDS:
                raise ValueError("Unrecognized filter option: %s" % k)
            setattr(self, '%s_%s' % (field, op), val)
            # pylint: disable=no-member
            if (isinstance(self.pageId_include, str) and self.pageId_include.startswith(REGEX_PREFIX)) or \
                (isinstance(self.pageId_include, list) and any([x.startswith(REGEX_PREFIX) for x in self.pageId_include])):
                raise Exception("OcrdMetsFilter does not support regex search for pageId")

    def __str__(self):
        ret = []
        for n, field in enumerate(FIELDS):
            if getattr(self, FIELDS_INCLUDE[n]):
                ret.append('%s==%s' % (field, getattr(self, FIELDS_INCLUDE[n])))
            if getattr(self, FIELDS_EXCLUDE[n]):
                ret.append('%s!=%s' % (field, getattr(self, FIELDS_EXCLUDE[n])))
        return 'OcrdMetsFilter(%s)' % (' and '.join(ret))

    def _file_is_excluded(self, f):
        # If only local resources should be returned and f is not a file path: skip the file
        if self.local_only and not is_local_filename(f.url):
            return True
        for n, field in enumerate(FIELDS):
            val = getattr(f, field)
            needle = getattr(self, FIELDS_EXCLUDE[n])
            # print('val=%s needle=%s' % (val, needle))
            if not needle or not val:
                continue
            if equals_or_regex_matches(val, needle):
                return True

    # pylint: disable=no-member
    def _file_is_included(self, cand, by_page_id=None):
        # LOG.debug('enter _file_is_included cand=%s by_page_id=%s', cand, by_page_id)
        ID = SELECTORS['ID'](cand)
        if self.ID_include:
            LOG.debug('ID=%s', equals_or_regex_matches(ID, self.ID_include))
            if not equals_or_regex_matches(ID, self.ID_include):
                return
        if by_page_id is not None and ID not in by_page_id:
            return
        fileGrp = SELECTORS['fileGrp'](cand)
        if self.fileGrp_include:
            if not equals_or_regex_matches(fileGrp, self.fileGrp_include):
                return
        mimetype = SELECTORS['mimetype'](cand)
        if self.mimetype_include:
            if not equals_or_regex_matches(mimetype, self.mimetype_include):
                return
        url = SELECTORS['url'](cand)
        if self.url_include:
            if not equals_or_regex_matches(url, self.url_include):
                return
        return True

    def find_files(self, mets):
        """
        Search ``mets:file`` in this METS document.

        Args:
            mets (OcrdMets|Workspace): OcrdMets or Workspace wrapping OcrdMets
        """
        LOG.info('Filtering METS with %s' % self)
        # XXX: Also support passing an OcrdWorkspace
        if hasattr(mets, 'mets'):
            mets = mets.mets
        files = []

        # IDs by page
        by_page_id = None
        if self.pageId_include:
            by_page_id = []
            for page in mets.etree_xpath('//mets:div[@TYPE="page"]'):
                page_id = page.get('ID')
                # print(page_id, self.pageId_include)
                if equals_or_regex_matches(page_id, self.pageId_include):
                    by_page_id.extend([fptr.get('FILEID') for fptr in mets.etree_findall('mets:fptr', page)])

        # include
        included = []
        for cand in mets.etree_xpath('//mets:file'):
            if not self._file_is_included(cand, by_page_id):
                continue
            f = OcrdFile(cand, mets=mets)
            included.append(f)

        # exclude
        ret = []
        for f in included:
            if self._file_is_excluded(f):
                continue
            ret.append(f)

        return ret
