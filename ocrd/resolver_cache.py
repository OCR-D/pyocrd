import os
import re

from ocrd.constants import DEFAULT_CACHE_FOLDER

from ocrd.utils import getLogger
log = getLogger('ocrd.cache')

def cache_key_from_url(url):
    ret = re.sub('[^A-Za-z0-9]', '', url)
    return ret

class ResolverCache(object):
    """
    Cache of downloads, based on URL.

    Args:
        cache_directory (string): Where to store cached files

    """

    def __init__(self, cache_directory=DEFAULT_CACHE_FOLDER):
        """
        Instantiate a cache
        """
        self.directory = cache_directory
        if not os.path.isdir(self.directory):
            log.info("Cache directory does not exist, creating: '%s'", self.directory)
            os.makedirs(self.directory)

    def get(self, url):
        cached_filename = os.path.join(self.directory, cache_key_from_url(url))
        if os.path.exists(cached_filename):
            return cached_filename

    def put(self, url, filename=None, content=None):
        cached_filename = os.path.join(self.directory, cache_key_from_url(url))
        if filename is None and content is None:
            raise Exception("cache.put requires 'filename' or 'content' kwarg")
        elif filename:
            with open(filename, 'r') as f:
                content = f.read()
        with open(cached_filename, 'wb') as outfile:
            outfile.write(content)
        return cached_filename
