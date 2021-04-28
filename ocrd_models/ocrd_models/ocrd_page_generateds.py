#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Mar 17 11:07:10 2021 by generateDS.py version 2.35.20.
# Python 3.6.9 (default, Jan 26 2021, 15:33:00)  [GCC 8.4.0]
#
# Command line options:
#   ('-f', '')
#   ('--root-element', 'PcGts')
#   ('-o', 'ocrd_models/ocrd_models/ocrd_page_generateds.py')
#   ('--silence', '')
#   ('--disable-generatedssuper-lookup', '')
#   ('--user-methods', 'ocrd_models/ocrd_page_user_methods.py')
#
# Command line arguments:
#   ocrd_validators/ocrd_validators/page.xsd
#
# Command line:
#   /home/kba/monorepo/ocrd_all/venv/bin/generateDS -f --root-element="PcGts" -o "ocrd_models/ocrd_models/ocrd_page_generateds.py" --silence --disable-generatedssuper-lookup --user-methods="ocrd_models/ocrd_page_user_methods.py" ocrd_validators/ocrd_validators/page.xsd
#
# Current working directory (os.getcwd()):
#   core
#

from six.moves import zip_longest
import os
import sys
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.


class GeneratedsSuper(object):
    __hash__ = object.__hash__
    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
    class _FixedOffsetTZ(datetime_.tzinfo):
        def __init__(self, offset, name):
            self.__offset = datetime_.timedelta(minutes=offset)
            self.__name = name
        def utcoffset(self, dt):
            return self.__offset
        def tzname(self, dt):
            return self.__name
        def dst(self, dt):
            return None
    def gds_format_string(self, input_data, input_name=''):
        return input_data
    def gds_parse_string(self, input_data, node=None, input_name=''):
        return input_data
    def gds_validate_string(self, input_data, node=None, input_name=''):
        if not input_data:
            return ''
        else:
            return input_data
    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data)
    def gds_validate_base64(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data
    def gds_parse_integer(self, input_data, node=None, input_name=''):
        try:
            ival = int(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires integer value: %s' % exp)
        return ival
    def gds_validate_integer(self, input_data, node=None, input_name=''):
        try:
            value = int(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires integer value')
        return value
    def gds_format_integer_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_integer_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                int(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of integer valuess')
        return values
    def gds_format_float(self, input_data, input_name=''):
        return ('%.15f' % input_data).rstrip('0')
    def gds_parse_float(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires float or double value: %s' % exp)
        return fval_
    def gds_validate_float(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires float value')
        return value
    def gds_format_float_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_float_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of float values')
        return values
    def gds_format_decimal(self, input_data, input_name=''):
        return ('%s' % input_data).rstrip('0')
    def gds_parse_decimal(self, input_data, node=None, input_name=''):
        try:
            decimal_value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return decimal_value
    def gds_validate_decimal(self, input_data, node=None, input_name=''):
        try:
            value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return value
    def gds_format_decimal_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_decimal_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                decimal_.Decimal(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of decimal values')
        return values
    def gds_format_double(self, input_data, input_name=''):
        return '%e' % input_data
    def gds_parse_double(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires double or float value: %s' % exp)
        return fval_
    def gds_validate_double(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires double or float value')
        return value
    def gds_format_double_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_double_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(
                    node, 'Requires sequence of double or float values')
        return values
    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()
    def gds_parse_boolean(self, input_data, node=None, input_name=''):
        if input_data in ('true', '1'):
            bval = True
        elif input_data in ('false', '0'):
            bval = False
        else:
            raise_parse_error(node, 'Requires boolean value')
        return bval
    def gds_validate_boolean(self, input_data, node=None, input_name=''):
        if input_data not in (True, 1, False, 0, ):
            raise_parse_error(
                node,
                'Requires boolean value '
                '(one of True, 1, False, 0)')
        return input_data
    def gds_format_boolean_list(self, input_data, input_name=''):
        return '%s' % ' '.join(input_data)
    def gds_validate_boolean_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires sequence of boolean values '
                    '(one of True, 1, False, 0)')
        return values
    def gds_validate_datetime(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_datetime(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    @classmethod
    def gds_parse_datetime(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        time_parts = input_data.split('.')
        if len(time_parts) > 1:
            micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
            input_data = '%s.%s' % (
                time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt
    def gds_validate_date(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_date(self, input_data, input_name=''):
        _svalue = '%04d-%02d-%02d' % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(
                            hours, minutes)
        except AttributeError:
            pass
        return _svalue
    @classmethod
    def gds_parse_date(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
        dt = dt.replace(tzinfo=tz)
        return dt.date()
    def gds_validate_time(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_time(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%02d:%02d:%02d' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%02d:%02d:%02d.%s' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    def gds_validate_simple_patterns(self, patterns, target):
        # pat is a list of lists of strings/patterns.
        # The target value must match at least one of the patterns
        # in order for the test to succeed.
        found1 = True
        for patterns1 in patterns:
            found2 = False
            for patterns2 in patterns1:
                mo = re_.search(patterns2, target)
                if mo is not None and len(mo.group(0)) == len(target):
                    found2 = True
                    break
            if not found2:
                found1 = False
                break
        return found1
    @classmethod
    def gds_parse_time(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt.time()
    def gds_check_cardinality_(
            self, value, input_name,
            min_occurs=0, max_occurs=1, required=None):
        if value is None:
            length = 0
        elif isinstance(value, list):
            length = len(value)
        else:
            length = 1
        if required is not None :
            if required and length < 1:
                self.gds_collector_.add_message(
                    "Required value {}{} is missing".format(
                        input_name, self.gds_get_node_lineno_()))
        if length < min_occurs:
            self.gds_collector_.add_message(
                "Number of values for {}{} is below "
                "the minimum allowed, "
                "expected at least {}, found {}".format(
                    input_name, self.gds_get_node_lineno_(),
                    min_occurs, length))
        elif length > max_occurs:
            self.gds_collector_.add_message(
                "Number of values for {}{} is above "
                "the maximum allowed, "
                "expected at most {}, found {}".format(
                    input_name, self.gds_get_node_lineno_(),
                    max_occurs, length))
    def gds_validate_builtin_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value, input_name=input_name)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_validate_defined_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_str_lower(self, instring):
        return instring.lower()
    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path
    Tag_strip_pattern_ = re_.compile(r'\{.*\}')
    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)
    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1
    def gds_build_any(self, node, type_name=None):
        # provide default value in case option --disable-xml is used.
        content = ""
        content = etree_.tostring(node, encoding="unicode")
        return content
    @classmethod
    def gds_reverse_node_mapping(cls, mapping):
        return dict(((v, k) for k, v in mapping.items()))
    @staticmethod
    def gds_encode(instring):
        if sys.version_info.major == 2:
            if ExternalEncoding:
                encoding = ExternalEncoding
            else:
                encoding = 'utf-8'
            return instring.encode(encoding)
        else:
            return instring
    @staticmethod
    def convert_unicode(instring):
        if isinstance(instring, str):
            result = quote_xml(instring)
        elif sys.version_info.major == 2 and isinstance(instring, unicode):
            result = quote_xml(instring).encode('utf8')
        else:
            result = GeneratedsSuper.gds_encode(str(instring))
        return result
    def __eq__(self, other):
        def excl_select_objs_(obj):
            return (obj[0] != 'parent_object_' and
                    obj[0] != 'gds_collector_')
        if type(self) != type(other):
            return False
        return all(x == y for x, y in zip_longest(
            filter(excl_select_objs_, self.__dict__.items()),
            filter(excl_select_objs_, other.__dict__.items())))
    def __ne__(self, other):
        return not self.__eq__(other)
    # Django ETL transform hooks.
    def gds_djo_etl_transform(self):
        pass
    def gds_djo_etl_transform_db_obj(self, dbobj):
        pass
    # SQLAlchemy ETL transform hooks.
    def gds_sqa_etl_transform(self):
        return 0, None
    def gds_sqa_etl_transform_db_obj(self, dbobj):
        pass
    def gds_get_node_lineno_(self):
        if (hasattr(self, "gds_elementtree_node_") and
                self.gds_elementtree_node_ is not None):
            return ' near line {}'.format(
                self.gds_elementtree_node_.sourceline)
        else:
            return ""


def getSubclassFromModule_(module, class_):
    '''Get the subclass of a class from a specific module.'''
    name = class_.__name__ + 'Sub'
    if hasattr(module, name):
        return getattr(module, name)
    else:
        return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class AlignSimpleType(str, Enum):
    LEFT='left'
    CENTRE='centre'
    RIGHT='right'
    JUSTIFY='justify'


class ChartTypeSimpleType(str, Enum):
    BAR='bar'
    LINE='line'
    PIE='pie'
    SCATTER='scatter'
    SURFACE='surface'
    OTHER='other'


class ColourDepthSimpleType(str, Enum):
    BILEVEL='bilevel'
    GREYSCALE='greyscale'
    COLOUR='colour'
    OTHER='other'


class ColourSimpleType(str, Enum):
    BLACK='black'
    BLUE='blue'
    BROWN='brown'
    CYAN='cyan'
    GREEN='green'
    GREY='grey'
    INDIGO='indigo'
    MAGENTA='magenta'
    ORANGE='orange'
    PINK='pink'
    RED='red'
    TURQUOISE='turquoise'
    VIOLET='violet'
    WHITE='white'
    YELLOW='yellow'
    OTHER='other'


class GraphicsTypeSimpleType(str, Enum):
    LOGO='logo'
    LETTERHEAD='letterhead'
    DECORATION='decoration'
    FRAME='frame'
    HANDWRITTENANNOTATION='handwritten-annotation'
    STAMP='stamp'
    SIGNATURE='signature'
    BARCODE='barcode'
    PAPERGROW='paper-grow'
    PUNCHHOLE='punch-hole'
    OTHER='other'


class GroupTypeSimpleType(str, Enum):
    PARAGRAPH='paragraph'
    LIST='list'
    LISTITEM='list-item'
    FIGURE='figure'
    ARTICLE='article'
    DIV='div'
    OTHER='other'


class PageTypeSimpleType(str, Enum):
    FRONTCOVER='front-cover'
    BACKCOVER='back-cover'
    TITLE='title'
    TABLEOFCONTENTS='table-of-contents'
    INDEX='index'
    CONTENT='content'
    BLANK='blank'
    OTHER='other'


class ProductionSimpleType(str, Enum):
    """Text production type"""
    PRINTED='printed'
    TYPEWRITTEN='typewritten'
    HANDWRITTENCURSIVE='handwritten-cursive'
    HANDWRITTENPRINTSCRIPT='handwritten-printscript'
    MEDIEVALMANUSCRIPT='medieval-manuscript'
    OTHER='other'


class ReadingDirectionSimpleType(str, Enum):
    LEFTTORIGHT='left-to-right'
    RIGHTTOLEFT='right-to-left'
    TOPTOBOTTOM='top-to-bottom'
    BOTTOMTOTOP='bottom-to-top'


class TextDataTypeSimpleType(str, Enum):
    XSDDECIMAL='xsd:decimal' # Examples: "123.456", "+1234.456", "-1234.456", "-.456", "-456"
    XSDFLOAT='xsd:float' # Examples: "123.456", "+1234.456", "-1.2344e56", "-.45E-6", "INF", "-INF", "NaN"
    XSDINTEGER='xsd:integer' # Examples: "123456", "+00000012", "-1", "-456"
    XSDBOOLEAN='xsd:boolean' # Examples: "true", "false", "1", "0"
    XSDDATE='xsd:date' # Examples: "2001-10-26", "2001-10-26+02:00", "2001-10-26Z", "2001-10-26+00:00", "-2001-10-26", "-20000-04-01"
    XSDTIME='xsd:time' # Examples: "21:32:52", "21:32:52+02:00", "19:32:52Z", "19:32:52+00:00", "21:32:52.12679"
    XSDDATE_TIME='xsd:dateTime' # Examples: "2001-10-26T21:32:52", "2001-10-26T21:32:52+02:00", "2001-10-26T19:32:52Z", "2001-10-26T19:32:52+00:00", "-2001-10-26T21:32:52", "2001-10-26T21:32:52.12679"
    XSDSTRING='xsd:string' # Generic text string
    OTHER='other' # An XSD type that is not listed or a custom type (use dataTypeDetails attribute).


class TextLineOrderSimpleType(str, Enum):
    TOPTOBOTTOM='top-to-bottom'
    BOTTOMTOTOP='bottom-to-top'
    LEFTTORIGHT='left-to-right'
    RIGHTTOLEFT='right-to-left'


class TextTypeSimpleType(str, Enum):
    PARAGRAPH='paragraph'
    HEADING='heading'
    CAPTION='caption'
    HEADER='header'
    FOOTER='footer'
    PAGENUMBER='page-number'
    DROPCAPITAL='drop-capital'
    CREDIT='credit'
    FLOATING='floating'
    SIGNATUREMARK='signature-mark'
    CATCHWORD='catch-word'
    MARGINALIA='marginalia'
    FOOTNOTE='footnote'
    FOOTNOTECONTINUED='footnote-continued'
    ENDNOTE='endnote'
    TOCENTRY='TOC-entry'
    LISTLABEL='list-label'
    OTHER='other'


class UnderlineStyleSimpleType(str, Enum):
    SINGLE_LINE='singleLine'
    DOUBLE_LINE='doubleLine'
    OTHER='other'


class PcGtsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('pcGtsId', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('Metadata', 'MetadataType', 0, 0, {'name': 'Metadata', 'type': 'MetadataType'}, None),
        MemberSpec_('Page', 'PageType', 0, 0, {'name': 'Page', 'type': 'PageType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, pcGtsId=None, Metadata=None, Page=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.pcGtsId = _cast(None, pcGtsId)
        self.pcGtsId_nsprefix_ = "pc"
        self.Metadata = Metadata
        self.Metadata_nsprefix_ = "pc"
        self.Page = Page
        self.Page_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PcGtsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PcGtsType.subclass:
            return PcGtsType.subclass(*args_, **kwargs_)
        else:
            return PcGtsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Metadata(self):
        return self.Metadata
    def set_Metadata(self, Metadata):
        self.Metadata = Metadata
    def get_Page(self):
        return self.Page
    def set_Page(self, Page):
        self.Page = Page
    def get_pcGtsId(self):
        return self.pcGtsId
    def set_pcGtsId(self, pcGtsId):
        self.pcGtsId = pcGtsId
    def hasContent_(self):
        if (
            self.Metadata is not None or
            self.Page is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='PcGtsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PcGtsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PcGtsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PcGtsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PcGtsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PcGtsType'):
        if self.pcGtsId is not None and 'pcGtsId' not in already_processed:
            already_processed.add('pcGtsId')
            outfile.write(' pcGtsId=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pcGtsId), input_name='pcGtsId')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='PcGtsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Metadata is not None:
            namespaceprefix_ = self.Metadata_nsprefix_ + ':' if (UseCapturedNS_ and self.Metadata_nsprefix_) else ''
            self.Metadata.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Metadata', pretty_print=pretty_print)
        if self.Page is not None:
            namespaceprefix_ = self.Page_nsprefix_ + ':' if (UseCapturedNS_ and self.Page_nsprefix_) else ''
            self.Page.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Page', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('pcGtsId', node)
        if value is not None and 'pcGtsId' not in already_processed:
            already_processed.add('pcGtsId')
            self.pcGtsId = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Metadata':
            obj_ = MetadataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Metadata = obj_
            obj_.original_tagname_ = 'Metadata'
        elif nodeName_ == 'Page':
            obj_ = PageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Page = obj_
            obj_.original_tagname_ = 'Page'
    def __hash__(self):
        return hash(self.id)
    @property
    def id(self):
        if hasattr(self, 'pcGtsId'):
            return self.pcGtsId
        return self.imageFilename
    def get_AllAlternativeImagePaths(self, page=True, region=True, line=True, word=True, glyph=True):
        """
        Get all the pc:AlternativeImage/@filename paths referenced in the PAGE-XML document.
    
    
        page (boolean): Get pc:Page level images
        region (boolean): Get images on pc:*Region level
        line (boolean) Get images on pc:TextLine level
        word (boolean) Get images on pc:Word level
        glyph (boolean) Get images on pc:Glyph level
        """
        from .constants import NAMESPACES, PAGE_REGION_TYPES # pylint: disable=relative-beyond-top-level,import-outside-toplevel
        from io import StringIO  # pylint: disable=import-outside-toplevel
        ret = []
        # XXX Since we're only interested in the **paths** of the images,
        # export, parse and xpath are less convoluted than traversing
        # the generateDS API. Quite possibly not as efficient as could be.
        sio = StringIO()
        self.export(
                outfile=sio,
                level=0,
                name_='PcGts',
                namespaceprefix_='pc:',
                namespacedef_='xmlns:pc="%s" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="%s %s/pagecontent.xsd"' % (
                    NAMESPACES['page'],
                    NAMESPACES['page'],
                    NAMESPACES['page']
                ))
        doc = parsexmlstring_(sio.getvalue())  # pylint: disable=undefined-variable
        # shortcut
        if page and region and line and word and glyph:
            ret += doc.xpath('//page:AlternativeImage/@filename', namespaces=NAMESPACES)
        else:
            if page:
                ret += doc.xpath('/page:PcGts/page:Page/page:AlternativeImage/@filename', namespaces=NAMESPACES)
            if region:
                for class_ in PAGE_REGION_TYPES:
                    ret += doc.xpath('//page:%sRegion/page:AlternativeImage/@filename' % class_, namespaces=NAMESPACES)
            if line:
                ret += doc.xpath('//page:TextLine/page:AlternativeImage/@filename', namespaces=NAMESPACES)
            if word:
                ret += doc.xpath('//page:Word/page:AlternativeImage/@filename', namespaces=NAMESPACES)
            if glyph:
                ret += doc.xpath('//page:Glyph/page:AlternativeImage/@filename', namespaces=NAMESPACES)
    
        return ret
    def prune_ReadingOrder(self):
        """
        Remove any empty ReadingOrder elements
        """
        ro = self.get_Page().get_ReadingOrder()
        if ro:
            og = ro.get_OrderedGroup()
            if og and (not og.get_RegionRefIndexed() and
                       not og.get_OrderedGroupIndexed() and
                       not og.get_UnorderedGroupIndexed()):
                og = None
            ug = ro.get_UnorderedGroup()
            if ug and (not ug.get_RegionRef() and
                       not ug.get_OrderedGroup() and
                       not ug.get_UnorderedGroup()):
                ug = None
            if not og and not ug:
                self.get_Page().set_ReadingOrder(None)
# end class PcGtsType


class MetadataType(GeneratedsSuper):
    """External reference of any kind"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('externalRef', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('Creator', 'string', 0, 0, {'name': 'Creator', 'type': 'string'}, None),
        MemberSpec_('Created', 'dateTime', 0, 0, {'name': 'Created', 'type': 'dateTime'}, None),
        MemberSpec_('LastChange', 'dateTime', 0, 0, {'name': 'LastChange', 'type': 'dateTime'}, None),
        MemberSpec_('Comments', 'string', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Comments', 'type': 'string'}, None),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('MetadataItem', 'MetadataItemType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'MetadataItem', 'type': 'MetadataItemType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, externalRef=None, Creator=None, Created=None, LastChange=None, Comments=None, UserDefined=None, MetadataItem=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.externalRef = _cast(None, externalRef)
        self.externalRef_nsprefix_ = "pc"
        self.Creator = Creator
        self.Creator_nsprefix_ = "pc"
        if isinstance(Created, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(Created, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = Created
        self.Created = initvalue_
        self.Created_nsprefix_ = "pc"
        if isinstance(LastChange, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(LastChange, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = LastChange
        self.LastChange = initvalue_
        self.LastChange_nsprefix_ = "pc"
        self.Comments = Comments
        self.Comments_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if MetadataItem is None:
            self.MetadataItem = []
        else:
            self.MetadataItem = MetadataItem
        self.MetadataItem_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetadataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetadataType.subclass:
            return MetadataType.subclass(*args_, **kwargs_)
        else:
            return MetadataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Creator(self):
        return self.Creator
    def set_Creator(self, Creator):
        self.Creator = Creator
    def get_Created(self):
        return self.Created
    def set_Created(self, Created):
        self.Created = Created
    def get_LastChange(self):
        return self.LastChange
    def set_LastChange(self, LastChange):
        self.LastChange = LastChange
    def get_Comments(self):
        return self.Comments
    def set_Comments(self, Comments):
        self.Comments = Comments
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_MetadataItem(self):
        return self.MetadataItem
    def set_MetadataItem(self, MetadataItem):
        self.MetadataItem = MetadataItem
    def add_MetadataItem(self, value):
        self.MetadataItem.append(value)
    def insert_MetadataItem_at(self, index, value):
        self.MetadataItem.insert(index, value)
    def replace_MetadataItem_at(self, index, value):
        self.MetadataItem[index] = value
    def get_externalRef(self):
        return self.externalRef
    def set_externalRef(self, externalRef):
        self.externalRef = externalRef
    def hasContent_(self):
        if (
            self.Creator is not None or
            self.Created is not None or
            self.LastChange is not None or
            self.Comments is not None or
            self.UserDefined is not None or
            self.MetadataItem
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='MetadataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetadataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetadataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetadataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetadataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetadataType'):
        if self.externalRef is not None and 'externalRef' not in already_processed:
            already_processed.add('externalRef')
            outfile.write(' externalRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.externalRef), input_name='externalRef')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='MetadataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Creator is not None:
            namespaceprefix_ = self.Creator_nsprefix_ + ':' if (UseCapturedNS_ and self.Creator_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCreator>%s</%sCreator>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Creator), input_name='Creator')), namespaceprefix_ , eol_))
        if self.Created is not None:
            namespaceprefix_ = self.Created_nsprefix_ + ':' if (UseCapturedNS_ and self.Created_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCreated>%s</%sCreated>%s' % (namespaceprefix_ , self.gds_format_datetime(self.Created, input_name='Created'), namespaceprefix_ , eol_))
        if self.LastChange is not None:
            namespaceprefix_ = self.LastChange_nsprefix_ + ':' if (UseCapturedNS_ and self.LastChange_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLastChange>%s</%sLastChange>%s' % (namespaceprefix_ , self.gds_format_datetime(self.LastChange, input_name='LastChange'), namespaceprefix_ , eol_))
        if self.Comments is not None:
            namespaceprefix_ = self.Comments_nsprefix_ + ':' if (UseCapturedNS_ and self.Comments_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sComments>%s</%sComments>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Comments), input_name='Comments')), namespaceprefix_ , eol_))
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for MetadataItem_ in self.MetadataItem:
            namespaceprefix_ = self.MetadataItem_nsprefix_ + ':' if (UseCapturedNS_ and self.MetadataItem_nsprefix_) else ''
            MetadataItem_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MetadataItem', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('externalRef', node)
        if value is not None and 'externalRef' not in already_processed:
            already_processed.add('externalRef')
            self.externalRef = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Creator':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Creator')
            value_ = self.gds_validate_string(value_, node, 'Creator')
            self.Creator = value_

        elif nodeName_ == 'Created':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.Created = dval_

        elif nodeName_ == 'LastChange':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.LastChange = dval_

        elif nodeName_ == 'Comments':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Comments')
            value_ = self.gds_validate_string(value_, node, 'Comments')
            self.Comments = value_

        elif nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'MetadataItem':
            obj_ = MetadataItemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MetadataItem.append(obj_)
            obj_.original_tagname_ = 'MetadataItem'
    def __hash__(self):
        return hash(self.id)
# end class MetadataType


class MetadataItemType(GeneratedsSuper):
    """Type of metadata (e.g. author)
    E.g. imagePhotometricInterpretation
    E.g. RGB"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('type_', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('name', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('value', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('date', 'dateTime', 0, 1, {'use': 'optional'}),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, type_=None, name=None, value=None, date=None, Labels=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.name = _cast(None, name)
        self.name_nsprefix_ = "pc"
        self.value = _cast(None, value)
        self.value_nsprefix_ = "pc"
        if isinstance(date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = date
        self.date = initvalue_
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MetadataItemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MetadataItemType.subclass:
            return MetadataItemType.subclass(*args_, **kwargs_)
        else:
            return MetadataItemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    def hasContent_(self):
        if (
            self.Labels
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='MetadataItemType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MetadataItemType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MetadataItemType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MetadataItemType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MetadataItemType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MetadataItemType'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.value), input_name='value')), ))
        if self.date is not None and 'date' not in already_processed:
            already_processed.add('date')
            outfile.write(' date="%s"' % self.gds_format_datetime(self.date, input_name='date'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='MetadataItemType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('value', node)
        if value is not None and 'value' not in already_processed:
            already_processed.add('value')
            self.value = value
        value = find_attr_value_('date', node)
        if value is not None and 'date' not in already_processed:
            already_processed.add('date')
            try:
                self.date = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (date): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
    def __hash__(self):
        return hash(self.id)
# end class MetadataItemType


class LabelsType(GeneratedsSuper):
    """Reference to external model / ontology / schema
    E.g. an RDF resource identifier
    (to be used as subject or object of an RDF triple)
    Prefix for all labels (e.g. first part of an URI)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('externalModel', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('externalId', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('prefix', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('Label', 'LabelType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Label', 'type': 'LabelType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, externalModel=None, externalId=None, prefix=None, comments=None, Label=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.externalModel = _cast(None, externalModel)
        self.externalModel_nsprefix_ = "pc"
        self.externalId = _cast(None, externalId)
        self.externalId_nsprefix_ = "pc"
        self.prefix = _cast(None, prefix)
        self.prefix_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        if Label is None:
            self.Label = []
        else:
            self.Label = Label
        self.Label_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LabelsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LabelsType.subclass:
            return LabelsType.subclass(*args_, **kwargs_)
        else:
            return LabelsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Label(self):
        return self.Label
    def set_Label(self, Label):
        self.Label = Label
    def add_Label(self, value):
        self.Label.append(value)
    def insert_Label_at(self, index, value):
        self.Label.insert(index, value)
    def replace_Label_at(self, index, value):
        self.Label[index] = value
    def get_externalModel(self):
        return self.externalModel
    def set_externalModel(self, externalModel):
        self.externalModel = externalModel
    def get_externalId(self):
        return self.externalId
    def set_externalId(self, externalId):
        self.externalId = externalId
    def get_prefix(self):
        return self.prefix
    def set_prefix(self, prefix):
        self.prefix = prefix
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def hasContent_(self):
        if (
            self.Label
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LabelsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LabelsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LabelsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LabelsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LabelsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LabelsType'):
        if self.externalModel is not None and 'externalModel' not in already_processed:
            already_processed.add('externalModel')
            outfile.write(' externalModel=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.externalModel), input_name='externalModel')), ))
        if self.externalId is not None and 'externalId' not in already_processed:
            already_processed.add('externalId')
            outfile.write(' externalId=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.externalId), input_name='externalId')), ))
        if self.prefix is not None and 'prefix' not in already_processed:
            already_processed.add('prefix')
            outfile.write(' prefix=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.prefix), input_name='prefix')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LabelsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Label_ in self.Label:
            namespaceprefix_ = self.Label_nsprefix_ + ':' if (UseCapturedNS_ and self.Label_nsprefix_) else ''
            Label_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Label', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('externalModel', node)
        if value is not None and 'externalModel' not in already_processed:
            already_processed.add('externalModel')
            self.externalModel = value
        value = find_attr_value_('externalId', node)
        if value is not None and 'externalId' not in already_processed:
            already_processed.add('externalId')
            self.externalId = value
        value = find_attr_value_('prefix', node)
        if value is not None and 'prefix' not in already_processed:
            already_processed.add('prefix')
            self.prefix = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Label':
            obj_ = LabelType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Label.append(obj_)
            obj_.original_tagname_ = 'Label'
    def __hash__(self):
        return hash(self.id)
# end class LabelsType


class LabelType(GeneratedsSuper):
    """Semantic label
    The label / tag (e.g. 'person').
    Can be an RDF resource identifier
    (e.g. object of an RDF triple).
    Additional information on the label
    (e.g. 'YYYY-mm-dd' for a date label).
    Can be used as predicate of an RDF triple."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('value', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('type_', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, value=None, type_=None, comments=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = _cast(None, value)
        self.value_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LabelType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LabelType.subclass:
            return LabelType.subclass(*args_, **kwargs_)
        else:
            return LabelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LabelType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LabelType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LabelType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LabelType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LabelType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LabelType'):
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.value), input_name='value')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LabelType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('value', node)
        if value is not None and 'value' not in already_processed:
            already_processed.add('value')
            self.value = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class LabelType


class PageType(GeneratedsSuper):
    """Contains the image file name including the file extension.
    Specifies the width of the image.Specifies the height of the
    image.Specifies the image resolution in width.Specifies the image
    resolution in height.
    Specifies the unit of the resolution information
    referring to a standardised unit of measurement
    (pixels per inch, pixels per centimeter or other).
    For generic use
    The angle the rectangle encapsulating the page
    (or its Border) has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    (The rotated image can be further referenced
    via “AlternativeImage”.)
    Range: -179.999,180
    The type of the page within the document
    (e.g. cover page).
    The primary language used in the page
    (lower-level definitions override the page-level definition).
    The secondary language used in the page
    (lower-level definitions override the page-level definition).
    The primary script used in the page
    (lower-level definitions override the page-level definition).
    The secondary script used in the page
    (lower-level definitions override the page-level definition).
    The direction in which text within lines
    should be read (order of words and characters),
    in addition to “textLineOrder”
    (lower-level definitions override the page-level definition).
    The order of text lines within a block,
    in addition to “readingDirection”
    (lower-level definitions override the page-level definition).
    Confidence value for whole page (between 0 and 1)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('imageFilename', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('imageWidth', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('imageHeight', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('imageXResolution', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('imageYResolution', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('imageResolutionUnit', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:PageTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('primaryLanguage', 'pc:LanguageSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('secondaryLanguage', 'pc:LanguageSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('primaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('secondaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('readingDirection', 'pc:ReadingDirectionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('textLineOrder', 'pc:TextLineOrderSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('conf', 'pc:ConfSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('AlternativeImage', 'AlternativeImageType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'AlternativeImage', 'type': 'AlternativeImageType'}, None),
        MemberSpec_('Border', 'BorderType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Border', 'type': 'BorderType'}, None),
        MemberSpec_('PrintSpace', 'PrintSpaceType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'PrintSpace', 'type': 'PrintSpaceType'}, None),
        MemberSpec_('ReadingOrder', 'ReadingOrderType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'ReadingOrder', 'type': 'ReadingOrderType'}, None),
        MemberSpec_('Layers', 'LayersType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Layers', 'type': 'LayersType'}, None),
        MemberSpec_('Relations', 'RelationsType', 0, 1, {'minOccurs': '0', 'name': 'Relations', 'type': 'RelationsType'}, None),
        MemberSpec_('TextStyle', 'TextStyleType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'TextStyle', 'type': 'TextStyleType'}, None),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('TextRegion', 'TextRegionType', 1, 1, {'name': 'TextRegion', 'type': 'TextRegionType'}, 1),
        MemberSpec_('ImageRegion', 'ImageRegionType', 1, 1, {'name': 'ImageRegion', 'type': 'ImageRegionType'}, 1),
        MemberSpec_('LineDrawingRegion', 'LineDrawingRegionType', 1, 1, {'name': 'LineDrawingRegion', 'type': 'LineDrawingRegionType'}, 1),
        MemberSpec_('GraphicRegion', 'GraphicRegionType', 1, 1, {'name': 'GraphicRegion', 'type': 'GraphicRegionType'}, 1),
        MemberSpec_('TableRegion', 'TableRegionType', 1, 1, {'name': 'TableRegion', 'type': 'TableRegionType'}, 1),
        MemberSpec_('ChartRegion', 'ChartRegionType', 1, 1, {'name': 'ChartRegion', 'type': 'ChartRegionType'}, 1),
        MemberSpec_('MapRegion', 'MapRegionType', 1, 1, {'name': 'MapRegion', 'type': 'MapRegionType'}, 1),
        MemberSpec_('SeparatorRegion', 'SeparatorRegionType', 1, 1, {'name': 'SeparatorRegion', 'type': 'SeparatorRegionType'}, 1),
        MemberSpec_('MathsRegion', 'MathsRegionType', 1, 1, {'name': 'MathsRegion', 'type': 'MathsRegionType'}, 1),
        MemberSpec_('ChemRegion', 'ChemRegionType', 1, 1, {'name': 'ChemRegion', 'type': 'ChemRegionType'}, 1),
        MemberSpec_('MusicRegion', 'MusicRegionType', 1, 1, {'name': 'MusicRegion', 'type': 'MusicRegionType'}, 1),
        MemberSpec_('AdvertRegion', 'AdvertRegionType', 1, 1, {'name': 'AdvertRegion', 'type': 'AdvertRegionType'}, 1),
        MemberSpec_('NoiseRegion', 'NoiseRegionType', 1, 1, {'name': 'NoiseRegion', 'type': 'NoiseRegionType'}, 1),
        MemberSpec_('UnknownRegion', 'UnknownRegionType', 1, 1, {'name': 'UnknownRegion', 'type': 'UnknownRegionType'}, 1),
        MemberSpec_('CustomRegion', 'CustomRegionType', 1, 1, {'name': 'CustomRegion', 'type': 'CustomRegionType'}, 1),
    ]
    subclass = None
    superclass = None
    def __init__(self, imageFilename=None, imageWidth=None, imageHeight=None, imageXResolution=None, imageYResolution=None, imageResolutionUnit=None, custom=None, orientation=None, type_=None, primaryLanguage=None, secondaryLanguage=None, primaryScript=None, secondaryScript=None, readingDirection=None, textLineOrder=None, conf=None, AlternativeImage=None, Border=None, PrintSpace=None, ReadingOrder=None, Layers=None, Relations=None, TextStyle=None, UserDefined=None, Labels=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, MapRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.imageFilename = _cast(None, imageFilename)
        self.imageFilename_nsprefix_ = "pc"
        self.imageWidth = _cast(int, imageWidth)
        self.imageWidth_nsprefix_ = "pc"
        self.imageHeight = _cast(int, imageHeight)
        self.imageHeight_nsprefix_ = "pc"
        self.imageXResolution = _cast(float, imageXResolution)
        self.imageXResolution_nsprefix_ = "pc"
        self.imageYResolution = _cast(float, imageYResolution)
        self.imageYResolution_nsprefix_ = "pc"
        self.imageResolutionUnit = _cast(None, imageResolutionUnit)
        self.imageResolutionUnit_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.primaryLanguage = _cast(None, primaryLanguage)
        self.primaryLanguage_nsprefix_ = "pc"
        self.secondaryLanguage = _cast(None, secondaryLanguage)
        self.secondaryLanguage_nsprefix_ = "pc"
        self.primaryScript = _cast(None, primaryScript)
        self.primaryScript_nsprefix_ = "pc"
        self.secondaryScript = _cast(None, secondaryScript)
        self.secondaryScript_nsprefix_ = "pc"
        self.readingDirection = _cast(None, readingDirection)
        self.readingDirection_nsprefix_ = "pc"
        self.textLineOrder = _cast(None, textLineOrder)
        self.textLineOrder_nsprefix_ = "pc"
        self.conf = _cast(float, conf)
        self.conf_nsprefix_ = "pc"
        if AlternativeImage is None:
            self.AlternativeImage = []
        else:
            self.AlternativeImage = AlternativeImage
        self.AlternativeImage_nsprefix_ = "pc"
        self.Border = Border
        self.Border_nsprefix_ = "pc"
        self.PrintSpace = PrintSpace
        self.PrintSpace_nsprefix_ = "pc"
        self.ReadingOrder = ReadingOrder
        self.ReadingOrder_nsprefix_ = "pc"
        self.Layers = Layers
        self.Layers_nsprefix_ = "pc"
        self.Relations = Relations
        self.Relations_nsprefix_ = "pc"
        self.TextStyle = TextStyle
        self.TextStyle_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        if TextRegion is None:
            self.TextRegion = []
        else:
            self.TextRegion = TextRegion
        self.TextRegion_nsprefix_ = "pc"
        if ImageRegion is None:
            self.ImageRegion = []
        else:
            self.ImageRegion = ImageRegion
        self.ImageRegion_nsprefix_ = "pc"
        if LineDrawingRegion is None:
            self.LineDrawingRegion = []
        else:
            self.LineDrawingRegion = LineDrawingRegion
        self.LineDrawingRegion_nsprefix_ = "pc"
        if GraphicRegion is None:
            self.GraphicRegion = []
        else:
            self.GraphicRegion = GraphicRegion
        self.GraphicRegion_nsprefix_ = "pc"
        if TableRegion is None:
            self.TableRegion = []
        else:
            self.TableRegion = TableRegion
        self.TableRegion_nsprefix_ = "pc"
        if ChartRegion is None:
            self.ChartRegion = []
        else:
            self.ChartRegion = ChartRegion
        self.ChartRegion_nsprefix_ = "pc"
        if MapRegion is None:
            self.MapRegion = []
        else:
            self.MapRegion = MapRegion
        self.MapRegion_nsprefix_ = "pc"
        if SeparatorRegion is None:
            self.SeparatorRegion = []
        else:
            self.SeparatorRegion = SeparatorRegion
        self.SeparatorRegion_nsprefix_ = "pc"
        if MathsRegion is None:
            self.MathsRegion = []
        else:
            self.MathsRegion = MathsRegion
        self.MathsRegion_nsprefix_ = "pc"
        if ChemRegion is None:
            self.ChemRegion = []
        else:
            self.ChemRegion = ChemRegion
        self.ChemRegion_nsprefix_ = "pc"
        if MusicRegion is None:
            self.MusicRegion = []
        else:
            self.MusicRegion = MusicRegion
        self.MusicRegion_nsprefix_ = "pc"
        if AdvertRegion is None:
            self.AdvertRegion = []
        else:
            self.AdvertRegion = AdvertRegion
        self.AdvertRegion_nsprefix_ = "pc"
        if NoiseRegion is None:
            self.NoiseRegion = []
        else:
            self.NoiseRegion = NoiseRegion
        self.NoiseRegion_nsprefix_ = "pc"
        if UnknownRegion is None:
            self.UnknownRegion = []
        else:
            self.UnknownRegion = UnknownRegion
        self.UnknownRegion_nsprefix_ = "pc"
        if CustomRegion is None:
            self.CustomRegion = []
        else:
            self.CustomRegion = CustomRegion
        self.CustomRegion_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PageType.subclass:
            return PageType.subclass(*args_, **kwargs_)
        else:
            return PageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AlternativeImage(self):
        return self.AlternativeImage
    def set_AlternativeImage(self, AlternativeImage):
        self.AlternativeImage = AlternativeImage
    def add_AlternativeImage(self, value):
        self.AlternativeImage.append(value)
    def insert_AlternativeImage_at(self, index, value):
        self.AlternativeImage.insert(index, value)
    def replace_AlternativeImage_at(self, index, value):
        self.AlternativeImage[index] = value
    def get_Border(self):
        return self.Border
    def set_Border(self, Border):
        self.Border = Border
    def get_PrintSpace(self):
        return self.PrintSpace
    def set_PrintSpace(self, PrintSpace):
        self.PrintSpace = PrintSpace
    def get_ReadingOrder(self):
        return self.ReadingOrder
    def set_ReadingOrder(self, ReadingOrder):
        self.ReadingOrder = ReadingOrder
    def get_Layers(self):
        return self.Layers
    def set_Layers(self, Layers):
        self.Layers = Layers
    def get_Relations(self):
        return self.Relations
    def set_Relations(self, Relations):
        self.Relations = Relations
    def get_TextStyle(self):
        return self.TextStyle
    def set_TextStyle(self, TextStyle):
        self.TextStyle = TextStyle
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_TextRegion(self):
        return self.TextRegion
    def set_TextRegion(self, TextRegion):
        self.TextRegion = TextRegion
    def add_TextRegion(self, value):
        self.TextRegion.append(value)
    def insert_TextRegion_at(self, index, value):
        self.TextRegion.insert(index, value)
    def replace_TextRegion_at(self, index, value):
        self.TextRegion[index] = value
    def get_ImageRegion(self):
        return self.ImageRegion
    def set_ImageRegion(self, ImageRegion):
        self.ImageRegion = ImageRegion
    def add_ImageRegion(self, value):
        self.ImageRegion.append(value)
    def insert_ImageRegion_at(self, index, value):
        self.ImageRegion.insert(index, value)
    def replace_ImageRegion_at(self, index, value):
        self.ImageRegion[index] = value
    def get_LineDrawingRegion(self):
        return self.LineDrawingRegion
    def set_LineDrawingRegion(self, LineDrawingRegion):
        self.LineDrawingRegion = LineDrawingRegion
    def add_LineDrawingRegion(self, value):
        self.LineDrawingRegion.append(value)
    def insert_LineDrawingRegion_at(self, index, value):
        self.LineDrawingRegion.insert(index, value)
    def replace_LineDrawingRegion_at(self, index, value):
        self.LineDrawingRegion[index] = value
    def get_GraphicRegion(self):
        return self.GraphicRegion
    def set_GraphicRegion(self, GraphicRegion):
        self.GraphicRegion = GraphicRegion
    def add_GraphicRegion(self, value):
        self.GraphicRegion.append(value)
    def insert_GraphicRegion_at(self, index, value):
        self.GraphicRegion.insert(index, value)
    def replace_GraphicRegion_at(self, index, value):
        self.GraphicRegion[index] = value
    def get_TableRegion(self):
        return self.TableRegion
    def set_TableRegion(self, TableRegion):
        self.TableRegion = TableRegion
    def add_TableRegion(self, value):
        self.TableRegion.append(value)
    def insert_TableRegion_at(self, index, value):
        self.TableRegion.insert(index, value)
    def replace_TableRegion_at(self, index, value):
        self.TableRegion[index] = value
    def get_ChartRegion(self):
        return self.ChartRegion
    def set_ChartRegion(self, ChartRegion):
        self.ChartRegion = ChartRegion
    def add_ChartRegion(self, value):
        self.ChartRegion.append(value)
    def insert_ChartRegion_at(self, index, value):
        self.ChartRegion.insert(index, value)
    def replace_ChartRegion_at(self, index, value):
        self.ChartRegion[index] = value
    def get_MapRegion(self):
        return self.MapRegion
    def set_MapRegion(self, MapRegion):
        self.MapRegion = MapRegion
    def add_MapRegion(self, value):
        self.MapRegion.append(value)
    def insert_MapRegion_at(self, index, value):
        self.MapRegion.insert(index, value)
    def replace_MapRegion_at(self, index, value):
        self.MapRegion[index] = value
    def get_SeparatorRegion(self):
        return self.SeparatorRegion
    def set_SeparatorRegion(self, SeparatorRegion):
        self.SeparatorRegion = SeparatorRegion
    def add_SeparatorRegion(self, value):
        self.SeparatorRegion.append(value)
    def insert_SeparatorRegion_at(self, index, value):
        self.SeparatorRegion.insert(index, value)
    def replace_SeparatorRegion_at(self, index, value):
        self.SeparatorRegion[index] = value
    def get_MathsRegion(self):
        return self.MathsRegion
    def set_MathsRegion(self, MathsRegion):
        self.MathsRegion = MathsRegion
    def add_MathsRegion(self, value):
        self.MathsRegion.append(value)
    def insert_MathsRegion_at(self, index, value):
        self.MathsRegion.insert(index, value)
    def replace_MathsRegion_at(self, index, value):
        self.MathsRegion[index] = value
    def get_ChemRegion(self):
        return self.ChemRegion
    def set_ChemRegion(self, ChemRegion):
        self.ChemRegion = ChemRegion
    def add_ChemRegion(self, value):
        self.ChemRegion.append(value)
    def insert_ChemRegion_at(self, index, value):
        self.ChemRegion.insert(index, value)
    def replace_ChemRegion_at(self, index, value):
        self.ChemRegion[index] = value
    def get_MusicRegion(self):
        return self.MusicRegion
    def set_MusicRegion(self, MusicRegion):
        self.MusicRegion = MusicRegion
    def add_MusicRegion(self, value):
        self.MusicRegion.append(value)
    def insert_MusicRegion_at(self, index, value):
        self.MusicRegion.insert(index, value)
    def replace_MusicRegion_at(self, index, value):
        self.MusicRegion[index] = value
    def get_AdvertRegion(self):
        return self.AdvertRegion
    def set_AdvertRegion(self, AdvertRegion):
        self.AdvertRegion = AdvertRegion
    def add_AdvertRegion(self, value):
        self.AdvertRegion.append(value)
    def insert_AdvertRegion_at(self, index, value):
        self.AdvertRegion.insert(index, value)
    def replace_AdvertRegion_at(self, index, value):
        self.AdvertRegion[index] = value
    def get_NoiseRegion(self):
        return self.NoiseRegion
    def set_NoiseRegion(self, NoiseRegion):
        self.NoiseRegion = NoiseRegion
    def add_NoiseRegion(self, value):
        self.NoiseRegion.append(value)
    def insert_NoiseRegion_at(self, index, value):
        self.NoiseRegion.insert(index, value)
    def replace_NoiseRegion_at(self, index, value):
        self.NoiseRegion[index] = value
    def get_UnknownRegion(self):
        return self.UnknownRegion
    def set_UnknownRegion(self, UnknownRegion):
        self.UnknownRegion = UnknownRegion
    def add_UnknownRegion(self, value):
        self.UnknownRegion.append(value)
    def insert_UnknownRegion_at(self, index, value):
        self.UnknownRegion.insert(index, value)
    def replace_UnknownRegion_at(self, index, value):
        self.UnknownRegion[index] = value
    def get_CustomRegion(self):
        return self.CustomRegion
    def set_CustomRegion(self, CustomRegion):
        self.CustomRegion = CustomRegion
    def add_CustomRegion(self, value):
        self.CustomRegion.append(value)
    def insert_CustomRegion_at(self, index, value):
        self.CustomRegion.insert(index, value)
    def replace_CustomRegion_at(self, index, value):
        self.CustomRegion[index] = value
    def get_imageFilename(self):
        return self.imageFilename
    def set_imageFilename(self, imageFilename):
        self.imageFilename = imageFilename
    def get_imageWidth(self):
        return self.imageWidth
    def set_imageWidth(self, imageWidth):
        self.imageWidth = imageWidth
    def get_imageHeight(self):
        return self.imageHeight
    def set_imageHeight(self, imageHeight):
        self.imageHeight = imageHeight
    def get_imageXResolution(self):
        return self.imageXResolution
    def set_imageXResolution(self, imageXResolution):
        self.imageXResolution = imageXResolution
    def get_imageYResolution(self):
        return self.imageYResolution
    def set_imageYResolution(self, imageYResolution):
        self.imageYResolution = imageYResolution
    def get_imageResolutionUnit(self):
        return self.imageResolutionUnit
    def set_imageResolutionUnit(self, imageResolutionUnit):
        self.imageResolutionUnit = imageResolutionUnit
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_primaryLanguage(self):
        return self.primaryLanguage
    def set_primaryLanguage(self, primaryLanguage):
        self.primaryLanguage = primaryLanguage
    def get_secondaryLanguage(self):
        return self.secondaryLanguage
    def set_secondaryLanguage(self, secondaryLanguage):
        self.secondaryLanguage = secondaryLanguage
    def get_primaryScript(self):
        return self.primaryScript
    def set_primaryScript(self, primaryScript):
        self.primaryScript = primaryScript
    def get_secondaryScript(self):
        return self.secondaryScript
    def set_secondaryScript(self, secondaryScript):
        self.secondaryScript = secondaryScript
    def get_readingDirection(self):
        return self.readingDirection
    def set_readingDirection(self, readingDirection):
        self.readingDirection = readingDirection
    def get_textLineOrder(self):
        return self.textLineOrder
    def set_textLineOrder(self, textLineOrder):
        self.textLineOrder = textLineOrder
    def get_conf(self):
        return self.conf
    def set_conf(self, conf):
        self.conf = conf
    def validate_PageTypeSimpleType(self, value):
        # Validate type pc:PageTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['front-cover', 'back-cover', 'title', 'table-of-contents', 'index', 'content', 'blank', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on PageTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_LanguageSimpleType(self, value):
        # Validate type pc:LanguageSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Abkhaz', 'Afar', 'Afrikaans', 'Akan', 'Albanian', 'Amharic', 'Arabic', 'Aragonese', 'Armenian', 'Assamese', 'Avaric', 'Avestan', 'Aymara', 'Azerbaijani', 'Bambara', 'Bashkir', 'Basque', 'Belarusian', 'Bengali', 'Bihari', 'Bislama', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', 'Cambodian', 'Cantonese', 'Catalan', 'Chamorro', 'Chechen', 'Chichewa', 'Chinese', 'Chuvash', 'Cornish', 'Corsican', 'Cree', 'Croatian', 'Czech', 'Danish', 'Divehi', 'Dutch', 'Dzongkha', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'French', 'Fula', 'Gaelic', 'Galician', 'Ganda', 'Georgian', 'German', 'Greek', 'Guaraní', 'Gujarati', 'Haitian', 'Hausa', 'Hebrew', 'Herero', 'Hindi', 'Hiri Motu', 'Hungarian', 'Icelandic', 'Ido', 'Igbo', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiaq', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kalaallisut', 'Kannada', 'Kanuri', 'Kashmiri', 'Kazakh', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kirundi', 'Komi', 'Kongo', 'Korean', 'Kurdish', 'Kwanyama', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Limburgish', 'Lingala', 'Lithuanian', 'Luba-Katanga', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Manx', 'Māori', 'Marathi', 'Marshallese', 'Mongolian', 'Nauru', 'Navajo', 'Ndonga', 'Nepali', 'North Ndebele', 'Northern Sami', 'Norwegian', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Nuosu', 'Occitan', 'Ojibwe', 'Old Church Slavonic', 'Oriya', 'Oromo', 'Ossetian', 'Pāli', 'Panjabi', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Romansh', 'Russian', 'Samoan', 'Sango', 'Sanskrit', 'Sardinian', 'Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovene', 'Somali', 'South Ndebele', 'Southern Sotho', 'Spanish', 'Sundanese', 'Swahili', 'Swati', 'Swedish', 'Tagalog', 'Tahitian', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Tswana', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda', 'Vietnamese', 'Volapük', 'Walloon', 'Welsh', 'Western Frisian', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zhuang', 'Zulu', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LanguageSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ScriptSimpleType(self, value):
        # Validate type pc:ScriptSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Adlm - Adlam', 'Afak - Afaka', 'Aghb - Caucasian Albanian', 'Ahom - Ahom, Tai Ahom', 'Arab - Arabic', 'Aran - Arabic (Nastaliq variant)', 'Armi - Imperial Aramaic', 'Armn - Armenian', 'Avst - Avestan', 'Bali - Balinese', 'Bamu - Bamum', 'Bass - Bassa Vah', 'Batk - Batak', 'Beng - Bengali', 'Bhks - Bhaiksuki', 'Blis - Blissymbols', 'Bopo - Bopomofo', 'Brah - Brahmi', 'Brai - Braille', 'Bugi - Buginese', 'Buhd - Buhid', 'Cakm - Chakma', 'Cans - Unified Canadian Aboriginal Syllabics', 'Cari - Carian', 'Cham - Cham', 'Cher - Cherokee', 'Cirt - Cirth', 'Copt - Coptic', 'Cprt - Cypriot', 'Cyrl - Cyrillic', 'Cyrs - Cyrillic (Old Church Slavonic variant)', 'Deva - Devanagari (Nagari)', 'Dsrt - Deseret (Mormon)', 'Dupl - Duployan shorthand, Duployan stenography', 'Egyd - Egyptian demotic', 'Egyh - Egyptian hieratic', 'Egyp - Egyptian hieroglyphs', 'Elba - Elbasan', 'Ethi - Ethiopic', 'Geok - Khutsuri (Asomtavruli and Nuskhuri)', 'Geor - Georgian (Mkhedruli)', 'Glag - Glagolitic', 'Goth - Gothic', 'Gran - Grantha', 'Grek - Greek', 'Gujr - Gujarati', 'Guru - Gurmukhi', 'Hanb - Han with Bopomofo', 'Hang - Hangul', 'Hani - Han (Hanzi, Kanji, Hanja)', 'Hano - Hanunoo (Hanunóo)', 'Hans - Han (Simplified variant)', 'Hant - Han (Traditional variant)', 'Hatr - Hatran', 'Hebr - Hebrew', 'Hira - Hiragana', 'Hluw - Anatolian Hieroglyphs', 'Hmng - Pahawh Hmong', 'Hrkt - Japanese syllabaries', 'Hung - Old Hungarian (Hungarian Runic)', 'Inds - Indus (Harappan)', 'Ital - Old Italic (Etruscan, Oscan etc.)', 'Jamo - Jamo', 'Java - Javanese', 'Jpan - Japanese', 'Jurc - Jurchen', 'Kali - Kayah Li', 'Kana - Katakana', 'Khar - Kharoshthi', 'Khmr - Khmer', 'Khoj - Khojki', 'Kitl - Khitan large script', 'Kits - Khitan small script', 'Knda - Kannada', 'Kore - Korean (alias for Hangul + Han)', 'Kpel - Kpelle', 'Kthi - Kaithi', 'Lana - Tai Tham (Lanna)', 'Laoo - Lao', 'Latf - Latin (Fraktur variant)', 'Latg - Latin (Gaelic variant)', 'Latn - Latin', 'Leke - Leke', 'Lepc - Lepcha (Róng)', 'Limb - Limbu', 'Lina - Linear A', 'Linb - Linear B', 'Lisu - Lisu (Fraser)', 'Loma - Loma', 'Lyci - Lycian', 'Lydi - Lydian', 'Mahj - Mahajani', 'Mand - Mandaic, Mandaean', 'Mani - Manichaean', 'Marc - Marchen', 'Maya - Mayan hieroglyphs', 'Mend - Mende Kikakui', 'Merc - Meroitic Cursive', 'Mero - Meroitic Hieroglyphs', 'Mlym - Malayalam', 'Modi - Modi, Moḍī', 'Mong - Mongolian', 'Moon - Moon (Moon code, Moon script, Moon type)', 'Mroo - Mro, Mru', 'Mtei - Meitei Mayek (Meithei, Meetei)', 'Mult - Multani', 'Mymr - Myanmar (Burmese)', 'Narb - Old North Arabian (Ancient North Arabian)', 'Nbat - Nabataean', 'Newa - Newa, Newar, Newari', 'Nkgb - Nakhi Geba', 'Nkoo - N’Ko', 'Nshu - Nüshu', 'Ogam - Ogham', 'Olck - Ol Chiki (Ol Cemet’, Ol, Santali)', 'Orkh - Old Turkic, Orkhon Runic', 'Orya - Oriya', 'Osge - Osage', 'Osma - Osmanya', 'Palm - Palmyrene', 'Pauc - Pau Cin Hau', 'Perm - Old Permic', 'Phag - Phags-pa', 'Phli - Inscriptional Pahlavi', 'Phlp - Psalter Pahlavi', 'Phlv - Book Pahlavi', 'Phnx - Phoenician', 'Piqd - Klingon (KLI pIqaD)', 'Plrd - Miao (Pollard)', 'Prti - Inscriptional Parthian', 'Rjng - Rejang (Redjang, Kaganga)', 'Roro - Rongorongo', 'Runr - Runic', 'Samr - Samaritan', 'Sara - Sarati', 'Sarb - Old South Arabian', 'Saur - Saurashtra', 'Sgnw - SignWriting', 'Shaw - Shavian (Shaw)', 'Shrd - Sharada, Śāradā', 'Sidd - Siddham', 'Sind - Khudawadi, Sindhi', 'Sinh - Sinhala', 'Sora - Sora Sompeng', 'Sund - Sundanese', 'Sylo - Syloti Nagri', 'Syrc - Syriac', 'Syre - Syriac (Estrangelo variant)', 'Syrj - Syriac (Western variant)', 'Syrn - Syriac (Eastern variant)', 'Tagb - Tagbanwa', 'Takr - Takri', 'Tale - Tai Le', 'Talu - New Tai Lue', 'Taml - Tamil', 'Tang - Tangut', 'Tavt - Tai Viet', 'Telu - Telugu', 'Teng - Tengwar', 'Tfng - Tifinagh (Berber)', 'Tglg - Tagalog (Baybayin, Alibata)', 'Thaa - Thaana', 'Thai - Thai', 'Tibt - Tibetan', 'Tirh - Tirhuta', 'Ugar - Ugaritic', 'Vaii - Vai', 'Visp - Visible Speech', 'Wara - Warang Citi (Varang Kshiti)', 'Wole - Woleai', 'Xpeo - Old Persian', 'Xsux - Cuneiform, Sumero-Akkadian', 'Yiii - Yi', 'Zinh - Code for inherited script', 'Zmth - Mathematical notation', 'Zsye - Symbols (Emoji variant)', 'Zsym - Symbols', 'Zxxx - Code for unwritten documents', 'Zyyy - Code for undetermined script', 'Zzzz - Code for uncoded script', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ScriptSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ReadingDirectionSimpleType(self, value):
        # Validate type pc:ReadingDirectionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['left-to-right', 'right-to-left', 'top-to-bottom', 'bottom-to-top']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ReadingDirectionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TextLineOrderSimpleType(self, value):
        # Validate type pc:TextLineOrderSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['top-to-bottom', 'bottom-to-top', 'left-to-right', 'right-to-left']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TextLineOrderSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ConfSimpleType(self, value):
        # Validate type pc:ConfSimpleType, a restriction on float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.AlternativeImage or
            self.Border is not None or
            self.PrintSpace is not None or
            self.ReadingOrder is not None or
            self.Layers is not None or
            self.Relations is not None or
            self.TextStyle is not None or
            self.UserDefined is not None or
            self.Labels or
            self.TextRegion or
            self.ImageRegion or
            self.LineDrawingRegion or
            self.GraphicRegion or
            self.TableRegion or
            self.ChartRegion or
            self.MapRegion or
            self.SeparatorRegion or
            self.MathsRegion or
            self.ChemRegion or
            self.MusicRegion or
            self.AdvertRegion or
            self.NoiseRegion or
            self.UnknownRegion or
            self.CustomRegion
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='PageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PageType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PageType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PageType'):
        if self.imageFilename is not None and 'imageFilename' not in already_processed:
            already_processed.add('imageFilename')
            outfile.write(' imageFilename=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.imageFilename), input_name='imageFilename')), ))
        if self.imageWidth is not None and 'imageWidth' not in already_processed:
            already_processed.add('imageWidth')
            outfile.write(' imageWidth="%s"' % self.gds_format_integer(self.imageWidth, input_name='imageWidth'))
        if self.imageHeight is not None and 'imageHeight' not in already_processed:
            already_processed.add('imageHeight')
            outfile.write(' imageHeight="%s"' % self.gds_format_integer(self.imageHeight, input_name='imageHeight'))
        if self.imageXResolution is not None and 'imageXResolution' not in already_processed:
            already_processed.add('imageXResolution')
            outfile.write(' imageXResolution="%s"' % self.gds_format_float(self.imageXResolution, input_name='imageXResolution'))
        if self.imageYResolution is not None and 'imageYResolution' not in already_processed:
            already_processed.add('imageYResolution')
            outfile.write(' imageYResolution="%s"' % self.gds_format_float(self.imageYResolution, input_name='imageYResolution'))
        if self.imageResolutionUnit is not None and 'imageResolutionUnit' not in already_processed:
            already_processed.add('imageResolutionUnit')
            outfile.write(' imageResolutionUnit=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.imageResolutionUnit), input_name='imageResolutionUnit')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.primaryLanguage is not None and 'primaryLanguage' not in already_processed:
            already_processed.add('primaryLanguage')
            outfile.write(' primaryLanguage=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryLanguage), input_name='primaryLanguage')), ))
        if self.secondaryLanguage is not None and 'secondaryLanguage' not in already_processed:
            already_processed.add('secondaryLanguage')
            outfile.write(' secondaryLanguage=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.secondaryLanguage), input_name='secondaryLanguage')), ))
        if self.primaryScript is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            outfile.write(' primaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryScript), input_name='primaryScript')), ))
        if self.secondaryScript is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            outfile.write(' secondaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.secondaryScript), input_name='secondaryScript')), ))
        if self.readingDirection is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            outfile.write(' readingDirection=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.readingDirection), input_name='readingDirection')), ))
        if self.textLineOrder is not None and 'textLineOrder' not in already_processed:
            already_processed.add('textLineOrder')
            outfile.write(' textLineOrder=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.textLineOrder), input_name='textLineOrder')), ))
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_float(self.conf, input_name='conf'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='PageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AlternativeImage_ in self.AlternativeImage:
            namespaceprefix_ = self.AlternativeImage_nsprefix_ + ':' if (UseCapturedNS_ and self.AlternativeImage_nsprefix_) else ''
            AlternativeImage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlternativeImage', pretty_print=pretty_print)
        if self.Border is not None:
            namespaceprefix_ = self.Border_nsprefix_ + ':' if (UseCapturedNS_ and self.Border_nsprefix_) else ''
            self.Border.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Border', pretty_print=pretty_print)
        if self.PrintSpace is not None:
            namespaceprefix_ = self.PrintSpace_nsprefix_ + ':' if (UseCapturedNS_ and self.PrintSpace_nsprefix_) else ''
            self.PrintSpace.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PrintSpace', pretty_print=pretty_print)
        if self.ReadingOrder is not None:
            namespaceprefix_ = self.ReadingOrder_nsprefix_ + ':' if (UseCapturedNS_ and self.ReadingOrder_nsprefix_) else ''
            self.ReadingOrder.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ReadingOrder', pretty_print=pretty_print)
        if self.Layers is not None:
            namespaceprefix_ = self.Layers_nsprefix_ + ':' if (UseCapturedNS_ and self.Layers_nsprefix_) else ''
            self.Layers.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Layers', pretty_print=pretty_print)
        if self.Relations is not None:
            namespaceprefix_ = self.Relations_nsprefix_ + ':' if (UseCapturedNS_ and self.Relations_nsprefix_) else ''
            self.Relations.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relations', pretty_print=pretty_print)
        if self.TextStyle is not None:
            namespaceprefix_ = self.TextStyle_nsprefix_ + ':' if (UseCapturedNS_ and self.TextStyle_nsprefix_) else ''
            self.TextStyle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextStyle', pretty_print=pretty_print)
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        for TextRegion_ in self.TextRegion:
            namespaceprefix_ = self.TextRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.TextRegion_nsprefix_) else ''
            TextRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextRegion', pretty_print=pretty_print)
        for ImageRegion_ in self.ImageRegion:
            namespaceprefix_ = self.ImageRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ImageRegion_nsprefix_) else ''
            ImageRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ImageRegion', pretty_print=pretty_print)
        for LineDrawingRegion_ in self.LineDrawingRegion:
            namespaceprefix_ = self.LineDrawingRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.LineDrawingRegion_nsprefix_) else ''
            LineDrawingRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LineDrawingRegion', pretty_print=pretty_print)
        for GraphicRegion_ in self.GraphicRegion:
            namespaceprefix_ = self.GraphicRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.GraphicRegion_nsprefix_) else ''
            GraphicRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GraphicRegion', pretty_print=pretty_print)
        for TableRegion_ in self.TableRegion:
            namespaceprefix_ = self.TableRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.TableRegion_nsprefix_) else ''
            TableRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TableRegion', pretty_print=pretty_print)
        for ChartRegion_ in self.ChartRegion:
            namespaceprefix_ = self.ChartRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ChartRegion_nsprefix_) else ''
            ChartRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChartRegion', pretty_print=pretty_print)
        for MapRegion_ in self.MapRegion:
            namespaceprefix_ = self.MapRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.MapRegion_nsprefix_) else ''
            MapRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MapRegion', pretty_print=pretty_print)
        for SeparatorRegion_ in self.SeparatorRegion:
            namespaceprefix_ = self.SeparatorRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.SeparatorRegion_nsprefix_) else ''
            SeparatorRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SeparatorRegion', pretty_print=pretty_print)
        for MathsRegion_ in self.MathsRegion:
            namespaceprefix_ = self.MathsRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.MathsRegion_nsprefix_) else ''
            MathsRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MathsRegion', pretty_print=pretty_print)
        for ChemRegion_ in self.ChemRegion:
            namespaceprefix_ = self.ChemRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ChemRegion_nsprefix_) else ''
            ChemRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChemRegion', pretty_print=pretty_print)
        for MusicRegion_ in self.MusicRegion:
            namespaceprefix_ = self.MusicRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.MusicRegion_nsprefix_) else ''
            MusicRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MusicRegion', pretty_print=pretty_print)
        for AdvertRegion_ in self.AdvertRegion:
            namespaceprefix_ = self.AdvertRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.AdvertRegion_nsprefix_) else ''
            AdvertRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AdvertRegion', pretty_print=pretty_print)
        for NoiseRegion_ in self.NoiseRegion:
            namespaceprefix_ = self.NoiseRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.NoiseRegion_nsprefix_) else ''
            NoiseRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NoiseRegion', pretty_print=pretty_print)
        for UnknownRegion_ in self.UnknownRegion:
            namespaceprefix_ = self.UnknownRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.UnknownRegion_nsprefix_) else ''
            UnknownRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnknownRegion', pretty_print=pretty_print)
        for CustomRegion_ in self.CustomRegion:
            namespaceprefix_ = self.CustomRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.CustomRegion_nsprefix_) else ''
            CustomRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CustomRegion', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('imageFilename', node)
        if value is not None and 'imageFilename' not in already_processed:
            already_processed.add('imageFilename')
            self.imageFilename = value
        value = find_attr_value_('imageWidth', node)
        if value is not None and 'imageWidth' not in already_processed:
            already_processed.add('imageWidth')
            self.imageWidth = self.gds_parse_integer(value, node, 'imageWidth')
        value = find_attr_value_('imageHeight', node)
        if value is not None and 'imageHeight' not in already_processed:
            already_processed.add('imageHeight')
            self.imageHeight = self.gds_parse_integer(value, node, 'imageHeight')
        value = find_attr_value_('imageXResolution', node)
        if value is not None and 'imageXResolution' not in already_processed:
            already_processed.add('imageXResolution')
            value = self.gds_parse_float(value, node, 'imageXResolution')
            self.imageXResolution = value
        value = find_attr_value_('imageYResolution', node)
        if value is not None and 'imageYResolution' not in already_processed:
            already_processed.add('imageYResolution')
            value = self.gds_parse_float(value, node, 'imageYResolution')
            self.imageYResolution = value
        value = find_attr_value_('imageResolutionUnit', node)
        if value is not None and 'imageResolutionUnit' not in already_processed:
            already_processed.add('imageResolutionUnit')
            self.imageResolutionUnit = value
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_PageTypeSimpleType(self.type_)    # validate type PageTypeSimpleType
        value = find_attr_value_('primaryLanguage', node)
        if value is not None and 'primaryLanguage' not in already_processed:
            already_processed.add('primaryLanguage')
            self.primaryLanguage = value
            self.validate_LanguageSimpleType(self.primaryLanguage)    # validate type LanguageSimpleType
        value = find_attr_value_('secondaryLanguage', node)
        if value is not None and 'secondaryLanguage' not in already_processed:
            already_processed.add('secondaryLanguage')
            self.secondaryLanguage = value
            self.validate_LanguageSimpleType(self.secondaryLanguage)    # validate type LanguageSimpleType
        value = find_attr_value_('primaryScript', node)
        if value is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            self.primaryScript = value
            self.validate_ScriptSimpleType(self.primaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('secondaryScript', node)
        if value is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            self.secondaryScript = value
            self.validate_ScriptSimpleType(self.secondaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('readingDirection', node)
        if value is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            self.readingDirection = value
            self.validate_ReadingDirectionSimpleType(self.readingDirection)    # validate type ReadingDirectionSimpleType
        value = find_attr_value_('textLineOrder', node)
        if value is not None and 'textLineOrder' not in already_processed:
            already_processed.add('textLineOrder')
            self.textLineOrder = value
            self.validate_TextLineOrderSimpleType(self.textLineOrder)    # validate type TextLineOrderSimpleType
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            value = self.gds_parse_float(value, node, 'conf')
            self.conf = value
            self.validate_ConfSimpleType(self.conf)    # validate type ConfSimpleType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlternativeImage':
            obj_ = AlternativeImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlternativeImage.append(obj_)
            obj_.original_tagname_ = 'AlternativeImage'
        elif nodeName_ == 'Border':
            obj_ = BorderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Border = obj_
            obj_.original_tagname_ = 'Border'
        elif nodeName_ == 'PrintSpace':
            obj_ = PrintSpaceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PrintSpace = obj_
            obj_.original_tagname_ = 'PrintSpace'
        elif nodeName_ == 'ReadingOrder':
            obj_ = ReadingOrderType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ReadingOrder = obj_
            obj_.original_tagname_ = 'ReadingOrder'
        elif nodeName_ == 'Layers':
            obj_ = LayersType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Layers = obj_
            obj_.original_tagname_ = 'Layers'
        elif nodeName_ == 'Relations':
            obj_ = RelationsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relations = obj_
            obj_.original_tagname_ = 'Relations'
        elif nodeName_ == 'TextStyle':
            obj_ = TextStyleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextStyle = obj_
            obj_.original_tagname_ = 'TextStyle'
        elif nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'TextRegion':
            obj_ = TextRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextRegion.append(obj_)
            obj_.original_tagname_ = 'TextRegion'
        elif nodeName_ == 'ImageRegion':
            obj_ = ImageRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ImageRegion.append(obj_)
            obj_.original_tagname_ = 'ImageRegion'
        elif nodeName_ == 'LineDrawingRegion':
            obj_ = LineDrawingRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LineDrawingRegion.append(obj_)
            obj_.original_tagname_ = 'LineDrawingRegion'
        elif nodeName_ == 'GraphicRegion':
            obj_ = GraphicRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GraphicRegion.append(obj_)
            obj_.original_tagname_ = 'GraphicRegion'
        elif nodeName_ == 'TableRegion':
            obj_ = TableRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TableRegion.append(obj_)
            obj_.original_tagname_ = 'TableRegion'
        elif nodeName_ == 'ChartRegion':
            obj_ = ChartRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChartRegion.append(obj_)
            obj_.original_tagname_ = 'ChartRegion'
        elif nodeName_ == 'MapRegion':
            obj_ = MapRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MapRegion.append(obj_)
            obj_.original_tagname_ = 'MapRegion'
        elif nodeName_ == 'SeparatorRegion':
            obj_ = SeparatorRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SeparatorRegion.append(obj_)
            obj_.original_tagname_ = 'SeparatorRegion'
        elif nodeName_ == 'MathsRegion':
            obj_ = MathsRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MathsRegion.append(obj_)
            obj_.original_tagname_ = 'MathsRegion'
        elif nodeName_ == 'ChemRegion':
            obj_ = ChemRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChemRegion.append(obj_)
            obj_.original_tagname_ = 'ChemRegion'
        elif nodeName_ == 'MusicRegion':
            obj_ = MusicRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MusicRegion.append(obj_)
            obj_.original_tagname_ = 'MusicRegion'
        elif nodeName_ == 'AdvertRegion':
            obj_ = AdvertRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AdvertRegion.append(obj_)
            obj_.original_tagname_ = 'AdvertRegion'
        elif nodeName_ == 'NoiseRegion':
            obj_ = NoiseRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NoiseRegion.append(obj_)
            obj_.original_tagname_ = 'NoiseRegion'
        elif nodeName_ == 'UnknownRegion':
            obj_ = UnknownRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnknownRegion.append(obj_)
            obj_.original_tagname_ = 'UnknownRegion'
        elif nodeName_ == 'CustomRegion':
            obj_ = CustomRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CustomRegion.append(obj_)
            obj_.original_tagname_ = 'CustomRegion'
    def __hash__(self):
        return hash(self.id)
    @property
    def id(self):
        if hasattr(self, 'pcGtsId'):
            return self.pcGtsId
        return self.imageFilename
    # pylint: disable=line-too-long,invalid-name,protected-access,missing-module-docstring
    def _region_class(self, x): # pylint: disable=unused-argument
        return x.__class__.__name__.replace('RegionType', '')
    
    def _get_recursive_regions(self, regions, level, classes=None):
        from .constants import PAGE_REGION_TYPES  # pylint: disable=relative-beyond-top-level,import-outside-toplevel
        if level == 1:
            # stop recursion, filter classes
            if classes:
                return [r for r in regions if self._region_class(r) in classes]
            if regions and regions[0].__class__.__name__ == 'PageType':
                regions = regions[1:]
            return regions
        # find more regions recursively
        more_regions = []
        for region in regions:
            more_regions.append([])
            for class_ in PAGE_REGION_TYPES:
                if class_ == 'Map' and not isinstance(region, PageType): # pylint: disable=undefined-variable
                    # 'Map' is not recursive in 2019 schema
                    continue
                more_regions[-1] += getattr(region, 'get_{}Region'.format(class_))()
        if not any(more_regions):
            return self._get_recursive_regions(regions, 1, classes)
        ret = []
        for r, more in zip(regions, more_regions):
            ret.append(r)
            ret += self._get_recursive_regions(more, level - 1 if level else 0, classes)
        return self._get_recursive_regions(ret, 1, classes)
    
    def _get_recursive_reading_order(self, rogroup):
        if isinstance(rogroup, (OrderedGroupType, OrderedGroupIndexedType)): # pylint: disable=undefined-variable
            elements = rogroup.get_AllIndexed()
        if isinstance(rogroup, (UnorderedGroupType, UnorderedGroupIndexedType)): # pylint: disable=undefined-variable
            elements = (rogroup.get_RegionRef() + rogroup.get_OrderedGroup() + rogroup.get_UnorderedGroup())
        regionrefs = list()
        for elem in elements:
            regionrefs.append(elem.get_regionRef())
            if not isinstance(elem, (RegionRefType, RegionRefIndexedType)): # pylint: disable=undefined-variable
                regionrefs.extend(self._get_recursive_reading_order(elem))
        return regionrefs
    
    def get_AllRegions(self, classes=None, order='document', depth=0):
        """
        Get all the *Region element or only those provided by ``classes``.
        Returned in document order unless ``order`` is ``reading-order``
        Arguments:
            classes (list) Classes of regions that shall be returned, e.g. ``['Text', 'Image']``
            order ("document"|"reading-order"|"reading-order-only") Whether to
                return regions sorted by document order (``document``, default) or by
                reading order with regions not in the reading order at the end of the
                returned list (``reading-order``) or regions not in the reading order
                omitted (``reading-order-only``)
            depth (int) Recursive depth to look for regions at, set to `0` for all regions at any depth. Default: 0
    
        For example, to get all text anywhere on the page in reading order, use:
        ::
            '\\n'.join(line.get_TextEquiv()[0].Unicode
                      for region in page.get_AllRegions(classes=['Text'], depth=0, order='reading-order')
                      for line in region.get_TextLine())
        """
        if order not in ['document', 'reading-order', 'reading-order-only']:
            raise Exception("Argument 'order' must be either 'document', 'reading-order' or 'reading-order-only', not '{}'".format(order))
        if depth < 0:
            raise Exception("Argument 'depth' must be an integer greater-or-equal 0, not '{}'".format(depth))
        ret = self._get_recursive_regions([self], depth + 1 if depth else 0, classes)
        if order.startswith('reading-order'):
            reading_order = self.get_ReadingOrder()
            if reading_order:
                reading_order = reading_order.get_OrderedGroup() or reading_order.get_UnorderedGroup()
            if reading_order:
                reading_order = self._get_recursive_reading_order(reading_order)
            if reading_order:
                id2region = {region.id: region for region in ret}
                in_reading_order = [id2region[region_id] for region_id in reading_order if region_id in id2region]
                #  print("ret: {} / in_ro: {} / not-in-ro: {}".format(
                #      len(ret),
                #      len([id2region[region_id] for region_id in reading_order if region_id in id2region]),
                #      len([r for r in ret if r not in in_reading_order])
                #      ))
                if order == 'reading-order-only':
                    ret = in_reading_order
                else:
                    ret = in_reading_order + [r for r in ret if r not in in_reading_order]
        return ret
    def get_AllAlternativeImages(self, page=True, region=True, line=True, word=True, glyph=True):
        """
        Get all the pc:AlternativeImage in a document
    
    
        page (boolean): Get pc:Page level images
        region (boolean): Get images on pc:*Region level
        line (boolean) Get images on pc:TextLine level
        word (boolean) Get images on pc:Word level
        glyph (boolean) Get images on pc:Glyph level
        """
        ret = []
        if page:
            ret += self.get_AlternativeImage()
        for this_region in self.get_AllRegions(['Text']):
            if region:
                ret += this_region.get_AlternativeImage()
            for this_line in this_region.get_TextLine():
                if line:
                    ret += this_line.get_AlternativeImage()
                for this_word in this_line.get_Word():
                    if word:
                        ret += this_word.get_AlternativeImage()
                    for this_glyph in this_word.get_Glyph():
                        if glyph:
                            ret += this_glyph.get_AlternativeImage()
        return ret
    
    def invalidate_AlternativeImage(self, feature_selector=None):
        """
        Remove derived images from this segment (due to changed coordinates).
    
        If ``feature_selector`` is not none, remove only images with
        matching ``@comments``, e.g. ``feature_selector=cropped,deskewed``.
        """
        existing_images = self.AlternativeImage or []
        removed_images = []
        if feature_selector:
            new_images = []
            for image in existing_images:
                features = image.get_comments() or ''
                if any(feature in features.split(',')
                       for feature in feature_selector.split(',') if feature):
                    removed_images.append(image)
                else:
                    new_images.append(image)
            self.AlternativeImage = new_images
        else:
            removed_images = existing_images
            self.AlternativeImage = []
        if hasattr(self, 'id'):
            name = self.id
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'pcGtsId'):
            name = self.parent_object_.pcGtsId
        else:
            name = ''
        for image in removed_images:
            self.gds_collector_.add_message('Removing AlternativeImage %s from "%s"' % (
                image.get_comments() or '', name))
    def set_Border(self, Border):
        """
        Set coordinate polygon by given object.
        Moreover, invalidate self's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        self.invalidate_AlternativeImage(feature_selector='cropped')
        self.Border = Border
    def get_AllTextLines(self, region_order='document', respect_textline_order=True):
        """
        Return all the TextLine in the document
    
        Arguments:
            region_order ("document"|"reading-order"|"reading-order-only") Whether to
                return regions sorted by document order (``document``, default) or by
                reading order with regions not in the reading order at the end of the
                returned list (``reading-order``) or regions not in the reading order
                omitted (``reading-order-only``)
            respect_textline_order (boolean) Whether to respect textlineOrder attribute
        """
        # TODO handle textLineOrder according to https://github.com/PRImA-Research-Lab/PAGE-XML/issues/26
        ret = []
        for reg in self.get_AllRegions(['Text'], order=region_order):
            lines = reg.get_TextLine()
            if not respect_textline_order:
                ret += lines
            else:
                lo = reg.get_textLineOrder() or self.get_textLineOrder() or 'top-to-bottom'
                ret += lines if lo in ['top-to-bottom', 'left-to-right'] else list(reversed(lines))
        return ret
    
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class PageType


class CoordsType(GeneratedsSuper):
    """Polygon outline of the element as a path of points.
    No points may lie outside the outline of its parent,
    which in the case of Border is the bounding rectangle
    of the root image. Paths are closed by convention,
    i.e. the last point logically connects with the first
    (and at least 3 points are required to span an area).
    Paths must be planar (i.e. must not self-intersect).
    Confidence value (between 0 and 1)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('points', 'pc:PointsType', 0, 0, {'use': 'required'}),
        MemberSpec_('conf', 'pc:ConfSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, points=None, conf=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.points = _cast(None, points)
        self.points_nsprefix_ = "pc"
        self.conf = _cast(float, conf)
        self.conf_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoordsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoordsType.subclass:
            return CoordsType.subclass(*args_, **kwargs_)
        else:
            return CoordsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_points(self):
        return self.points
    def set_points(self, points):
        self.points = points
    def get_conf(self):
        return self.conf
    def set_conf(self, conf):
        self.conf = conf
    def validate_PointsType(self, value):
        # Validate type pc:PointsType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PointsType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PointsType_patterns_, ))
    validate_PointsType_patterns_ = [['^(([0-9]+,[0-9]+ )+([0-9]+,[0-9]+))$']]
    def validate_ConfSimpleType(self, value):
        # Validate type pc:ConfSimpleType, a restriction on float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='CoordsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoordsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CoordsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoordsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoordsType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CoordsType'):
        if self.points is not None and 'points' not in already_processed:
            already_processed.add('points')
            outfile.write(' points=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.points), input_name='points')), ))
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_float(self.conf, input_name='conf'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='CoordsType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('points', node)
        if value is not None and 'points' not in already_processed:
            already_processed.add('points')
            self.points = value
            self.validate_PointsType(self.points)    # validate type PointsType
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            value = self.gds_parse_float(value, node, 'conf')
            self.conf = value
            self.validate_ConfSimpleType(self.conf)    # validate type ConfSimpleType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
    def set_points(self, points):
        """
        Set coordinate polygon by given string.
        Moreover, invalidate the parent's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        if hasattr(self, 'parent_object_'):
            parent = self.parent_object_
            if hasattr(parent, 'invalidate_AlternativeImage'):
                # RegionType, TextLineType, WordType, GlyphType:
                parent.invalidate_AlternativeImage()
            elif hasattr(parent, 'parent_object_') and hasattr(parent.parent_object_, 'invalidate_AlternativeImage'):
                # BorderType:
                parent.parent_object_.invalidate_AlternativeImage(feature_selector='cropped')
        self.points = points
# end class CoordsType


class TextLineType(GeneratedsSuper):
    """Overrides primaryLanguage attribute of parent text
    region
    The primary script used in the text line
    The secondary script used in the text line
    The direction in which text within the line
    should be read (order of words and characters).
    Overrides the production attribute of the parent
    text region
    For generic use
    Position (order number) of this text line within the
    parent text region."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('primaryLanguage', 'pc:LanguageSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('primaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('secondaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('readingDirection', 'pc:ReadingDirectionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('production', 'pc:ProductionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('index', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('AlternativeImage', 'AlternativeImageType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'AlternativeImage', 'type': 'AlternativeImageType'}, None),
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
        MemberSpec_('Baseline', 'BaselineType', 0, 1, {'minOccurs': '0', 'name': 'Baseline', 'type': 'BaselineType'}, None),
        MemberSpec_('Word', 'WordType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Word', 'type': 'WordType'}, None),
        MemberSpec_('TextEquiv', 'TextEquivType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'TextEquiv', 'type': 'TextEquivType'}, None),
        MemberSpec_('TextStyle', 'TextStyleType', 0, 1, {'minOccurs': '0', 'name': 'TextStyle', 'type': 'TextStyleType'}, None),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, primaryLanguage=None, primaryScript=None, secondaryScript=None, readingDirection=None, production=None, custom=None, comments=None, index=None, AlternativeImage=None, Coords=None, Baseline=None, Word=None, TextEquiv=None, TextStyle=None, UserDefined=None, Labels=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.primaryLanguage = _cast(None, primaryLanguage)
        self.primaryLanguage_nsprefix_ = "pc"
        self.primaryScript = _cast(None, primaryScript)
        self.primaryScript_nsprefix_ = "pc"
        self.secondaryScript = _cast(None, secondaryScript)
        self.secondaryScript_nsprefix_ = "pc"
        self.readingDirection = _cast(None, readingDirection)
        self.readingDirection_nsprefix_ = "pc"
        self.production = _cast(None, production)
        self.production_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        if AlternativeImage is None:
            self.AlternativeImage = []
        else:
            self.AlternativeImage = AlternativeImage
        self.AlternativeImage_nsprefix_ = "pc"
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
        self.Baseline = Baseline
        self.Baseline_nsprefix_ = "pc"
        if Word is None:
            self.Word = []
        else:
            self.Word = Word
        self.Word_nsprefix_ = "pc"
        if TextEquiv is None:
            self.TextEquiv = []
        else:
            self.TextEquiv = TextEquiv
        self.TextEquiv_nsprefix_ = "pc"
        self.TextStyle = TextStyle
        self.TextStyle_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TextLineType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TextLineType.subclass:
            return TextLineType.subclass(*args_, **kwargs_)
        else:
            return TextLineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AlternativeImage(self):
        return self.AlternativeImage
    def set_AlternativeImage(self, AlternativeImage):
        self.AlternativeImage = AlternativeImage
    def add_AlternativeImage(self, value):
        self.AlternativeImage.append(value)
    def insert_AlternativeImage_at(self, index, value):
        self.AlternativeImage.insert(index, value)
    def replace_AlternativeImage_at(self, index, value):
        self.AlternativeImage[index] = value
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def get_Baseline(self):
        return self.Baseline
    def set_Baseline(self, Baseline):
        self.Baseline = Baseline
    def get_Word(self):
        return self.Word
    def set_Word(self, Word):
        self.Word = Word
    def add_Word(self, value):
        self.Word.append(value)
    def insert_Word_at(self, index, value):
        self.Word.insert(index, value)
    def replace_Word_at(self, index, value):
        self.Word[index] = value
    def get_TextEquiv(self):
        return self.TextEquiv
    def set_TextEquiv(self, TextEquiv):
        self.TextEquiv = TextEquiv
    def add_TextEquiv(self, value):
        self.TextEquiv.append(value)
    def insert_TextEquiv_at(self, index, value):
        self.TextEquiv.insert(index, value)
    def replace_TextEquiv_at(self, index, value):
        self.TextEquiv[index] = value
    def get_TextStyle(self):
        return self.TextStyle
    def set_TextStyle(self, TextStyle):
        self.TextStyle = TextStyle
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_primaryLanguage(self):
        return self.primaryLanguage
    def set_primaryLanguage(self, primaryLanguage):
        self.primaryLanguage = primaryLanguage
    def get_primaryScript(self):
        return self.primaryScript
    def set_primaryScript(self, primaryScript):
        self.primaryScript = primaryScript
    def get_secondaryScript(self):
        return self.secondaryScript
    def set_secondaryScript(self, secondaryScript):
        self.secondaryScript = secondaryScript
    def get_readingDirection(self):
        return self.readingDirection
    def set_readingDirection(self, readingDirection):
        self.readingDirection = readingDirection
    def get_production(self):
        return self.production
    def set_production(self, production):
        self.production = production
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def validate_LanguageSimpleType(self, value):
        # Validate type pc:LanguageSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Abkhaz', 'Afar', 'Afrikaans', 'Akan', 'Albanian', 'Amharic', 'Arabic', 'Aragonese', 'Armenian', 'Assamese', 'Avaric', 'Avestan', 'Aymara', 'Azerbaijani', 'Bambara', 'Bashkir', 'Basque', 'Belarusian', 'Bengali', 'Bihari', 'Bislama', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', 'Cambodian', 'Cantonese', 'Catalan', 'Chamorro', 'Chechen', 'Chichewa', 'Chinese', 'Chuvash', 'Cornish', 'Corsican', 'Cree', 'Croatian', 'Czech', 'Danish', 'Divehi', 'Dutch', 'Dzongkha', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'French', 'Fula', 'Gaelic', 'Galician', 'Ganda', 'Georgian', 'German', 'Greek', 'Guaraní', 'Gujarati', 'Haitian', 'Hausa', 'Hebrew', 'Herero', 'Hindi', 'Hiri Motu', 'Hungarian', 'Icelandic', 'Ido', 'Igbo', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiaq', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kalaallisut', 'Kannada', 'Kanuri', 'Kashmiri', 'Kazakh', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kirundi', 'Komi', 'Kongo', 'Korean', 'Kurdish', 'Kwanyama', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Limburgish', 'Lingala', 'Lithuanian', 'Luba-Katanga', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Manx', 'Māori', 'Marathi', 'Marshallese', 'Mongolian', 'Nauru', 'Navajo', 'Ndonga', 'Nepali', 'North Ndebele', 'Northern Sami', 'Norwegian', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Nuosu', 'Occitan', 'Ojibwe', 'Old Church Slavonic', 'Oriya', 'Oromo', 'Ossetian', 'Pāli', 'Panjabi', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Romansh', 'Russian', 'Samoan', 'Sango', 'Sanskrit', 'Sardinian', 'Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovene', 'Somali', 'South Ndebele', 'Southern Sotho', 'Spanish', 'Sundanese', 'Swahili', 'Swati', 'Swedish', 'Tagalog', 'Tahitian', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Tswana', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda', 'Vietnamese', 'Volapük', 'Walloon', 'Welsh', 'Western Frisian', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zhuang', 'Zulu', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LanguageSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ScriptSimpleType(self, value):
        # Validate type pc:ScriptSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Adlm - Adlam', 'Afak - Afaka', 'Aghb - Caucasian Albanian', 'Ahom - Ahom, Tai Ahom', 'Arab - Arabic', 'Aran - Arabic (Nastaliq variant)', 'Armi - Imperial Aramaic', 'Armn - Armenian', 'Avst - Avestan', 'Bali - Balinese', 'Bamu - Bamum', 'Bass - Bassa Vah', 'Batk - Batak', 'Beng - Bengali', 'Bhks - Bhaiksuki', 'Blis - Blissymbols', 'Bopo - Bopomofo', 'Brah - Brahmi', 'Brai - Braille', 'Bugi - Buginese', 'Buhd - Buhid', 'Cakm - Chakma', 'Cans - Unified Canadian Aboriginal Syllabics', 'Cari - Carian', 'Cham - Cham', 'Cher - Cherokee', 'Cirt - Cirth', 'Copt - Coptic', 'Cprt - Cypriot', 'Cyrl - Cyrillic', 'Cyrs - Cyrillic (Old Church Slavonic variant)', 'Deva - Devanagari (Nagari)', 'Dsrt - Deseret (Mormon)', 'Dupl - Duployan shorthand, Duployan stenography', 'Egyd - Egyptian demotic', 'Egyh - Egyptian hieratic', 'Egyp - Egyptian hieroglyphs', 'Elba - Elbasan', 'Ethi - Ethiopic', 'Geok - Khutsuri (Asomtavruli and Nuskhuri)', 'Geor - Georgian (Mkhedruli)', 'Glag - Glagolitic', 'Goth - Gothic', 'Gran - Grantha', 'Grek - Greek', 'Gujr - Gujarati', 'Guru - Gurmukhi', 'Hanb - Han with Bopomofo', 'Hang - Hangul', 'Hani - Han (Hanzi, Kanji, Hanja)', 'Hano - Hanunoo (Hanunóo)', 'Hans - Han (Simplified variant)', 'Hant - Han (Traditional variant)', 'Hatr - Hatran', 'Hebr - Hebrew', 'Hira - Hiragana', 'Hluw - Anatolian Hieroglyphs', 'Hmng - Pahawh Hmong', 'Hrkt - Japanese syllabaries', 'Hung - Old Hungarian (Hungarian Runic)', 'Inds - Indus (Harappan)', 'Ital - Old Italic (Etruscan, Oscan etc.)', 'Jamo - Jamo', 'Java - Javanese', 'Jpan - Japanese', 'Jurc - Jurchen', 'Kali - Kayah Li', 'Kana - Katakana', 'Khar - Kharoshthi', 'Khmr - Khmer', 'Khoj - Khojki', 'Kitl - Khitan large script', 'Kits - Khitan small script', 'Knda - Kannada', 'Kore - Korean (alias for Hangul + Han)', 'Kpel - Kpelle', 'Kthi - Kaithi', 'Lana - Tai Tham (Lanna)', 'Laoo - Lao', 'Latf - Latin (Fraktur variant)', 'Latg - Latin (Gaelic variant)', 'Latn - Latin', 'Leke - Leke', 'Lepc - Lepcha (Róng)', 'Limb - Limbu', 'Lina - Linear A', 'Linb - Linear B', 'Lisu - Lisu (Fraser)', 'Loma - Loma', 'Lyci - Lycian', 'Lydi - Lydian', 'Mahj - Mahajani', 'Mand - Mandaic, Mandaean', 'Mani - Manichaean', 'Marc - Marchen', 'Maya - Mayan hieroglyphs', 'Mend - Mende Kikakui', 'Merc - Meroitic Cursive', 'Mero - Meroitic Hieroglyphs', 'Mlym - Malayalam', 'Modi - Modi, Moḍī', 'Mong - Mongolian', 'Moon - Moon (Moon code, Moon script, Moon type)', 'Mroo - Mro, Mru', 'Mtei - Meitei Mayek (Meithei, Meetei)', 'Mult - Multani', 'Mymr - Myanmar (Burmese)', 'Narb - Old North Arabian (Ancient North Arabian)', 'Nbat - Nabataean', 'Newa - Newa, Newar, Newari', 'Nkgb - Nakhi Geba', 'Nkoo - N’Ko', 'Nshu - Nüshu', 'Ogam - Ogham', 'Olck - Ol Chiki (Ol Cemet’, Ol, Santali)', 'Orkh - Old Turkic, Orkhon Runic', 'Orya - Oriya', 'Osge - Osage', 'Osma - Osmanya', 'Palm - Palmyrene', 'Pauc - Pau Cin Hau', 'Perm - Old Permic', 'Phag - Phags-pa', 'Phli - Inscriptional Pahlavi', 'Phlp - Psalter Pahlavi', 'Phlv - Book Pahlavi', 'Phnx - Phoenician', 'Piqd - Klingon (KLI pIqaD)', 'Plrd - Miao (Pollard)', 'Prti - Inscriptional Parthian', 'Rjng - Rejang (Redjang, Kaganga)', 'Roro - Rongorongo', 'Runr - Runic', 'Samr - Samaritan', 'Sara - Sarati', 'Sarb - Old South Arabian', 'Saur - Saurashtra', 'Sgnw - SignWriting', 'Shaw - Shavian (Shaw)', 'Shrd - Sharada, Śāradā', 'Sidd - Siddham', 'Sind - Khudawadi, Sindhi', 'Sinh - Sinhala', 'Sora - Sora Sompeng', 'Sund - Sundanese', 'Sylo - Syloti Nagri', 'Syrc - Syriac', 'Syre - Syriac (Estrangelo variant)', 'Syrj - Syriac (Western variant)', 'Syrn - Syriac (Eastern variant)', 'Tagb - Tagbanwa', 'Takr - Takri', 'Tale - Tai Le', 'Talu - New Tai Lue', 'Taml - Tamil', 'Tang - Tangut', 'Tavt - Tai Viet', 'Telu - Telugu', 'Teng - Tengwar', 'Tfng - Tifinagh (Berber)', 'Tglg - Tagalog (Baybayin, Alibata)', 'Thaa - Thaana', 'Thai - Thai', 'Tibt - Tibetan', 'Tirh - Tirhuta', 'Ugar - Ugaritic', 'Vaii - Vai', 'Visp - Visible Speech', 'Wara - Warang Citi (Varang Kshiti)', 'Wole - Woleai', 'Xpeo - Old Persian', 'Xsux - Cuneiform, Sumero-Akkadian', 'Yiii - Yi', 'Zinh - Code for inherited script', 'Zmth - Mathematical notation', 'Zsye - Symbols (Emoji variant)', 'Zsym - Symbols', 'Zxxx - Code for unwritten documents', 'Zyyy - Code for undetermined script', 'Zzzz - Code for uncoded script', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ScriptSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ReadingDirectionSimpleType(self, value):
        # Validate type pc:ReadingDirectionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['left-to-right', 'right-to-left', 'top-to-bottom', 'bottom-to-top']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ReadingDirectionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ProductionSimpleType(self, value):
        # Validate type pc:ProductionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['printed', 'typewritten', 'handwritten-cursive', 'handwritten-printscript', 'medieval-manuscript', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.AlternativeImage or
            self.Coords is not None or
            self.Baseline is not None or
            self.Word or
            self.TextEquiv or
            self.TextStyle is not None or
            self.UserDefined is not None or
            self.Labels
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='TextLineType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TextLineType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TextLineType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextLineType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TextLineType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TextLineType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.primaryLanguage is not None and 'primaryLanguage' not in already_processed:
            already_processed.add('primaryLanguage')
            outfile.write(' primaryLanguage=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryLanguage), input_name='primaryLanguage')), ))
        if self.primaryScript is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            outfile.write(' primaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryScript), input_name='primaryScript')), ))
        if self.secondaryScript is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            outfile.write(' secondaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.secondaryScript), input_name='secondaryScript')), ))
        if self.readingDirection is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            outfile.write(' readingDirection=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.readingDirection), input_name='readingDirection')), ))
        if self.production is not None and 'production' not in already_processed:
            already_processed.add('production')
            outfile.write(' production=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.production), input_name='production')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='TextLineType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AlternativeImage_ in self.AlternativeImage:
            namespaceprefix_ = self.AlternativeImage_nsprefix_ + ':' if (UseCapturedNS_ and self.AlternativeImage_nsprefix_) else ''
            AlternativeImage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlternativeImage', pretty_print=pretty_print)
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
        if self.Baseline is not None:
            namespaceprefix_ = self.Baseline_nsprefix_ + ':' if (UseCapturedNS_ and self.Baseline_nsprefix_) else ''
            self.Baseline.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Baseline', pretty_print=pretty_print)
        for Word_ in self.Word:
            namespaceprefix_ = self.Word_nsprefix_ + ':' if (UseCapturedNS_ and self.Word_nsprefix_) else ''
            Word_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Word', pretty_print=pretty_print)
        for TextEquiv_ in self.TextEquiv:
            namespaceprefix_ = self.TextEquiv_nsprefix_ + ':' if (UseCapturedNS_ and self.TextEquiv_nsprefix_) else ''
            TextEquiv_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextEquiv', pretty_print=pretty_print)
        if self.TextStyle is not None:
            namespaceprefix_ = self.TextStyle_nsprefix_ + ':' if (UseCapturedNS_ and self.TextStyle_nsprefix_) else ''
            self.TextStyle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextStyle', pretty_print=pretty_print)
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('primaryLanguage', node)
        if value is not None and 'primaryLanguage' not in already_processed:
            already_processed.add('primaryLanguage')
            self.primaryLanguage = value
            self.validate_LanguageSimpleType(self.primaryLanguage)    # validate type LanguageSimpleType
        value = find_attr_value_('primaryScript', node)
        if value is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            self.primaryScript = value
            self.validate_ScriptSimpleType(self.primaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('secondaryScript', node)
        if value is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            self.secondaryScript = value
            self.validate_ScriptSimpleType(self.secondaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('readingDirection', node)
        if value is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            self.readingDirection = value
            self.validate_ReadingDirectionSimpleType(self.readingDirection)    # validate type ReadingDirectionSimpleType
        value = find_attr_value_('production', node)
        if value is not None and 'production' not in already_processed:
            already_processed.add('production')
            self.production = value
            self.validate_ProductionSimpleType(self.production)    # validate type ProductionSimpleType
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlternativeImage':
            obj_ = AlternativeImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlternativeImage.append(obj_)
            obj_.original_tagname_ = 'AlternativeImage'
        elif nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
        elif nodeName_ == 'Baseline':
            obj_ = BaselineType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Baseline = obj_
            obj_.original_tagname_ = 'Baseline'
        elif nodeName_ == 'Word':
            obj_ = WordType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Word.append(obj_)
            obj_.original_tagname_ = 'Word'
        elif nodeName_ == 'TextEquiv':
            obj_ = TextEquivType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextEquiv.append(obj_)
            obj_.original_tagname_ = 'TextEquiv'
        elif nodeName_ == 'TextStyle':
            obj_ = TextStyleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextStyle = obj_
            obj_.original_tagname_ = 'TextStyle'
        elif nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
    def __hash__(self):
        return hash(self.id)
    def invalidate_AlternativeImage(self, feature_selector=None):
        """
        Remove derived images from this segment (due to changed coordinates).
    
        If ``feature_selector`` is not none, remove only images with
        matching ``@comments``, e.g. ``feature_selector=cropped,deskewed``.
        """
        existing_images = self.AlternativeImage or []
        removed_images = []
        if feature_selector:
            new_images = []
            for image in existing_images:
                features = image.get_comments() or ''
                if any(feature in features.split(',')
                       for feature in feature_selector.split(',') if feature):
                    removed_images.append(image)
                else:
                    new_images.append(image)
            self.AlternativeImage = new_images
        else:
            removed_images = existing_images
            self.AlternativeImage = []
        if hasattr(self, 'id'):
            name = self.id
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'pcGtsId'):
            name = self.parent_object_.pcGtsId
        else:
            name = ''
        for image in removed_images:
            self.gds_collector_.add_message('Removing AlternativeImage %s from "%s"' % (
                image.get_comments() or '', name))
    def set_Coords(self, Coords):
        """
        Set coordinate polygon by given object.
        Moreover, invalidate self's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # RegionType, TextLineType, WordType, GlyphType:
            self.invalidate_AlternativeImage()
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'invalidate_AlternativeImage'):
            # BorderType:
            self.parent_object_.invalidate_AlternativeImage(feature_selector='cropped')
        self.Coords = Coords
# end class TextLineType


class WordType(GeneratedsSuper):
    """Overrides primaryLanguage attribute of parent line
    and/or text region
    The primary script used in the word
    The secondary script used in the word
    The direction in which text within the word
    should be read (order of characters).
    Overrides the production attribute of the parent
    text line and/or text region.
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('language', 'pc:LanguageSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('primaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('secondaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('readingDirection', 'pc:ReadingDirectionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('production', 'pc:ProductionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('AlternativeImage', 'AlternativeImageType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'AlternativeImage', 'type': 'AlternativeImageType'}, None),
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
        MemberSpec_('Glyph', 'GlyphType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Glyph', 'type': 'GlyphType'}, None),
        MemberSpec_('TextEquiv', 'TextEquivType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'TextEquiv', 'type': 'TextEquivType'}, None),
        MemberSpec_('TextStyle', 'TextStyleType', 0, 1, {'minOccurs': '0', 'name': 'TextStyle', 'type': 'TextStyleType'}, None),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, language=None, primaryScript=None, secondaryScript=None, readingDirection=None, production=None, custom=None, comments=None, AlternativeImage=None, Coords=None, Glyph=None, TextEquiv=None, TextStyle=None, UserDefined=None, Labels=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.language = _cast(None, language)
        self.language_nsprefix_ = "pc"
        self.primaryScript = _cast(None, primaryScript)
        self.primaryScript_nsprefix_ = "pc"
        self.secondaryScript = _cast(None, secondaryScript)
        self.secondaryScript_nsprefix_ = "pc"
        self.readingDirection = _cast(None, readingDirection)
        self.readingDirection_nsprefix_ = "pc"
        self.production = _cast(None, production)
        self.production_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        if AlternativeImage is None:
            self.AlternativeImage = []
        else:
            self.AlternativeImage = AlternativeImage
        self.AlternativeImage_nsprefix_ = "pc"
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
        if Glyph is None:
            self.Glyph = []
        else:
            self.Glyph = Glyph
        self.Glyph_nsprefix_ = "pc"
        if TextEquiv is None:
            self.TextEquiv = []
        else:
            self.TextEquiv = TextEquiv
        self.TextEquiv_nsprefix_ = "pc"
        self.TextStyle = TextStyle
        self.TextStyle_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, WordType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if WordType.subclass:
            return WordType.subclass(*args_, **kwargs_)
        else:
            return WordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AlternativeImage(self):
        return self.AlternativeImage
    def set_AlternativeImage(self, AlternativeImage):
        self.AlternativeImage = AlternativeImage
    def add_AlternativeImage(self, value):
        self.AlternativeImage.append(value)
    def insert_AlternativeImage_at(self, index, value):
        self.AlternativeImage.insert(index, value)
    def replace_AlternativeImage_at(self, index, value):
        self.AlternativeImage[index] = value
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def get_Glyph(self):
        return self.Glyph
    def set_Glyph(self, Glyph):
        self.Glyph = Glyph
    def add_Glyph(self, value):
        self.Glyph.append(value)
    def insert_Glyph_at(self, index, value):
        self.Glyph.insert(index, value)
    def replace_Glyph_at(self, index, value):
        self.Glyph[index] = value
    def get_TextEquiv(self):
        return self.TextEquiv
    def set_TextEquiv(self, TextEquiv):
        self.TextEquiv = TextEquiv
    def add_TextEquiv(self, value):
        self.TextEquiv.append(value)
    def insert_TextEquiv_at(self, index, value):
        self.TextEquiv.insert(index, value)
    def replace_TextEquiv_at(self, index, value):
        self.TextEquiv[index] = value
    def get_TextStyle(self):
        return self.TextStyle
    def set_TextStyle(self, TextStyle):
        self.TextStyle = TextStyle
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_language(self):
        return self.language
    def set_language(self, language):
        self.language = language
    def get_primaryScript(self):
        return self.primaryScript
    def set_primaryScript(self, primaryScript):
        self.primaryScript = primaryScript
    def get_secondaryScript(self):
        return self.secondaryScript
    def set_secondaryScript(self, secondaryScript):
        self.secondaryScript = secondaryScript
    def get_readingDirection(self):
        return self.readingDirection
    def set_readingDirection(self, readingDirection):
        self.readingDirection = readingDirection
    def get_production(self):
        return self.production
    def set_production(self, production):
        self.production = production
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_LanguageSimpleType(self, value):
        # Validate type pc:LanguageSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Abkhaz', 'Afar', 'Afrikaans', 'Akan', 'Albanian', 'Amharic', 'Arabic', 'Aragonese', 'Armenian', 'Assamese', 'Avaric', 'Avestan', 'Aymara', 'Azerbaijani', 'Bambara', 'Bashkir', 'Basque', 'Belarusian', 'Bengali', 'Bihari', 'Bislama', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', 'Cambodian', 'Cantonese', 'Catalan', 'Chamorro', 'Chechen', 'Chichewa', 'Chinese', 'Chuvash', 'Cornish', 'Corsican', 'Cree', 'Croatian', 'Czech', 'Danish', 'Divehi', 'Dutch', 'Dzongkha', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'French', 'Fula', 'Gaelic', 'Galician', 'Ganda', 'Georgian', 'German', 'Greek', 'Guaraní', 'Gujarati', 'Haitian', 'Hausa', 'Hebrew', 'Herero', 'Hindi', 'Hiri Motu', 'Hungarian', 'Icelandic', 'Ido', 'Igbo', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiaq', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kalaallisut', 'Kannada', 'Kanuri', 'Kashmiri', 'Kazakh', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kirundi', 'Komi', 'Kongo', 'Korean', 'Kurdish', 'Kwanyama', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Limburgish', 'Lingala', 'Lithuanian', 'Luba-Katanga', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Manx', 'Māori', 'Marathi', 'Marshallese', 'Mongolian', 'Nauru', 'Navajo', 'Ndonga', 'Nepali', 'North Ndebele', 'Northern Sami', 'Norwegian', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Nuosu', 'Occitan', 'Ojibwe', 'Old Church Slavonic', 'Oriya', 'Oromo', 'Ossetian', 'Pāli', 'Panjabi', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Romansh', 'Russian', 'Samoan', 'Sango', 'Sanskrit', 'Sardinian', 'Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovene', 'Somali', 'South Ndebele', 'Southern Sotho', 'Spanish', 'Sundanese', 'Swahili', 'Swati', 'Swedish', 'Tagalog', 'Tahitian', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Tswana', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda', 'Vietnamese', 'Volapük', 'Walloon', 'Welsh', 'Western Frisian', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zhuang', 'Zulu', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LanguageSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ScriptSimpleType(self, value):
        # Validate type pc:ScriptSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Adlm - Adlam', 'Afak - Afaka', 'Aghb - Caucasian Albanian', 'Ahom - Ahom, Tai Ahom', 'Arab - Arabic', 'Aran - Arabic (Nastaliq variant)', 'Armi - Imperial Aramaic', 'Armn - Armenian', 'Avst - Avestan', 'Bali - Balinese', 'Bamu - Bamum', 'Bass - Bassa Vah', 'Batk - Batak', 'Beng - Bengali', 'Bhks - Bhaiksuki', 'Blis - Blissymbols', 'Bopo - Bopomofo', 'Brah - Brahmi', 'Brai - Braille', 'Bugi - Buginese', 'Buhd - Buhid', 'Cakm - Chakma', 'Cans - Unified Canadian Aboriginal Syllabics', 'Cari - Carian', 'Cham - Cham', 'Cher - Cherokee', 'Cirt - Cirth', 'Copt - Coptic', 'Cprt - Cypriot', 'Cyrl - Cyrillic', 'Cyrs - Cyrillic (Old Church Slavonic variant)', 'Deva - Devanagari (Nagari)', 'Dsrt - Deseret (Mormon)', 'Dupl - Duployan shorthand, Duployan stenography', 'Egyd - Egyptian demotic', 'Egyh - Egyptian hieratic', 'Egyp - Egyptian hieroglyphs', 'Elba - Elbasan', 'Ethi - Ethiopic', 'Geok - Khutsuri (Asomtavruli and Nuskhuri)', 'Geor - Georgian (Mkhedruli)', 'Glag - Glagolitic', 'Goth - Gothic', 'Gran - Grantha', 'Grek - Greek', 'Gujr - Gujarati', 'Guru - Gurmukhi', 'Hanb - Han with Bopomofo', 'Hang - Hangul', 'Hani - Han (Hanzi, Kanji, Hanja)', 'Hano - Hanunoo (Hanunóo)', 'Hans - Han (Simplified variant)', 'Hant - Han (Traditional variant)', 'Hatr - Hatran', 'Hebr - Hebrew', 'Hira - Hiragana', 'Hluw - Anatolian Hieroglyphs', 'Hmng - Pahawh Hmong', 'Hrkt - Japanese syllabaries', 'Hung - Old Hungarian (Hungarian Runic)', 'Inds - Indus (Harappan)', 'Ital - Old Italic (Etruscan, Oscan etc.)', 'Jamo - Jamo', 'Java - Javanese', 'Jpan - Japanese', 'Jurc - Jurchen', 'Kali - Kayah Li', 'Kana - Katakana', 'Khar - Kharoshthi', 'Khmr - Khmer', 'Khoj - Khojki', 'Kitl - Khitan large script', 'Kits - Khitan small script', 'Knda - Kannada', 'Kore - Korean (alias for Hangul + Han)', 'Kpel - Kpelle', 'Kthi - Kaithi', 'Lana - Tai Tham (Lanna)', 'Laoo - Lao', 'Latf - Latin (Fraktur variant)', 'Latg - Latin (Gaelic variant)', 'Latn - Latin', 'Leke - Leke', 'Lepc - Lepcha (Róng)', 'Limb - Limbu', 'Lina - Linear A', 'Linb - Linear B', 'Lisu - Lisu (Fraser)', 'Loma - Loma', 'Lyci - Lycian', 'Lydi - Lydian', 'Mahj - Mahajani', 'Mand - Mandaic, Mandaean', 'Mani - Manichaean', 'Marc - Marchen', 'Maya - Mayan hieroglyphs', 'Mend - Mende Kikakui', 'Merc - Meroitic Cursive', 'Mero - Meroitic Hieroglyphs', 'Mlym - Malayalam', 'Modi - Modi, Moḍī', 'Mong - Mongolian', 'Moon - Moon (Moon code, Moon script, Moon type)', 'Mroo - Mro, Mru', 'Mtei - Meitei Mayek (Meithei, Meetei)', 'Mult - Multani', 'Mymr - Myanmar (Burmese)', 'Narb - Old North Arabian (Ancient North Arabian)', 'Nbat - Nabataean', 'Newa - Newa, Newar, Newari', 'Nkgb - Nakhi Geba', 'Nkoo - N’Ko', 'Nshu - Nüshu', 'Ogam - Ogham', 'Olck - Ol Chiki (Ol Cemet’, Ol, Santali)', 'Orkh - Old Turkic, Orkhon Runic', 'Orya - Oriya', 'Osge - Osage', 'Osma - Osmanya', 'Palm - Palmyrene', 'Pauc - Pau Cin Hau', 'Perm - Old Permic', 'Phag - Phags-pa', 'Phli - Inscriptional Pahlavi', 'Phlp - Psalter Pahlavi', 'Phlv - Book Pahlavi', 'Phnx - Phoenician', 'Piqd - Klingon (KLI pIqaD)', 'Plrd - Miao (Pollard)', 'Prti - Inscriptional Parthian', 'Rjng - Rejang (Redjang, Kaganga)', 'Roro - Rongorongo', 'Runr - Runic', 'Samr - Samaritan', 'Sara - Sarati', 'Sarb - Old South Arabian', 'Saur - Saurashtra', 'Sgnw - SignWriting', 'Shaw - Shavian (Shaw)', 'Shrd - Sharada, Śāradā', 'Sidd - Siddham', 'Sind - Khudawadi, Sindhi', 'Sinh - Sinhala', 'Sora - Sora Sompeng', 'Sund - Sundanese', 'Sylo - Syloti Nagri', 'Syrc - Syriac', 'Syre - Syriac (Estrangelo variant)', 'Syrj - Syriac (Western variant)', 'Syrn - Syriac (Eastern variant)', 'Tagb - Tagbanwa', 'Takr - Takri', 'Tale - Tai Le', 'Talu - New Tai Lue', 'Taml - Tamil', 'Tang - Tangut', 'Tavt - Tai Viet', 'Telu - Telugu', 'Teng - Tengwar', 'Tfng - Tifinagh (Berber)', 'Tglg - Tagalog (Baybayin, Alibata)', 'Thaa - Thaana', 'Thai - Thai', 'Tibt - Tibetan', 'Tirh - Tirhuta', 'Ugar - Ugaritic', 'Vaii - Vai', 'Visp - Visible Speech', 'Wara - Warang Citi (Varang Kshiti)', 'Wole - Woleai', 'Xpeo - Old Persian', 'Xsux - Cuneiform, Sumero-Akkadian', 'Yiii - Yi', 'Zinh - Code for inherited script', 'Zmth - Mathematical notation', 'Zsye - Symbols (Emoji variant)', 'Zsym - Symbols', 'Zxxx - Code for unwritten documents', 'Zyyy - Code for undetermined script', 'Zzzz - Code for uncoded script', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ScriptSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ReadingDirectionSimpleType(self, value):
        # Validate type pc:ReadingDirectionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['left-to-right', 'right-to-left', 'top-to-bottom', 'bottom-to-top']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ReadingDirectionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ProductionSimpleType(self, value):
        # Validate type pc:ProductionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['printed', 'typewritten', 'handwritten-cursive', 'handwritten-printscript', 'medieval-manuscript', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.AlternativeImage or
            self.Coords is not None or
            self.Glyph or
            self.TextEquiv or
            self.TextStyle is not None or
            self.UserDefined is not None or
            self.Labels
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='WordType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('WordType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'WordType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='WordType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='WordType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='WordType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.language is not None and 'language' not in already_processed:
            already_processed.add('language')
            outfile.write(' language=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.language), input_name='language')), ))
        if self.primaryScript is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            outfile.write(' primaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryScript), input_name='primaryScript')), ))
        if self.secondaryScript is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            outfile.write(' secondaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.secondaryScript), input_name='secondaryScript')), ))
        if self.readingDirection is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            outfile.write(' readingDirection=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.readingDirection), input_name='readingDirection')), ))
        if self.production is not None and 'production' not in already_processed:
            already_processed.add('production')
            outfile.write(' production=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.production), input_name='production')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='WordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AlternativeImage_ in self.AlternativeImage:
            namespaceprefix_ = self.AlternativeImage_nsprefix_ + ':' if (UseCapturedNS_ and self.AlternativeImage_nsprefix_) else ''
            AlternativeImage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlternativeImage', pretty_print=pretty_print)
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
        for Glyph_ in self.Glyph:
            namespaceprefix_ = self.Glyph_nsprefix_ + ':' if (UseCapturedNS_ and self.Glyph_nsprefix_) else ''
            Glyph_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Glyph', pretty_print=pretty_print)
        for TextEquiv_ in self.TextEquiv:
            namespaceprefix_ = self.TextEquiv_nsprefix_ + ':' if (UseCapturedNS_ and self.TextEquiv_nsprefix_) else ''
            TextEquiv_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextEquiv', pretty_print=pretty_print)
        if self.TextStyle is not None:
            namespaceprefix_ = self.TextStyle_nsprefix_ + ':' if (UseCapturedNS_ and self.TextStyle_nsprefix_) else ''
            self.TextStyle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextStyle', pretty_print=pretty_print)
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('language', node)
        if value is not None and 'language' not in already_processed:
            already_processed.add('language')
            self.language = value
            self.validate_LanguageSimpleType(self.language)    # validate type LanguageSimpleType
        value = find_attr_value_('primaryScript', node)
        if value is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            self.primaryScript = value
            self.validate_ScriptSimpleType(self.primaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('secondaryScript', node)
        if value is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            self.secondaryScript = value
            self.validate_ScriptSimpleType(self.secondaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('readingDirection', node)
        if value is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            self.readingDirection = value
            self.validate_ReadingDirectionSimpleType(self.readingDirection)    # validate type ReadingDirectionSimpleType
        value = find_attr_value_('production', node)
        if value is not None and 'production' not in already_processed:
            already_processed.add('production')
            self.production = value
            self.validate_ProductionSimpleType(self.production)    # validate type ProductionSimpleType
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlternativeImage':
            obj_ = AlternativeImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlternativeImage.append(obj_)
            obj_.original_tagname_ = 'AlternativeImage'
        elif nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
        elif nodeName_ == 'Glyph':
            obj_ = GlyphType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Glyph.append(obj_)
            obj_.original_tagname_ = 'Glyph'
        elif nodeName_ == 'TextEquiv':
            obj_ = TextEquivType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextEquiv.append(obj_)
            obj_.original_tagname_ = 'TextEquiv'
        elif nodeName_ == 'TextStyle':
            obj_ = TextStyleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextStyle = obj_
            obj_.original_tagname_ = 'TextStyle'
        elif nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
    def __hash__(self):
        return hash(self.id)
    def invalidate_AlternativeImage(self, feature_selector=None):
        """
        Remove derived images from this segment (due to changed coordinates).
    
        If ``feature_selector`` is not none, remove only images with
        matching ``@comments``, e.g. ``feature_selector=cropped,deskewed``.
        """
        existing_images = self.AlternativeImage or []
        removed_images = []
        if feature_selector:
            new_images = []
            for image in existing_images:
                features = image.get_comments() or ''
                if any(feature in features.split(',')
                       for feature in feature_selector.split(',') if feature):
                    removed_images.append(image)
                else:
                    new_images.append(image)
            self.AlternativeImage = new_images
        else:
            removed_images = existing_images
            self.AlternativeImage = []
        if hasattr(self, 'id'):
            name = self.id
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'pcGtsId'):
            name = self.parent_object_.pcGtsId
        else:
            name = ''
        for image in removed_images:
            self.gds_collector_.add_message('Removing AlternativeImage %s from "%s"' % (
                image.get_comments() or '', name))
    def set_Coords(self, Coords):
        """
        Set coordinate polygon by given object.
        Moreover, invalidate self's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # RegionType, TextLineType, WordType, GlyphType:
            self.invalidate_AlternativeImage()
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'invalidate_AlternativeImage'):
            # BorderType:
            self.parent_object_.invalidate_AlternativeImage(feature_selector='cropped')
        self.Coords = Coords
# end class WordType


class GlyphType(GeneratedsSuper):
    """The script used for the glyph
    Overrides the production attribute of the parent
    word / text line / text region.
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('ligature', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('symbol', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('script', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('production', 'pc:ProductionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('AlternativeImage', 'AlternativeImageType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'AlternativeImage', 'type': 'AlternativeImageType'}, None),
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
        MemberSpec_('Graphemes', 'GraphemesType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Graphemes', 'type': 'GraphemesType'}, None),
        MemberSpec_('TextEquiv', 'TextEquivType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'TextEquiv', 'type': 'TextEquivType'}, None),
        MemberSpec_('TextStyle', 'TextStyleType', 0, 1, {'minOccurs': '0', 'name': 'TextStyle', 'type': 'TextStyleType'}, None),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, ligature=None, symbol=None, script=None, production=None, custom=None, comments=None, AlternativeImage=None, Coords=None, Graphemes=None, TextEquiv=None, TextStyle=None, UserDefined=None, Labels=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.ligature = _cast(bool, ligature)
        self.ligature_nsprefix_ = "pc"
        self.symbol = _cast(bool, symbol)
        self.symbol_nsprefix_ = "pc"
        self.script = _cast(None, script)
        self.script_nsprefix_ = "pc"
        self.production = _cast(None, production)
        self.production_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        if AlternativeImage is None:
            self.AlternativeImage = []
        else:
            self.AlternativeImage = AlternativeImage
        self.AlternativeImage_nsprefix_ = "pc"
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
        self.Graphemes = Graphemes
        self.Graphemes_nsprefix_ = "pc"
        if TextEquiv is None:
            self.TextEquiv = []
        else:
            self.TextEquiv = TextEquiv
        self.TextEquiv_nsprefix_ = "pc"
        self.TextStyle = TextStyle
        self.TextStyle_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GlyphType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GlyphType.subclass:
            return GlyphType.subclass(*args_, **kwargs_)
        else:
            return GlyphType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AlternativeImage(self):
        return self.AlternativeImage
    def set_AlternativeImage(self, AlternativeImage):
        self.AlternativeImage = AlternativeImage
    def add_AlternativeImage(self, value):
        self.AlternativeImage.append(value)
    def insert_AlternativeImage_at(self, index, value):
        self.AlternativeImage.insert(index, value)
    def replace_AlternativeImage_at(self, index, value):
        self.AlternativeImage[index] = value
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def get_Graphemes(self):
        return self.Graphemes
    def set_Graphemes(self, Graphemes):
        self.Graphemes = Graphemes
    def get_TextEquiv(self):
        return self.TextEquiv
    def set_TextEquiv(self, TextEquiv):
        self.TextEquiv = TextEquiv
    def add_TextEquiv(self, value):
        self.TextEquiv.append(value)
    def insert_TextEquiv_at(self, index, value):
        self.TextEquiv.insert(index, value)
    def replace_TextEquiv_at(self, index, value):
        self.TextEquiv[index] = value
    def get_TextStyle(self):
        return self.TextStyle
    def set_TextStyle(self, TextStyle):
        self.TextStyle = TextStyle
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_ligature(self):
        return self.ligature
    def set_ligature(self, ligature):
        self.ligature = ligature
    def get_symbol(self):
        return self.symbol
    def set_symbol(self, symbol):
        self.symbol = symbol
    def get_script(self):
        return self.script
    def set_script(self, script):
        self.script = script
    def get_production(self):
        return self.production
    def set_production(self, production):
        self.production = production
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_ScriptSimpleType(self, value):
        # Validate type pc:ScriptSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Adlm - Adlam', 'Afak - Afaka', 'Aghb - Caucasian Albanian', 'Ahom - Ahom, Tai Ahom', 'Arab - Arabic', 'Aran - Arabic (Nastaliq variant)', 'Armi - Imperial Aramaic', 'Armn - Armenian', 'Avst - Avestan', 'Bali - Balinese', 'Bamu - Bamum', 'Bass - Bassa Vah', 'Batk - Batak', 'Beng - Bengali', 'Bhks - Bhaiksuki', 'Blis - Blissymbols', 'Bopo - Bopomofo', 'Brah - Brahmi', 'Brai - Braille', 'Bugi - Buginese', 'Buhd - Buhid', 'Cakm - Chakma', 'Cans - Unified Canadian Aboriginal Syllabics', 'Cari - Carian', 'Cham - Cham', 'Cher - Cherokee', 'Cirt - Cirth', 'Copt - Coptic', 'Cprt - Cypriot', 'Cyrl - Cyrillic', 'Cyrs - Cyrillic (Old Church Slavonic variant)', 'Deva - Devanagari (Nagari)', 'Dsrt - Deseret (Mormon)', 'Dupl - Duployan shorthand, Duployan stenography', 'Egyd - Egyptian demotic', 'Egyh - Egyptian hieratic', 'Egyp - Egyptian hieroglyphs', 'Elba - Elbasan', 'Ethi - Ethiopic', 'Geok - Khutsuri (Asomtavruli and Nuskhuri)', 'Geor - Georgian (Mkhedruli)', 'Glag - Glagolitic', 'Goth - Gothic', 'Gran - Grantha', 'Grek - Greek', 'Gujr - Gujarati', 'Guru - Gurmukhi', 'Hanb - Han with Bopomofo', 'Hang - Hangul', 'Hani - Han (Hanzi, Kanji, Hanja)', 'Hano - Hanunoo (Hanunóo)', 'Hans - Han (Simplified variant)', 'Hant - Han (Traditional variant)', 'Hatr - Hatran', 'Hebr - Hebrew', 'Hira - Hiragana', 'Hluw - Anatolian Hieroglyphs', 'Hmng - Pahawh Hmong', 'Hrkt - Japanese syllabaries', 'Hung - Old Hungarian (Hungarian Runic)', 'Inds - Indus (Harappan)', 'Ital - Old Italic (Etruscan, Oscan etc.)', 'Jamo - Jamo', 'Java - Javanese', 'Jpan - Japanese', 'Jurc - Jurchen', 'Kali - Kayah Li', 'Kana - Katakana', 'Khar - Kharoshthi', 'Khmr - Khmer', 'Khoj - Khojki', 'Kitl - Khitan large script', 'Kits - Khitan small script', 'Knda - Kannada', 'Kore - Korean (alias for Hangul + Han)', 'Kpel - Kpelle', 'Kthi - Kaithi', 'Lana - Tai Tham (Lanna)', 'Laoo - Lao', 'Latf - Latin (Fraktur variant)', 'Latg - Latin (Gaelic variant)', 'Latn - Latin', 'Leke - Leke', 'Lepc - Lepcha (Róng)', 'Limb - Limbu', 'Lina - Linear A', 'Linb - Linear B', 'Lisu - Lisu (Fraser)', 'Loma - Loma', 'Lyci - Lycian', 'Lydi - Lydian', 'Mahj - Mahajani', 'Mand - Mandaic, Mandaean', 'Mani - Manichaean', 'Marc - Marchen', 'Maya - Mayan hieroglyphs', 'Mend - Mende Kikakui', 'Merc - Meroitic Cursive', 'Mero - Meroitic Hieroglyphs', 'Mlym - Malayalam', 'Modi - Modi, Moḍī', 'Mong - Mongolian', 'Moon - Moon (Moon code, Moon script, Moon type)', 'Mroo - Mro, Mru', 'Mtei - Meitei Mayek (Meithei, Meetei)', 'Mult - Multani', 'Mymr - Myanmar (Burmese)', 'Narb - Old North Arabian (Ancient North Arabian)', 'Nbat - Nabataean', 'Newa - Newa, Newar, Newari', 'Nkgb - Nakhi Geba', 'Nkoo - N’Ko', 'Nshu - Nüshu', 'Ogam - Ogham', 'Olck - Ol Chiki (Ol Cemet’, Ol, Santali)', 'Orkh - Old Turkic, Orkhon Runic', 'Orya - Oriya', 'Osge - Osage', 'Osma - Osmanya', 'Palm - Palmyrene', 'Pauc - Pau Cin Hau', 'Perm - Old Permic', 'Phag - Phags-pa', 'Phli - Inscriptional Pahlavi', 'Phlp - Psalter Pahlavi', 'Phlv - Book Pahlavi', 'Phnx - Phoenician', 'Piqd - Klingon (KLI pIqaD)', 'Plrd - Miao (Pollard)', 'Prti - Inscriptional Parthian', 'Rjng - Rejang (Redjang, Kaganga)', 'Roro - Rongorongo', 'Runr - Runic', 'Samr - Samaritan', 'Sara - Sarati', 'Sarb - Old South Arabian', 'Saur - Saurashtra', 'Sgnw - SignWriting', 'Shaw - Shavian (Shaw)', 'Shrd - Sharada, Śāradā', 'Sidd - Siddham', 'Sind - Khudawadi, Sindhi', 'Sinh - Sinhala', 'Sora - Sora Sompeng', 'Sund - Sundanese', 'Sylo - Syloti Nagri', 'Syrc - Syriac', 'Syre - Syriac (Estrangelo variant)', 'Syrj - Syriac (Western variant)', 'Syrn - Syriac (Eastern variant)', 'Tagb - Tagbanwa', 'Takr - Takri', 'Tale - Tai Le', 'Talu - New Tai Lue', 'Taml - Tamil', 'Tang - Tangut', 'Tavt - Tai Viet', 'Telu - Telugu', 'Teng - Tengwar', 'Tfng - Tifinagh (Berber)', 'Tglg - Tagalog (Baybayin, Alibata)', 'Thaa - Thaana', 'Thai - Thai', 'Tibt - Tibetan', 'Tirh - Tirhuta', 'Ugar - Ugaritic', 'Vaii - Vai', 'Visp - Visible Speech', 'Wara - Warang Citi (Varang Kshiti)', 'Wole - Woleai', 'Xpeo - Old Persian', 'Xsux - Cuneiform, Sumero-Akkadian', 'Yiii - Yi', 'Zinh - Code for inherited script', 'Zmth - Mathematical notation', 'Zsye - Symbols (Emoji variant)', 'Zsym - Symbols', 'Zxxx - Code for unwritten documents', 'Zyyy - Code for undetermined script', 'Zzzz - Code for uncoded script', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ScriptSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ProductionSimpleType(self, value):
        # Validate type pc:ProductionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['printed', 'typewritten', 'handwritten-cursive', 'handwritten-printscript', 'medieval-manuscript', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.AlternativeImage or
            self.Coords is not None or
            self.Graphemes is not None or
            self.TextEquiv or
            self.TextStyle is not None or
            self.UserDefined is not None or
            self.Labels
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GlyphType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GlyphType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GlyphType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GlyphType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GlyphType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GlyphType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.ligature is not None and 'ligature' not in already_processed:
            already_processed.add('ligature')
            outfile.write(' ligature="%s"' % self.gds_format_boolean(self.ligature, input_name='ligature'))
        if self.symbol is not None and 'symbol' not in already_processed:
            already_processed.add('symbol')
            outfile.write(' symbol="%s"' % self.gds_format_boolean(self.symbol, input_name='symbol'))
        if self.script is not None and 'script' not in already_processed:
            already_processed.add('script')
            outfile.write(' script=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.script), input_name='script')), ))
        if self.production is not None and 'production' not in already_processed:
            already_processed.add('production')
            outfile.write(' production=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.production), input_name='production')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GlyphType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AlternativeImage_ in self.AlternativeImage:
            namespaceprefix_ = self.AlternativeImage_nsprefix_ + ':' if (UseCapturedNS_ and self.AlternativeImage_nsprefix_) else ''
            AlternativeImage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlternativeImage', pretty_print=pretty_print)
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
        if self.Graphemes is not None:
            namespaceprefix_ = self.Graphemes_nsprefix_ + ':' if (UseCapturedNS_ and self.Graphemes_nsprefix_) else ''
            self.Graphemes.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Graphemes', pretty_print=pretty_print)
        for TextEquiv_ in self.TextEquiv:
            namespaceprefix_ = self.TextEquiv_nsprefix_ + ':' if (UseCapturedNS_ and self.TextEquiv_nsprefix_) else ''
            TextEquiv_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextEquiv', pretty_print=pretty_print)
        if self.TextStyle is not None:
            namespaceprefix_ = self.TextStyle_nsprefix_ + ':' if (UseCapturedNS_ and self.TextStyle_nsprefix_) else ''
            self.TextStyle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextStyle', pretty_print=pretty_print)
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('ligature', node)
        if value is not None and 'ligature' not in already_processed:
            already_processed.add('ligature')
            if value in ('true', '1'):
                self.ligature = True
            elif value in ('false', '0'):
                self.ligature = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('symbol', node)
        if value is not None and 'symbol' not in already_processed:
            already_processed.add('symbol')
            if value in ('true', '1'):
                self.symbol = True
            elif value in ('false', '0'):
                self.symbol = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('script', node)
        if value is not None and 'script' not in already_processed:
            already_processed.add('script')
            self.script = value
            self.validate_ScriptSimpleType(self.script)    # validate type ScriptSimpleType
        value = find_attr_value_('production', node)
        if value is not None and 'production' not in already_processed:
            already_processed.add('production')
            self.production = value
            self.validate_ProductionSimpleType(self.production)    # validate type ProductionSimpleType
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlternativeImage':
            obj_ = AlternativeImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlternativeImage.append(obj_)
            obj_.original_tagname_ = 'AlternativeImage'
        elif nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
        elif nodeName_ == 'Graphemes':
            obj_ = GraphemesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Graphemes = obj_
            obj_.original_tagname_ = 'Graphemes'
        elif nodeName_ == 'TextEquiv':
            obj_ = TextEquivType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextEquiv.append(obj_)
            obj_.original_tagname_ = 'TextEquiv'
        elif nodeName_ == 'TextStyle':
            obj_ = TextStyleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextStyle = obj_
            obj_.original_tagname_ = 'TextStyle'
        elif nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
    def __hash__(self):
        return hash(self.id)
    def invalidate_AlternativeImage(self, feature_selector=None):
        """
        Remove derived images from this segment (due to changed coordinates).
    
        If ``feature_selector`` is not none, remove only images with
        matching ``@comments``, e.g. ``feature_selector=cropped,deskewed``.
        """
        existing_images = self.AlternativeImage or []
        removed_images = []
        if feature_selector:
            new_images = []
            for image in existing_images:
                features = image.get_comments() or ''
                if any(feature in features.split(',')
                       for feature in feature_selector.split(',') if feature):
                    removed_images.append(image)
                else:
                    new_images.append(image)
            self.AlternativeImage = new_images
        else:
            removed_images = existing_images
            self.AlternativeImage = []
        if hasattr(self, 'id'):
            name = self.id
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'pcGtsId'):
            name = self.parent_object_.pcGtsId
        else:
            name = ''
        for image in removed_images:
            self.gds_collector_.add_message('Removing AlternativeImage %s from "%s"' % (
                image.get_comments() or '', name))
    def set_Coords(self, Coords):
        """
        Set coordinate polygon by given object.
        Moreover, invalidate self's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # RegionType, TextLineType, WordType, GlyphType:
            self.invalidate_AlternativeImage()
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'invalidate_AlternativeImage'):
            # BorderType:
            self.parent_object_.invalidate_AlternativeImage(feature_selector='cropped')
        self.Coords = Coords
# end class GlyphType


class TextEquivType(GeneratedsSuper):
    """Used for sort order in case multiple TextEquivs are defined.
    The text content with the lowest index should be interpreted
    as the main text content.
    OCR confidence value (between 0 and 1)
    Type of text content (is it free text or a number, for instance).
    This is only a descriptive attribute, the text type
    is not checked during XML validation.
    Refinement for dataType attribute. Can be a regular expression, for
    instance."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('index', 'integer', 0, 1, {'use': 'optional'}),
        MemberSpec_('conf', 'pc:ConfSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('dataType', 'pc:TextDataTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('dataTypeDetails', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('PlainText', 'string', 0, 1, {'minOccurs': '0', 'name': 'PlainText', 'type': 'string'}, None),
        MemberSpec_('Unicode', 'string', 0, 0, {'name': 'Unicode', 'type': 'string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, index=None, conf=None, dataType=None, dataTypeDetails=None, comments=None, PlainText=None, Unicode=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        self.conf = _cast(float, conf)
        self.conf_nsprefix_ = "pc"
        self.dataType = _cast(None, dataType)
        self.dataType_nsprefix_ = "pc"
        self.dataTypeDetails = _cast(None, dataTypeDetails)
        self.dataTypeDetails_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.PlainText = PlainText
        self.PlainText_nsprefix_ = "pc"
        self.Unicode = Unicode
        self.Unicode_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TextEquivType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TextEquivType.subclass:
            return TextEquivType.subclass(*args_, **kwargs_)
        else:
            return TextEquivType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_PlainText(self):
        return self.PlainText
    def set_PlainText(self, PlainText):
        self.PlainText = PlainText
    def get_Unicode(self):
        return self.Unicode
    def set_Unicode(self, Unicode):
        self.Unicode = Unicode
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_conf(self):
        return self.conf
    def set_conf(self, conf):
        self.conf = conf
    def get_dataType(self):
        return self.dataType
    def set_dataType(self, dataType):
        self.dataType = dataType
    def get_dataTypeDetails(self):
        return self.dataTypeDetails
    def set_dataTypeDetails(self, dataTypeDetails):
        self.dataTypeDetails = dataTypeDetails
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_ConfSimpleType(self, value):
        # Validate type pc:ConfSimpleType, a restriction on float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
    def validate_TextDataTypeSimpleType(self, value):
        # Validate type pc:TextDataTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['xsd:decimal', 'xsd:float', 'xsd:integer', 'xsd:boolean', 'xsd:date', 'xsd:time', 'xsd:dateTime', 'xsd:string', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TextDataTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.PlainText is not None or
            self.Unicode is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TextEquivType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TextEquivType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TextEquivType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextEquivType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TextEquivType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TextEquivType'):
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_float(self.conf, input_name='conf'))
        if self.dataType is not None and 'dataType' not in already_processed:
            already_processed.add('dataType')
            outfile.write(' dataType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.dataType), input_name='dataType')), ))
        if self.dataTypeDetails is not None and 'dataTypeDetails' not in already_processed:
            already_processed.add('dataTypeDetails')
            outfile.write(' dataTypeDetails=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.dataTypeDetails), input_name='dataTypeDetails')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15" xmlns:None="http://www.w3.org/2001/XMLSchema" ', name_='TextEquivType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PlainText is not None:
            namespaceprefix_ = self.PlainText_nsprefix_ + ':' if (UseCapturedNS_ and self.PlainText_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sPlainText>%s</%sPlainText>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.PlainText), input_name='PlainText')), namespaceprefix_ , eol_))
        if self.Unicode is not None:
            namespaceprefix_ = self.Unicode_nsprefix_ + ':' if (UseCapturedNS_ and self.Unicode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUnicode>%s</%sUnicode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Unicode), input_name='Unicode')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            value = self.gds_parse_float(value, node, 'conf')
            self.conf = value
            self.validate_ConfSimpleType(self.conf)    # validate type ConfSimpleType
        value = find_attr_value_('dataType', node)
        if value is not None and 'dataType' not in already_processed:
            already_processed.add('dataType')
            self.dataType = value
            self.validate_TextDataTypeSimpleType(self.dataType)    # validate type TextDataTypeSimpleType
        value = find_attr_value_('dataTypeDetails', node)
        if value is not None and 'dataTypeDetails' not in already_processed:
            already_processed.add('dataTypeDetails')
            self.dataTypeDetails = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'PlainText':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'PlainText')
            value_ = self.gds_validate_string(value_, node, 'PlainText')
            self.PlainText = value_

        elif nodeName_ == 'Unicode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Unicode')
            value_ = self.gds_validate_string(value_, node, 'Unicode')
            self.Unicode = value_

    def __hash__(self):
        return hash(self.id)
# end class TextEquivType


class GridType(GeneratedsSuper):
    """Matrix of grid points defining the table grid on the page."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('GridPoints', 'GridPointsType', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '2', 'name': 'GridPoints', 'type': 'GridPointsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, GridPoints=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if GridPoints is None:
            self.GridPoints = []
        else:
            self.GridPoints = GridPoints
        self.GridPoints_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GridType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GridType.subclass:
            return GridType.subclass(*args_, **kwargs_)
        else:
            return GridType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_GridPoints(self):
        return self.GridPoints
    def set_GridPoints(self, GridPoints):
        self.GridPoints = GridPoints
    def add_GridPoints(self, value):
        self.GridPoints.append(value)
    def insert_GridPoints_at(self, index, value):
        self.GridPoints.insert(index, value)
    def replace_GridPoints_at(self, index, value):
        self.GridPoints[index] = value
    def hasContent_(self):
        if (
            self.GridPoints
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GridType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GridType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GridType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GridType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GridType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GridType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GridType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for GridPoints_ in self.GridPoints:
            namespaceprefix_ = self.GridPoints_nsprefix_ + ':' if (UseCapturedNS_ and self.GridPoints_nsprefix_) else ''
            GridPoints_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GridPoints', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'GridPoints':
            obj_ = GridPointsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GridPoints.append(obj_)
            obj_.original_tagname_ = 'GridPoints'
    def __hash__(self):
        return hash(self.id)
# end class GridType


class GridPointsType(GeneratedsSuper):
    """Points with x,y coordinates.
    The grid row index"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('index', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('points', 'pc:PointsType', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, index=None, points=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        self.points = _cast(None, points)
        self.points_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GridPointsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GridPointsType.subclass:
            return GridPointsType.subclass(*args_, **kwargs_)
        else:
            return GridPointsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_points(self):
        return self.points
    def set_points(self, points):
        self.points = points
    def validate_PointsType(self, value):
        # Validate type pc:PointsType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PointsType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PointsType_patterns_, ))
    validate_PointsType_patterns_ = [['^(([0-9]+,[0-9]+ )+([0-9]+,[0-9]+))$']]
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GridPointsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GridPointsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GridPointsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GridPointsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GridPointsType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GridPointsType'):
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.points is not None and 'points' not in already_processed:
            already_processed.add('points')
            outfile.write(' points=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.points), input_name='points')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GridPointsType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
        value = find_attr_value_('points', node)
        if value is not None and 'points' not in already_processed:
            already_processed.add('points')
            self.points = value
            self.validate_PointsType(self.points)    # validate type PointsType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class GridPointsType


class PrintSpaceType(GeneratedsSuper):
    """Determines the effective area on the paper of a printed page.
    Its size is equal for all pages of a book
    (exceptions: titlepage, multipage pictures).
    It contains all living elements (except marginals)
    like body type, footnotes, headings, running titles.
    It does not contain pagenumber (if not part of running title),
    marginals, signature mark, preview words."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Coords=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PrintSpaceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PrintSpaceType.subclass:
            return PrintSpaceType.subclass(*args_, **kwargs_)
        else:
            return PrintSpaceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def hasContent_(self):
        if (
            self.Coords is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='PrintSpaceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PrintSpaceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'PrintSpaceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PrintSpaceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PrintSpaceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='PrintSpaceType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='PrintSpaceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
    def __hash__(self):
        return hash(self.id)
# end class PrintSpaceType


class ReadingOrderType(GeneratedsSuper):
    """Definition of the reading order within the page.
    To express a reading order between elements
    they have to be included in an OrderedGroup.
    Groups may contain further groups.
    Confidence value (between 0 and 1)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('conf', 'pc:ConfSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('OrderedGroup', 'OrderedGroupType', 0, 0, {'name': 'OrderedGroup', 'type': 'OrderedGroupType'}, 2),
        MemberSpec_('UnorderedGroup', 'UnorderedGroupType', 0, 0, {'name': 'UnorderedGroup', 'type': 'UnorderedGroupType'}, 2),
    ]
    subclass = None
    superclass = None
    def __init__(self, conf=None, OrderedGroup=None, UnorderedGroup=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.conf = _cast(float, conf)
        self.conf_nsprefix_ = "pc"
        self.OrderedGroup = OrderedGroup
        self.OrderedGroup_nsprefix_ = "pc"
        self.UnorderedGroup = UnorderedGroup
        self.UnorderedGroup_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReadingOrderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReadingOrderType.subclass:
            return ReadingOrderType.subclass(*args_, **kwargs_)
        else:
            return ReadingOrderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_OrderedGroup(self):
        return self.OrderedGroup
    def set_OrderedGroup(self, OrderedGroup):
        self.OrderedGroup = OrderedGroup
    def get_UnorderedGroup(self):
        return self.UnorderedGroup
    def set_UnorderedGroup(self, UnorderedGroup):
        self.UnorderedGroup = UnorderedGroup
    def get_conf(self):
        return self.conf
    def set_conf(self, conf):
        self.conf = conf
    def validate_ConfSimpleType(self, value):
        # Validate type pc:ConfSimpleType, a restriction on float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.OrderedGroup is not None or
            self.UnorderedGroup is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='ReadingOrderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReadingOrderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReadingOrderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReadingOrderType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReadingOrderType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ReadingOrderType'):
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_float(self.conf, input_name='conf'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='ReadingOrderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.OrderedGroup is not None:
            namespaceprefix_ = self.OrderedGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.OrderedGroup_nsprefix_) else ''
            self.OrderedGroup.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrderedGroup', pretty_print=pretty_print)
        if self.UnorderedGroup is not None:
            namespaceprefix_ = self.UnorderedGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.UnorderedGroup_nsprefix_) else ''
            self.UnorderedGroup.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnorderedGroup', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            value = self.gds_parse_float(value, node, 'conf')
            self.conf = value
            self.validate_ConfSimpleType(self.conf)    # validate type ConfSimpleType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OrderedGroup':
            obj_ = OrderedGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrderedGroup = obj_
            obj_.original_tagname_ = 'OrderedGroup'
        elif nodeName_ == 'UnorderedGroup':
            obj_ = UnorderedGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnorderedGroup = obj_
            obj_.original_tagname_ = 'UnorderedGroup'
    def __hash__(self):
        return hash(self.id)
# end class ReadingOrderType


class RegionRefIndexedType(GeneratedsSuper):
    """Numbered regionPosition (order number) of this item within the current
    hierarchy level."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('index', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('regionRef', 'string', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, index=None, regionRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        self.regionRef = _cast(None, regionRef)
        self.regionRef_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RegionRefIndexedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RegionRefIndexedType.subclass:
            return RegionRefIndexedType.subclass(*args_, **kwargs_)
        else:
            return RegionRefIndexedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_regionRef(self):
        return self.regionRef
    def set_regionRef(self, regionRef):
        self.regionRef = regionRef
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RegionRefIndexedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RegionRefIndexedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RegionRefIndexedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RegionRefIndexedType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RegionRefIndexedType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RegionRefIndexedType'):
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.regionRef is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            outfile.write(' regionRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regionRef), input_name='regionRef')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RegionRefIndexedType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
        value = find_attr_value_('regionRef', node)
        if value is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            self.regionRef = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class RegionRefIndexedType


class OrderedGroupIndexedType(GeneratedsSuper):
    """Indexed group containing ordered elements
    Optional link to a parent region of nested regions.
    The parent region doubles as reading order group.
    Only the nested regions should be allowed as group members.
    Position (order number) of this item within the
    current hierarchy level.
    Is this group a continuation of another group (from
    previous column or page, for example)?
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('regionRef', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('index', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('caption', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:GroupTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('continuation', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('RegionRefIndexed', 'RegionRefIndexedType', 1, 0, {'name': 'RegionRefIndexed', 'type': 'RegionRefIndexedType'}, 3),
        MemberSpec_('OrderedGroupIndexed', 'OrderedGroupIndexedType', 1, 0, {'name': 'OrderedGroupIndexed', 'type': 'OrderedGroupIndexedType'}, 3),
        MemberSpec_('UnorderedGroupIndexed', 'UnorderedGroupIndexedType', 1, 0, {'name': 'UnorderedGroupIndexed', 'type': 'UnorderedGroupIndexedType'}, 3),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, regionRef=None, index=None, caption=None, type_=None, continuation=None, custom=None, comments=None, UserDefined=None, Labels=None, RegionRefIndexed=None, OrderedGroupIndexed=None, UnorderedGroupIndexed=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.regionRef = _cast(None, regionRef)
        self.regionRef_nsprefix_ = "pc"
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        self.caption = _cast(None, caption)
        self.caption_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.continuation = _cast(bool, continuation)
        self.continuation_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        if RegionRefIndexed is None:
            self.RegionRefIndexed = []
        else:
            self.RegionRefIndexed = RegionRefIndexed
        self.RegionRefIndexed_nsprefix_ = "pc"
        if OrderedGroupIndexed is None:
            self.OrderedGroupIndexed = []
        else:
            self.OrderedGroupIndexed = OrderedGroupIndexed
        self.OrderedGroupIndexed_nsprefix_ = "pc"
        if UnorderedGroupIndexed is None:
            self.UnorderedGroupIndexed = []
        else:
            self.UnorderedGroupIndexed = UnorderedGroupIndexed
        self.UnorderedGroupIndexed_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OrderedGroupIndexedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OrderedGroupIndexedType.subclass:
            return OrderedGroupIndexedType.subclass(*args_, **kwargs_)
        else:
            return OrderedGroupIndexedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_RegionRefIndexed(self):
        return self.RegionRefIndexed
    def set_RegionRefIndexed(self, RegionRefIndexed):
        self.RegionRefIndexed = RegionRefIndexed
    def add_RegionRefIndexed(self, value):
        self.RegionRefIndexed.append(value)
    def insert_RegionRefIndexed_at(self, index, value):
        self.RegionRefIndexed.insert(index, value)
    def replace_RegionRefIndexed_at(self, index, value):
        self.RegionRefIndexed[index] = value
    def get_OrderedGroupIndexed(self):
        return self.OrderedGroupIndexed
    def set_OrderedGroupIndexed(self, OrderedGroupIndexed):
        self.OrderedGroupIndexed = OrderedGroupIndexed
    def add_OrderedGroupIndexed(self, value):
        self.OrderedGroupIndexed.append(value)
    def insert_OrderedGroupIndexed_at(self, index, value):
        self.OrderedGroupIndexed.insert(index, value)
    def replace_OrderedGroupIndexed_at(self, index, value):
        self.OrderedGroupIndexed[index] = value
    def get_UnorderedGroupIndexed(self):
        return self.UnorderedGroupIndexed
    def set_UnorderedGroupIndexed(self, UnorderedGroupIndexed):
        self.UnorderedGroupIndexed = UnorderedGroupIndexed
    def add_UnorderedGroupIndexed(self, value):
        self.UnorderedGroupIndexed.append(value)
    def insert_UnorderedGroupIndexed_at(self, index, value):
        self.UnorderedGroupIndexed.insert(index, value)
    def replace_UnorderedGroupIndexed_at(self, index, value):
        self.UnorderedGroupIndexed[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_regionRef(self):
        return self.regionRef
    def set_regionRef(self, regionRef):
        self.regionRef = regionRef
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_caption(self):
        return self.caption
    def set_caption(self, caption):
        self.caption = caption
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_continuation(self):
        return self.continuation
    def set_continuation(self, continuation):
        self.continuation = continuation
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_GroupTypeSimpleType(self, value):
        # Validate type pc:GroupTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['paragraph', 'list', 'list-item', 'figure', 'article', 'div', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on GroupTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.UserDefined is not None or
            self.Labels or
            self.RegionRefIndexed or
            self.OrderedGroupIndexed or
            self.UnorderedGroupIndexed
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='OrderedGroupIndexedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OrderedGroupIndexedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OrderedGroupIndexedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OrderedGroupIndexedType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OrderedGroupIndexedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OrderedGroupIndexedType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.regionRef is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            outfile.write(' regionRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regionRef), input_name='regionRef')), ))
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.caption is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            outfile.write(' caption=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.caption), input_name='caption')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.continuation is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            outfile.write(' continuation="%s"' % self.gds_format_boolean(self.continuation, input_name='continuation'))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='OrderedGroupIndexedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        for RegionRefIndexed_ in self.RegionRefIndexed:
            namespaceprefix_ = self.RegionRefIndexed_nsprefix_ + ':' if (UseCapturedNS_ and self.RegionRefIndexed_nsprefix_) else ''
            RegionRefIndexed_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RegionRefIndexed', pretty_print=pretty_print)
        for OrderedGroupIndexed_ in self.OrderedGroupIndexed:
            namespaceprefix_ = self.OrderedGroupIndexed_nsprefix_ + ':' if (UseCapturedNS_ and self.OrderedGroupIndexed_nsprefix_) else ''
            OrderedGroupIndexed_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrderedGroupIndexed', pretty_print=pretty_print)
        for UnorderedGroupIndexed_ in self.UnorderedGroupIndexed:
            namespaceprefix_ = self.UnorderedGroupIndexed_nsprefix_ + ':' if (UseCapturedNS_ and self.UnorderedGroupIndexed_nsprefix_) else ''
            UnorderedGroupIndexed_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnorderedGroupIndexed', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('regionRef', node)
        if value is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            self.regionRef = value
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
        value = find_attr_value_('caption', node)
        if value is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            self.caption = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_GroupTypeSimpleType(self.type_)    # validate type GroupTypeSimpleType
        value = find_attr_value_('continuation', node)
        if value is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            if value in ('true', '1'):
                self.continuation = True
            elif value in ('false', '0'):
                self.continuation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'RegionRefIndexed':
            obj_ = RegionRefIndexedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RegionRefIndexed.append(obj_)
            obj_.original_tagname_ = 'RegionRefIndexed'
        elif nodeName_ == 'OrderedGroupIndexed':
            obj_ = OrderedGroupIndexedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrderedGroupIndexed.append(obj_)
            obj_.original_tagname_ = 'OrderedGroupIndexed'
        elif nodeName_ == 'UnorderedGroupIndexed':
            obj_ = UnorderedGroupIndexedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnorderedGroupIndexed.append(obj_)
            obj_.original_tagname_ = 'UnorderedGroupIndexed'
    def __hash__(self):
        return hash(self.id)
    # pylint: disable=invalid-name,missing-module-docstring,line-too-long
    def get_AllIndexed(self, classes=None, index_sort=True):
        """
        Get all indexed children sorted by their ``@index``.
    
        Arguments:
            classes (list): Type of children to return. Default: ['RegionRef', 'OrderedGroup', 'UnorderedGroup']
            index_sort (boolean): Whether to sort by ``@index``
        """
        if not classes:
            classes = ['RegionRef', 'OrderedGroup', 'UnorderedGroup']
        ret = []
        for class_ in classes:
            ret += getattr(self, 'get_{}Indexed'.format(class_))()
        if index_sort:
            return sorted(ret, key=lambda x: x.index)
        return ret
    def clear_AllIndexed(self):
        ret = self.get_AllIndexed()
        self.set_RegionRefIndexed([])
        self.set_OrderedGroupIndexed([])
        self.set_UnorderedGroupIndexed([])
        return ret
    
    # pylint: disable=line-too-long,invalid-name,missing-module-docstring
    def extend_AllIndexed(self, elements, validate_continuity=False):
        """
        Add all elements in list ``elements``, respecting ``@index`` order.
        With ``validate_continuity``, check that all new elements come after all old elements
        (or raise an exception). 
        Otherwise, ensure this condition silently (by increasing ``@index`` accordingly).
        """
        if not isinstance(elements, list):
            elements = [elements]
        siblings = self.get_AllIndexed()
        highest_sibling_index = siblings[-1].index if siblings else -1
        if validate_continuity:
            elements = sorted(elements, key=lambda x: x.index)
            lowest_element_index = elements[0].index
            if lowest_element_index <= highest_sibling_index:
                raise Exception("@index already used: {}".format(lowest_element_index))
        else:
            for element in elements:
                highest_sibling_index += 1
                element.index = highest_sibling_index
        for element in elements:
            if isinstance(element, RegionRefIndexedType): # pylint: disable=undefined-variable
                self.add_RegionRefIndexed(element)
            elif isinstance(element, OrderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_OrderedGroupIndexed(element)
            elif isinstance(element, UnorderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_UnorderedGroupIndexed(element)
        return self.get_AllIndexed()
    # pylint: disable=line-too-long,invalid-name,missing-module-docstring
    def sort_AllIndexed(self, validate_uniqueness=True):
        """
        Sort all indexed children in-place.
        """
        elements = self.get_AllIndexed(index_sort=True)
        self.clear_AllIndexed()
        for element in elements:
            if isinstance(element, RegionRefIndexedType): # pylint: disable=undefined-variable
                self.add_RegionRefIndexed(element)
            elif isinstance(element, OrderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_OrderedGroupIndexed(element)
            elif isinstance(element, UnorderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_UnorderedGroupIndexed(element)
        return self.get_AllIndexed()
    
    # pylint: disable=line-too-long,invalid-name,missing-module-docstring,missing-function-docstring
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='OrderedGroupType', fromsubclass_=False, pretty_print=True): # pylint: disable=unused-argument,too-many-arguments
        namespaceprefix_ = 'pc:'
        if self.UserDefined is not None:
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        cleaned = []
        def replaceWithRRI(group):
            rri = RegionRefIndexedType.factory(parent_object_=self) # pylint: disable=undefined-variable
            rri.index = group.index
            rri.regionRef = group.regionRef
            cleaned.append(rri)
        # remove emtpy groups and replace with RegionRefIndexedType
        for entry in self.get_AllIndexed():
            # pylint: disable=undefined-variable
            if isinstance(entry, (OrderedGroupIndexedType)) and not entry.get_AllIndexed():
                replaceWithRRI(entry)
            elif isinstance(entry, UnorderedGroupIndexedType) and not entry.get_UnorderedGroupChildren():
                replaceWithRRI(entry)
            else:
                cleaned.append(entry)
        for entry in cleaned:
            entry.export(outfile, level, namespaceprefix_, namespacedef_='', name_=entry.__class__.__name__[:-4], pretty_print=pretty_print)
# end class OrderedGroupIndexedType


class UnorderedGroupIndexedType(GeneratedsSuper):
    """Indexed group containing unordered elements
    Optional link to a parent region of nested regions.
    The parent region doubles as reading order group.
    Only the nested regions should be allowed as group members.
    Position (order number) of this item within the
    current hierarchy level.
    Is this group a continuation of another group
    (from previous column or page, for example)?
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('regionRef', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('index', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('caption', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:GroupTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('continuation', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('RegionRef', 'RegionRefType', 1, 0, {'name': 'RegionRef', 'type': 'RegionRefType'}, 4),
        MemberSpec_('OrderedGroup', 'OrderedGroupType', 1, 0, {'name': 'OrderedGroup', 'type': 'OrderedGroupType'}, 4),
        MemberSpec_('UnorderedGroup', 'UnorderedGroupType', 1, 0, {'name': 'UnorderedGroup', 'type': 'UnorderedGroupType'}, 4),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, regionRef=None, index=None, caption=None, type_=None, continuation=None, custom=None, comments=None, UserDefined=None, Labels=None, RegionRef=None, OrderedGroup=None, UnorderedGroup=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.regionRef = _cast(None, regionRef)
        self.regionRef_nsprefix_ = "pc"
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        self.caption = _cast(None, caption)
        self.caption_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.continuation = _cast(bool, continuation)
        self.continuation_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        if RegionRef is None:
            self.RegionRef = []
        else:
            self.RegionRef = RegionRef
        self.RegionRef_nsprefix_ = "pc"
        if OrderedGroup is None:
            self.OrderedGroup = []
        else:
            self.OrderedGroup = OrderedGroup
        self.OrderedGroup_nsprefix_ = "pc"
        if UnorderedGroup is None:
            self.UnorderedGroup = []
        else:
            self.UnorderedGroup = UnorderedGroup
        self.UnorderedGroup_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UnorderedGroupIndexedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UnorderedGroupIndexedType.subclass:
            return UnorderedGroupIndexedType.subclass(*args_, **kwargs_)
        else:
            return UnorderedGroupIndexedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_RegionRef(self):
        return self.RegionRef
    def set_RegionRef(self, RegionRef):
        self.RegionRef = RegionRef
    def add_RegionRef(self, value):
        self.RegionRef.append(value)
    def insert_RegionRef_at(self, index, value):
        self.RegionRef.insert(index, value)
    def replace_RegionRef_at(self, index, value):
        self.RegionRef[index] = value
    def get_OrderedGroup(self):
        return self.OrderedGroup
    def set_OrderedGroup(self, OrderedGroup):
        self.OrderedGroup = OrderedGroup
    def add_OrderedGroup(self, value):
        self.OrderedGroup.append(value)
    def insert_OrderedGroup_at(self, index, value):
        self.OrderedGroup.insert(index, value)
    def replace_OrderedGroup_at(self, index, value):
        self.OrderedGroup[index] = value
    def get_UnorderedGroup(self):
        return self.UnorderedGroup
    def set_UnorderedGroup(self, UnorderedGroup):
        self.UnorderedGroup = UnorderedGroup
    def add_UnorderedGroup(self, value):
        self.UnorderedGroup.append(value)
    def insert_UnorderedGroup_at(self, index, value):
        self.UnorderedGroup.insert(index, value)
    def replace_UnorderedGroup_at(self, index, value):
        self.UnorderedGroup[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_regionRef(self):
        return self.regionRef
    def set_regionRef(self, regionRef):
        self.regionRef = regionRef
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_caption(self):
        return self.caption
    def set_caption(self, caption):
        self.caption = caption
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_continuation(self):
        return self.continuation
    def set_continuation(self, continuation):
        self.continuation = continuation
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_GroupTypeSimpleType(self, value):
        # Validate type pc:GroupTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['paragraph', 'list', 'list-item', 'figure', 'article', 'div', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on GroupTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.UserDefined is not None or
            self.Labels or
            self.RegionRef or
            self.OrderedGroup or
            self.UnorderedGroup
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UnorderedGroupIndexedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UnorderedGroupIndexedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UnorderedGroupIndexedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnorderedGroupIndexedType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UnorderedGroupIndexedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UnorderedGroupIndexedType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.regionRef is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            outfile.write(' regionRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regionRef), input_name='regionRef')), ))
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.caption is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            outfile.write(' caption=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.caption), input_name='caption')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.continuation is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            outfile.write(' continuation="%s"' % self.gds_format_boolean(self.continuation, input_name='continuation'))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UnorderedGroupIndexedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        for RegionRef_ in self.RegionRef:
            namespaceprefix_ = self.RegionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.RegionRef_nsprefix_) else ''
            RegionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RegionRef', pretty_print=pretty_print)
        for OrderedGroup_ in self.OrderedGroup:
            namespaceprefix_ = self.OrderedGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.OrderedGroup_nsprefix_) else ''
            OrderedGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrderedGroup', pretty_print=pretty_print)
        for UnorderedGroup_ in self.UnorderedGroup:
            namespaceprefix_ = self.UnorderedGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.UnorderedGroup_nsprefix_) else ''
            UnorderedGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnorderedGroup', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('regionRef', node)
        if value is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            self.regionRef = value
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
        value = find_attr_value_('caption', node)
        if value is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            self.caption = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_GroupTypeSimpleType(self.type_)    # validate type GroupTypeSimpleType
        value = find_attr_value_('continuation', node)
        if value is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            if value in ('true', '1'):
                self.continuation = True
            elif value in ('false', '0'):
                self.continuation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'RegionRef':
            obj_ = RegionRefType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RegionRef.append(obj_)
            obj_.original_tagname_ = 'RegionRef'
        elif nodeName_ == 'OrderedGroup':
            obj_ = OrderedGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrderedGroup.append(obj_)
            obj_.original_tagname_ = 'OrderedGroup'
        elif nodeName_ == 'UnorderedGroup':
            obj_ = UnorderedGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnorderedGroup.append(obj_)
            obj_.original_tagname_ = 'UnorderedGroup'
    def __hash__(self):
        return hash(self.id)
    def get_UnorderedGroupChildren(self):
        """
        List all non-metadata children of an UnorderedGroup
        """
        # TODO: should not change order
        return self.get_RegionRef() + self.get_OrderedGroup() + self.get_UnorderedGroup()
    
# end class UnorderedGroupIndexedType


class RegionRefType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('regionRef', 'string', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, regionRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.regionRef = _cast(None, regionRef)
        self.regionRef_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RegionRefType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RegionRefType.subclass:
            return RegionRefType.subclass(*args_, **kwargs_)
        else:
            return RegionRefType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_regionRef(self):
        return self.regionRef
    def set_regionRef(self, regionRef):
        self.regionRef = regionRef
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RegionRefType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RegionRefType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RegionRefType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RegionRefType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RegionRefType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RegionRefType'):
        if self.regionRef is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            outfile.write(' regionRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regionRef), input_name='regionRef')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RegionRefType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('regionRef', node)
        if value is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            self.regionRef = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class RegionRefType


class OrderedGroupType(GeneratedsSuper):
    """Numbered group (contains ordered elements)
    Optional link to a parent region of nested regions.
    The parent region doubles as reading order group.
    Only the nested regions should be allowed as group members.
    Is this group a continuation of another group
    (from previous column or page, for example)?
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('regionRef', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('caption', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:GroupTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('continuation', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('RegionRefIndexed', 'RegionRefIndexedType', 1, 0, {'name': 'RegionRefIndexed', 'type': 'RegionRefIndexedType'}, 5),
        MemberSpec_('OrderedGroupIndexed', 'OrderedGroupIndexedType', 1, 0, {'name': 'OrderedGroupIndexed', 'type': 'OrderedGroupIndexedType'}, 5),
        MemberSpec_('UnorderedGroupIndexed', 'UnorderedGroupIndexedType', 1, 0, {'name': 'UnorderedGroupIndexed', 'type': 'UnorderedGroupIndexedType'}, 5),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, regionRef=None, caption=None, type_=None, continuation=None, custom=None, comments=None, UserDefined=None, Labels=None, RegionRefIndexed=None, OrderedGroupIndexed=None, UnorderedGroupIndexed=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.regionRef = _cast(None, regionRef)
        self.regionRef_nsprefix_ = "pc"
        self.caption = _cast(None, caption)
        self.caption_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.continuation = _cast(bool, continuation)
        self.continuation_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        if RegionRefIndexed is None:
            self.RegionRefIndexed = []
        else:
            self.RegionRefIndexed = RegionRefIndexed
        self.RegionRefIndexed_nsprefix_ = "pc"
        if OrderedGroupIndexed is None:
            self.OrderedGroupIndexed = []
        else:
            self.OrderedGroupIndexed = OrderedGroupIndexed
        self.OrderedGroupIndexed_nsprefix_ = "pc"
        if UnorderedGroupIndexed is None:
            self.UnorderedGroupIndexed = []
        else:
            self.UnorderedGroupIndexed = UnorderedGroupIndexed
        self.UnorderedGroupIndexed_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OrderedGroupType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OrderedGroupType.subclass:
            return OrderedGroupType.subclass(*args_, **kwargs_)
        else:
            return OrderedGroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_RegionRefIndexed(self):
        return self.RegionRefIndexed
    def set_RegionRefIndexed(self, RegionRefIndexed):
        self.RegionRefIndexed = RegionRefIndexed
    def add_RegionRefIndexed(self, value):
        self.RegionRefIndexed.append(value)
    def insert_RegionRefIndexed_at(self, index, value):
        self.RegionRefIndexed.insert(index, value)
    def replace_RegionRefIndexed_at(self, index, value):
        self.RegionRefIndexed[index] = value
    def get_OrderedGroupIndexed(self):
        return self.OrderedGroupIndexed
    def set_OrderedGroupIndexed(self, OrderedGroupIndexed):
        self.OrderedGroupIndexed = OrderedGroupIndexed
    def add_OrderedGroupIndexed(self, value):
        self.OrderedGroupIndexed.append(value)
    def insert_OrderedGroupIndexed_at(self, index, value):
        self.OrderedGroupIndexed.insert(index, value)
    def replace_OrderedGroupIndexed_at(self, index, value):
        self.OrderedGroupIndexed[index] = value
    def get_UnorderedGroupIndexed(self):
        return self.UnorderedGroupIndexed
    def set_UnorderedGroupIndexed(self, UnorderedGroupIndexed):
        self.UnorderedGroupIndexed = UnorderedGroupIndexed
    def add_UnorderedGroupIndexed(self, value):
        self.UnorderedGroupIndexed.append(value)
    def insert_UnorderedGroupIndexed_at(self, index, value):
        self.UnorderedGroupIndexed.insert(index, value)
    def replace_UnorderedGroupIndexed_at(self, index, value):
        self.UnorderedGroupIndexed[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_regionRef(self):
        return self.regionRef
    def set_regionRef(self, regionRef):
        self.regionRef = regionRef
    def get_caption(self):
        return self.caption
    def set_caption(self, caption):
        self.caption = caption
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_continuation(self):
        return self.continuation
    def set_continuation(self, continuation):
        self.continuation = continuation
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_GroupTypeSimpleType(self, value):
        # Validate type pc:GroupTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['paragraph', 'list', 'list-item', 'figure', 'article', 'div', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on GroupTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.UserDefined is not None or
            self.Labels or
            self.RegionRefIndexed or
            self.OrderedGroupIndexed or
            self.UnorderedGroupIndexed
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='OrderedGroupType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OrderedGroupType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'OrderedGroupType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OrderedGroupType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OrderedGroupType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='OrderedGroupType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.regionRef is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            outfile.write(' regionRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regionRef), input_name='regionRef')), ))
        if self.caption is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            outfile.write(' caption=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.caption), input_name='caption')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.continuation is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            outfile.write(' continuation="%s"' % self.gds_format_boolean(self.continuation, input_name='continuation'))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='OrderedGroupType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        for RegionRefIndexed_ in self.RegionRefIndexed:
            namespaceprefix_ = self.RegionRefIndexed_nsprefix_ + ':' if (UseCapturedNS_ and self.RegionRefIndexed_nsprefix_) else ''
            RegionRefIndexed_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RegionRefIndexed', pretty_print=pretty_print)
        for OrderedGroupIndexed_ in self.OrderedGroupIndexed:
            namespaceprefix_ = self.OrderedGroupIndexed_nsprefix_ + ':' if (UseCapturedNS_ and self.OrderedGroupIndexed_nsprefix_) else ''
            OrderedGroupIndexed_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrderedGroupIndexed', pretty_print=pretty_print)
        for UnorderedGroupIndexed_ in self.UnorderedGroupIndexed:
            namespaceprefix_ = self.UnorderedGroupIndexed_nsprefix_ + ':' if (UseCapturedNS_ and self.UnorderedGroupIndexed_nsprefix_) else ''
            UnorderedGroupIndexed_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnorderedGroupIndexed', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('regionRef', node)
        if value is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            self.regionRef = value
        value = find_attr_value_('caption', node)
        if value is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            self.caption = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_GroupTypeSimpleType(self.type_)    # validate type GroupTypeSimpleType
        value = find_attr_value_('continuation', node)
        if value is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            if value in ('true', '1'):
                self.continuation = True
            elif value in ('false', '0'):
                self.continuation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'RegionRefIndexed':
            obj_ = RegionRefIndexedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RegionRefIndexed.append(obj_)
            obj_.original_tagname_ = 'RegionRefIndexed'
        elif nodeName_ == 'OrderedGroupIndexed':
            obj_ = OrderedGroupIndexedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrderedGroupIndexed.append(obj_)
            obj_.original_tagname_ = 'OrderedGroupIndexed'
        elif nodeName_ == 'UnorderedGroupIndexed':
            obj_ = UnorderedGroupIndexedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnorderedGroupIndexed.append(obj_)
            obj_.original_tagname_ = 'UnorderedGroupIndexed'
    def __hash__(self):
        return hash(self.id)
    # pylint: disable=invalid-name,missing-module-docstring,line-too-long
    def get_AllIndexed(self, classes=None, index_sort=True):
        """
        Get all indexed children sorted by their ``@index``.
    
        Arguments:
            classes (list): Type of children to return. Default: ['RegionRef', 'OrderedGroup', 'UnorderedGroup']
            index_sort (boolean): Whether to sort by ``@index``
        """
        if not classes:
            classes = ['RegionRef', 'OrderedGroup', 'UnorderedGroup']
        ret = []
        for class_ in classes:
            ret += getattr(self, 'get_{}Indexed'.format(class_))()
        if index_sort:
            return sorted(ret, key=lambda x: x.index)
        return ret
    def clear_AllIndexed(self):
        ret = self.get_AllIndexed()
        self.set_RegionRefIndexed([])
        self.set_OrderedGroupIndexed([])
        self.set_UnorderedGroupIndexed([])
        return ret
    
    # pylint: disable=line-too-long,invalid-name,missing-module-docstring
    def extend_AllIndexed(self, elements, validate_continuity=False):
        """
        Add all elements in list ``elements``, respecting ``@index`` order.
        With ``validate_continuity``, check that all new elements come after all old elements
        (or raise an exception). 
        Otherwise, ensure this condition silently (by increasing ``@index`` accordingly).
        """
        if not isinstance(elements, list):
            elements = [elements]
        siblings = self.get_AllIndexed()
        highest_sibling_index = siblings[-1].index if siblings else -1
        if validate_continuity:
            elements = sorted(elements, key=lambda x: x.index)
            lowest_element_index = elements[0].index
            if lowest_element_index <= highest_sibling_index:
                raise Exception("@index already used: {}".format(lowest_element_index))
        else:
            for element in elements:
                highest_sibling_index += 1
                element.index = highest_sibling_index
        for element in elements:
            if isinstance(element, RegionRefIndexedType): # pylint: disable=undefined-variable
                self.add_RegionRefIndexed(element)
            elif isinstance(element, OrderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_OrderedGroupIndexed(element)
            elif isinstance(element, UnorderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_UnorderedGroupIndexed(element)
        return self.get_AllIndexed()
    # pylint: disable=line-too-long,invalid-name,missing-module-docstring
    def sort_AllIndexed(self, validate_uniqueness=True):
        """
        Sort all indexed children in-place.
        """
        elements = self.get_AllIndexed(index_sort=True)
        self.clear_AllIndexed()
        for element in elements:
            if isinstance(element, RegionRefIndexedType): # pylint: disable=undefined-variable
                self.add_RegionRefIndexed(element)
            elif isinstance(element, OrderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_OrderedGroupIndexed(element)
            elif isinstance(element, UnorderedGroupIndexedType): # pylint: disable=undefined-variable
                self.add_UnorderedGroupIndexed(element)
        return self.get_AllIndexed()
    
    # pylint: disable=line-too-long,invalid-name,missing-module-docstring,missing-function-docstring
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='OrderedGroupType', fromsubclass_=False, pretty_print=True): # pylint: disable=unused-argument,too-many-arguments
        namespaceprefix_ = 'pc:'
        if self.UserDefined is not None:
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        cleaned = []
        def replaceWithRRI(group):
            rri = RegionRefIndexedType.factory(parent_object_=self) # pylint: disable=undefined-variable
            rri.index = group.index
            rri.regionRef = group.regionRef
            cleaned.append(rri)
        # remove emtpy groups and replace with RegionRefIndexedType
        for entry in self.get_AllIndexed():
            # pylint: disable=undefined-variable
            if isinstance(entry, (OrderedGroupIndexedType)) and not entry.get_AllIndexed():
                replaceWithRRI(entry)
            elif isinstance(entry, UnorderedGroupIndexedType) and not entry.get_UnorderedGroupChildren():
                replaceWithRRI(entry)
            else:
                cleaned.append(entry)
        for entry in cleaned:
            entry.export(outfile, level, namespaceprefix_, namespacedef_='', name_=entry.__class__.__name__[:-4], pretty_print=pretty_print)
# end class OrderedGroupType


class UnorderedGroupType(GeneratedsSuper):
    """Numbered group (contains unordered elements)
    Optional link to a parent region of nested regions.
    The parent region doubles as reading order group.
    Only the nested regions should be allowed as group members.
    Is this group a continuation of another group
    (from previous column or page, for example)?
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('regionRef', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('caption', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:GroupTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('continuation', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('RegionRef', 'RegionRefType', 1, 0, {'name': 'RegionRef', 'type': 'RegionRefType'}, 6),
        MemberSpec_('OrderedGroup', 'OrderedGroupType', 1, 0, {'name': 'OrderedGroup', 'type': 'OrderedGroupType'}, 6),
        MemberSpec_('UnorderedGroup', 'UnorderedGroupType', 1, 0, {'name': 'UnorderedGroup', 'type': 'UnorderedGroupType'}, 6),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, regionRef=None, caption=None, type_=None, continuation=None, custom=None, comments=None, UserDefined=None, Labels=None, RegionRef=None, OrderedGroup=None, UnorderedGroup=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.regionRef = _cast(None, regionRef)
        self.regionRef_nsprefix_ = "pc"
        self.caption = _cast(None, caption)
        self.caption_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.continuation = _cast(bool, continuation)
        self.continuation_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        if RegionRef is None:
            self.RegionRef = []
        else:
            self.RegionRef = RegionRef
        self.RegionRef_nsprefix_ = "pc"
        if OrderedGroup is None:
            self.OrderedGroup = []
        else:
            self.OrderedGroup = OrderedGroup
        self.OrderedGroup_nsprefix_ = "pc"
        if UnorderedGroup is None:
            self.UnorderedGroup = []
        else:
            self.UnorderedGroup = UnorderedGroup
        self.UnorderedGroup_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UnorderedGroupType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UnorderedGroupType.subclass:
            return UnorderedGroupType.subclass(*args_, **kwargs_)
        else:
            return UnorderedGroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_RegionRef(self):
        return self.RegionRef
    def set_RegionRef(self, RegionRef):
        self.RegionRef = RegionRef
    def add_RegionRef(self, value):
        self.RegionRef.append(value)
    def insert_RegionRef_at(self, index, value):
        self.RegionRef.insert(index, value)
    def replace_RegionRef_at(self, index, value):
        self.RegionRef[index] = value
    def get_OrderedGroup(self):
        return self.OrderedGroup
    def set_OrderedGroup(self, OrderedGroup):
        self.OrderedGroup = OrderedGroup
    def add_OrderedGroup(self, value):
        self.OrderedGroup.append(value)
    def insert_OrderedGroup_at(self, index, value):
        self.OrderedGroup.insert(index, value)
    def replace_OrderedGroup_at(self, index, value):
        self.OrderedGroup[index] = value
    def get_UnorderedGroup(self):
        return self.UnorderedGroup
    def set_UnorderedGroup(self, UnorderedGroup):
        self.UnorderedGroup = UnorderedGroup
    def add_UnorderedGroup(self, value):
        self.UnorderedGroup.append(value)
    def insert_UnorderedGroup_at(self, index, value):
        self.UnorderedGroup.insert(index, value)
    def replace_UnorderedGroup_at(self, index, value):
        self.UnorderedGroup[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_regionRef(self):
        return self.regionRef
    def set_regionRef(self, regionRef):
        self.regionRef = regionRef
    def get_caption(self):
        return self.caption
    def set_caption(self, caption):
        self.caption = caption
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_continuation(self):
        return self.continuation
    def set_continuation(self, continuation):
        self.continuation = continuation
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def validate_GroupTypeSimpleType(self, value):
        # Validate type pc:GroupTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['paragraph', 'list', 'list-item', 'figure', 'article', 'div', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on GroupTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.UserDefined is not None or
            self.Labels or
            self.RegionRef or
            self.OrderedGroup or
            self.UnorderedGroup
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UnorderedGroupType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UnorderedGroupType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UnorderedGroupType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnorderedGroupType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UnorderedGroupType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UnorderedGroupType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.regionRef is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            outfile.write(' regionRef=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.regionRef), input_name='regionRef')), ))
        if self.caption is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            outfile.write(' caption=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.caption), input_name='caption')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.continuation is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            outfile.write(' continuation="%s"' % self.gds_format_boolean(self.continuation, input_name='continuation'))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UnorderedGroupType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        for RegionRef_ in self.RegionRef:
            namespaceprefix_ = self.RegionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.RegionRef_nsprefix_) else ''
            RegionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RegionRef', pretty_print=pretty_print)
        for OrderedGroup_ in self.OrderedGroup:
            namespaceprefix_ = self.OrderedGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.OrderedGroup_nsprefix_) else ''
            OrderedGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OrderedGroup', pretty_print=pretty_print)
        for UnorderedGroup_ in self.UnorderedGroup:
            namespaceprefix_ = self.UnorderedGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.UnorderedGroup_nsprefix_) else ''
            UnorderedGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnorderedGroup', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('regionRef', node)
        if value is not None and 'regionRef' not in already_processed:
            already_processed.add('regionRef')
            self.regionRef = value
        value = find_attr_value_('caption', node)
        if value is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            self.caption = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_GroupTypeSimpleType(self.type_)    # validate type GroupTypeSimpleType
        value = find_attr_value_('continuation', node)
        if value is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            if value in ('true', '1'):
                self.continuation = True
            elif value in ('false', '0'):
                self.continuation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'RegionRef':
            obj_ = RegionRefType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RegionRef.append(obj_)
            obj_.original_tagname_ = 'RegionRef'
        elif nodeName_ == 'OrderedGroup':
            obj_ = OrderedGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OrderedGroup.append(obj_)
            obj_.original_tagname_ = 'OrderedGroup'
        elif nodeName_ == 'UnorderedGroup':
            obj_ = UnorderedGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnorderedGroup.append(obj_)
            obj_.original_tagname_ = 'UnorderedGroup'
    def __hash__(self):
        return hash(self.id)
    def get_UnorderedGroupChildren(self):
        """
        List all non-metadata children of an UnorderedGroup
        """
        # TODO: should not change order
        return self.get_RegionRef() + self.get_OrderedGroup() + self.get_UnorderedGroup()
    
# end class UnorderedGroupType


class BorderType(GeneratedsSuper):
    """Border of the actual page (if the scanned image
    contains parts not belonging to the page)."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Coords=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BorderType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BorderType.subclass:
            return BorderType.subclass(*args_, **kwargs_)
        else:
            return BorderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def hasContent_(self):
        if (
            self.Coords is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='BorderType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BorderType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BorderType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BorderType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BorderType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BorderType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='BorderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
    def __hash__(self):
        return hash(self.id)
    def set_Coords(self, Coords):
        """
        Set coordinate polygon by given object.
        Moreover, invalidate self's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # RegionType, TextLineType, WordType, GlyphType:
            self.invalidate_AlternativeImage()
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'invalidate_AlternativeImage'):
            # BorderType:
            self.parent_object_.invalidate_AlternativeImage(feature_selector='cropped')
        self.Coords = Coords
# end class BorderType


class LayersType(GeneratedsSuper):
    """Can be used to express the z-index of overlapping
    regions. An element with a greater z-index is always in
    front of another element with lower z-index."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Layer', 'LayerType', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'Layer', 'type': 'LayerType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Layer=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Layer is None:
            self.Layer = []
        else:
            self.Layer = Layer
        self.Layer_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LayersType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LayersType.subclass:
            return LayersType.subclass(*args_, **kwargs_)
        else:
            return LayersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Layer(self):
        return self.Layer
    def set_Layer(self, Layer):
        self.Layer = Layer
    def add_Layer(self, value):
        self.Layer.append(value)
    def insert_Layer_at(self, index, value):
        self.Layer.insert(index, value)
    def replace_Layer_at(self, index, value):
        self.Layer[index] = value
    def hasContent_(self):
        if (
            self.Layer
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LayersType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LayersType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LayersType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LayersType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LayersType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LayersType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LayersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Layer_ in self.Layer:
            namespaceprefix_ = self.Layer_nsprefix_ + ':' if (UseCapturedNS_ and self.Layer_nsprefix_) else ''
            Layer_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Layer', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Layer':
            obj_ = LayerType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Layer.append(obj_)
            obj_.original_tagname_ = 'Layer'
    def __hash__(self):
        return hash(self.id)
# end class LayersType


class LayerType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('zIndex', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('caption', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('RegionRef', 'RegionRefType', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'RegionRef', 'type': 'RegionRefType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, zIndex=None, caption=None, RegionRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.zIndex = _cast(int, zIndex)
        self.zIndex_nsprefix_ = "pc"
        self.caption = _cast(None, caption)
        self.caption_nsprefix_ = "pc"
        if RegionRef is None:
            self.RegionRef = []
        else:
            self.RegionRef = RegionRef
        self.RegionRef_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LayerType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LayerType.subclass:
            return LayerType.subclass(*args_, **kwargs_)
        else:
            return LayerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_RegionRef(self):
        return self.RegionRef
    def set_RegionRef(self, RegionRef):
        self.RegionRef = RegionRef
    def add_RegionRef(self, value):
        self.RegionRef.append(value)
    def insert_RegionRef_at(self, index, value):
        self.RegionRef.insert(index, value)
    def replace_RegionRef_at(self, index, value):
        self.RegionRef[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_zIndex(self):
        return self.zIndex
    def set_zIndex(self, zIndex):
        self.zIndex = zIndex
    def get_caption(self):
        return self.caption
    def set_caption(self, caption):
        self.caption = caption
    def hasContent_(self):
        if (
            self.RegionRef
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LayerType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LayerType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LayerType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LayerType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LayerType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LayerType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.zIndex is not None and 'zIndex' not in already_processed:
            already_processed.add('zIndex')
            outfile.write(' zIndex="%s"' % self.gds_format_integer(self.zIndex, input_name='zIndex'))
        if self.caption is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            outfile.write(' caption=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.caption), input_name='caption')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='LayerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for RegionRef_ in self.RegionRef:
            namespaceprefix_ = self.RegionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.RegionRef_nsprefix_) else ''
            RegionRef_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='RegionRef', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('zIndex', node)
        if value is not None and 'zIndex' not in already_processed:
            already_processed.add('zIndex')
            self.zIndex = self.gds_parse_integer(value, node, 'zIndex')
        value = find_attr_value_('caption', node)
        if value is not None and 'caption' not in already_processed:
            already_processed.add('caption')
            self.caption = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'RegionRef':
            obj_ = RegionRefType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.RegionRef.append(obj_)
            obj_.original_tagname_ = 'RegionRef'
    def __hash__(self):
        return hash(self.id)
# end class LayerType


class BaselineType(GeneratedsSuper):
    """Confidence value (between 0 and 1)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('points', 'pc:PointsType', 0, 0, {'use': 'required'}),
        MemberSpec_('conf', 'pc:ConfSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, points=None, conf=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.points = _cast(None, points)
        self.points_nsprefix_ = "pc"
        self.conf = _cast(float, conf)
        self.conf_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, BaselineType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BaselineType.subclass:
            return BaselineType.subclass(*args_, **kwargs_)
        else:
            return BaselineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_points(self):
        return self.points
    def set_points(self, points):
        self.points = points
    def get_conf(self):
        return self.conf
    def set_conf(self, conf):
        self.conf = conf
    def validate_PointsType(self, value):
        # Validate type pc:PointsType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_PointsType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_PointsType_patterns_, ))
    validate_PointsType_patterns_ = [['^(([0-9]+,[0-9]+ )+([0-9]+,[0-9]+))$']]
    def validate_ConfSimpleType(self, value):
        # Validate type pc:ConfSimpleType, a restriction on float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='BaselineType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('BaselineType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'BaselineType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='BaselineType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='BaselineType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='BaselineType'):
        if self.points is not None and 'points' not in already_processed:
            already_processed.add('points')
            outfile.write(' points=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.points), input_name='points')), ))
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_float(self.conf, input_name='conf'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='BaselineType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('points', node)
        if value is not None and 'points' not in already_processed:
            already_processed.add('points')
            self.points = value
            self.validate_PointsType(self.points)    # validate type PointsType
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            value = self.gds_parse_float(value, node, 'conf')
            self.conf = value
            self.validate_ConfSimpleType(self.conf)    # validate type ConfSimpleType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class BaselineType


class RelationsType(GeneratedsSuper):
    """Container for one-to-one relations between layout
    objects (for example: DropCap - paragraph, caption -
    image)."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Relation', 'RelationType', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'Relation', 'type': 'RelationType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Relation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Relation is None:
            self.Relation = []
        else:
            self.Relation = Relation
        self.Relation_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelationsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelationsType.subclass:
            return RelationsType.subclass(*args_, **kwargs_)
        else:
            return RelationsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Relation(self):
        return self.Relation
    def set_Relation(self, Relation):
        self.Relation = Relation
    def add_Relation(self, value):
        self.Relation.append(value)
    def insert_Relation_at(self, index, value):
        self.Relation.insert(index, value)
    def replace_Relation_at(self, index, value):
        self.Relation[index] = value
    def hasContent_(self):
        if (
            self.Relation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RelationsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelationsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelationsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelationsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelationsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelationsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RelationsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Relation_ in self.Relation:
            namespaceprefix_ = self.Relation_nsprefix_ + ':' if (UseCapturedNS_ and self.Relation_nsprefix_) else ''
            Relation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Relation', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Relation':
            obj_ = RelationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Relation.append(obj_)
            obj_.original_tagname_ = 'Relation'
    def __hash__(self):
        return hash(self.id)
# end class RelationsType


class RelationType(GeneratedsSuper):
    """One-to-one relation between to layout object. Use 'link'
    for loose relations and 'join' for strong relations
    (where something is fragmented for instance).
    Examples for 'link': caption - image floating -
    paragraph paragraph - paragraph (when a paragraph is
    split across columns and the last word of the first
    paragraph DOES NOT continue in the second paragraph)
    drop-cap - paragraph (when the drop-cap is a whole word)
    Examples for 'join': word - word (separated word at the
    end of a line) drop-cap - paragraph (when the drop-cap
    is not a whole word) paragraph - paragraph (when a
    pragraph is split across columns and the last word of
    the first paragraph DOES continue in the second
    paragraph)
    For generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('type_', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('SourceRegionRef', 'RegionRefType', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'SourceRegionRef', 'type': 'RegionRefType'}, None),
        MemberSpec_('TargetRegionRef', 'RegionRefType', 0, 0, {'maxOccurs': '1', 'minOccurs': '1', 'name': 'TargetRegionRef', 'type': 'RegionRefType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, type_=None, custom=None, comments=None, Labels=None, SourceRegionRef=None, TargetRegionRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        self.SourceRegionRef = SourceRegionRef
        self.SourceRegionRef_nsprefix_ = "pc"
        self.TargetRegionRef = TargetRegionRef
        self.TargetRegionRef_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RelationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RelationType.subclass:
            return RelationType.subclass(*args_, **kwargs_)
        else:
            return RelationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_SourceRegionRef(self):
        return self.SourceRegionRef
    def set_SourceRegionRef(self, SourceRegionRef):
        self.SourceRegionRef = SourceRegionRef
    def get_TargetRegionRef(self):
        return self.TargetRegionRef
    def set_TargetRegionRef(self, TargetRegionRef):
        self.TargetRegionRef = TargetRegionRef
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def hasContent_(self):
        if (
            self.Labels or
            self.SourceRegionRef is not None or
            self.TargetRegionRef is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RelationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RelationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RelationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RelationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RelationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RelationType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RelationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        if self.SourceRegionRef is not None:
            namespaceprefix_ = self.SourceRegionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.SourceRegionRef_nsprefix_) else ''
            self.SourceRegionRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SourceRegionRef', pretty_print=pretty_print)
        if self.TargetRegionRef is not None:
            namespaceprefix_ = self.TargetRegionRef_nsprefix_ + ':' if (UseCapturedNS_ and self.TargetRegionRef_nsprefix_) else ''
            self.TargetRegionRef.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TargetRegionRef', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'SourceRegionRef':
            obj_ = RegionRefType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SourceRegionRef = obj_
            obj_.original_tagname_ = 'SourceRegionRef'
        elif nodeName_ == 'TargetRegionRef':
            obj_ = RegionRefType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TargetRegionRef = obj_
            obj_.original_tagname_ = 'TargetRegionRef'
    def __hash__(self):
        return hash(self.id)
# end class RelationType


class TextStyleType(GeneratedsSuper):
    """Monospace (fixed-pitch, non-proportional) or
    proportional font.
    For instance: Arial, Times New Roman.
    Add more information if necessary
    (e.g. blackletter, antiqua).
    Serif or sans-serif typeface.
    The size of the characters in points.
    The x-height or corpus size refers to the distance
    between the baseline and the mean line of
    lower-case letters in a typeface.
    The unit is assumed to be pixels.
    The degree of space (in points) between
    the characters in a string of text.
    Text colour in RGB encoded format
    (red value) + (256 x green value) + (65536 x blue value).
    Background colour
    Background colour in RGB encoded format
    (red value) + (256 x green value) + (65536 x blue value).
    Specifies whether the colour of the text appears
    reversed against a background colour.
    Line style details if "underlined" is TRUE"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('fontFamily', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('serif', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('monospace', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('fontSize', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('xHeight', 'integer', 0, 1, {'use': 'optional'}),
        MemberSpec_('kerning', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('textColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('textColourRgb', 'integer', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColourRgb', 'integer', 0, 1, {'use': 'optional'}),
        MemberSpec_('reverseVideo', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('bold', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('italic', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('underlined', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('underlineStyle', 'pc:UnderlineStyleSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('subscript', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('superscript', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('strikethrough', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('smallCaps', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('letterSpaced', 'boolean', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, fontFamily=None, serif=None, monospace=None, fontSize=None, xHeight=None, kerning=None, textColour=None, textColourRgb=None, bgColour=None, bgColourRgb=None, reverseVideo=None, bold=None, italic=None, underlined=None, underlineStyle=None, subscript=None, superscript=None, strikethrough=None, smallCaps=None, letterSpaced=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fontFamily = _cast(None, fontFamily)
        self.fontFamily_nsprefix_ = "pc"
        self.serif = _cast(bool, serif)
        self.serif_nsprefix_ = "pc"
        self.monospace = _cast(bool, monospace)
        self.monospace_nsprefix_ = "pc"
        self.fontSize = _cast(float, fontSize)
        self.fontSize_nsprefix_ = "pc"
        self.xHeight = _cast(int, xHeight)
        self.xHeight_nsprefix_ = "pc"
        self.kerning = _cast(int, kerning)
        self.kerning_nsprefix_ = "pc"
        self.textColour = _cast(None, textColour)
        self.textColour_nsprefix_ = "pc"
        self.textColourRgb = _cast(int, textColourRgb)
        self.textColourRgb_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
        self.bgColourRgb = _cast(int, bgColourRgb)
        self.bgColourRgb_nsprefix_ = "pc"
        self.reverseVideo = _cast(bool, reverseVideo)
        self.reverseVideo_nsprefix_ = "pc"
        self.bold = _cast(bool, bold)
        self.bold_nsprefix_ = "pc"
        self.italic = _cast(bool, italic)
        self.italic_nsprefix_ = "pc"
        self.underlined = _cast(bool, underlined)
        self.underlined_nsprefix_ = "pc"
        self.underlineStyle = _cast(None, underlineStyle)
        self.underlineStyle_nsprefix_ = "pc"
        self.subscript = _cast(bool, subscript)
        self.subscript_nsprefix_ = "pc"
        self.superscript = _cast(bool, superscript)
        self.superscript_nsprefix_ = "pc"
        self.strikethrough = _cast(bool, strikethrough)
        self.strikethrough_nsprefix_ = "pc"
        self.smallCaps = _cast(bool, smallCaps)
        self.smallCaps_nsprefix_ = "pc"
        self.letterSpaced = _cast(bool, letterSpaced)
        self.letterSpaced_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TextStyleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TextStyleType.subclass:
            return TextStyleType.subclass(*args_, **kwargs_)
        else:
            return TextStyleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_fontFamily(self):
        return self.fontFamily
    def set_fontFamily(self, fontFamily):
        self.fontFamily = fontFamily
    def get_serif(self):
        return self.serif
    def set_serif(self, serif):
        self.serif = serif
    def get_monospace(self):
        return self.monospace
    def set_monospace(self, monospace):
        self.monospace = monospace
    def get_fontSize(self):
        return self.fontSize
    def set_fontSize(self, fontSize):
        self.fontSize = fontSize
    def get_xHeight(self):
        return self.xHeight
    def set_xHeight(self, xHeight):
        self.xHeight = xHeight
    def get_kerning(self):
        return self.kerning
    def set_kerning(self, kerning):
        self.kerning = kerning
    def get_textColour(self):
        return self.textColour
    def set_textColour(self, textColour):
        self.textColour = textColour
    def get_textColourRgb(self):
        return self.textColourRgb
    def set_textColourRgb(self, textColourRgb):
        self.textColourRgb = textColourRgb
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def get_bgColourRgb(self):
        return self.bgColourRgb
    def set_bgColourRgb(self, bgColourRgb):
        self.bgColourRgb = bgColourRgb
    def get_reverseVideo(self):
        return self.reverseVideo
    def set_reverseVideo(self, reverseVideo):
        self.reverseVideo = reverseVideo
    def get_bold(self):
        return self.bold
    def set_bold(self, bold):
        self.bold = bold
    def get_italic(self):
        return self.italic
    def set_italic(self, italic):
        self.italic = italic
    def get_underlined(self):
        return self.underlined
    def set_underlined(self, underlined):
        self.underlined = underlined
    def get_underlineStyle(self):
        return self.underlineStyle
    def set_underlineStyle(self, underlineStyle):
        self.underlineStyle = underlineStyle
    def get_subscript(self):
        return self.subscript
    def set_subscript(self, subscript):
        self.subscript = subscript
    def get_superscript(self):
        return self.superscript
    def set_superscript(self, superscript):
        self.superscript = superscript
    def get_strikethrough(self):
        return self.strikethrough
    def set_strikethrough(self, strikethrough):
        self.strikethrough = strikethrough
    def get_smallCaps(self):
        return self.smallCaps
    def set_smallCaps(self, smallCaps):
        self.smallCaps = smallCaps
    def get_letterSpaced(self):
        return self.letterSpaced
    def set_letterSpaced(self, letterSpaced):
        self.letterSpaced = letterSpaced
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_UnderlineStyleSimpleType(self, value):
        # Validate type pc:UnderlineStyleSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['singleLine', 'doubleLine', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on UnderlineStyleSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='TextStyleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TextStyleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TextStyleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextStyleType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TextStyleType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TextStyleType'):
        if self.fontFamily is not None and 'fontFamily' not in already_processed:
            already_processed.add('fontFamily')
            outfile.write(' fontFamily=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fontFamily), input_name='fontFamily')), ))
        if self.serif is not None and 'serif' not in already_processed:
            already_processed.add('serif')
            outfile.write(' serif="%s"' % self.gds_format_boolean(self.serif, input_name='serif'))
        if self.monospace is not None and 'monospace' not in already_processed:
            already_processed.add('monospace')
            outfile.write(' monospace="%s"' % self.gds_format_boolean(self.monospace, input_name='monospace'))
        if self.fontSize is not None and 'fontSize' not in already_processed:
            already_processed.add('fontSize')
            outfile.write(' fontSize="%s"' % self.gds_format_float(self.fontSize, input_name='fontSize'))
        if self.xHeight is not None and 'xHeight' not in already_processed:
            already_processed.add('xHeight')
            outfile.write(' xHeight="%s"' % self.gds_format_integer(self.xHeight, input_name='xHeight'))
        if self.kerning is not None and 'kerning' not in already_processed:
            already_processed.add('kerning')
            outfile.write(' kerning="%s"' % self.gds_format_integer(self.kerning, input_name='kerning'))
        if self.textColour is not None and 'textColour' not in already_processed:
            already_processed.add('textColour')
            outfile.write(' textColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.textColour), input_name='textColour')), ))
        if self.textColourRgb is not None and 'textColourRgb' not in already_processed:
            already_processed.add('textColourRgb')
            outfile.write(' textColourRgb="%s"' % self.gds_format_integer(self.textColourRgb, input_name='textColourRgb'))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
        if self.bgColourRgb is not None and 'bgColourRgb' not in already_processed:
            already_processed.add('bgColourRgb')
            outfile.write(' bgColourRgb="%s"' % self.gds_format_integer(self.bgColourRgb, input_name='bgColourRgb'))
        if self.reverseVideo is not None and 'reverseVideo' not in already_processed:
            already_processed.add('reverseVideo')
            outfile.write(' reverseVideo="%s"' % self.gds_format_boolean(self.reverseVideo, input_name='reverseVideo'))
        if self.bold is not None and 'bold' not in already_processed:
            already_processed.add('bold')
            outfile.write(' bold="%s"' % self.gds_format_boolean(self.bold, input_name='bold'))
        if self.italic is not None and 'italic' not in already_processed:
            already_processed.add('italic')
            outfile.write(' italic="%s"' % self.gds_format_boolean(self.italic, input_name='italic'))
        if self.underlined is not None and 'underlined' not in already_processed:
            already_processed.add('underlined')
            outfile.write(' underlined="%s"' % self.gds_format_boolean(self.underlined, input_name='underlined'))
        if self.underlineStyle is not None and 'underlineStyle' not in already_processed:
            already_processed.add('underlineStyle')
            outfile.write(' underlineStyle=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.underlineStyle), input_name='underlineStyle')), ))
        if self.subscript is not None and 'subscript' not in already_processed:
            already_processed.add('subscript')
            outfile.write(' subscript="%s"' % self.gds_format_boolean(self.subscript, input_name='subscript'))
        if self.superscript is not None and 'superscript' not in already_processed:
            already_processed.add('superscript')
            outfile.write(' superscript="%s"' % self.gds_format_boolean(self.superscript, input_name='superscript'))
        if self.strikethrough is not None and 'strikethrough' not in already_processed:
            already_processed.add('strikethrough')
            outfile.write(' strikethrough="%s"' % self.gds_format_boolean(self.strikethrough, input_name='strikethrough'))
        if self.smallCaps is not None and 'smallCaps' not in already_processed:
            already_processed.add('smallCaps')
            outfile.write(' smallCaps="%s"' % self.gds_format_boolean(self.smallCaps, input_name='smallCaps'))
        if self.letterSpaced is not None and 'letterSpaced' not in already_processed:
            already_processed.add('letterSpaced')
            outfile.write(' letterSpaced="%s"' % self.gds_format_boolean(self.letterSpaced, input_name='letterSpaced'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='TextStyleType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('fontFamily', node)
        if value is not None and 'fontFamily' not in already_processed:
            already_processed.add('fontFamily')
            self.fontFamily = value
        value = find_attr_value_('serif', node)
        if value is not None and 'serif' not in already_processed:
            already_processed.add('serif')
            if value in ('true', '1'):
                self.serif = True
            elif value in ('false', '0'):
                self.serif = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('monospace', node)
        if value is not None and 'monospace' not in already_processed:
            already_processed.add('monospace')
            if value in ('true', '1'):
                self.monospace = True
            elif value in ('false', '0'):
                self.monospace = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fontSize', node)
        if value is not None and 'fontSize' not in already_processed:
            already_processed.add('fontSize')
            value = self.gds_parse_float(value, node, 'fontSize')
            self.fontSize = value
        value = find_attr_value_('xHeight', node)
        if value is not None and 'xHeight' not in already_processed:
            already_processed.add('xHeight')
            self.xHeight = self.gds_parse_integer(value, node, 'xHeight')
        value = find_attr_value_('kerning', node)
        if value is not None and 'kerning' not in already_processed:
            already_processed.add('kerning')
            self.kerning = self.gds_parse_integer(value, node, 'kerning')
        value = find_attr_value_('textColour', node)
        if value is not None and 'textColour' not in already_processed:
            already_processed.add('textColour')
            self.textColour = value
            self.validate_ColourSimpleType(self.textColour)    # validate type ColourSimpleType
        value = find_attr_value_('textColourRgb', node)
        if value is not None and 'textColourRgb' not in already_processed:
            already_processed.add('textColourRgb')
            self.textColourRgb = self.gds_parse_integer(value, node, 'textColourRgb')
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        value = find_attr_value_('bgColourRgb', node)
        if value is not None and 'bgColourRgb' not in already_processed:
            already_processed.add('bgColourRgb')
            self.bgColourRgb = self.gds_parse_integer(value, node, 'bgColourRgb')
        value = find_attr_value_('reverseVideo', node)
        if value is not None and 'reverseVideo' not in already_processed:
            already_processed.add('reverseVideo')
            if value in ('true', '1'):
                self.reverseVideo = True
            elif value in ('false', '0'):
                self.reverseVideo = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('bold', node)
        if value is not None and 'bold' not in already_processed:
            already_processed.add('bold')
            if value in ('true', '1'):
                self.bold = True
            elif value in ('false', '0'):
                self.bold = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('italic', node)
        if value is not None and 'italic' not in already_processed:
            already_processed.add('italic')
            if value in ('true', '1'):
                self.italic = True
            elif value in ('false', '0'):
                self.italic = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('underlined', node)
        if value is not None and 'underlined' not in already_processed:
            already_processed.add('underlined')
            if value in ('true', '1'):
                self.underlined = True
            elif value in ('false', '0'):
                self.underlined = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('underlineStyle', node)
        if value is not None and 'underlineStyle' not in already_processed:
            already_processed.add('underlineStyle')
            self.underlineStyle = value
            self.validate_UnderlineStyleSimpleType(self.underlineStyle)    # validate type UnderlineStyleSimpleType
        value = find_attr_value_('subscript', node)
        if value is not None and 'subscript' not in already_processed:
            already_processed.add('subscript')
            if value in ('true', '1'):
                self.subscript = True
            elif value in ('false', '0'):
                self.subscript = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('superscript', node)
        if value is not None and 'superscript' not in already_processed:
            already_processed.add('superscript')
            if value in ('true', '1'):
                self.superscript = True
            elif value in ('false', '0'):
                self.superscript = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('strikethrough', node)
        if value is not None and 'strikethrough' not in already_processed:
            already_processed.add('strikethrough')
            if value in ('true', '1'):
                self.strikethrough = True
            elif value in ('false', '0'):
                self.strikethrough = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('smallCaps', node)
        if value is not None and 'smallCaps' not in already_processed:
            already_processed.add('smallCaps')
            if value in ('true', '1'):
                self.smallCaps = True
            elif value in ('false', '0'):
                self.smallCaps = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('letterSpaced', node)
        if value is not None and 'letterSpaced' not in already_processed:
            already_processed.add('letterSpaced')
            if value in ('true', '1'):
                self.letterSpaced = True
            elif value in ('false', '0'):
                self.letterSpaced = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class TextStyleType


class RegionType(GeneratedsSuper):
    """For generic use
    Is this region a continuation of another region
    (in previous column or page, for example)?"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('continuation', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('AlternativeImage', 'AlternativeImageType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'AlternativeImage', 'type': 'AlternativeImageType'}, None),
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
        MemberSpec_('UserDefined', 'UserDefinedType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'UserDefined', 'type': 'UserDefinedType'}, None),
        MemberSpec_('Labels', 'LabelsType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'Labels', 'type': 'LabelsType'}, None),
        MemberSpec_('Roles', 'RolesType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Roles', 'type': 'RolesType'}, None),
        MemberSpec_('TextRegion', 'TextRegionType', 1, 1, {'name': 'TextRegion', 'type': 'TextRegionType'}, 7),
        MemberSpec_('ImageRegion', 'ImageRegionType', 1, 1, {'name': 'ImageRegion', 'type': 'ImageRegionType'}, 7),
        MemberSpec_('LineDrawingRegion', 'LineDrawingRegionType', 1, 1, {'name': 'LineDrawingRegion', 'type': 'LineDrawingRegionType'}, 7),
        MemberSpec_('GraphicRegion', 'GraphicRegionType', 1, 1, {'name': 'GraphicRegion', 'type': 'GraphicRegionType'}, 7),
        MemberSpec_('TableRegion', 'TableRegionType', 1, 1, {'name': 'TableRegion', 'type': 'TableRegionType'}, 7),
        MemberSpec_('ChartRegion', 'ChartRegionType', 1, 1, {'name': 'ChartRegion', 'type': 'ChartRegionType'}, 7),
        MemberSpec_('SeparatorRegion', 'SeparatorRegionType', 1, 1, {'name': 'SeparatorRegion', 'type': 'SeparatorRegionType'}, 7),
        MemberSpec_('MathsRegion', 'MathsRegionType', 1, 1, {'name': 'MathsRegion', 'type': 'MathsRegionType'}, 7),
        MemberSpec_('ChemRegion', 'ChemRegionType', 1, 1, {'name': 'ChemRegion', 'type': 'ChemRegionType'}, 7),
        MemberSpec_('MusicRegion', 'MusicRegionType', 1, 1, {'name': 'MusicRegion', 'type': 'MusicRegionType'}, 7),
        MemberSpec_('AdvertRegion', 'AdvertRegionType', 1, 1, {'name': 'AdvertRegion', 'type': 'AdvertRegionType'}, 7),
        MemberSpec_('NoiseRegion', 'NoiseRegionType', 1, 1, {'name': 'NoiseRegion', 'type': 'NoiseRegionType'}, 7),
        MemberSpec_('UnknownRegion', 'UnknownRegionType', 1, 1, {'name': 'UnknownRegion', 'type': 'UnknownRegionType'}, 7),
        MemberSpec_('CustomRegion', 'CustomRegionType', 1, 1, {'name': 'CustomRegion', 'type': 'CustomRegionType'}, 7),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.continuation = _cast(bool, continuation)
        self.continuation_nsprefix_ = "pc"
        if AlternativeImage is None:
            self.AlternativeImage = []
        else:
            self.AlternativeImage = AlternativeImage
        self.AlternativeImage_nsprefix_ = "pc"
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
        self.UserDefined = UserDefined
        self.UserDefined_nsprefix_ = "pc"
        if Labels is None:
            self.Labels = []
        else:
            self.Labels = Labels
        self.Labels_nsprefix_ = "pc"
        self.Roles = Roles
        self.Roles_nsprefix_ = "pc"
        if TextRegion is None:
            self.TextRegion = []
        else:
            self.TextRegion = TextRegion
        self.TextRegion_nsprefix_ = "pc"
        if ImageRegion is None:
            self.ImageRegion = []
        else:
            self.ImageRegion = ImageRegion
        self.ImageRegion_nsprefix_ = "pc"
        if LineDrawingRegion is None:
            self.LineDrawingRegion = []
        else:
            self.LineDrawingRegion = LineDrawingRegion
        self.LineDrawingRegion_nsprefix_ = "pc"
        if GraphicRegion is None:
            self.GraphicRegion = []
        else:
            self.GraphicRegion = GraphicRegion
        self.GraphicRegion_nsprefix_ = "pc"
        if TableRegion is None:
            self.TableRegion = []
        else:
            self.TableRegion = TableRegion
        self.TableRegion_nsprefix_ = "pc"
        if ChartRegion is None:
            self.ChartRegion = []
        else:
            self.ChartRegion = ChartRegion
        self.ChartRegion_nsprefix_ = "pc"
        if SeparatorRegion is None:
            self.SeparatorRegion = []
        else:
            self.SeparatorRegion = SeparatorRegion
        self.SeparatorRegion_nsprefix_ = "pc"
        if MathsRegion is None:
            self.MathsRegion = []
        else:
            self.MathsRegion = MathsRegion
        self.MathsRegion_nsprefix_ = "pc"
        if ChemRegion is None:
            self.ChemRegion = []
        else:
            self.ChemRegion = ChemRegion
        self.ChemRegion_nsprefix_ = "pc"
        if MusicRegion is None:
            self.MusicRegion = []
        else:
            self.MusicRegion = MusicRegion
        self.MusicRegion_nsprefix_ = "pc"
        if AdvertRegion is None:
            self.AdvertRegion = []
        else:
            self.AdvertRegion = AdvertRegion
        self.AdvertRegion_nsprefix_ = "pc"
        if NoiseRegion is None:
            self.NoiseRegion = []
        else:
            self.NoiseRegion = NoiseRegion
        self.NoiseRegion_nsprefix_ = "pc"
        if UnknownRegion is None:
            self.UnknownRegion = []
        else:
            self.UnknownRegion = UnknownRegion
        self.UnknownRegion_nsprefix_ = "pc"
        if CustomRegion is None:
            self.CustomRegion = []
        else:
            self.CustomRegion = CustomRegion
        self.CustomRegion_nsprefix_ = "pc"
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RegionType.subclass:
            return RegionType.subclass(*args_, **kwargs_)
        else:
            return RegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_AlternativeImage(self):
        return self.AlternativeImage
    def set_AlternativeImage(self, AlternativeImage):
        self.AlternativeImage = AlternativeImage
    def add_AlternativeImage(self, value):
        self.AlternativeImage.append(value)
    def insert_AlternativeImage_at(self, index, value):
        self.AlternativeImage.insert(index, value)
    def replace_AlternativeImage_at(self, index, value):
        self.AlternativeImage[index] = value
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def get_UserDefined(self):
        return self.UserDefined
    def set_UserDefined(self, UserDefined):
        self.UserDefined = UserDefined
    def get_Labels(self):
        return self.Labels
    def set_Labels(self, Labels):
        self.Labels = Labels
    def add_Labels(self, value):
        self.Labels.append(value)
    def insert_Labels_at(self, index, value):
        self.Labels.insert(index, value)
    def replace_Labels_at(self, index, value):
        self.Labels[index] = value
    def get_Roles(self):
        return self.Roles
    def set_Roles(self, Roles):
        self.Roles = Roles
    def get_TextRegion(self):
        return self.TextRegion
    def set_TextRegion(self, TextRegion):
        self.TextRegion = TextRegion
    def add_TextRegion(self, value):
        self.TextRegion.append(value)
    def insert_TextRegion_at(self, index, value):
        self.TextRegion.insert(index, value)
    def replace_TextRegion_at(self, index, value):
        self.TextRegion[index] = value
    def get_ImageRegion(self):
        return self.ImageRegion
    def set_ImageRegion(self, ImageRegion):
        self.ImageRegion = ImageRegion
    def add_ImageRegion(self, value):
        self.ImageRegion.append(value)
    def insert_ImageRegion_at(self, index, value):
        self.ImageRegion.insert(index, value)
    def replace_ImageRegion_at(self, index, value):
        self.ImageRegion[index] = value
    def get_LineDrawingRegion(self):
        return self.LineDrawingRegion
    def set_LineDrawingRegion(self, LineDrawingRegion):
        self.LineDrawingRegion = LineDrawingRegion
    def add_LineDrawingRegion(self, value):
        self.LineDrawingRegion.append(value)
    def insert_LineDrawingRegion_at(self, index, value):
        self.LineDrawingRegion.insert(index, value)
    def replace_LineDrawingRegion_at(self, index, value):
        self.LineDrawingRegion[index] = value
    def get_GraphicRegion(self):
        return self.GraphicRegion
    def set_GraphicRegion(self, GraphicRegion):
        self.GraphicRegion = GraphicRegion
    def add_GraphicRegion(self, value):
        self.GraphicRegion.append(value)
    def insert_GraphicRegion_at(self, index, value):
        self.GraphicRegion.insert(index, value)
    def replace_GraphicRegion_at(self, index, value):
        self.GraphicRegion[index] = value
    def get_TableRegion(self):
        return self.TableRegion
    def set_TableRegion(self, TableRegion):
        self.TableRegion = TableRegion
    def add_TableRegion(self, value):
        self.TableRegion.append(value)
    def insert_TableRegion_at(self, index, value):
        self.TableRegion.insert(index, value)
    def replace_TableRegion_at(self, index, value):
        self.TableRegion[index] = value
    def get_ChartRegion(self):
        return self.ChartRegion
    def set_ChartRegion(self, ChartRegion):
        self.ChartRegion = ChartRegion
    def add_ChartRegion(self, value):
        self.ChartRegion.append(value)
    def insert_ChartRegion_at(self, index, value):
        self.ChartRegion.insert(index, value)
    def replace_ChartRegion_at(self, index, value):
        self.ChartRegion[index] = value
    def get_SeparatorRegion(self):
        return self.SeparatorRegion
    def set_SeparatorRegion(self, SeparatorRegion):
        self.SeparatorRegion = SeparatorRegion
    def add_SeparatorRegion(self, value):
        self.SeparatorRegion.append(value)
    def insert_SeparatorRegion_at(self, index, value):
        self.SeparatorRegion.insert(index, value)
    def replace_SeparatorRegion_at(self, index, value):
        self.SeparatorRegion[index] = value
    def get_MathsRegion(self):
        return self.MathsRegion
    def set_MathsRegion(self, MathsRegion):
        self.MathsRegion = MathsRegion
    def add_MathsRegion(self, value):
        self.MathsRegion.append(value)
    def insert_MathsRegion_at(self, index, value):
        self.MathsRegion.insert(index, value)
    def replace_MathsRegion_at(self, index, value):
        self.MathsRegion[index] = value
    def get_ChemRegion(self):
        return self.ChemRegion
    def set_ChemRegion(self, ChemRegion):
        self.ChemRegion = ChemRegion
    def add_ChemRegion(self, value):
        self.ChemRegion.append(value)
    def insert_ChemRegion_at(self, index, value):
        self.ChemRegion.insert(index, value)
    def replace_ChemRegion_at(self, index, value):
        self.ChemRegion[index] = value
    def get_MusicRegion(self):
        return self.MusicRegion
    def set_MusicRegion(self, MusicRegion):
        self.MusicRegion = MusicRegion
    def add_MusicRegion(self, value):
        self.MusicRegion.append(value)
    def insert_MusicRegion_at(self, index, value):
        self.MusicRegion.insert(index, value)
    def replace_MusicRegion_at(self, index, value):
        self.MusicRegion[index] = value
    def get_AdvertRegion(self):
        return self.AdvertRegion
    def set_AdvertRegion(self, AdvertRegion):
        self.AdvertRegion = AdvertRegion
    def add_AdvertRegion(self, value):
        self.AdvertRegion.append(value)
    def insert_AdvertRegion_at(self, index, value):
        self.AdvertRegion.insert(index, value)
    def replace_AdvertRegion_at(self, index, value):
        self.AdvertRegion[index] = value
    def get_NoiseRegion(self):
        return self.NoiseRegion
    def set_NoiseRegion(self, NoiseRegion):
        self.NoiseRegion = NoiseRegion
    def add_NoiseRegion(self, value):
        self.NoiseRegion.append(value)
    def insert_NoiseRegion_at(self, index, value):
        self.NoiseRegion.insert(index, value)
    def replace_NoiseRegion_at(self, index, value):
        self.NoiseRegion[index] = value
    def get_UnknownRegion(self):
        return self.UnknownRegion
    def set_UnknownRegion(self, UnknownRegion):
        self.UnknownRegion = UnknownRegion
    def add_UnknownRegion(self, value):
        self.UnknownRegion.append(value)
    def insert_UnknownRegion_at(self, index, value):
        self.UnknownRegion.insert(index, value)
    def replace_UnknownRegion_at(self, index, value):
        self.UnknownRegion[index] = value
    def get_CustomRegion(self):
        return self.CustomRegion
    def set_CustomRegion(self, CustomRegion):
        self.CustomRegion = CustomRegion
    def add_CustomRegion(self, value):
        self.CustomRegion.append(value)
    def insert_CustomRegion_at(self, index, value):
        self.CustomRegion.insert(index, value)
    def replace_CustomRegion_at(self, index, value):
        self.CustomRegion[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def get_continuation(self):
        return self.continuation
    def set_continuation(self, continuation):
        self.continuation = continuation
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.AlternativeImage or
            self.Coords is not None or
            self.UserDefined is not None or
            self.Labels or
            self.Roles is not None or
            self.TextRegion or
            self.ImageRegion or
            self.LineDrawingRegion or
            self.GraphicRegion or
            self.TableRegion or
            self.ChartRegion or
            self.SeparatorRegion or
            self.MathsRegion or
            self.ChemRegion or
            self.MusicRegion or
            self.AdvertRegion or
            self.NoiseRegion or
            self.UnknownRegion or
            self.CustomRegion
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RegionType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
        if self.continuation is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            outfile.write(' continuation="%s"' % self.gds_format_boolean(self.continuation, input_name='continuation'))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RegionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AlternativeImage_ in self.AlternativeImage:
            namespaceprefix_ = self.AlternativeImage_nsprefix_ + ':' if (UseCapturedNS_ and self.AlternativeImage_nsprefix_) else ''
            AlternativeImage_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlternativeImage', pretty_print=pretty_print)
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
        if self.UserDefined is not None:
            namespaceprefix_ = self.UserDefined_nsprefix_ + ':' if (UseCapturedNS_ and self.UserDefined_nsprefix_) else ''
            self.UserDefined.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserDefined', pretty_print=pretty_print)
        for Labels_ in self.Labels:
            namespaceprefix_ = self.Labels_nsprefix_ + ':' if (UseCapturedNS_ and self.Labels_nsprefix_) else ''
            Labels_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Labels', pretty_print=pretty_print)
        if self.Roles is not None:
            namespaceprefix_ = self.Roles_nsprefix_ + ':' if (UseCapturedNS_ and self.Roles_nsprefix_) else ''
            self.Roles.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Roles', pretty_print=pretty_print)
        for TextRegion_ in self.TextRegion:
            namespaceprefix_ = self.TextRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.TextRegion_nsprefix_) else ''
            TextRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextRegion', pretty_print=pretty_print)
        for ImageRegion_ in self.ImageRegion:
            namespaceprefix_ = self.ImageRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ImageRegion_nsprefix_) else ''
            ImageRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ImageRegion', pretty_print=pretty_print)
        for LineDrawingRegion_ in self.LineDrawingRegion:
            namespaceprefix_ = self.LineDrawingRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.LineDrawingRegion_nsprefix_) else ''
            LineDrawingRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LineDrawingRegion', pretty_print=pretty_print)
        for GraphicRegion_ in self.GraphicRegion:
            namespaceprefix_ = self.GraphicRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.GraphicRegion_nsprefix_) else ''
            GraphicRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GraphicRegion', pretty_print=pretty_print)
        for TableRegion_ in self.TableRegion:
            namespaceprefix_ = self.TableRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.TableRegion_nsprefix_) else ''
            TableRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TableRegion', pretty_print=pretty_print)
        for ChartRegion_ in self.ChartRegion:
            namespaceprefix_ = self.ChartRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ChartRegion_nsprefix_) else ''
            ChartRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChartRegion', pretty_print=pretty_print)
        for SeparatorRegion_ in self.SeparatorRegion:
            namespaceprefix_ = self.SeparatorRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.SeparatorRegion_nsprefix_) else ''
            SeparatorRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SeparatorRegion', pretty_print=pretty_print)
        for MathsRegion_ in self.MathsRegion:
            namespaceprefix_ = self.MathsRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.MathsRegion_nsprefix_) else ''
            MathsRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MathsRegion', pretty_print=pretty_print)
        for ChemRegion_ in self.ChemRegion:
            namespaceprefix_ = self.ChemRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ChemRegion_nsprefix_) else ''
            ChemRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ChemRegion', pretty_print=pretty_print)
        for MusicRegion_ in self.MusicRegion:
            namespaceprefix_ = self.MusicRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.MusicRegion_nsprefix_) else ''
            MusicRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='MusicRegion', pretty_print=pretty_print)
        for AdvertRegion_ in self.AdvertRegion:
            namespaceprefix_ = self.AdvertRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.AdvertRegion_nsprefix_) else ''
            AdvertRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AdvertRegion', pretty_print=pretty_print)
        for NoiseRegion_ in self.NoiseRegion:
            namespaceprefix_ = self.NoiseRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.NoiseRegion_nsprefix_) else ''
            NoiseRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NoiseRegion', pretty_print=pretty_print)
        for UnknownRegion_ in self.UnknownRegion:
            namespaceprefix_ = self.UnknownRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.UnknownRegion_nsprefix_) else ''
            UnknownRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UnknownRegion', pretty_print=pretty_print)
        for CustomRegion_ in self.CustomRegion:
            namespaceprefix_ = self.CustomRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.CustomRegion_nsprefix_) else ''
            CustomRegion_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CustomRegion', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
        value = find_attr_value_('continuation', node)
        if value is not None and 'continuation' not in already_processed:
            already_processed.add('continuation')
            if value in ('true', '1'):
                self.continuation = True
            elif value in ('false', '0'):
                self.continuation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlternativeImage':
            obj_ = AlternativeImageType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlternativeImage.append(obj_)
            obj_.original_tagname_ = 'AlternativeImage'
        elif nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
        elif nodeName_ == 'UserDefined':
            obj_ = UserDefinedType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserDefined = obj_
            obj_.original_tagname_ = 'UserDefined'
        elif nodeName_ == 'Labels':
            obj_ = LabelsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Labels.append(obj_)
            obj_.original_tagname_ = 'Labels'
        elif nodeName_ == 'Roles':
            obj_ = RolesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Roles = obj_
            obj_.original_tagname_ = 'Roles'
        elif nodeName_ == 'TextRegion':
            obj_ = TextRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextRegion.append(obj_)
            obj_.original_tagname_ = 'TextRegion'
        elif nodeName_ == 'ImageRegion':
            obj_ = ImageRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ImageRegion.append(obj_)
            obj_.original_tagname_ = 'ImageRegion'
        elif nodeName_ == 'LineDrawingRegion':
            obj_ = LineDrawingRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LineDrawingRegion.append(obj_)
            obj_.original_tagname_ = 'LineDrawingRegion'
        elif nodeName_ == 'GraphicRegion':
            obj_ = GraphicRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GraphicRegion.append(obj_)
            obj_.original_tagname_ = 'GraphicRegion'
        elif nodeName_ == 'TableRegion':
            obj_ = TableRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TableRegion.append(obj_)
            obj_.original_tagname_ = 'TableRegion'
        elif nodeName_ == 'ChartRegion':
            obj_ = ChartRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChartRegion.append(obj_)
            obj_.original_tagname_ = 'ChartRegion'
        elif nodeName_ == 'SeparatorRegion':
            obj_ = SeparatorRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SeparatorRegion.append(obj_)
            obj_.original_tagname_ = 'SeparatorRegion'
        elif nodeName_ == 'MathsRegion':
            obj_ = MathsRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MathsRegion.append(obj_)
            obj_.original_tagname_ = 'MathsRegion'
        elif nodeName_ == 'ChemRegion':
            obj_ = ChemRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChemRegion.append(obj_)
            obj_.original_tagname_ = 'ChemRegion'
        elif nodeName_ == 'MusicRegion':
            obj_ = MusicRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MusicRegion.append(obj_)
            obj_.original_tagname_ = 'MusicRegion'
        elif nodeName_ == 'AdvertRegion':
            obj_ = AdvertRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AdvertRegion.append(obj_)
            obj_.original_tagname_ = 'AdvertRegion'
        elif nodeName_ == 'NoiseRegion':
            obj_ = NoiseRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NoiseRegion.append(obj_)
            obj_.original_tagname_ = 'NoiseRegion'
        elif nodeName_ == 'UnknownRegion':
            obj_ = UnknownRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UnknownRegion.append(obj_)
            obj_.original_tagname_ = 'UnknownRegion'
        elif nodeName_ == 'CustomRegion':
            obj_ = CustomRegionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CustomRegion.append(obj_)
            obj_.original_tagname_ = 'CustomRegion'
    def __hash__(self):
        return hash(self.id)
    def invalidate_AlternativeImage(self, feature_selector=None):
        """
        Remove derived images from this segment (due to changed coordinates).
    
        If ``feature_selector`` is not none, remove only images with
        matching ``@comments``, e.g. ``feature_selector=cropped,deskewed``.
        """
        existing_images = self.AlternativeImage or []
        removed_images = []
        if feature_selector:
            new_images = []
            for image in existing_images:
                features = image.get_comments() or ''
                if any(feature in features.split(',')
                       for feature in feature_selector.split(',') if feature):
                    removed_images.append(image)
                else:
                    new_images.append(image)
            self.AlternativeImage = new_images
        else:
            removed_images = existing_images
            self.AlternativeImage = []
        if hasattr(self, 'id'):
            name = self.id
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'pcGtsId'):
            name = self.parent_object_.pcGtsId
        else:
            name = ''
        for image in removed_images:
            self.gds_collector_.add_message('Removing AlternativeImage %s from "%s"' % (
                image.get_comments() or '', name))
    def set_Coords(self, Coords):
        """
        Set coordinate polygon by given object.
        Moreover, invalidate self's AlternativeImages
        (because they will have been cropped with a bbox
         of the previous polygon).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # RegionType, TextLineType, WordType, GlyphType:
            self.invalidate_AlternativeImage()
        elif hasattr(self, 'parent_object_') and hasattr(self.parent_object_, 'invalidate_AlternativeImage'):
            # BorderType:
            self.parent_object_.invalidate_AlternativeImage(feature_selector='cropped')
        self.Coords = Coords
# end class RegionType


class AlternativeImageType(GeneratedsSuper):
    """Confidence value (between 0 and 1)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('filename', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('conf', 'pc:ConfSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, filename=None, comments=None, conf=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.filename = _cast(None, filename)
        self.filename_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        self.conf = _cast(float, conf)
        self.conf_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AlternativeImageType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AlternativeImageType.subclass:
            return AlternativeImageType.subclass(*args_, **kwargs_)
        else:
            return AlternativeImageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_filename(self):
        return self.filename
    def set_filename(self, filename):
        self.filename = filename
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def get_conf(self):
        return self.conf
    def set_conf(self, conf):
        self.conf = conf
    def validate_ConfSimpleType(self, value):
        # Validate type pc:ConfSimpleType, a restriction on float.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
            if value > 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on ConfSimpleType' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='AlternativeImageType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AlternativeImageType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AlternativeImageType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AlternativeImageType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AlternativeImageType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AlternativeImageType'):
        if self.filename is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            outfile.write(' filename=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.filename), input_name='filename')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_float(self.conf, input_name='conf'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='AlternativeImageType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('filename', node)
        if value is not None and 'filename' not in already_processed:
            already_processed.add('filename')
            self.filename = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            value = self.gds_parse_float(value, node, 'conf')
            self.conf = value
            self.validate_ConfSimpleType(self.conf)    # validate type ConfSimpleType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class AlternativeImageType


class GraphemesType(GeneratedsSuper):
    """Container for graphemes, grapheme groups and
    non-printing characters."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Grapheme', 'GraphemeType', 1, 0, {'name': 'Grapheme', 'type': 'GraphemeType'}, 8),
        MemberSpec_('NonPrintingChar', 'NonPrintingCharType', 1, 0, {'name': 'NonPrintingChar', 'type': 'NonPrintingCharType'}, 8),
        MemberSpec_('GraphemeGroup', 'GraphemeGroupType', 1, 0, {'name': 'GraphemeGroup', 'type': 'GraphemeGroupType'}, 8),
    ]
    subclass = None
    superclass = None
    def __init__(self, Grapheme=None, NonPrintingChar=None, GraphemeGroup=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Grapheme is None:
            self.Grapheme = []
        else:
            self.Grapheme = Grapheme
        self.Grapheme_nsprefix_ = "pc"
        if NonPrintingChar is None:
            self.NonPrintingChar = []
        else:
            self.NonPrintingChar = NonPrintingChar
        self.NonPrintingChar_nsprefix_ = "pc"
        if GraphemeGroup is None:
            self.GraphemeGroup = []
        else:
            self.GraphemeGroup = GraphemeGroup
        self.GraphemeGroup_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GraphemesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GraphemesType.subclass:
            return GraphemesType.subclass(*args_, **kwargs_)
        else:
            return GraphemesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Grapheme(self):
        return self.Grapheme
    def set_Grapheme(self, Grapheme):
        self.Grapheme = Grapheme
    def add_Grapheme(self, value):
        self.Grapheme.append(value)
    def insert_Grapheme_at(self, index, value):
        self.Grapheme.insert(index, value)
    def replace_Grapheme_at(self, index, value):
        self.Grapheme[index] = value
    def get_NonPrintingChar(self):
        return self.NonPrintingChar
    def set_NonPrintingChar(self, NonPrintingChar):
        self.NonPrintingChar = NonPrintingChar
    def add_NonPrintingChar(self, value):
        self.NonPrintingChar.append(value)
    def insert_NonPrintingChar_at(self, index, value):
        self.NonPrintingChar.insert(index, value)
    def replace_NonPrintingChar_at(self, index, value):
        self.NonPrintingChar[index] = value
    def get_GraphemeGroup(self):
        return self.GraphemeGroup
    def set_GraphemeGroup(self, GraphemeGroup):
        self.GraphemeGroup = GraphemeGroup
    def add_GraphemeGroup(self, value):
        self.GraphemeGroup.append(value)
    def insert_GraphemeGroup_at(self, index, value):
        self.GraphemeGroup.insert(index, value)
    def replace_GraphemeGroup_at(self, index, value):
        self.GraphemeGroup[index] = value
    def hasContent_(self):
        if (
            self.Grapheme or
            self.NonPrintingChar or
            self.GraphemeGroup
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GraphemesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GraphemesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphemesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GraphemesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GraphemesType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Grapheme_ in self.Grapheme:
            namespaceprefix_ = self.Grapheme_nsprefix_ + ':' if (UseCapturedNS_ and self.Grapheme_nsprefix_) else ''
            Grapheme_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Grapheme', pretty_print=pretty_print)
        for NonPrintingChar_ in self.NonPrintingChar:
            namespaceprefix_ = self.NonPrintingChar_nsprefix_ + ':' if (UseCapturedNS_ and self.NonPrintingChar_nsprefix_) else ''
            NonPrintingChar_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NonPrintingChar', pretty_print=pretty_print)
        for GraphemeGroup_ in self.GraphemeGroup:
            namespaceprefix_ = self.GraphemeGroup_nsprefix_ + ':' if (UseCapturedNS_ and self.GraphemeGroup_nsprefix_) else ''
            GraphemeGroup_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GraphemeGroup', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Grapheme':
            obj_ = GraphemeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Grapheme.append(obj_)
            obj_.original_tagname_ = 'Grapheme'
        elif nodeName_ == 'NonPrintingChar':
            obj_ = NonPrintingCharType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NonPrintingChar.append(obj_)
            obj_.original_tagname_ = 'NonPrintingChar'
        elif nodeName_ == 'GraphemeGroup':
            obj_ = GraphemeGroupType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GraphemeGroup.append(obj_)
            obj_.original_tagname_ = 'GraphemeGroup'
    def __hash__(self):
        return hash(self.id)
# end class GraphemesType


class GraphemeBaseType(GeneratedsSuper):
    """Base type for graphemes, grapheme groups and non-printing characters.
    Order index of grapheme, group, or non-printing character
    within the parent container (graphemes or glyph or grapheme group).
    Type of character represented by the
    grapheme, group, or non-printing character element.
    For generic useFor generic use"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('id', 'string', 0, 0, {'use': 'required'}),
        MemberSpec_('index', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('ligature', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('charType', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('custom', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('comments', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('TextEquiv', 'TextEquivType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'TextEquiv', 'type': 'TextEquivType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, id=None, index=None, ligature=None, charType=None, custom=None, comments=None, TextEquiv=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = "pc"
        self.index = _cast(int, index)
        self.index_nsprefix_ = "pc"
        self.ligature = _cast(bool, ligature)
        self.ligature_nsprefix_ = "pc"
        self.charType = _cast(None, charType)
        self.charType_nsprefix_ = "pc"
        self.custom = _cast(None, custom)
        self.custom_nsprefix_ = "pc"
        self.comments = _cast(None, comments)
        self.comments_nsprefix_ = "pc"
        if TextEquiv is None:
            self.TextEquiv = []
        else:
            self.TextEquiv = TextEquiv
        self.TextEquiv_nsprefix_ = "pc"
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GraphemeBaseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GraphemeBaseType.subclass:
            return GraphemeBaseType.subclass(*args_, **kwargs_)
        else:
            return GraphemeBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TextEquiv(self):
        return self.TextEquiv
    def set_TextEquiv(self, TextEquiv):
        self.TextEquiv = TextEquiv
    def add_TextEquiv(self, value):
        self.TextEquiv.append(value)
    def insert_TextEquiv_at(self, index, value):
        self.TextEquiv.insert(index, value)
    def replace_TextEquiv_at(self, index, value):
        self.TextEquiv[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_index(self):
        return self.index
    def set_index(self, index):
        self.index = index
    def get_ligature(self):
        return self.ligature
    def set_ligature(self, ligature):
        self.ligature = ligature
    def get_charType(self):
        return self.charType
    def set_charType(self, charType):
        self.charType = charType
    def get_custom(self):
        return self.custom
    def set_custom(self, custom):
        self.custom = custom
    def get_comments(self):
        return self.comments
    def set_comments(self, comments):
        self.comments = comments
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.TextEquiv
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemeBaseType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GraphemeBaseType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GraphemeBaseType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphemeBaseType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GraphemeBaseType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GraphemeBaseType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.index is not None and 'index' not in already_processed:
            already_processed.add('index')
            outfile.write(' index="%s"' % self.gds_format_integer(self.index, input_name='index'))
        if self.ligature is not None and 'ligature' not in already_processed:
            already_processed.add('ligature')
            outfile.write(' ligature="%s"' % self.gds_format_boolean(self.ligature, input_name='ligature'))
        if self.charType is not None and 'charType' not in already_processed:
            already_processed.add('charType')
            outfile.write(' charType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.charType), input_name='charType')), ))
        if self.custom is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            outfile.write(' custom=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.custom), input_name='custom')), ))
        if self.comments is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            outfile.write(' comments=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.comments), input_name='comments')), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemeBaseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TextEquiv_ in self.TextEquiv:
            namespaceprefix_ = self.TextEquiv_nsprefix_ + ':' if (UseCapturedNS_ and self.TextEquiv_nsprefix_) else ''
            TextEquiv_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextEquiv', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('index', node)
        if value is not None and 'index' not in already_processed:
            already_processed.add('index')
            self.index = self.gds_parse_integer(value, node, 'index')
        value = find_attr_value_('ligature', node)
        if value is not None and 'ligature' not in already_processed:
            already_processed.add('ligature')
            if value in ('true', '1'):
                self.ligature = True
            elif value in ('false', '0'):
                self.ligature = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('charType', node)
        if value is not None and 'charType' not in already_processed:
            already_processed.add('charType')
            self.charType = value
        value = find_attr_value_('custom', node)
        if value is not None and 'custom' not in already_processed:
            already_processed.add('custom')
            self.custom = value
        value = find_attr_value_('comments', node)
        if value is not None and 'comments' not in already_processed:
            already_processed.add('comments')
            self.comments = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TextEquiv':
            obj_ = TextEquivType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextEquiv.append(obj_)
            obj_.original_tagname_ = 'TextEquiv'
    def __hash__(self):
        return hash(self.id)
# end class GraphemeBaseType


class GraphemeType(GraphemeBaseType):
    """Represents a sub-element of a glyph.
    Smallest graphical unit that can be
    assigned a Unicode code point."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Coords', 'CoordsType', 0, 0, {'name': 'Coords', 'type': 'CoordsType'}, None),
    ]
    subclass = None
    superclass = GraphemeBaseType
    def __init__(self, id=None, index=None, ligature=None, charType=None, custom=None, comments=None, TextEquiv=None, Coords=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(GraphemeType, self).__init__(id, index, ligature, charType, custom, comments, TextEquiv,  **kwargs_)
        self.Coords = Coords
        self.Coords_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GraphemeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GraphemeType.subclass:
            return GraphemeType.subclass(*args_, **kwargs_)
        else:
            return GraphemeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Coords(self):
        return self.Coords
    def set_Coords(self, Coords):
        self.Coords = Coords
    def hasContent_(self):
        if (
            self.Coords is not None or
            super(GraphemeType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GraphemeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GraphemeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphemeType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GraphemeType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GraphemeType'):
        super(GraphemeType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphemeType')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemeType', fromsubclass_=False, pretty_print=True):
        super(GraphemeType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Coords is not None:
            namespaceprefix_ = self.Coords_nsprefix_ + ':' if (UseCapturedNS_ and self.Coords_nsprefix_) else ''
            self.Coords.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Coords', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(GraphemeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Coords':
            obj_ = CoordsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Coords = obj_
            obj_.original_tagname_ = 'Coords'
        super(GraphemeType, self).buildChildren(child_, node, nodeName_, True)
    def __hash__(self):
        return hash(self.id)
# end class GraphemeType


class NonPrintingCharType(GraphemeBaseType):
    """A glyph component without visual representation
    but with Unicode code point.
    Non-visual / non-printing / control character.
    Part of grapheme container (of glyph) or grapheme sub group."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
    ]
    subclass = None
    superclass = GraphemeBaseType
    def __init__(self, id=None, index=None, ligature=None, charType=None, custom=None, comments=None, TextEquiv=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(NonPrintingCharType, self).__init__(id, index, ligature, charType, custom, comments, TextEquiv,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NonPrintingCharType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NonPrintingCharType.subclass:
            return NonPrintingCharType.subclass(*args_, **kwargs_)
        else:
            return NonPrintingCharType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def hasContent_(self):
        if (
            super(NonPrintingCharType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='NonPrintingCharType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NonPrintingCharType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NonPrintingCharType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonPrintingCharType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NonPrintingCharType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NonPrintingCharType'):
        super(NonPrintingCharType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NonPrintingCharType')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='NonPrintingCharType', fromsubclass_=False, pretty_print=True):
        super(NonPrintingCharType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(NonPrintingCharType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(NonPrintingCharType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
# end class NonPrintingCharType


class GraphemeGroupType(GraphemeBaseType):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Grapheme', 'GraphemeType', 1, 1, {'name': 'Grapheme', 'type': 'GraphemeType'}, 9),
        MemberSpec_('NonPrintingChar', 'NonPrintingCharType', 1, 1, {'name': 'NonPrintingChar', 'type': 'NonPrintingCharType'}, 9),
    ]
    subclass = None
    superclass = GraphemeBaseType
    def __init__(self, id=None, index=None, ligature=None, charType=None, custom=None, comments=None, TextEquiv=None, Grapheme=None, NonPrintingChar=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(GraphemeGroupType, self).__init__(id, index, ligature, charType, custom, comments, TextEquiv,  **kwargs_)
        if Grapheme is None:
            self.Grapheme = []
        else:
            self.Grapheme = Grapheme
        self.Grapheme_nsprefix_ = "pc"
        if NonPrintingChar is None:
            self.NonPrintingChar = []
        else:
            self.NonPrintingChar = NonPrintingChar
        self.NonPrintingChar_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GraphemeGroupType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GraphemeGroupType.subclass:
            return GraphemeGroupType.subclass(*args_, **kwargs_)
        else:
            return GraphemeGroupType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Grapheme(self):
        return self.Grapheme
    def set_Grapheme(self, Grapheme):
        self.Grapheme = Grapheme
    def add_Grapheme(self, value):
        self.Grapheme.append(value)
    def insert_Grapheme_at(self, index, value):
        self.Grapheme.insert(index, value)
    def replace_Grapheme_at(self, index, value):
        self.Grapheme[index] = value
    def get_NonPrintingChar(self):
        return self.NonPrintingChar
    def set_NonPrintingChar(self, NonPrintingChar):
        self.NonPrintingChar = NonPrintingChar
    def add_NonPrintingChar(self, value):
        self.NonPrintingChar.append(value)
    def insert_NonPrintingChar_at(self, index, value):
        self.NonPrintingChar.insert(index, value)
    def replace_NonPrintingChar_at(self, index, value):
        self.NonPrintingChar[index] = value
    def hasContent_(self):
        if (
            self.Grapheme or
            self.NonPrintingChar or
            super(GraphemeGroupType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemeGroupType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GraphemeGroupType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GraphemeGroupType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphemeGroupType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GraphemeGroupType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GraphemeGroupType'):
        super(GraphemeGroupType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphemeGroupType')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='GraphemeGroupType', fromsubclass_=False, pretty_print=True):
        super(GraphemeGroupType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Grapheme_ in self.Grapheme:
            namespaceprefix_ = self.Grapheme_nsprefix_ + ':' if (UseCapturedNS_ and self.Grapheme_nsprefix_) else ''
            Grapheme_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Grapheme', pretty_print=pretty_print)
        for NonPrintingChar_ in self.NonPrintingChar:
            namespaceprefix_ = self.NonPrintingChar_nsprefix_ + ':' if (UseCapturedNS_ and self.NonPrintingChar_nsprefix_) else ''
            NonPrintingChar_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='NonPrintingChar', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(GraphemeGroupType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Grapheme':
            obj_ = GraphemeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Grapheme.append(obj_)
            obj_.original_tagname_ = 'Grapheme'
        elif nodeName_ == 'NonPrintingChar':
            obj_ = NonPrintingCharType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NonPrintingChar.append(obj_)
            obj_.original_tagname_ = 'NonPrintingChar'
        super(GraphemeGroupType, self).buildChildren(child_, node, nodeName_, True)
    def __hash__(self):
        return hash(self.id)
# end class GraphemeGroupType


class UserDefinedType(GeneratedsSuper):
    """Container for user-defined attributes"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('UserAttribute', 'UserAttributeType', 1, 0, {'maxOccurs': 'unbounded', 'minOccurs': '1', 'name': 'UserAttribute', 'type': 'UserAttributeType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, UserAttribute=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if UserAttribute is None:
            self.UserAttribute = []
        else:
            self.UserAttribute = UserAttribute
        self.UserAttribute_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UserDefinedType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UserDefinedType.subclass:
            return UserDefinedType.subclass(*args_, **kwargs_)
        else:
            return UserDefinedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_UserAttribute(self):
        return self.UserAttribute
    def set_UserAttribute(self, UserAttribute):
        self.UserAttribute = UserAttribute
    def add_UserAttribute(self, value):
        self.UserAttribute.append(value)
    def insert_UserAttribute_at(self, index, value):
        self.UserAttribute.insert(index, value)
    def replace_UserAttribute_at(self, index, value):
        self.UserAttribute[index] = value
    def hasContent_(self):
        if (
            self.UserAttribute
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UserDefinedType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UserDefinedType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UserDefinedType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UserDefinedType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UserDefinedType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UserDefinedType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UserDefinedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for UserAttribute_ in self.UserAttribute:
            namespaceprefix_ = self.UserAttribute_nsprefix_ + ':' if (UseCapturedNS_ and self.UserAttribute_nsprefix_) else ''
            UserAttribute_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='UserAttribute', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'UserAttribute':
            obj_ = UserAttributeType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.UserAttribute.append(obj_)
            obj_.original_tagname_ = 'UserAttribute'
    def __hash__(self):
        return hash(self.id)
# end class UserDefinedType


class UserAttributeType(GeneratedsSuper):
    """Structured custom data defined by name, type and value."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('name', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('description', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'string', 0, 1, {'use': 'optional'}),
        MemberSpec_('value', 'string', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, name=None, description=None, type_=None, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = "pc"
        self.description = _cast(None, description)
        self.description_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.value = _cast(None, value)
        self.value_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UserAttributeType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UserAttributeType.subclass:
            return UserAttributeType.subclass(*args_, **kwargs_)
        else:
            return UserAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UserAttributeType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UserAttributeType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UserAttributeType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UserAttributeType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UserAttributeType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UserAttributeType'):
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            outfile.write(' name=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.name), input_name='name')), ))
        if self.description is not None and 'description' not in already_processed:
            already_processed.add('description')
            outfile.write(' description=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.description), input_name='description')), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.value is not None and 'value' not in already_processed:
            already_processed.add('value')
            outfile.write(' value=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.value), input_name='value')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='UserAttributeType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('description', node)
        if value is not None and 'description' not in already_processed:
            already_processed.add('description')
            self.description = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        value = find_attr_value_('value', node)
        if value is not None and 'value' not in already_processed:
            already_processed.add('value')
            self.value = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class UserAttributeType


class TableCellRoleType(GeneratedsSuper):
    """Cell position in table starting with row 0Cell position in table
    starting with column 0Number of rows the cell spans (optional; default
    is 1)Number of columns the cell spans (optional; default is 1)
    Is the cell a column or row header?"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('rowIndex', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('columnIndex', 'int', 0, 0, {'use': 'required'}),
        MemberSpec_('rowSpan', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('colSpan', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('header', 'boolean', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, rowIndex=None, columnIndex=None, rowSpan=None, colSpan=None, header=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rowIndex = _cast(int, rowIndex)
        self.rowIndex_nsprefix_ = "pc"
        self.columnIndex = _cast(int, columnIndex)
        self.columnIndex_nsprefix_ = "pc"
        self.rowSpan = _cast(int, rowSpan)
        self.rowSpan_nsprefix_ = "pc"
        self.colSpan = _cast(int, colSpan)
        self.colSpan_nsprefix_ = "pc"
        self.header = _cast(bool, header)
        self.header_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TableCellRoleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TableCellRoleType.subclass:
            return TableCellRoleType.subclass(*args_, **kwargs_)
        else:
            return TableCellRoleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_rowIndex(self):
        return self.rowIndex
    def set_rowIndex(self, rowIndex):
        self.rowIndex = rowIndex
    def get_columnIndex(self):
        return self.columnIndex
    def set_columnIndex(self, columnIndex):
        self.columnIndex = columnIndex
    def get_rowSpan(self):
        return self.rowSpan
    def set_rowSpan(self, rowSpan):
        self.rowSpan = rowSpan
    def get_colSpan(self):
        return self.colSpan
    def set_colSpan(self, colSpan):
        self.colSpan = colSpan
    def get_header(self):
        return self.header
    def set_header(self, header):
        self.header = header
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='TableCellRoleType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TableCellRoleType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TableCellRoleType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TableCellRoleType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TableCellRoleType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TableCellRoleType'):
        if self.rowIndex is not None and 'rowIndex' not in already_processed:
            already_processed.add('rowIndex')
            outfile.write(' rowIndex="%s"' % self.gds_format_integer(self.rowIndex, input_name='rowIndex'))
        if self.columnIndex is not None and 'columnIndex' not in already_processed:
            already_processed.add('columnIndex')
            outfile.write(' columnIndex="%s"' % self.gds_format_integer(self.columnIndex, input_name='columnIndex'))
        if self.rowSpan is not None and 'rowSpan' not in already_processed:
            already_processed.add('rowSpan')
            outfile.write(' rowSpan="%s"' % self.gds_format_integer(self.rowSpan, input_name='rowSpan'))
        if self.colSpan is not None and 'colSpan' not in already_processed:
            already_processed.add('colSpan')
            outfile.write(' colSpan="%s"' % self.gds_format_integer(self.colSpan, input_name='colSpan'))
        if self.header is not None and 'header' not in already_processed:
            already_processed.add('header')
            outfile.write(' header="%s"' % self.gds_format_boolean(self.header, input_name='header'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='TableCellRoleType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rowIndex', node)
        if value is not None and 'rowIndex' not in already_processed:
            already_processed.add('rowIndex')
            self.rowIndex = self.gds_parse_integer(value, node, 'rowIndex')
        value = find_attr_value_('columnIndex', node)
        if value is not None and 'columnIndex' not in already_processed:
            already_processed.add('columnIndex')
            self.columnIndex = self.gds_parse_integer(value, node, 'columnIndex')
        value = find_attr_value_('rowSpan', node)
        if value is not None and 'rowSpan' not in already_processed:
            already_processed.add('rowSpan')
            self.rowSpan = self.gds_parse_integer(value, node, 'rowSpan')
        value = find_attr_value_('colSpan', node)
        if value is not None and 'colSpan' not in already_processed:
            already_processed.add('colSpan')
            self.colSpan = self.gds_parse_integer(value, node, 'colSpan')
        value = find_attr_value_('header', node)
        if value is not None and 'header' not in already_processed:
            already_processed.add('header')
            if value in ('true', '1'):
                self.header = True
            elif value in ('false', '0'):
                self.header = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
    def __hash__(self):
        return hash(self.id)
# end class TableCellRoleType


class RolesType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('TableCellRole', 'TableCellRoleType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'TableCellRole', 'type': 'TableCellRoleType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, TableCellRole=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.TableCellRole = TableCellRole
        self.TableCellRole_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RolesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RolesType.subclass:
            return RolesType.subclass(*args_, **kwargs_)
        else:
            return RolesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TableCellRole(self):
        return self.TableCellRole
    def set_TableCellRole(self, TableCellRole):
        self.TableCellRole = TableCellRole
    def hasContent_(self):
        if (
            self.TableCellRole is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RolesType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RolesType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'RolesType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RolesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RolesType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='RolesType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"', name_='RolesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TableCellRole is not None:
            namespaceprefix_ = self.TableCellRole_nsprefix_ + ':' if (UseCapturedNS_ and self.TableCellRole_nsprefix_) else ''
            self.TableCellRole.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TableCellRole', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TableCellRole':
            obj_ = TableCellRoleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TableCellRole = obj_
            obj_.original_tagname_ = 'TableCellRole'
    def __hash__(self):
        return hash(self.id)
# end class RolesType


class CustomRegionType(RegionType):
    """Regions containing content that is not covered
    by the default types (text, graphic, image,
    line drawing, chart, table, separator, maths,
    map, music, chem, advert, noise, unknown).
    Information on the type of content represented by this region"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('type_', 'string', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(CustomRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CustomRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CustomRegionType.subclass:
            return CustomRegionType.subclass(*args_, **kwargs_)
        else:
            return CustomRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def hasContent_(self):
        if (
            super(CustomRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CustomRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CustomRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CustomRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CustomRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CustomRegionType'):
        super(CustomRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CustomRegionType')
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CustomRegionType', fromsubclass_=False, pretty_print=True):
        super(CustomRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
        super(CustomRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(CustomRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
# end class CustomRegionType


class UnknownRegionType(RegionType):
    """To be used if the region type cannot be ascertained."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(UnknownRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, UnknownRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if UnknownRegionType.subclass:
            return UnknownRegionType.subclass(*args_, **kwargs_)
        else:
            return UnknownRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def hasContent_(self):
        if (
            super(UnknownRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='UnknownRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('UnknownRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'UnknownRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnknownRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='UnknownRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='UnknownRegionType'):
        super(UnknownRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='UnknownRegionType')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='UnknownRegionType', fromsubclass_=False, pretty_print=True):
        super(UnknownRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(UnknownRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(UnknownRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
# end class UnknownRegionType


class NoiseRegionType(RegionType):
    """Noise regions are regions where no real data lies, only
    false data created by artifacts on the document or
    scanner noise."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(NoiseRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NoiseRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NoiseRegionType.subclass:
            return NoiseRegionType.subclass(*args_, **kwargs_)
        else:
            return NoiseRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def hasContent_(self):
        if (
            super(NoiseRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoiseRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('NoiseRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'NoiseRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NoiseRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='NoiseRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='NoiseRegionType'):
        super(NoiseRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='NoiseRegionType')
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='NoiseRegionType', fromsubclass_=False, pretty_print=True):
        super(NoiseRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(NoiseRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(NoiseRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
# end class NoiseRegionType


class AdvertRegionType(RegionType):
    """Regions containing advertisements.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The background colour of the region"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, bgColour=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(AdvertRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AdvertRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AdvertRegionType.subclass:
            return AdvertRegionType.subclass(*args_, **kwargs_)
        else:
            return AdvertRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(AdvertRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AdvertRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AdvertRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'AdvertRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdvertRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AdvertRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='AdvertRegionType'):
        super(AdvertRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AdvertRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='AdvertRegionType', fromsubclass_=False, pretty_print=True):
        super(AdvertRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        super(AdvertRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(AdvertRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class AdvertRegionType


class MusicRegionType(RegionType):
    """Regions containing musical notations.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The background colour of the region"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, bgColour=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(MusicRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MusicRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MusicRegionType.subclass:
            return MusicRegionType.subclass(*args_, **kwargs_)
        else:
            return MusicRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(MusicRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MusicRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MusicRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MusicRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MusicRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MusicRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MusicRegionType'):
        super(MusicRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MusicRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MusicRegionType', fromsubclass_=False, pretty_print=True):
        super(MusicRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        super(MusicRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(MusicRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class MusicRegionType


class MapRegionType(RegionType):
    """Regions containing maps.
    The angle the rectangle encapsulating a
    region has to be rotated in clockwise
    direction in order to correct the present
    skew (negative values indicate
    anti-clockwise rotation). Range:
    -179.999,180"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(MapRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MapRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MapRegionType.subclass:
            return MapRegionType.subclass(*args_, **kwargs_)
        else:
            return MapRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def hasContent_(self):
        if (
            super(MapRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MapRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MapRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MapRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MapRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MapRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MapRegionType'):
        super(MapRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MapRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MapRegionType', fromsubclass_=False, pretty_print=True):
        super(MapRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        super(MapRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(MapRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class MapRegionType


class ChemRegionType(RegionType):
    """Regions containing chemical formulas.
    The angle the rectangle encapsulating a
    region has to be rotated in clockwise
    direction in order to correct the present
    skew (negative values indicate
    anti-clockwise rotation). Range:
    -179.999,180
    The background colour of the region"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, bgColour=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(ChemRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChemRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChemRegionType.subclass:
            return ChemRegionType.subclass(*args_, **kwargs_)
        else:
            return ChemRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(ChemRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChemRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChemRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChemRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChemRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChemRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChemRegionType'):
        super(ChemRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChemRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChemRegionType', fromsubclass_=False, pretty_print=True):
        super(ChemRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        super(ChemRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ChemRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class ChemRegionType


class MathsRegionType(RegionType):
    """Regions containing equations and mathematical symbols
    should be marked as maths regions.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The background colour of the region"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, bgColour=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(MathsRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MathsRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MathsRegionType.subclass:
            return MathsRegionType.subclass(*args_, **kwargs_)
        else:
            return MathsRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(MathsRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MathsRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MathsRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'MathsRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MathsRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MathsRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MathsRegionType'):
        super(MathsRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MathsRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='MathsRegionType', fromsubclass_=False, pretty_print=True):
        super(MathsRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        super(MathsRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(MathsRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class MathsRegionType


class SeparatorRegionType(RegionType):
    """Separators are lines that lie between columns and
    paragraphs and can be used to logically separate
    different articles from each other.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The colour of the separator"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('colour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, colour=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(SeparatorRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.colour = _cast(None, colour)
        self.colour_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SeparatorRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SeparatorRegionType.subclass:
            return SeparatorRegionType.subclass(*args_, **kwargs_)
        else:
            return SeparatorRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_colour(self):
        return self.colour
    def set_colour(self, colour):
        self.colour = colour
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(SeparatorRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SeparatorRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SeparatorRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SeparatorRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SeparatorRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SeparatorRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SeparatorRegionType'):
        super(SeparatorRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SeparatorRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.colour is not None and 'colour' not in already_processed:
            already_processed.add('colour')
            outfile.write(' colour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.colour), input_name='colour')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SeparatorRegionType', fromsubclass_=False, pretty_print=True):
        super(SeparatorRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('colour', node)
        if value is not None and 'colour' not in already_processed:
            already_processed.add('colour')
            self.colour = value
            self.validate_ColourSimpleType(self.colour)    # validate type ColourSimpleType
        super(SeparatorRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(SeparatorRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class SeparatorRegionType


class ChartRegionType(RegionType):
    """Regions containing charts or graphs of any type, should
    be marked as chart regions.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The type of chart in the region
    An approximation of the number of colours
    used in the region
    The background colour of the region
    Specifies whether the region also contains
    text"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:ChartTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('numColours', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('embText', 'boolean', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, type_=None, numColours=None, bgColour=None, embText=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(ChartRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.numColours = _cast(int, numColours)
        self.numColours_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
        self.embText = _cast(bool, embText)
        self.embText_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChartRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChartRegionType.subclass:
            return ChartRegionType.subclass(*args_, **kwargs_)
        else:
            return ChartRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_numColours(self):
        return self.numColours
    def set_numColours(self, numColours):
        self.numColours = numColours
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def get_embText(self):
        return self.embText
    def set_embText(self, embText):
        self.embText = embText
    def validate_ChartTypeSimpleType(self, value):
        # Validate type pc:ChartTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['bar', 'line', 'pie', 'scatter', 'surface', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ChartTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(ChartRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChartRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ChartRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ChartRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChartRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ChartRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ChartRegionType'):
        super(ChartRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ChartRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.numColours is not None and 'numColours' not in already_processed:
            already_processed.add('numColours')
            outfile.write(' numColours="%s"' % self.gds_format_integer(self.numColours, input_name='numColours'))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
        if self.embText is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            outfile.write(' embText="%s"' % self.gds_format_boolean(self.embText, input_name='embText'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ChartRegionType', fromsubclass_=False, pretty_print=True):
        super(ChartRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_ChartTypeSimpleType(self.type_)    # validate type ChartTypeSimpleType
        value = find_attr_value_('numColours', node)
        if value is not None and 'numColours' not in already_processed:
            already_processed.add('numColours')
            self.numColours = self.gds_parse_integer(value, node, 'numColours')
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        value = find_attr_value_('embText', node)
        if value is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            if value in ('true', '1'):
                self.embText = True
            elif value in ('false', '0'):
                self.embText = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(ChartRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ChartRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class ChartRegionType


class TableRegionType(RegionType):
    """Tabular data in any form is represented with a table
    region. Rows and columns may or may not have separator
    lines; these lines are not separator regions.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The number of rows present in the table
    The number of columns present in the table
    The colour of the lines used in the region
    The background colour of the region
    Specifies the presence of line separators
    Specifies whether the region also contains
    text"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('rows', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('columns', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('lineColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('lineSeparators', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('embText', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('Grid', 'GridType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'Grid', 'type': 'GridType'}, None),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, rows=None, columns=None, lineColour=None, bgColour=None, lineSeparators=None, embText=None, Grid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(TableRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.rows = _cast(int, rows)
        self.rows_nsprefix_ = "pc"
        self.columns = _cast(int, columns)
        self.columns_nsprefix_ = "pc"
        self.lineColour = _cast(None, lineColour)
        self.lineColour_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
        self.lineSeparators = _cast(bool, lineSeparators)
        self.lineSeparators_nsprefix_ = "pc"
        self.embText = _cast(bool, embText)
        self.embText_nsprefix_ = "pc"
        self.Grid = Grid
        self.Grid_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TableRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TableRegionType.subclass:
            return TableRegionType.subclass(*args_, **kwargs_)
        else:
            return TableRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_Grid(self):
        return self.Grid
    def set_Grid(self, Grid):
        self.Grid = Grid
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_rows(self):
        return self.rows
    def set_rows(self, rows):
        self.rows = rows
    def get_columns(self):
        return self.columns
    def set_columns(self, columns):
        self.columns = columns
    def get_lineColour(self):
        return self.lineColour
    def set_lineColour(self, lineColour):
        self.lineColour = lineColour
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def get_lineSeparators(self):
        return self.lineSeparators
    def set_lineSeparators(self, lineSeparators):
        self.lineSeparators = lineSeparators
    def get_embText(self):
        return self.embText
    def set_embText(self, embText):
        self.embText = embText
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.Grid is not None or
            super(TableRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TableRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TableRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TableRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TableRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TableRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TableRegionType'):
        super(TableRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TableRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.rows is not None and 'rows' not in already_processed:
            already_processed.add('rows')
            outfile.write(' rows="%s"' % self.gds_format_integer(self.rows, input_name='rows'))
        if self.columns is not None and 'columns' not in already_processed:
            already_processed.add('columns')
            outfile.write(' columns="%s"' % self.gds_format_integer(self.columns, input_name='columns'))
        if self.lineColour is not None and 'lineColour' not in already_processed:
            already_processed.add('lineColour')
            outfile.write(' lineColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lineColour), input_name='lineColour')), ))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
        if self.lineSeparators is not None and 'lineSeparators' not in already_processed:
            already_processed.add('lineSeparators')
            outfile.write(' lineSeparators="%s"' % self.gds_format_boolean(self.lineSeparators, input_name='lineSeparators'))
        if self.embText is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            outfile.write(' embText="%s"' % self.gds_format_boolean(self.embText, input_name='embText'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TableRegionType', fromsubclass_=False, pretty_print=True):
        super(TableRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Grid is not None:
            namespaceprefix_ = self.Grid_nsprefix_ + ':' if (UseCapturedNS_ and self.Grid_nsprefix_) else ''
            self.Grid.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Grid', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('rows', node)
        if value is not None and 'rows' not in already_processed:
            already_processed.add('rows')
            self.rows = self.gds_parse_integer(value, node, 'rows')
        value = find_attr_value_('columns', node)
        if value is not None and 'columns' not in already_processed:
            already_processed.add('columns')
            self.columns = self.gds_parse_integer(value, node, 'columns')
        value = find_attr_value_('lineColour', node)
        if value is not None and 'lineColour' not in already_processed:
            already_processed.add('lineColour')
            self.lineColour = value
            self.validate_ColourSimpleType(self.lineColour)    # validate type ColourSimpleType
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        value = find_attr_value_('lineSeparators', node)
        if value is not None and 'lineSeparators' not in already_processed:
            already_processed.add('lineSeparators')
            if value in ('true', '1'):
                self.lineSeparators = True
            elif value in ('false', '0'):
                self.lineSeparators = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('embText', node)
        if value is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            if value in ('true', '1'):
                self.embText = True
            elif value in ('false', '0'):
                self.embText = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(TableRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Grid':
            obj_ = GridType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Grid = obj_
            obj_.original_tagname_ = 'Grid'
        super(TableRegionType, self).buildChildren(child_, node, nodeName_, True)
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class TableRegionType


class GraphicRegionType(RegionType):
    """Regions containing simple graphics, such as a company
    logo, should be marked as graphic regions.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The type of graphic in the region
    An approximation of the number of colours
    used in the region
    Specifies whether the region also contains
    text."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:GraphicsTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('numColours', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('embText', 'boolean', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, type_=None, numColours=None, embText=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(GraphicRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.numColours = _cast(int, numColours)
        self.numColours_nsprefix_ = "pc"
        self.embText = _cast(bool, embText)
        self.embText_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GraphicRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GraphicRegionType.subclass:
            return GraphicRegionType.subclass(*args_, **kwargs_)
        else:
            return GraphicRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_numColours(self):
        return self.numColours
    def set_numColours(self, numColours):
        self.numColours = numColours
    def get_embText(self):
        return self.embText
    def set_embText(self, embText):
        self.embText = embText
    def validate_GraphicsTypeSimpleType(self, value):
        # Validate type pc:GraphicsTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['logo', 'letterhead', 'decoration', 'frame', 'handwritten-annotation', 'stamp', 'signature', 'barcode', 'paper-grow', 'punch-hole', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on GraphicsTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(GraphicRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GraphicRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GraphicRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'GraphicRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphicRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GraphicRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GraphicRegionType'):
        super(GraphicRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GraphicRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.numColours is not None and 'numColours' not in already_processed:
            already_processed.add('numColours')
            outfile.write(' numColours="%s"' % self.gds_format_integer(self.numColours, input_name='numColours'))
        if self.embText is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            outfile.write(' embText="%s"' % self.gds_format_boolean(self.embText, input_name='embText'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='GraphicRegionType', fromsubclass_=False, pretty_print=True):
        super(GraphicRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_GraphicsTypeSimpleType(self.type_)    # validate type GraphicsTypeSimpleType
        value = find_attr_value_('numColours', node)
        if value is not None and 'numColours' not in already_processed:
            already_processed.add('numColours')
            self.numColours = self.gds_parse_integer(value, node, 'numColours')
        value = find_attr_value_('embText', node)
        if value is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            if value in ('true', '1'):
                self.embText = True
            elif value in ('false', '0'):
                self.embText = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(GraphicRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(GraphicRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class GraphicRegionType


class LineDrawingRegionType(RegionType):
    """A line drawing is a single colour illustration without
    solid areas.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The pen (foreground) colour of the region
    The background colour of the region
    Specifies whether the region also contains
    text"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('penColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('embText', 'boolean', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, penColour=None, bgColour=None, embText=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(LineDrawingRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.penColour = _cast(None, penColour)
        self.penColour_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
        self.embText = _cast(bool, embText)
        self.embText_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, LineDrawingRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if LineDrawingRegionType.subclass:
            return LineDrawingRegionType.subclass(*args_, **kwargs_)
        else:
            return LineDrawingRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_penColour(self):
        return self.penColour
    def set_penColour(self, penColour):
        self.penColour = penColour
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def get_embText(self):
        return self.embText
    def set_embText(self, embText):
        self.embText = embText
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(LineDrawingRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LineDrawingRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('LineDrawingRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'LineDrawingRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineDrawingRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='LineDrawingRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='LineDrawingRegionType'):
        super(LineDrawingRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='LineDrawingRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.penColour is not None and 'penColour' not in already_processed:
            already_processed.add('penColour')
            outfile.write(' penColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.penColour), input_name='penColour')), ))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
        if self.embText is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            outfile.write(' embText="%s"' % self.gds_format_boolean(self.embText, input_name='embText'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='LineDrawingRegionType', fromsubclass_=False, pretty_print=True):
        super(LineDrawingRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('penColour', node)
        if value is not None and 'penColour' not in already_processed:
            already_processed.add('penColour')
            self.penColour = value
            self.validate_ColourSimpleType(self.penColour)    # validate type ColourSimpleType
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        value = find_attr_value_('embText', node)
        if value is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            if value in ('true', '1'):
                self.embText = True
            elif value in ('false', '0'):
                self.embText = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(LineDrawingRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(LineDrawingRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class LineDrawingRegionType


class ImageRegionType(RegionType):
    """An image is considered to be more intricate and complex
    than a graphic. These can be photos or drawings.
    The angle the rectangle encapsulating a region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    The colour bit depth required for the region
    The background colour of the region
    Specifies whether the region also contains
    text"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('colourDepth', 'pc:ColourDepthSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('bgColour', 'pc:ColourSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('embText', 'boolean', 0, 1, {'use': 'optional'}),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, colourDepth=None, bgColour=None, embText=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(ImageRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.colourDepth = _cast(None, colourDepth)
        self.colourDepth_nsprefix_ = "pc"
        self.bgColour = _cast(None, bgColour)
        self.bgColour_nsprefix_ = "pc"
        self.embText = _cast(bool, embText)
        self.embText_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ImageRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ImageRegionType.subclass:
            return ImageRegionType.subclass(*args_, **kwargs_)
        else:
            return ImageRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_colourDepth(self):
        return self.colourDepth
    def set_colourDepth(self, colourDepth):
        self.colourDepth = colourDepth
    def get_bgColour(self):
        return self.bgColour
    def set_bgColour(self, bgColour):
        self.bgColour = bgColour
    def get_embText(self):
        return self.embText
    def set_embText(self, embText):
        self.embText = embText
    def validate_ColourDepthSimpleType(self, value):
        # Validate type pc:ColourDepthSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['bilevel', 'greyscale', 'colour', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourDepthSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ColourSimpleType(self, value):
        # Validate type pc:ColourSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['black', 'blue', 'brown', 'cyan', 'green', 'grey', 'indigo', 'magenta', 'orange', 'pink', 'red', 'turquoise', 'violet', 'white', 'yellow', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ColourSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            super(ImageRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ImageRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ImageRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ImageRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ImageRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ImageRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ImageRegionType'):
        super(ImageRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ImageRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.colourDepth is not None and 'colourDepth' not in already_processed:
            already_processed.add('colourDepth')
            outfile.write(' colourDepth=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.colourDepth), input_name='colourDepth')), ))
        if self.bgColour is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            outfile.write(' bgColour=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.bgColour), input_name='bgColour')), ))
        if self.embText is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            outfile.write(' embText="%s"' % self.gds_format_boolean(self.embText, input_name='embText'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='ImageRegionType', fromsubclass_=False, pretty_print=True):
        super(ImageRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('colourDepth', node)
        if value is not None and 'colourDepth' not in already_processed:
            already_processed.add('colourDepth')
            self.colourDepth = value
            self.validate_ColourDepthSimpleType(self.colourDepth)    # validate type ColourDepthSimpleType
        value = find_attr_value_('bgColour', node)
        if value is not None and 'bgColour' not in already_processed:
            already_processed.add('bgColour')
            self.bgColour = value
            self.validate_ColourSimpleType(self.bgColour)    # validate type ColourSimpleType
        value = find_attr_value_('embText', node)
        if value is not None and 'embText' not in already_processed:
            already_processed.add('embText')
            if value in ('true', '1'):
                self.embText = True
            elif value in ('false', '0'):
                self.embText = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(ImageRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(ImageRegionType, self).buildChildren(child_, node, nodeName_, True)
        pass
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class ImageRegionType


class TextRegionType(RegionType):
    """Pure text is represented as a text region. This includes
    drop capitals, but practically ornate text may be
    considered as a graphic.
    The angle the rectangle encapsulating the region
    has to be rotated in clockwise direction
    in order to correct the present skew
    (negative values indicate anti-clockwise rotation).
    (The rotated image can be further referenced
    via “AlternativeImage”.)
    Range: -179.999,180
    The nature of the text in the region
    The degree of space in points between the lines of
    text (line spacing)
    The direction in which text within lines
    should be read (order of words and characters),
    in addition to “textLineOrder”.
    The order of text lines within the block,
    in addition to “readingDirection”.
    The angle the baseline of text within the region
    has to be rotated (relative to the rectangle
    encapsulating the region) in clockwise direction
    in order to correct the present skew,
    in addition to “orientation”
    (negative values indicate anti-clockwise rotation).
    Range: -179.999,180
    Defines whether a region of text is indented or not
    Text align
    The primary language used in the region
    The secondary language used in the region
    The primary script used in the region
    The secondary script used in the region"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('orientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('type_', 'pc:TextTypeSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('leading', 'int', 0, 1, {'use': 'optional'}),
        MemberSpec_('readingDirection', 'pc:ReadingDirectionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('textLineOrder', 'pc:TextLineOrderSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('readingOrientation', 'float', 0, 1, {'use': 'optional'}),
        MemberSpec_('indented', 'boolean', 0, 1, {'use': 'optional'}),
        MemberSpec_('align', 'pc:AlignSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('primaryLanguage', 'pc:LanguageSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('secondaryLanguage', 'pc:LanguageSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('primaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('secondaryScript', 'pc:ScriptSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('production', 'pc:ProductionSimpleType', 0, 1, {'use': 'optional'}),
        MemberSpec_('TextLine', 'TextLineType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'TextLine', 'type': 'TextLineType'}, None),
        MemberSpec_('TextEquiv', 'TextEquivType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'TextEquiv', 'type': 'TextEquivType'}, None),
        MemberSpec_('TextStyle', 'TextStyleType', 0, 1, {'maxOccurs': '1', 'minOccurs': '0', 'name': 'TextStyle', 'type': 'TextStyleType'}, None),
    ]
    subclass = None
    superclass = RegionType
    def __init__(self, id=None, custom=None, comments=None, continuation=None, AlternativeImage=None, Coords=None, UserDefined=None, Labels=None, Roles=None, TextRegion=None, ImageRegion=None, LineDrawingRegion=None, GraphicRegion=None, TableRegion=None, ChartRegion=None, SeparatorRegion=None, MathsRegion=None, ChemRegion=None, MusicRegion=None, AdvertRegion=None, NoiseRegion=None, UnknownRegion=None, CustomRegion=None, orientation=None, type_=None, leading=None, readingDirection=None, textLineOrder=None, readingOrientation=None, indented=None, align=None, primaryLanguage=None, secondaryLanguage=None, primaryScript=None, secondaryScript=None, production=None, TextLine=None, TextEquiv=None, TextStyle=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(TextRegionType, self).__init__(id, custom, comments, continuation, AlternativeImage, Coords, UserDefined, Labels, Roles, TextRegion, ImageRegion, LineDrawingRegion, GraphicRegion, TableRegion, ChartRegion, SeparatorRegion, MathsRegion, ChemRegion, MusicRegion, AdvertRegion, NoiseRegion, UnknownRegion, CustomRegion,  **kwargs_)
        self.orientation = _cast(float, orientation)
        self.orientation_nsprefix_ = "pc"
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = "pc"
        self.leading = _cast(int, leading)
        self.leading_nsprefix_ = "pc"
        self.readingDirection = _cast(None, readingDirection)
        self.readingDirection_nsprefix_ = "pc"
        self.textLineOrder = _cast(None, textLineOrder)
        self.textLineOrder_nsprefix_ = "pc"
        self.readingOrientation = _cast(float, readingOrientation)
        self.readingOrientation_nsprefix_ = "pc"
        self.indented = _cast(bool, indented)
        self.indented_nsprefix_ = "pc"
        self.align = _cast(None, align)
        self.align_nsprefix_ = "pc"
        self.primaryLanguage = _cast(None, primaryLanguage)
        self.primaryLanguage_nsprefix_ = "pc"
        self.secondaryLanguage = _cast(None, secondaryLanguage)
        self.secondaryLanguage_nsprefix_ = "pc"
        self.primaryScript = _cast(None, primaryScript)
        self.primaryScript_nsprefix_ = "pc"
        self.secondaryScript = _cast(None, secondaryScript)
        self.secondaryScript_nsprefix_ = "pc"
        self.production = _cast(None, production)
        self.production_nsprefix_ = "pc"
        if TextLine is None:
            self.TextLine = []
        else:
            self.TextLine = TextLine
        self.TextLine_nsprefix_ = "pc"
        if TextEquiv is None:
            self.TextEquiv = []
        else:
            self.TextEquiv = TextEquiv
        self.TextEquiv_nsprefix_ = "pc"
        self.TextStyle = TextStyle
        self.TextStyle_nsprefix_ = "pc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TextRegionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TextRegionType.subclass:
            return TextRegionType.subclass(*args_, **kwargs_)
        else:
            return TextRegionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_TextLine(self):
        return self.TextLine
    def set_TextLine(self, TextLine):
        self.TextLine = TextLine
    def add_TextLine(self, value):
        self.TextLine.append(value)
    def insert_TextLine_at(self, index, value):
        self.TextLine.insert(index, value)
    def replace_TextLine_at(self, index, value):
        self.TextLine[index] = value
    def get_TextEquiv(self):
        return self.TextEquiv
    def set_TextEquiv(self, TextEquiv):
        self.TextEquiv = TextEquiv
    def add_TextEquiv(self, value):
        self.TextEquiv.append(value)
    def insert_TextEquiv_at(self, index, value):
        self.TextEquiv.insert(index, value)
    def replace_TextEquiv_at(self, index, value):
        self.TextEquiv[index] = value
    def get_TextStyle(self):
        return self.TextStyle
    def set_TextStyle(self, TextStyle):
        self.TextStyle = TextStyle
    def get_orientation(self):
        return self.orientation
    def set_orientation(self, orientation):
        self.orientation = orientation
    def get_type(self):
        return self.type_
    def set_type(self, type_):
        self.type_ = type_
    def get_leading(self):
        return self.leading
    def set_leading(self, leading):
        self.leading = leading
    def get_readingDirection(self):
        return self.readingDirection
    def set_readingDirection(self, readingDirection):
        self.readingDirection = readingDirection
    def get_textLineOrder(self):
        return self.textLineOrder
    def set_textLineOrder(self, textLineOrder):
        self.textLineOrder = textLineOrder
    def get_readingOrientation(self):
        return self.readingOrientation
    def set_readingOrientation(self, readingOrientation):
        self.readingOrientation = readingOrientation
    def get_indented(self):
        return self.indented
    def set_indented(self, indented):
        self.indented = indented
    def get_align(self):
        return self.align
    def set_align(self, align):
        self.align = align
    def get_primaryLanguage(self):
        return self.primaryLanguage
    def set_primaryLanguage(self, primaryLanguage):
        self.primaryLanguage = primaryLanguage
    def get_secondaryLanguage(self):
        return self.secondaryLanguage
    def set_secondaryLanguage(self, secondaryLanguage):
        self.secondaryLanguage = secondaryLanguage
    def get_primaryScript(self):
        return self.primaryScript
    def set_primaryScript(self, primaryScript):
        self.primaryScript = primaryScript
    def get_secondaryScript(self):
        return self.secondaryScript
    def set_secondaryScript(self, secondaryScript):
        self.secondaryScript = secondaryScript
    def get_production(self):
        return self.production
    def set_production(self, production):
        self.production = production
    def validate_TextTypeSimpleType(self, value):
        # Validate type pc:TextTypeSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['paragraph', 'heading', 'caption', 'header', 'footer', 'page-number', 'drop-capital', 'credit', 'floating', 'signature-mark', 'catch-word', 'marginalia', 'footnote', 'footnote-continued', 'endnote', 'TOC-entry', 'list-label', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TextTypeSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ReadingDirectionSimpleType(self, value):
        # Validate type pc:ReadingDirectionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['left-to-right', 'right-to-left', 'top-to-bottom', 'bottom-to-top']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ReadingDirectionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TextLineOrderSimpleType(self, value):
        # Validate type pc:TextLineOrderSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['top-to-bottom', 'bottom-to-top', 'left-to-right', 'right-to-left']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TextLineOrderSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_AlignSimpleType(self, value):
        # Validate type pc:AlignSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['left', 'centre', 'right', 'justify']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on AlignSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_LanguageSimpleType(self, value):
        # Validate type pc:LanguageSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Abkhaz', 'Afar', 'Afrikaans', 'Akan', 'Albanian', 'Amharic', 'Arabic', 'Aragonese', 'Armenian', 'Assamese', 'Avaric', 'Avestan', 'Aymara', 'Azerbaijani', 'Bambara', 'Bashkir', 'Basque', 'Belarusian', 'Bengali', 'Bihari', 'Bislama', 'Bosnian', 'Breton', 'Bulgarian', 'Burmese', 'Cambodian', 'Cantonese', 'Catalan', 'Chamorro', 'Chechen', 'Chichewa', 'Chinese', 'Chuvash', 'Cornish', 'Corsican', 'Cree', 'Croatian', 'Czech', 'Danish', 'Divehi', 'Dutch', 'Dzongkha', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Faroese', 'Fijian', 'Finnish', 'French', 'Fula', 'Gaelic', 'Galician', 'Ganda', 'Georgian', 'German', 'Greek', 'Guaraní', 'Gujarati', 'Haitian', 'Hausa', 'Hebrew', 'Herero', 'Hindi', 'Hiri Motu', 'Hungarian', 'Icelandic', 'Ido', 'Igbo', 'Indonesian', 'Interlingua', 'Interlingue', 'Inuktitut', 'Inupiaq', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kalaallisut', 'Kannada', 'Kanuri', 'Kashmiri', 'Kazakh', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kirundi', 'Komi', 'Kongo', 'Korean', 'Kurdish', 'Kwanyama', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Limburgish', 'Lingala', 'Lithuanian', 'Luba-Katanga', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Manx', 'Māori', 'Marathi', 'Marshallese', 'Mongolian', 'Nauru', 'Navajo', 'Ndonga', 'Nepali', 'North Ndebele', 'Northern Sami', 'Norwegian', 'Norwegian Bokmål', 'Norwegian Nynorsk', 'Nuosu', 'Occitan', 'Ojibwe', 'Old Church Slavonic', 'Oriya', 'Oromo', 'Ossetian', 'Pāli', 'Panjabi', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 'Quechua', 'Romanian', 'Romansh', 'Russian', 'Samoan', 'Sango', 'Sanskrit', 'Sardinian', 'Serbian', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovene', 'Somali', 'South Ndebele', 'Southern Sotho', 'Spanish', 'Sundanese', 'Swahili', 'Swati', 'Swedish', 'Tagalog', 'Tahitian', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Tibetan', 'Tigrinya', 'Tonga', 'Tsonga', 'Tswana', 'Turkish', 'Turkmen', 'Twi', 'Uighur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda', 'Vietnamese', 'Volapük', 'Walloon', 'Welsh', 'Western Frisian', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zhuang', 'Zulu', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on LanguageSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ScriptSimpleType(self, value):
        # Validate type pc:ScriptSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Adlm - Adlam', 'Afak - Afaka', 'Aghb - Caucasian Albanian', 'Ahom - Ahom, Tai Ahom', 'Arab - Arabic', 'Aran - Arabic (Nastaliq variant)', 'Armi - Imperial Aramaic', 'Armn - Armenian', 'Avst - Avestan', 'Bali - Balinese', 'Bamu - Bamum', 'Bass - Bassa Vah', 'Batk - Batak', 'Beng - Bengali', 'Bhks - Bhaiksuki', 'Blis - Blissymbols', 'Bopo - Bopomofo', 'Brah - Brahmi', 'Brai - Braille', 'Bugi - Buginese', 'Buhd - Buhid', 'Cakm - Chakma', 'Cans - Unified Canadian Aboriginal Syllabics', 'Cari - Carian', 'Cham - Cham', 'Cher - Cherokee', 'Cirt - Cirth', 'Copt - Coptic', 'Cprt - Cypriot', 'Cyrl - Cyrillic', 'Cyrs - Cyrillic (Old Church Slavonic variant)', 'Deva - Devanagari (Nagari)', 'Dsrt - Deseret (Mormon)', 'Dupl - Duployan shorthand, Duployan stenography', 'Egyd - Egyptian demotic', 'Egyh - Egyptian hieratic', 'Egyp - Egyptian hieroglyphs', 'Elba - Elbasan', 'Ethi - Ethiopic', 'Geok - Khutsuri (Asomtavruli and Nuskhuri)', 'Geor - Georgian (Mkhedruli)', 'Glag - Glagolitic', 'Goth - Gothic', 'Gran - Grantha', 'Grek - Greek', 'Gujr - Gujarati', 'Guru - Gurmukhi', 'Hanb - Han with Bopomofo', 'Hang - Hangul', 'Hani - Han (Hanzi, Kanji, Hanja)', 'Hano - Hanunoo (Hanunóo)', 'Hans - Han (Simplified variant)', 'Hant - Han (Traditional variant)', 'Hatr - Hatran', 'Hebr - Hebrew', 'Hira - Hiragana', 'Hluw - Anatolian Hieroglyphs', 'Hmng - Pahawh Hmong', 'Hrkt - Japanese syllabaries', 'Hung - Old Hungarian (Hungarian Runic)', 'Inds - Indus (Harappan)', 'Ital - Old Italic (Etruscan, Oscan etc.)', 'Jamo - Jamo', 'Java - Javanese', 'Jpan - Japanese', 'Jurc - Jurchen', 'Kali - Kayah Li', 'Kana - Katakana', 'Khar - Kharoshthi', 'Khmr - Khmer', 'Khoj - Khojki', 'Kitl - Khitan large script', 'Kits - Khitan small script', 'Knda - Kannada', 'Kore - Korean (alias for Hangul + Han)', 'Kpel - Kpelle', 'Kthi - Kaithi', 'Lana - Tai Tham (Lanna)', 'Laoo - Lao', 'Latf - Latin (Fraktur variant)', 'Latg - Latin (Gaelic variant)', 'Latn - Latin', 'Leke - Leke', 'Lepc - Lepcha (Róng)', 'Limb - Limbu', 'Lina - Linear A', 'Linb - Linear B', 'Lisu - Lisu (Fraser)', 'Loma - Loma', 'Lyci - Lycian', 'Lydi - Lydian', 'Mahj - Mahajani', 'Mand - Mandaic, Mandaean', 'Mani - Manichaean', 'Marc - Marchen', 'Maya - Mayan hieroglyphs', 'Mend - Mende Kikakui', 'Merc - Meroitic Cursive', 'Mero - Meroitic Hieroglyphs', 'Mlym - Malayalam', 'Modi - Modi, Moḍī', 'Mong - Mongolian', 'Moon - Moon (Moon code, Moon script, Moon type)', 'Mroo - Mro, Mru', 'Mtei - Meitei Mayek (Meithei, Meetei)', 'Mult - Multani', 'Mymr - Myanmar (Burmese)', 'Narb - Old North Arabian (Ancient North Arabian)', 'Nbat - Nabataean', 'Newa - Newa, Newar, Newari', 'Nkgb - Nakhi Geba', 'Nkoo - N’Ko', 'Nshu - Nüshu', 'Ogam - Ogham', 'Olck - Ol Chiki (Ol Cemet’, Ol, Santali)', 'Orkh - Old Turkic, Orkhon Runic', 'Orya - Oriya', 'Osge - Osage', 'Osma - Osmanya', 'Palm - Palmyrene', 'Pauc - Pau Cin Hau', 'Perm - Old Permic', 'Phag - Phags-pa', 'Phli - Inscriptional Pahlavi', 'Phlp - Psalter Pahlavi', 'Phlv - Book Pahlavi', 'Phnx - Phoenician', 'Piqd - Klingon (KLI pIqaD)', 'Plrd - Miao (Pollard)', 'Prti - Inscriptional Parthian', 'Rjng - Rejang (Redjang, Kaganga)', 'Roro - Rongorongo', 'Runr - Runic', 'Samr - Samaritan', 'Sara - Sarati', 'Sarb - Old South Arabian', 'Saur - Saurashtra', 'Sgnw - SignWriting', 'Shaw - Shavian (Shaw)', 'Shrd - Sharada, Śāradā', 'Sidd - Siddham', 'Sind - Khudawadi, Sindhi', 'Sinh - Sinhala', 'Sora - Sora Sompeng', 'Sund - Sundanese', 'Sylo - Syloti Nagri', 'Syrc - Syriac', 'Syre - Syriac (Estrangelo variant)', 'Syrj - Syriac (Western variant)', 'Syrn - Syriac (Eastern variant)', 'Tagb - Tagbanwa', 'Takr - Takri', 'Tale - Tai Le', 'Talu - New Tai Lue', 'Taml - Tamil', 'Tang - Tangut', 'Tavt - Tai Viet', 'Telu - Telugu', 'Teng - Tengwar', 'Tfng - Tifinagh (Berber)', 'Tglg - Tagalog (Baybayin, Alibata)', 'Thaa - Thaana', 'Thai - Thai', 'Tibt - Tibetan', 'Tirh - Tirhuta', 'Ugar - Ugaritic', 'Vaii - Vai', 'Visp - Visible Speech', 'Wara - Warang Citi (Varang Kshiti)', 'Wole - Woleai', 'Xpeo - Old Persian', 'Xsux - Cuneiform, Sumero-Akkadian', 'Yiii - Yi', 'Zinh - Code for inherited script', 'Zmth - Mathematical notation', 'Zsye - Symbols (Emoji variant)', 'Zsym - Symbols', 'Zxxx - Code for unwritten documents', 'Zyyy - Code for undetermined script', 'Zzzz - Code for uncoded script', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ScriptSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ProductionSimpleType(self, value):
        # Validate type pc:ProductionSimpleType, a restriction on string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['printed', 'typewritten', 'handwritten-cursive', 'handwritten-printscript', 'medieval-manuscript', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ProductionSimpleType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.TextLine or
            self.TextEquiv or
            self.TextStyle is not None or
            super(TextRegionType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TextRegionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TextRegionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TextRegionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextRegionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TextRegionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TextRegionType'):
        super(TextRegionType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TextRegionType')
        if self.orientation is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            outfile.write(' orientation="%s"' % self.gds_format_float(self.orientation, input_name='orientation'))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.add('type_')
            outfile.write(' type=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.type_), input_name='type')), ))
        if self.leading is not None and 'leading' not in already_processed:
            already_processed.add('leading')
            outfile.write(' leading="%s"' % self.gds_format_integer(self.leading, input_name='leading'))
        if self.readingDirection is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            outfile.write(' readingDirection=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.readingDirection), input_name='readingDirection')), ))
        if self.textLineOrder is not None and 'textLineOrder' not in already_processed:
            already_processed.add('textLineOrder')
            outfile.write(' textLineOrder=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.textLineOrder), input_name='textLineOrder')), ))
        if self.readingOrientation is not None and 'readingOrientation' not in already_processed:
            already_processed.add('readingOrientation')
            outfile.write(' readingOrientation="%s"' % self.gds_format_float(self.readingOrientation, input_name='readingOrientation'))
        if self.indented is not None and 'indented' not in already_processed:
            already_processed.add('indented')
            outfile.write(' indented="%s"' % self.gds_format_boolean(self.indented, input_name='indented'))
        if self.align is not None and 'align' not in already_processed:
            already_processed.add('align')
            outfile.write(' align=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.align), input_name='align')), ))
        if self.primaryLanguage is not None and 'primaryLanguage' not in already_processed:
            already_processed.add('primaryLanguage')
            outfile.write(' primaryLanguage=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryLanguage), input_name='primaryLanguage')), ))
        if self.secondaryLanguage is not None and 'secondaryLanguage' not in already_processed:
            already_processed.add('secondaryLanguage')
            outfile.write(' secondaryLanguage=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.secondaryLanguage), input_name='secondaryLanguage')), ))
        if self.primaryScript is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            outfile.write(' primaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.primaryScript), input_name='primaryScript')), ))
        if self.secondaryScript is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            outfile.write(' secondaryScript=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.secondaryScript), input_name='secondaryScript')), ))
        if self.production is not None and 'production' not in already_processed:
            already_processed.add('production')
            outfile.write(' production=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.production), input_name='production')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TextRegionType', fromsubclass_=False, pretty_print=True):
        super(TextRegionType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TextLine_ in self.TextLine:
            namespaceprefix_ = self.TextLine_nsprefix_ + ':' if (UseCapturedNS_ and self.TextLine_nsprefix_) else ''
            TextLine_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextLine', pretty_print=pretty_print)
        for TextEquiv_ in self.TextEquiv:
            namespaceprefix_ = self.TextEquiv_nsprefix_ + ':' if (UseCapturedNS_ and self.TextEquiv_nsprefix_) else ''
            TextEquiv_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextEquiv', pretty_print=pretty_print)
        if self.TextStyle is not None:
            namespaceprefix_ = self.TextStyle_nsprefix_ + ':' if (UseCapturedNS_ and self.TextStyle_nsprefix_) else ''
            self.TextStyle.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TextStyle', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('orientation', node)
        if value is not None and 'orientation' not in already_processed:
            already_processed.add('orientation')
            value = self.gds_parse_float(value, node, 'orientation')
            self.orientation = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_TextTypeSimpleType(self.type_)    # validate type TextTypeSimpleType
        value = find_attr_value_('leading', node)
        if value is not None and 'leading' not in already_processed:
            already_processed.add('leading')
            self.leading = self.gds_parse_integer(value, node, 'leading')
        value = find_attr_value_('readingDirection', node)
        if value is not None and 'readingDirection' not in already_processed:
            already_processed.add('readingDirection')
            self.readingDirection = value
            self.validate_ReadingDirectionSimpleType(self.readingDirection)    # validate type ReadingDirectionSimpleType
        value = find_attr_value_('textLineOrder', node)
        if value is not None and 'textLineOrder' not in already_processed:
            already_processed.add('textLineOrder')
            self.textLineOrder = value
            self.validate_TextLineOrderSimpleType(self.textLineOrder)    # validate type TextLineOrderSimpleType
        value = find_attr_value_('readingOrientation', node)
        if value is not None and 'readingOrientation' not in already_processed:
            already_processed.add('readingOrientation')
            value = self.gds_parse_float(value, node, 'readingOrientation')
            self.readingOrientation = value
        value = find_attr_value_('indented', node)
        if value is not None and 'indented' not in already_processed:
            already_processed.add('indented')
            if value in ('true', '1'):
                self.indented = True
            elif value in ('false', '0'):
                self.indented = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('align', node)
        if value is not None and 'align' not in already_processed:
            already_processed.add('align')
            self.align = value
            self.validate_AlignSimpleType(self.align)    # validate type AlignSimpleType
        value = find_attr_value_('primaryLanguage', node)
        if value is not None and 'primaryLanguage' not in already_processed:
            already_processed.add('primaryLanguage')
            self.primaryLanguage = value
            self.validate_LanguageSimpleType(self.primaryLanguage)    # validate type LanguageSimpleType
        value = find_attr_value_('secondaryLanguage', node)
        if value is not None and 'secondaryLanguage' not in already_processed:
            already_processed.add('secondaryLanguage')
            self.secondaryLanguage = value
            self.validate_LanguageSimpleType(self.secondaryLanguage)    # validate type LanguageSimpleType
        value = find_attr_value_('primaryScript', node)
        if value is not None and 'primaryScript' not in already_processed:
            already_processed.add('primaryScript')
            self.primaryScript = value
            self.validate_ScriptSimpleType(self.primaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('secondaryScript', node)
        if value is not None and 'secondaryScript' not in already_processed:
            already_processed.add('secondaryScript')
            self.secondaryScript = value
            self.validate_ScriptSimpleType(self.secondaryScript)    # validate type ScriptSimpleType
        value = find_attr_value_('production', node)
        if value is not None and 'production' not in already_processed:
            already_processed.add('production')
            self.production = value
            self.validate_ProductionSimpleType(self.production)    # validate type ProductionSimpleType
        super(TextRegionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'TextLine':
            obj_ = TextLineType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextLine.append(obj_)
            obj_.original_tagname_ = 'TextLine'
        elif nodeName_ == 'TextEquiv':
            obj_ = TextEquivType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextEquiv.append(obj_)
            obj_.original_tagname_ = 'TextEquiv'
        elif nodeName_ == 'TextStyle':
            obj_ = TextStyleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TextStyle = obj_
            obj_.original_tagname_ = 'TextStyle'
        super(TextRegionType, self).buildChildren(child_, node, nodeName_, True)
    def __hash__(self):
        return hash(self.id)
    def set_orientation(self, orientation):
        """
        Set deskewing angle to given number.
        Moreover, invalidate self's AlternativeImages
        (because they will have been rotated and enlarged
         with the angle of the previous value).
        """
        if hasattr(self, 'invalidate_AlternativeImage'):
            # PageType, RegionType:
            self.invalidate_AlternativeImage(feature_selector='deskewed')
        self.orientation = orientation
# end class TextRegionType


GDSClassesMapping = {
    'PcGts': PcGtsType,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGts'
        rootClass = PcGts
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_=namespacedefs,
##             pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGts'
        rootClass = PcGts
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(str(content))
##         sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGts'
        rootClass = PcGts
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='xmlns:pc="http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'PcGts'
        rootClass = PcGts
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('#from ocrd_page_generateds import *\n\n')
##         sys.stdout.write('import ocrd_page_generateds as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

__all__ = [
    "AdvertRegionType",
    "AlternativeImageType",
    "BaselineType",
    "BorderType",
    "ChartRegionType",
    "ChemRegionType",
    "CoordsType",
    "CustomRegionType",
    "GlyphType",
    "GraphemeBaseType",
    "GraphemeGroupType",
    "GraphemeType",
    "GraphemesType",
    "GraphicRegionType",
    "GridPointsType",
    "GridType",
    "ImageRegionType",
    "LabelType",
    "LabelsType",
    "LayerType",
    "LayersType",
    "LineDrawingRegionType",
    "MapRegionType",
    "MathsRegionType",
    "MetadataItemType",
    "MetadataType",
    "MusicRegionType",
    "NoiseRegionType",
    "NonPrintingCharType",
    "OrderedGroupIndexedType",
    "OrderedGroupType",
    "PageType",
    "PcGtsType",
    "PrintSpaceType",
    "ReadingOrderType",
    "RegionRefIndexedType",
    "RegionRefType",
    "RegionType",
    "RelationType",
    "RelationsType",
    "RolesType",
    "SeparatorRegionType",
    "TableCellRoleType",
    "TableRegionType",
    "TextEquivType",
    "TextLineType",
    "TextRegionType",
    "TextStyleType",
    "UnknownRegionType",
    "UnorderedGroupIndexedType",
    "UnorderedGroupType",
    "UserAttributeType",
    "UserDefinedType",
    "WordType"
]
