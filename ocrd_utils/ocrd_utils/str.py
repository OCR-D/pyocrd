"""
Utility functions for strings, paths and URL.
"""

import re
import json
from .constants import REGEX_PREFIX

__all__ = [
    'assert_file_grp_cardinality',
    'concat_padded',
    'equals_or_regex_matches',
    'get_local_filename',
    'is_local_filename',
    'is_string',
    'make_file_id',
    'nth_url_segment',
    'parse_json_string_or_file',
    'parse_json_string_with_comments',
    'remove_non_path_from_url',
    'safe_filename',
]


def assert_file_grp_cardinality(grps, n, msg=None):
    """
    Assert that a string of comma-separated fileGrps contains exactly ``n`` entries.
    """
    if isinstance(grps, str):
        grps = grps.split(',')
    assert len(grps) == n, \
            "Expected exactly %d output file group%s%s, but '%s' has %d" % (
                n,
                '' if n == 1 else 's',
                ' (%s)' % msg if msg else '',
                grps,
                len(grps)
            )

def concat_padded(base, *args):
    """
    Concatenate string and zero-padded 4 digit number
    """
    ret = base
    for n in args:
        if is_string(n):
            ret = "%s_%s" % (ret, n)
        else:
            ret = "%s_%04i"  % (ret, n)
    return ret

def remove_non_path_from_url(url):
    """
    Remove everything from URL after path.
    """
    url = url.split('?', 1)[0]    # query
    url = url.split('#', 1)[0]    # fragment identifier
    url = re.sub(r"/+$", "", url) # trailing slashes
    return url

def make_file_id(ocrd_file, output_file_grp):
    """
    Derive a new file ID for an output file from an existing input file ``ocrd_file``
    and the name of the output file's ``fileGrp/@USE``, ``output_file_grp``.
    If ``ocrd_file``'s ID contains the input file's fileGrp name, then replace it by ``output_file_grp``.
    Otherwise use ``output_file_grp`` together with the position of ``ocrd_file`` within the input fileGrp
    (as a fallback counter). Increment counter until there is no more ID conflict.
    """
    ret = ocrd_file.ID.replace(ocrd_file.fileGrp, output_file_grp)
    if ret == ocrd_file.ID:
        m = re.match(r'.*?(\d{3,}).*', ocrd_file.pageId or '')
        if m:
            n = int(m.group(1))
        else:
            ids = [f.ID for f in ocrd_file.mets.find_files(fileGrp=ocrd_file.fileGrp, mimetype=ocrd_file.mimetype)]
            try:
                n = ids.index(ocrd_file.ID) + 1
            except ValueError:
                n = len(ids)
        ret = concat_padded(output_file_grp, n)
        while ocrd_file.mets.find_files(ID=ret):
            n += 1
            ret = concat_padded(output_file_grp, n)
    return ret

def nth_url_segment(url, n=-1):
    """
    Return the last /-delimited segment of a URL-like string

    Arguments:
        url (string):
        n (integer): index of segment, default: -1
    """
    segments = remove_non_path_from_url(url).split('/')
    try:
        return segments[n]
    except IndexError:
        return ''

def get_local_filename(url, start=None):
    """
    Return local filename, optionally relative to ``start``

    Arguments:
        url (string): filename or URL
        start (string): Base path to remove from filename. Raise an exception if not a prefix of url
    """
    if url.startswith('https://') or url.startswith('http:'):
        raise Exception("Can't determine local filename of http(s) URL")
    if url.startswith('file://'):
        url = url[len('file://'):]
    # Goobi/Kitodo produces those, they are always absolute
    if url.startswith('file:/'):
        raise Exception("Invalid (java) URL: %s" % url)
    if start:
        if not url.startswith(start):
            raise Exception("Cannot remove prefix %s from url %s" % (start, url))
        if not start.endswith('/'):
            start += '/'
        url = url[len(start):]
    return url

def is_local_filename(url):
    """
    Whether a url is a local filename.
    """
    return url.startswith('file://') or not('://' in url)

def is_string(val):
    """
    Return whether a value is a ``str``.
    """
    return isinstance(val, str)


def parse_json_string_with_comments(val):
    """
    Parse a string of JSON interspersed with #-prefixed full-line comments
    """
    jsonstr = re.sub(r'^\s*#.*$', '', val, flags=re.MULTILINE)
    return json.loads(jsonstr)

def parse_json_string_or_file(*values):    # pylint: disable=unused-argument
    """
    Parse a string as either the path to a JSON object or a literal JSON object.

    Empty strings are equivalent to '{}'
    """
    ret = {}
    for value in values:
        err = None
        value_parsed = None
        if re.fullmatch(r"\s*", value):
            continue
        try:
            try:
                with open(value, 'r') as f:
                    value_parsed = parse_json_string_with_comments(f.read())
            except (FileNotFoundError, OSError):
                value_parsed = parse_json_string_with_comments(value.strip())
            if not isinstance(value_parsed, dict):
                err = ValueError("Not a valid JSON object: '%s' (parsed as '%s')" % (value, value_parsed))
        except json.decoder.JSONDecodeError as e:
            err = ValueError("Error parsing '%s': %s" % (value, e))
        if err:
            raise err       # pylint: disable=raising-bad-type
        ret = {**ret, **value_parsed}
    return ret

def safe_filename(url):
    """
    Sanitize input to be safely used as the basename of a local file.
    """
    ret = re.sub('[^A-Za-z0-9]+', '.', url)
    #  print('safe filename: %s -> %s' % (url, ret))
    return ret

def equals_or_regex_matches_recursive(val, needle):
    # XXX string comparison only
    val = str(val)
    if needle.startswith(REGEX_PREFIX):
        return re.fullmatch(needle[len(REGEX_PREFIX):], val)
    return val == needle

def equals_or_regex_matches(val, needle):
    if isinstance(needle, list):
        if any(equals_or_regex_matches_recursive(val, k) for k in needle):
            return True
    else:
        if equals_or_regex_matches_recursive(val, needle):
            return True

