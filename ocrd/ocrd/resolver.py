import tempfile
from pathlib import Path

import requests

from ocrd.constants import TMP_PREFIX
from ocrd_utils import (
    getLogger,
    is_local_filename,
    get_local_filename,
    remove_non_path_from_url,
    nth_url_segment
)
from ocrd.workspace import Workspace
from ocrd_models import OcrdMets, OcrdMetsFilter

log = getLogger('ocrd.resolver')

class Resolver():
    """
    Handle Uploads, Downloads, Repository access and manage temporary directories
    """

    def download_to_directory(self, directory, url, basename=None, if_exists='skip', subdir=None):
        """
        Download a file to a directory.

        Early Shortcut: If url is a local file and that file is already in the directory, keep it there.

        If basename is not given but subdir is, assume user knows what she's doing and use last URL segment as the basename.
        If basename is not given and no subdir is given, use the alnum characters in the URL as the basename.

        Args:
            directory (string): Directory to download files to
            basename (string, None): basename part of the filename on disk.
            url (string): URL to download from
            if_exists (string, "skip"): What to do if target file already exists. One of ``skip`` (default), ``overwrite`` or ``raise``
            subdir (string, None): Subdirectory to create within the directory. Think fileGrp.

        Returns:
            Local filename, __relative__ to directory
        """
        log = getLogger('ocrd.resolver.download_to_directory') # pylint: disable=redefined-outer-name
        log.debug("directory=|%s| url=|%s| basename=|%s| if_exists=|%s| subdir=|%s|", directory, url, basename, if_exists, subdir)

        if not url:
            raise Exception("'url' must be a string")
        if not directory:
            raise Exception("'directory' must be a string")  # actually Path would also work

        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        directory = str(directory.resolve())

        subdir_path = Path(subdir if subdir else '')
        basename_path = Path(basename if basename else nth_url_segment(url))
        ret = str(Path(subdir_path, basename_path))
        dst_path = Path(directory, ret)

        #  log.info("\n\tdst_path='%s \n\turl=%s", dst_path, url)
        #  print('url=%s', url)
        #  print('directory=%s', directory)
        #  print('subdir_path=%s', subdir_path)
        #  print('basename_path=%s', basename_path)
        #  print('ret=%s', ret)
        #  print('dst_path=%s', dst_path)

        src_path = None
        if is_local_filename(url):
            try:
                # XXX this raises FNFE in Python 3.5 if src_path doesn't exist but not 3.6+
                src_path = Path(get_local_filename(url)).resolve()
            except FileNotFoundError as e:
                log.error("Failed to resolve URL locally: %s --> '%s' which does not exist" % (url, src_path))
                raise e
            if not src_path.exists():
                raise FileNotFoundError("File path passed as 'url' to download_to_directory does not exist: %s" % url)
            if src_path == dst_path:
                log.debug("Stop early, src_path and dst_path are the same: '%s' (url: '%s')" % (src_path, url))
                return ret

        # Respect 'if_exists' arg
        if dst_path.exists():
            if if_exists == 'skip':
                return ret
            if if_exists == 'raise':
                raise FileExistsError("File already exists and if_exists == 'raise': %s" % (dst_path))

        # Create dst_path parent dir
        dst_path.parent.mkdir(parents=True, exist_ok=True)

        # Copy files or download remote assets
        if src_path:
            log.debug("Copying file '%s' to '%s'", src_path, dst_path)
            dst_path.write_bytes(src_path.read_bytes())
        else:
            log.debug("Downloading URL '%s' to '%s'", url, dst_path)
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception("HTTP request failed: %s (HTTP %d)" % (url, response.status_code))
            dst_path.write_bytes(response.content)

        return ret

    def workspace_from_url(self, mets_url, dst_dir=None, clobber_mets=False, mets_basename=None, download=False, src_baseurl=None):
        """
        Create a workspace from a METS by URL (i.e. clone it).

        Sets the mets.xml file

        Arguments:
            mets_url (string): Source mets URL
            dst_dir (string, None): Target directory for the workspace
            clobber_mets (boolean, False): Whether to overwrite existing mets.xml. By default existing mets.xml will raise an exception.
            download (boolean, False): Whether to download all the files
            src_baseurl (string, None): Base URL for resolving relative file locations

        Returns:
            Workspace
        """

        if mets_url is None:
            raise ValueError("Must pass 'mets_url' workspace_from_url")

        # if mets_url is a relative filename, make it absolute
        if is_local_filename(mets_url) and not Path(mets_url).is_absolute():
            mets_url = str(Path(Path.cwd() / mets_url))

        # if mets_basename is not given, use the last URL segment of the mets_url
        if mets_basename is None:
            mets_basename = nth_url_segment(mets_url, -1)

        # If src_baseurl wasn't given, determine from mets_url by removing last url segment
        if not src_baseurl:
            last_segment = nth_url_segment(mets_url)
            src_baseurl = remove_non_path_from_url(remove_non_path_from_url(mets_url)[:-len(last_segment)])

        # resolve dst_dir
        if not dst_dir:
            if is_local_filename(mets_url):
                log.debug("Deriving dst_dir %s from %s", Path(mets_url).parent, mets_url)
                dst_dir = Path(mets_url).parent
            else:
                log.debug("Creating ephemeral workspace '%s' for METS @ <%s>", dst_dir, mets_url)
                dst_dir = tempfile.mkdtemp(prefix=TMP_PREFIX)
        # XXX Path.resolve is always strict in Python <= 3.5, so create dst_dir unless it exists consistently
        if not Path(dst_dir).exists():
            Path(dst_dir).mkdir(parents=True, exist_ok=False)
        dst_dir = str(Path(dst_dir).resolve())

        log.debug("workspace_from_url\nmets_basename='%s'\nmets_url='%s'\nsrc_baseurl='%s'\ndst_dir='%s'",
            mets_basename, mets_url, src_baseurl, dst_dir)

        self.download_to_directory(dst_dir, mets_url, basename=mets_basename, if_exists='overwrite' if clobber_mets else 'skip')

        workspace = Workspace(self, dst_dir, mets_basename=mets_basename, baseurl=src_baseurl)

        # XXX an empty dict is false-y but valid in this context
        if download or download == {}:
            if not isinstance(download, dict):
                download = {}
            mets_filter = OcrdMetsFilter(**download)
            for f in mets_filter.find_files(workspace):
                workspace.download_file(f)

        return workspace

    def workspace_from_nothing(self, directory, mets_basename='mets.xml', clobber_mets=False):
        """
        Create an empty workspace.
        """
        if directory is None:
            directory = tempfile.mkdtemp(prefix=TMP_PREFIX)
        Path(directory).mkdir(parents=True, exist_ok=True)
        mets_path = Path(directory, mets_basename)
        if mets_path.exists() and not clobber_mets:
            raise FileExistsError("METS '%s' already exists in '%s' and clobber_mets not set." % (mets_basename, directory))
        mets = OcrdMets.empty_mets()
        log.info("Writing METS to %s", mets_path)
        mets_path.write_bytes(mets.to_xml(xmllint=True))

        return Workspace(self, directory, mets, mets_basename=mets_basename)
