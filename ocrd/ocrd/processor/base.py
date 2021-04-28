"""
Processor base class and helper functions.
"""

__all__ = [
    'Processor',
    'generate_processor_help',
    'run_cli',
    'run_processor'
]

from os import makedirs
from os.path import exists, isdir, join
from shutil import copyfileobj
import json
import os
from os import getcwd
import re
import sys

import requests

from ocrd_utils import (
    VERSION as OCRD_VERSION,
    MIMETYPE_PAGE,
    getLogger,
    initLogging,
    list_resource_candidates,
    list_all_resources,
)
from ocrd_validators import ParameterValidator
from ocrd_models.ocrd_page import MetadataItemType, LabelType, LabelsType
from ..resource_manager import OcrdResourceManager

# XXX imports must remain for backwards-compatibilty
from .helpers import run_api, run_cli, run_processor, generate_processor_help # pylint: disable=unused-import

class Processor():
    """
    A processor is a tool that implements the uniform OCR-D command-line interface
    for run-time data processing. That is, it executes a single workflow step,
    or a combination of workflow steps, on the workspace (represented by local METS).
    It reads input files for all or requested physical pages of the input fileGrp(s),
    and writes output files for them into the output fileGrp(s). It may take 
    a number of optional or mandatory parameters.
    """

    def __init__(
            self,
            workspace,
            ocrd_tool=None,
            parameter=None,
            input_file_grp=None,
            output_file_grp=None,
            page_id=None,
            show_resource=None,
            list_resources=False,
            show_help=False,
            show_version=False,
            dump_json=False,
            version=None
    ):
        """
        Instantiate, but do not process. Unless ``list_resources`` or
        ``show_resource`` or ``show_help`` or ``show_version`` or
        ``dump_json`` is true, setup for processing (parsing and
        validating parameters, entering the workspace directory).
        """
        if parameter is None:
            parameter = {}
        if dump_json:
            print(json.dumps(ocrd_tool, indent=True))
            return
        if list_resources:
            for res in list_all_resources(ocrd_tool['executable']):
                print(res)
            return
        if show_resource:
            res_fname = list_resource_candidates(ocrd_tool['executable'], show_resource, is_file=True)
            if not res_fname:
                initLogging()
                logger = getLogger('ocrd.%s.__init__' % ocrd_tool['executable'])
                logger.error("Failed to resolve %s for processor %s" % (show_resource, ocrd_tool['executable']))
            else:
                with open(res_fname[0], 'rb') as f:
                    copyfileobj(f, sys.stdout.buffer)
            return
        self.ocrd_tool = ocrd_tool
        if show_help:
            self.show_help()
            return
        self.version = version
        if show_version:
            self.show_version()
            return
        self.workspace = workspace
        # FIXME HACK would be better to use pushd_popd(self.workspace.directory)
        # but there is no way to do that in process here since it's an
        # overridden method. chdir is almost always an anti-pattern.
        if self.workspace:
            self.old_pwd = getcwd()
            os.chdir(self.workspace.directory)
        self.input_file_grp = input_file_grp
        self.output_file_grp = output_file_grp
        self.page_id = None if page_id == [] or page_id is None else page_id
        parameterValidator = ParameterValidator(ocrd_tool)
        report = parameterValidator.validate(parameter)
        if not report.is_valid:
            raise Exception("Invalid parameters %s" % report.errors)
        self.parameter = parameter

    def show_help(self):
        print(generate_processor_help(self.ocrd_tool, processor_instance=self))

    def show_version(self):
        print("Version %s, ocrd/core %s" % (self.version, OCRD_VERSION))

    def verify(self):
        """
        Verify that the input fulfills the processor's requirements.
        """
        return True

    def process(self):
        """
        Process the :py:attr:`workspace` 
        from the given :py:attr:`input_file_grp`s
        to the given :py:attr:`output_file_grp`s
        under the given :py:attr:`parameter`s.
        
        (This contains the main functionality and needs to be overridden by subclasses.)
        """
        raise Exception("Must be implemented")


    def add_metadata(self, pcgts):
        """
        Add PAGE-XML `MetadataItem` describing the processing step and runtime parameters to :py:class:`ocrd_models.ocrd_page.PcGtsType` ``pcgts``.
        """
        pcgts.get_Metadata().add_MetadataItem(
                MetadataItemType(type_="processingStep",
                    name=self.ocrd_tool['steps'][0],
                    value=self.ocrd_tool['executable'],
                    Labels=[LabelsType(
                        externalModel="ocrd-tool",
                        externalId="parameters",
                        Label=[LabelType(type_=name,
                                         value=self.parameter[name])
                               for name in self.parameter.keys()]),
                            LabelsType(
                        externalModel="ocrd-tool",
                        externalId="version",
                        Label=[LabelType(type_=self.ocrd_tool['executable'],
                                         value=self.version),
                               LabelType(type_='ocrd/core',
                                         value=OCRD_VERSION)])
                    ]))

    def resolve_resource(self, val):
        """
        Resolve a resource name to an absolute file path with the algorithm in
        https://ocr-d.de/en/spec/ocrd_tool#file-parameters

        Args:
            val (string): resource value to resolve
        """
        executable = self.ocrd_tool['executable']
        log = getLogger('ocrd.%s.resolve_resource' % executable)
        if exists(val):
            log.debug("Resolved to absolute path %s" % val)
            return val
        ret = [cand for cand in list_resource_candidates(executable, val, cwd=self.old_pwd) if exists(cand)]
        if ret:
            log.debug("Resolved %s to absolute path %s" % (val, ret[0]))
            return ret[0]
        log.error("Could not find resource '%s' for executable '%s'. Try 'ocrd resmgr download %s %s' to download this resource.",
                val, executable, executable, val)
        sys.exit(1)

    def list_all_resources(self):
        """
        List all resources found in the filesystem
        """
        return list_all_resources(self.ocrd_tool['executable'])

    @property
    def input_files(self):
        """
        List the input files (for single-valued :py:attr:`input_file_grp`).

        For each physical page:
        - If there is a single PAGE-XML for the page, take it (and forget about all
          other files for that page)
        - Else if there is a single image file, take it (and forget about all other
          files for that page)
        - Otherwise raise an error (complaining that only PAGE-XML warrants
          having multiple images for a single page)
        Algorithm <https://github.com/cisocrgroup/ocrd_cis/pull/57#issuecomment-656336593>_
        
        Returns:
            A list of :py:class:`ocrd_models.ocrd_file.OcrdFile` objects.
        """
        if not self.input_file_grp:
            raise ValueError("Processor is missing input fileGrp")
        ret = self.zip_input_files(mimetype=None, on_error='abort')
        if not ret:
            return []
        assert len(ret[0]) == 1, 'Use zip_input_files() instead of input_files when processing multiple input fileGrps'
        return [tuples[0] for tuples in ret]

    def zip_input_files(self, require_first=True, mimetype=None, on_error='skip'):
        """
        List tuples of input files (for multi-valued :py:attr:`input_file_grp`).

        Processors that expect/need multiple input file groups,
        cannot use :py:data:`input_files`. They must align (zip) input files
        across pages. This includes the case where not all pages
        are equally present in all file groups. It also requires
        making a consistent selection if there are multiple files
        per page.

        Following the OCR-D functional model, this function tries to
        find a single PAGE file per page, or fall back to a single
        image file per page. In either case, multiple matches per page
        are an error (see error handling below).
        This default behaviour can be changed by using a fixed MIME
        type filter via ``mimetype``. But still, multiple matching
        files per page are an error.

        Single-page multiple-file errors are handled according to
        ``on_error``:
        - if `'skip'`, then the page for the respective fileGrp will be
          silently skipped (as if there was no match at all)
        - if `'first'`, then the first matching file for the page will be
          silently selected (as if the first was the only match)
        - if `'last'`, then the last matching file for the page will be
          silently selected (as if the last was the only match)
        - if `'abort'`, then an exception will be raised.
        Multiple matches for PAGE-XML will always raise an exception.

        Keyword Args:
             require_first (boolean): If true, then skip a page entirely
                 whenever it is not available in the first input `fileGrp`.
             mimetype (string): If not `None`, filter by the specified MIME
                 type (literal or regex prefixed by `//`). Otherwise prefer
                 PAGE or image.
        Returns:
            A list of :py:class:`ocrd_models.ocrd_file.OcrdFile` tuples.
        """
        if not self.input_file_grp:
            raise ValueError("Processor is missing input fileGrp")

        LOG = getLogger('ocrd.processor.base')
        ifgs = self.input_file_grp.split(",")
        # Iterating over all files repeatedly may seem inefficient at first sight,
        # but the unnecessary OcrdFile instantiations for posterior fileGrp filtering
        # can actually be much more costly than traversing the ltree.
        # This might depend on the number of pages vs number of fileGrps.

        pages = dict()
        for i, ifg in enumerate(ifgs):
            for file_ in sorted(self.workspace.mets.find_all_files(
                    pageId=self.page_id, fileGrp=ifg, mimetype=mimetype),
                                # sort by MIME type so PAGE comes before images
                                key=lambda file_: file_.mimetype):
                if not file_.pageId:
                    continue
                ift = pages.setdefault(file_.pageId, [None]*len(ifgs))
                if ift[i]:
                    LOG.debug("another file %s for page %s in input file group %s", file_.ID, file_.pageId, ifg)
                    # fileGrp has multiple files for this page ID
                    if mimetype:
                        # filter was active, this must not happen
                        if on_error == 'skip':
                            ift[i] = None
                        elif on_error == 'first':
                            pass # keep first match
                        elif on_error == 'last':
                            ift[i] = file_
                        elif on_error == 'abort':
                            raise ValueError(
                                "Multiple '%s' matches for page '%s' in fileGrp '%s'." % (
                                    mimetype, file_.pageId, ifg))
                        else:
                            raise Exception("Unknown 'on_error' strategy '%s'" % on_error)
                    elif (ift[i].mimetype == MIMETYPE_PAGE and
                          file_.mimetype != MIMETYPE_PAGE):
                        pass # keep PAGE match
                    elif (ift[i].mimetype == MIMETYPE_PAGE and
                          file_.mimetype == MIMETYPE_PAGE):
                        raise ValueError(
                            "Multiple PAGE-XML matches for page '%s' in fileGrp '%s'." % (
                                file_.pageId, ifg))
                    else:
                        # filter was inactive but no PAGE is in control, this must not happen
                        if on_error == 'skip':
                            ift[i] = None
                        elif on_error == 'first':
                            pass # keep first match
                        elif on_error == 'last':
                            ift[i] = file_
                        elif on_error == 'abort':
                            raise ValueError(
                                "No PAGE-XML for page '%s' in fileGrp '%s' but multiple matches." % (
                                    file_.pageId, ifg))
                        else:
                            raise Exception("Unknown 'on_error' strategy '%s'" % on_error)
                else:
                    LOG.debug("adding file %s for page %s to input file group %s", file_.ID, file_.pageId, ifg)
                    ift[i] = file_
        ifts = list()
        for page, ifiles in pages.items():
            for i, ifg in enumerate(ifgs):
                if not ifiles[i]:
                    # other fallback options?
                    LOG.error('found no page %s in file group %s',
                              page, ifg)
            if ifiles[0] or not require_first:
                ifts.append(tuple(ifiles))
        return ifts
