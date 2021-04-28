#!/usr/bin/env python

# source: https://bitbucket.org/dkuhlman/generateds/src/default/gends_user_methods.py

import re
import codecs
from os.path import dirname, join

#
# You must include the following class definition at the top of
#   your method specification file.
#
class MethodSpec():
    def __init__(self, name='', source='', class_names='',
            class_names_compiled=None):
        """MethodSpec -- A specification of a method.
        Member variables:
            name -- The method name
            source -- The source code for the method.  Must be
                indented to fit in a class definition.
            class_names -- A regular expression that must match the
                class names in which the method is to be inserted.
            class_names_compiled -- The compiled class names.
                generateDS.py will do this compile for you.
        """
        self.name = name
        self.source = source
        if class_names is None:
            self.class_names = ('.*', )
        else:
            self.class_names = class_names
        if class_names_compiled is None:
            self.class_names_compiled = re.compile(self.class_names)
        else:
            self.class_names_compiled = class_names_compiled
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_class_names(self):
        return self.class_names
    def set_class_names(self, class_names):
        self.class_names = class_names
        self.class_names_compiled = re.compile(class_names)
    def get_class_names_compiled(self):
        return self.class_names_compiled
    def set_class_names_compiled(self, class_names_compiled):
        self.class_names_compiled = class_names_compiled
    def match_name(self, class_name):
        """Match against the name of the class currently being generated.
        If this method returns True, the method will be inserted in
          the generated class.
        """
        if self.class_names_compiled.search(class_name):
            return True
        return False
    def get_interpolated_source(self, values_dict):
        """Get the method source code, interpolating values from values_dict
        into it.  The source returned by this method is inserted into
        the generated class.
        """
        source = self.source % values_dict
        return source
    def show(self):
        print('specification:')
        print('    name: %s' % (self.name, ))
        print(self.source)
        print('    class_names: %s' % (self.class_names, ))
        print('    names pat  : %s' % (self.class_names_compiled.pattern, ))


#
# Provide one or more method specification such as the following.
# Notes:
# - Each generated class contains a class variable _member_data_items.
#   This variable contains a list of instances of class _MemberSpec.
#   See the definition of class _MemberSpec near the top of the
#   generated superclass file and also section "User Methods" in
#   the documentation, as well as the examples below.

def _add_method(class_re, method_name, file_name=None):
    """
    Loads a file ./ocrd_page_user_methods/{{ method_name }}.py and defines a MethodSpec applying to class_re
    """
    source = []
    if not file_name:
        file_name = method_name
    with codecs.open(join(dirname(__file__), 'ocrd_page_user_methods', '%s.py' % file_name)) as f:
        for line in f.readlines():
            source.append('    %s' % line.replace('%', '%%') if line else line)
    return MethodSpec(name=method_name, class_names=class_re, source=''.join(source))

#
# Provide a list of your method specifications.
#   This list of specifications must be named METHOD_SPECS.
#
METHOD_SPECS = (
    _add_method(r'^.*$', '__hash__'),
    _add_method(r'^(OrderedGroupType|OrderedGroupIndexedType)$', 'get_AllIndexed'),
    _add_method(r'^(OrderedGroupType|OrderedGroupIndexedType)$', 'clear_AllIndexed'),
    _add_method(r'^(OrderedGroupType|OrderedGroupIndexedType)$', 'extend_AllIndexed'),
    _add_method(r'^(OrderedGroupType|OrderedGroupIndexedType)$', 'sort_AllIndexed'),
    _add_method(r'^(OrderedGroupType|OrderedGroupIndexedType)$', 'exportChildren', 'exportChildren_GroupType'),
    _add_method(r'^(UnorderedGroupType|UnorderedGroupIndexedType)$', 'get_UnorderedGroupChildren'),
    _add_method(r'^(PcGtsType|PageType)$', 'id'),
    _add_method(r'^(PageType)$', 'get_AllRegions'),
    _add_method(r'^(PcGtsType)$', 'get_AllAlternativeImagePaths'),
    _add_method(r'^(PageType)$', 'get_AllAlternativeImages'),
    _add_method(r'^(PcGtsType)$', 'prune_ReadingOrder'),
    _add_method(r'^(PageType|RegionType|TextLineType|WordType|GlyphType)$', 'invalidate_AlternativeImage'),
    _add_method(r'^(BorderType|RegionType|TextLineType|WordType|GlyphType)$', 'set_Coords'),
    _add_method(r'^(PageType)$', 'set_Border'),
    _add_method(r'^(CoordsType)$', 'set_points'),
    _add_method(r'^(PageType)$', 'get_AllTextLines'),
    # for some reason, pagecontent.xsd does not declare @orientation at the abstract/base RegionType:
    _add_method(r'^(PageType|AdvertRegionType|MusicRegionType|MapRegionType|ChemRegionType|MathsRegionType|SeparatorRegionType|ChartRegionType|TableRegionType|GraphicRegionType|LineDrawingRegionType|ImageRegionType|TextRegionType)$', 'set_orientation'),
    )


def test():
    for spec in METHOD_SPECS:
        spec.show()

def main():
    test()


if __name__ == '__main__':
    main()
