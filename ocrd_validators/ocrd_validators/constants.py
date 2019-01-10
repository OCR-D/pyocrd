import yaml
from pkg_resources import resource_string

OCRD_TOOL_SCHEMA = yaml.load(resource_string(__name__, 'yaml-files/ocrd_tool.schema.yml'))
BAGIT_TXT = 'BagIt-Version: 1.0\nTag-File-Character-Encoding: UTF-8'
FILE_GROUP_PREFIX = 'OCR-D-'
FILE_GROUP_CATEGORIES = ['IMG', 'SEG', 'OCR', 'COR', 'GT']
TMP_BAGIT_PREFIX = 'ocrd-bagit-'
OCRD_BAGIT_PROFILE = yaml.load(resource_string(__name__, 'yaml-files/bagit-profile.yml'))
OCRD_BAGIT_PROFILE_URL = 'https://ocr-d.github.io/bagit-profile.json'
