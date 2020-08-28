import sys

import click
from json import loads
import codecs

from ocrd import Resolver, Workspace
from ocrd_models import OcrdWf, OcrdWfStep

from ocrd_utils import (
    parse_json_string_or_file
)
from ocrd_validators import (
    OcrdToolValidator,
    OcrdZipValidator,
    PageValidator,
    ParameterValidator,
    WorkspaceValidator,
    OcrdWfValidator,
)

def _inform_of_result(report):
    if not report.is_valid:
        print(report.to_xml())
        sys.exit(1)


@click.group("validate")
def validate_cli():
    """
    All the validation in one CLI
    """

@validate_cli.command('tool-json')
@click.argument('ocrd_tool', required=False, nargs=1)
def validate_ocrd_tool(ocrd_tool):
    '''
    Validate OCRD_TOOL as an ocrd-tool.json file.
    '''
    if not ocrd_tool:
        ocrd_tool = 'ocrd-tool.json'
    with codecs.open(ocrd_tool, encoding='utf-8') as f:
        ocrd_tool = loads(f.read())
    _inform_of_result(OcrdToolValidator.validate(ocrd_tool))

@validate_cli.command('parameters')
@click.argument('ocrd_tool')
@click.argument('executable')
@click.argument('param_json')
def validate_parameters(ocrd_tool, executable, param_json):
    '''
    Validate PARAM_JSON against parameter definition of EXECUTABLE in OCRD_TOOL
    '''
    with codecs.open(ocrd_tool, encoding='utf-8') as f:
        ocrd_tool = loads(f.read())
    _inform_of_result(ParameterValidator(ocrd_tool['tools'][executable]).validate(parse_json_string_or_file(param_json)))

@validate_cli.command('page')
@click.argument('page', required=True, nargs=1)
@click.option('--page-textequiv-consistency', help="How strict to check PAGE multi-level textequiv consistency", type=click.Choice(['strict', 'lax', 'fix', 'off']), default='strict')
@click.option('--page-textequiv-strategy', help="Strategy to determine the correct textequiv", type=click.Choice(['first']), default='first')
@click.option('--check-baseline', help="Whether Baseline must be fully within TextLine/Coords", is_flag=True, default=False)
@click.option('--check-coords', help="Whether *Region/TextLine/Word/Glyph must each be fully contained within Border/*Region/TextLine/Word, resp.", is_flag=True, default=False)
def validate_page(page, **kwargs):
    '''
    Validate PAGE against OCR-D conventions
    '''
    _inform_of_result(PageValidator.validate(filename=page, **kwargs))

#  @validate_cli.command('zip')
#  @click.argument('src', type=click.Path(dir_okay=True, readable=True, resolve_path=True), required=True)
#  @click.option('-Z', '--skip-unzip', help="Treat SRC as a directory not a ZIP", is_flag=True, default=False)
#  @click.option('-B', '--skip-bag', help="Whether to skip all checks of manifests and files", is_flag=True, default=False)
#  @click.option('-C', '--skip-checksums', help="Whether to omit checksum checks but still check basic BagIt conformance", is_flag=True, default=False)
#  @click.option('-D', '--skip-delete', help="Whether to skip deleting the unpacked OCRD-ZIP dir after valdiation", is_flag=True, default=False)
#  @click.option('-j', '--processes', help="Number of parallel processes", type=int, default=1)
#  def validate(src, **kwargs):
#      """
#      Validate OCRD-ZIP

#      SRC must exist an be an OCRD-ZIP, either a ZIP file or a directory.
#      """
#      _inform_of_result(OcrdZipValidator(Resolver(), src).validate(**kwargs))

#  @validate_cli.command('workspace')
#  @click.option('-a', '--download', is_flag=True, help="Download all files")
#  @click.option('-s', '--skip', help="Tests to skip", default=[], multiple=True, type=click.Choice(['imagefilename', 'dimension', 'mets_unique_identifier', 'mets_file_group_names', 'mets_files', 'pixel_density', 'page', 'url']))
#  @click.option('--page-textequiv-consistency', '--page-strictness', help="How strict to check PAGE multi-level textequiv consistency", type=click.Choice(['strict', 'lax', 'fix', 'off']), default='strict')
#  @click.option('--page-coordinate-consistency', help="How fierce to check PAGE multi-level coordinate consistency", type=click.Choice(['poly', 'baseline', 'both', 'off']), default='poly')
#  @click.argument('mets_url')
#  def validate_workspace(mets_url, **kwargs):
#      '''
#          Validate a workspace
#      '''
#      _inform_of_result(WorkspaceValidator.validate(Resolver(), mets_url, **kwargs))

@validate_cli.command('tasks')
@click.option('--workspace', nargs=1, required=False, help='Workspace these tasks are to be run. If omitted, only validate syntax')
@click.argument('tasks', nargs=-1, required=True)
def validate_process(tasks, workspace):
    '''
    Validate a sequence of tasks passable to 'ocrd process'
    '''
    wf_val = OcrdWfValidator()
    if workspace:
        wf = OcrdWf(steps=[OcrdWfStep.parse(t) for t in tasks])
        _inform_of_result(wf_val.validate(wf, workspace=Workspace(Resolver(), directory=workspace)))
    else:
        for t in [OcrdWfStep.parse(t) for t in tasks]:
            _inform_of_result(wf_val.step_is_resolveable(t))
