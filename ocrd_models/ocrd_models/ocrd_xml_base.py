"""
Base class for XML documents loaded from either content or filename.
"""
from os.path import exists
from lxml import etree as ET

from .constants import NAMESPACES as NS
from .utils import xmllint_format


for curie in NS:
    ET.register_namespace(curie, NS[curie])

class OcrdXmlDocument():
    """
    Base class for XML documents loaded from either content or filename.
    """

    def __init__(self, filename=None, content=None):
        """
        Args:
            filename (string):
            content (string):
        """
        #  print(self, filename, content)
        if filename is None and content is None:
            raise Exception("Must pass 'filename' or 'content' to " + self.__class__.__name__)
        if content:
            self._tree = ET.ElementTree(ET.XML(content, parser=ET.XMLParser(encoding='utf-8')))
        else:
            self._tree = ET.ElementTree()
            filename = filename.replace('file://', '')
            if not exists(filename):
                raise Exception('File does not exist: %s' % filename)
            self._tree.parse(filename)

    @property
    def etree_root(self):
        """
        Return root element
        """
        return self._tree.getroot()

    def etree_xpath(self, xpath, el=None):
        """
        ET.xpath from ``el`` or root element
        """
        return (el if el is not None else self.etree_root).xpath(xpath, namespaces=NS)

    def etree_find(self, xpath, el=None):
        """
        ET.find from ``el`` or root element
        """
        return (el if el is not None else self.etree_root).find(xpath, namespaces=NS)

    def etree_findall(self, xpath, el=None):
        """
        ET.findall from ``el`` or root elemen
        """
        return (el if el is not None else self.etree_root).findall(xpath, namespaces=NS)

    def to_xml(self, xmllint=False):
        """
        Serialize all properties as pretty-printed XML

        Args:
            xmllint (boolean): Format with ``xmllint`` in addition to pretty-printing
        """
        ret = ET.tostring(ET.ElementTree(self.etree_root), pretty_print=True, encoding='UTF-8')
        if xmllint:
            ret = xmllint_format(ret)
        return ret
