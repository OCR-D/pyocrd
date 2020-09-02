from os.path import isfile
from re import match, sub, IGNORECASE
from itertools import product
import sys
from string import Template

import click

from ocrd_utils import (
    is_local_filename,
    get_local_filename,
    setOverrideLogLevel,
    parse_json_string_or_file,
    set_json_key_value_overrides,
)

from ocrd_utils import getLogger
from .resolver import Resolver
from .processor.base import run_processor
from ocrd_validators import WorkspaceValidator
from ocrd_models.ocrd_mets_filter import FIELDS

def _set_root_logger_version(ctx, param, value):    # pylint: disable=unused-argument
    setOverrideLogLevel(value)
    return value

loglevel_option = click.option('-l', '--log-level', help="Log level",
                               type=click.Choice(['OFF', 'ERROR', 'WARN', 'INFO', 'DEBUG', 'TRACE']),
                               default=None, callback=_set_root_logger_version)

def _handle_param_option(ctx, param, value):
    return parse_json_string_or_file(*list(value))

parameter_option = click.option('-p', '--parameter',
                                help="Parameters, either JSON string or path to JSON file",
                                multiple=True,
                                default=['{}'],
                                callback=_handle_param_option)

parameter_override_option = click.option('-P', '--parameter-override',
                                help="Parameter override",
                                nargs=2,
                                multiple=True,
                                callback=lambda ctx, param, kv: kv)
                                # callback=lambda ctx, param, kv: {kv[0]: kv[1]})

def ocrd_cli_wrap_processor(
    processorClass,
    ocrd_tool=None,
    mets=None,
    working_dir=None,
    dump_json=False,
    help=False, # pylint: disable=redefined-builtin
    version=False,
    overwrite=False,
    **kwargs
):
    if dump_json or help or version:
        setOverrideLogLevel('OFF', silent=True)
        processorClass(workspace=None, dump_json=dump_json, show_help=help, show_version=version)
        sys.exit()
    else:
        LOG = getLogger('ocrd_cli_wrap_processor')
        if not mets or (is_local_filename(mets) and not isfile(get_local_filename(mets))):
            processorClass(workspace=None, show_help=True)
            sys.exit(1)
        # LOG.info('kwargs=%s' % kwargs)
        # Merge parameter overrides and parameters
        if 'parameter_override' in kwargs:
            set_json_key_value_overrides(kwargs['parameter'], *kwargs['parameter_override'])
        # TODO OCR-D/core#274
        # Assert -I / -O
        # if not kwargs['input_file_grp']:
        #     raise ValueError('-I/--input-file-grp is required')
        # if not kwargs['output_file_grp']:
        #     raise ValueError('-O/--output-file-grp is required')
        if is_local_filename(mets) and not isfile(get_local_filename(mets)):
            msg = "File does not exist: %s" % mets
            LOG.error(msg)
            raise Exception(msg)
        resolver = Resolver()
        workspace = resolver.workspace_from_url(mets, working_dir)
        page_id = kwargs.get('page_id')
        # XXX not possible while processors do not adhere to # https://github.com/OCR-D/core/issues/505
        # if overwrite
        #     if 'output_file_grp' not in kwargs or not kwargs['output_file_grp']:
        #         raise Exception("--overwrite requires --output-file-grp")
        #     LOG.info("Removing files because of --overwrite")
        #     for grp in kwargs['output_file_grp'].split(','):
        #         if page_id:
        #             for one_page_id in kwargs['page_id'].split(','):
        #                 LOG.debug("Removing files in output file group %s with page ID %s", grp, one_page_id)
        #                 for file in workspace.mets.find_files(pageId=one_page_id, fileGrp=grp):
        #                     workspace.remove_file(file, force=True, keep_file=False, page_recursive=True)
        #         else:
        #             LOG.debug("Removing all files in output file group %s ", grp)
        #             # TODO: can be reduced to `page_same_group=True` as soon as core#505 has landed (in all processors)
        #             workspace.remove_file_group(grp, recursive=True, force=True, keep_files=False, page_recursive=True, page_same_group=False)
        #     workspace.save_mets()
        # XXX While https://github.com/OCR-D/core/issues/505 is open, set 'overwrite_mode' globally on the workspace
        if overwrite:
            workspace.overwrite_mode = True
        report = WorkspaceValidator.check_file_grp(workspace, kwargs['input_file_grp'], '' if overwrite else kwargs['output_file_grp'], page_id)
        if not report.is_valid:
            raise Exception("Invalid input/output file grps:\n\t%s" % '\n\t'.join(report.errors))
        run_processor(processorClass, ocrd_tool, mets, workspace=workspace, **kwargs)

def ocrd_loglevel(f):
    """
    Add an option '--log-level' to set the log level.
    """
    loglevel_option(f)
    return f

