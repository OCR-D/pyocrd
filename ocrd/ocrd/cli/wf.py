# import os
# from os.path import relpath, exists, join, isabs
# from pathlib import Path
# import sys
# from glob import glob   # XXX pathlib.Path.glob does not support absolute globs
import io
import re

import click

from ocrd import Resolver, Workspace, WorkspaceValidator, WorkspaceBackupManager
from ocrd_validators import OcrdWfValidator
from ocrd_models import OcrdWf, OcrdWfStep
from ocrd_utils import getLogger, pushd_popd, EXT_TO_MIME

log = getLogger('ocrd.cli.wf')

# ----------------------------------------------------------------------
# ocrd wf
# ----------------------------------------------------------------------

@click.group("wf")
def wf_cli():
    """
    Working with OCRD-WF workflows
    """

# ----------------------------------------------------------------------
# ocrd wf is-well-formed WF_FILE
# ----------------------------------------------------------------------

@wf_cli.command('is-well-formed')
@click.argument('wf_file', required=True, type=click.File('r'))
def validate_workspace(wf_file):
    """
    Try to parse an OCRD-WF workflow.
    """
    OcrdWf.parse(wf_file.read())
    print("ok - well-formed")