def ocrd_cli_options(f):
    """
    Implement MP CLI.

    Usage::

        import ocrd_cli_options from ocrd.utils

        @click.command()
        @ocrd_cli_options
        def cli(mets_url, **kwargs):
            print(mets_url)
    """
    params = [
        click.option('-m', '--mets', help="METS to process", default="mets.xml"),
        click.option('-w', '--working-dir', help="Working Directory"),
        # TODO OCR-D/core#274
        # click.option('-I', '--input-file-grp', help='File group(s) used as input. **required**'),
        # click.option('-O', '--output-file-grp', help='File group(s) used as output. **required**'),
        click.option('-I', '--input-file-grp', help='File group(s) used as input.', default='INPUT'),
        click.option('-O', '--output-file-grp', help='File group(s) used as output.', default='OUTPUT'),
        click.option('-g', '--page-id', help="ID(s) of the pages to process"),
        click.option('--overwrite', help="Overwrite the output file group or a page range (--page-id)", is_flag=True, default=False),
        parameter_option,
        parameter_override_option,
        click.option('-J', '--dump-json', help="Dump tool description as JSON and exit", is_flag=True, default=False),
        loglevel_option,
        click.option('-V', '--version', help="Show version", is_flag=True, default=False),
        click.option('-h', '--help', help="This help message", is_flag=True, default=False),
    ]
    for param in params:
        param(f)
    return f

TEMPLATE_DEFAULTS = {
    'metavar':        'PAT',
    'required':       False,
    'parameter':      '${field}_${operator}clude',
    'help':           '${field} ${operation} ${type}',
    'help_field':     '${field}',
    'help_operation': 'to ${operator}clude',
    'help_type':      '(string/regex/comma-separated)',
}
class ocrd_mets_filter_options():
    """
    Adds include/exclude filter options
    """

    def __init__(self, fields=FIELDS, operators=None, **templates):
        self.fields = fields
        self.operators = operators if operators else ['ex', 'in']
        templates={**TEMPLATE_DEFAULTS, **templates}
        self.templates = {}
        for (tpl_name, tpl), field, operator in product(templates.items(), self.fields, self.operators):
            if tpl_name not in self.templates:
                self.templates[tpl_name] = dict()
            key = field
            if tpl_name in ['help_operation']:
                key = '%sclude' % operator
            elif tpl_name in ['parameter', 'required']:
                key = '%s_%sclude' % (field, operator)
            if key not in self.templates[tpl_name]:
                if isinstance(tpl, dict):
                    self.templates[tpl_name][key] = Template(str(tpl[key] if key in tpl else TEMPLATE_DEFAULTS[tpl_name]))
                else:
                    self.templates[tpl_name][key] = Template(str(tpl if tpl else TEMPLATE_DEFAULTS[tpl_name]))

    def _expand_template(self, tpl_name, field, operator, tpl_vars):
        tpl = self.templates[tpl_name]
        if tpl_name in ['help_operation']:
            return tpl['%sclude' % operator].safe_substitute(tpl_vars)
        if tpl_name in ['parameter']:
            return tpl['%s_%sclude' % (field, operator)].safe_substitute(tpl_vars)
        if tpl_name in ['required']:
            return 'True' == tpl['%s_%sclude' % (field, operator)].safe_substitute(tpl_vars)
        return tpl[field].safe_substitute(tpl_vars)

    def __call__(self, f):
        for field, operator in product(self.fields, self.operators):
            _tpl = lambda tpl_name: lambda **tpl_vars_: self._expand_template(tpl_name, field,
                    operator, tpl_vars={**{'field': field, 'operator': operator}, **tpl_vars_})

            # XXX Controls the kwarg name of this field in the decorated command
            args = [_tpl('parameter')()]
            kwargs = dict(
                default=None,
                callback=lambda ctx, param, value: value.split(',') if value and ',' in value else value,
                required=_tpl('required')(),
                metavar=_tpl('metavar')(),
                help=_tpl('help')(
                    field=_tpl('help_field')(),
                    operation=_tpl('help_operation')(),
                    type=_tpl('help_type')()
                ))

            # XXX No regex search for pageId search currently
            if field == 'pageId' and operator == 'in':
                kwargs['help'] = sub(r'[,/]?\s*regexp?\b', '', kwargs['help'], flags=IGNORECASE)

            # pylint: disable=multiple-statements
            # XXX must be retained for backwards-compatibility
            if operator == 'in':
                if field == 'ID':       args.extend(['-i', '--file-id'])
                if field == 'pageId':   args.extend(['-g', '--page-id'])
                if field == 'fileGrp':  args.extend(['-G', '--file-grp'])
                if field == 'mimetype': args.extend(['-m', '--mimetype'])

            # # 0
            # args.append('--%s%s' % ('not-' if operator == 'ex' else '', field))
            # if field.lower() != field:
            #     args.append('--%s%s' % ('not-' if operator == 'ex' else '', field.lower()))

            # 2
            args.append('--%s%s' % ('not-' if operator == 'ex' else '', field.lower()))

            # 3
            # args.append('--%s%s' % ('not-' if operator == 'ex' else '', field))

            # 4
            # if operator == 'in':
            #     args.append('--%s' % field.lower())
            # else:
            #     args.append('--%s%s' % ('not-' if operator == 'ex' else '', field))

            click.option(*args, **kwargs)(f)
        # print({k: v.safe_substitute({}) for k, v in self.templates['required'].items()})
        return f
