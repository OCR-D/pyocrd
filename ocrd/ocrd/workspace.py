import io
from os import makedirs, unlink, listdir, path
from pathlib import Path
from shutil import move, copyfileobj
from re import sub

from cv2 import COLOR_GRAY2BGR, COLOR_RGB2BGR, cvtColor
from PIL import Image
import numpy as np
from deprecated.sphinx import deprecated

from ocrd_models import OcrdMets, OcrdFile
from ocrd_models.ocrd_page import parse, BorderType, to_xml
from ocrd_modelfactory import exif_from_filename, page_from_file
from ocrd_utils import (
    atomic_write,
    getLogger,
    image_from_polygon,
    coordinates_of_segment,
    adjust_canvas_to_rotation,
    adjust_canvas_to_transposition,
    shift_coordinates,
    rotate_coordinates,
    transform_coordinates,
    transpose_coordinates,
    crop_image,
    rotate_image,
    transpose_image,
    bbox_from_polygon,
    polygon_from_points,
    xywh_from_bbox,
    pushd_popd,
    MIME_TO_EXT,
    MIME_TO_PIL,
    MIMETYPE_PAGE,
    REGEX_PREFIX
)

from .workspace_backup import WorkspaceBackupManager

class Workspace():
    """
    A workspace is a temporary directory set up for a processor. It's the
    interface to the METS/PAGE XML and delegates download and upload to the
    :py:class:`ocrd.Resolver`.

    Args:

        directory (string) : Filesystem folder to work in
        mets (:py:class:`ocrd_models.ocrd_mets.OcrdMets`) : `OcrdMets` representing this workspace. 
            Loaded from `'mets.xml'` if `None`.
        mets_basename (string) : Basename of the METS XML file. Default: Last URL segment of the mets_url.
        overwrite_mode (boolean) : Whether to force add operations on this workspace globally
        baseurl (string) : Base URL to prefix to relative URL.
    """

    def __init__(self, resolver, directory, mets=None, mets_basename='mets.xml', automatic_backup=False, baseurl=None):
        self.resolver = resolver
        self.directory = directory
        self.mets_target = str(Path(directory, mets_basename))
        self.overwrite_mode = False
        if mets is None:
            mets = OcrdMets(filename=self.mets_target)
        self.mets = mets
        self.automatic_backup = automatic_backup
        self.baseurl = baseurl
        #  print(mets.to_xml(xmllint=True).decode('utf-8'))

    def __str__(self):
        return 'Workspace[directory=%s, baseurl=%s, file_groups=%s, files=%s]' % (
            self.directory,
            self.baseurl,
            self.mets.file_groups,
            [str(f) for f in self.mets.find_all_files()],
        )

    def reload_mets(self):
        """
        Reload METS from the filesystem.
        """
        self.mets = OcrdMets(filename=self.mets_target)

    def merge(self, other_workspace, copy_files=True, **kwargs):
        """
        Merge ``other_workspace`` into this one

        See :py:func:OcrdMets.merge: for the ``kwargs``

        Keyword Args:
            copy_files (boolean): Whether to copy files from ``other_workspace`` to this one
        """
        def after_add_cb(f):
            if not copy_files:
                return
            fpath_src = Path(other_workspace.directory, f.url)
            fpath_dest = Path(self.directory, f.url)
            if fpath_src.exists():
                if fpath_dest.exists():
                    raise Exception("Copying %s to %s would overwrite the latter" % (fpath_src, fpath_dest))
                if not fpath_dest.parent.is_dir():
                    makedirs(str(fpath_dest.parent))
                with open(str(fpath_src), 'rb') as fstream_in, open(str(fpath_dest), 'wb') as fstream_out:
                    copyfileobj(fstream_in, fstream_out)
        self.mets.merge(other_workspace.mets, after_add_cb=after_add_cb, **kwargs)


    @deprecated(version='1.0.0', reason="Use workspace.download_file")
    def download_url(self, url, **kwargs):
        """
        Download a URL to the workspace.

        Args:
            url (string): URL to download to directory
            **kwargs : See :py:class:`ocrd_models.ocrd_file.OcrdFile`

        Returns:
            The local filename of the downloaded file
        """
        f = OcrdFile(None, url=url, **kwargs)
        f = self.download_file(f)
        return f.local_filename


    def download_file(self, f, _recursion_count=0):
        """
        Download a :py:class:`ocrd_models.ocrd_file.OcrdFile` to the workspace.
        """
        log = getLogger('ocrd.workspace.download_file')
        log.debug('download_file %s [_recursion_count=%s]' % (f, _recursion_count))
        with pushd_popd(self.directory):
            try:
                # If the f.url is already a file path, and is within self.directory, do nothing
                url_path = Path(f.url).resolve()
                if not (url_path.exists() and url_path.relative_to(str(Path(self.directory).resolve()))):
                    raise Exception("Not already downloaded, moving on")
            except Exception as e:
                basename = '%s%s' % (f.ID, MIME_TO_EXT.get(f.mimetype, '')) if f.ID else f.basename
                try:
                    f.url = self.resolver.download_to_directory(self.directory, f.url, subdir=f.fileGrp, basename=basename)
                except FileNotFoundError as e:
                    if not self.baseurl:
                        raise Exception("No baseurl defined by workspace. Cannot retrieve '%s'" % f.url)
                    if _recursion_count >= 1:
                        raise Exception("Already tried prepending baseurl '%s'. Cannot retrieve '%s'" % (self.baseurl, f.url))
                    log.debug("First run of resolver.download_to_directory(%s) failed, try prepending baseurl '%s': %s", f.url, self.baseurl, e)
                    f.url = '%s/%s' % (self.baseurl, f.url)
                    f.url = self.download_file(f, _recursion_count + 1).local_filename
            f.local_filename = f.url
            return f

    def remove_file(self, ID, force=False, keep_file=False, page_recursive=False, page_same_group=False):
        """
        Remove a METS `file` from the workspace.

        Arguments:
            ID (string|:py:class:`ocrd_models.ocrd_file.OcrdFile`): `@ID` of the METS `file`
                to delete or the file itself
        Keyword Args:
            force (boolean): Continue removing even if file not found in METS
            keep_file (boolean): Whether to keep files on disk
            page_recursive (boolean): Whether to remove all images referenced in the file
                if the file is a PAGE-XML document.
            page_same_group (boolean): Remove only images in the same file group as the PAGE-XML.
                Has no effect unless ``page_recursive`` is `True`.
        """
        log = getLogger('ocrd.workspace.remove_file')
        log.debug('Deleting mets:file %s', ID)
        if not force and self.overwrite_mode:
            force = True
        if isinstance(ID, OcrdFile):
            ID = ID.ID
        try:
            ocrd_file_ = self.mets.remove_file(ID)
            ocrd_files = [ocrd_file_] if isinstance(ocrd_file_, OcrdFile) else ocrd_file_
            if page_recursive:
                with pushd_popd(self.directory):
                    for ocrd_file in ocrd_files:
                        if ocrd_file.mimetype != MIMETYPE_PAGE:
                            continue
                        ocrd_page = parse(self.download_file(ocrd_file).local_filename, silence=True)
                        for img_url in ocrd_page.get_AllAlternativeImagePaths():
                            img_kwargs = {'url': img_url}
                            if page_same_group:
                                img_kwargs['fileGrp'] = ocrd_file.fileGrp
                            for img_file in self.mets.find_files(**img_kwargs):
                                self.remove_file(img_file, keep_file=keep_file, force=force)
            if not keep_file:
                with pushd_popd(self.directory):
                    for ocrd_file in ocrd_files:
                        if not ocrd_file.local_filename:
                            log.warning("File not locally available %s", ocrd_file)
                            if not force:
                                raise Exception("File not locally available %s" % ocrd_file)
                        else:
                            log.info("rm %s [cwd=%s]", ocrd_file.local_filename, self.directory)
                            unlink(ocrd_file.local_filename)
            return ocrd_file_
        except FileNotFoundError as e:
            if not force:
                raise e

    def remove_file_group(self, USE, recursive=False, force=False, keep_files=False, page_recursive=False, page_same_group=False):
        """
        Remove a METS `fileGrp`.

        Arguments:
            USE (string): `@USE` of the METS `fileGrp` to delete
        Keyword Args:
            recursive (boolean): Whether to recursively delete all files in the group
            force (boolean): Continue removing even if group or containing files not found in METS
            keep_files (boolean): When deleting recursively whether to keep files on disk
            page_recursive (boolean): Whether to remove all images referenced in the file 
                if the file is a PAGE-XML document.
            page_same_group (boolean): Remove only images in the same file group as the PAGE-XML. 
                Has no effect unless ``page_recursive`` is `True`.
        """
        if not force and self.overwrite_mode:
            force = True

        if (not USE.startswith(REGEX_PREFIX)) and (USE not in self.mets.file_groups) and (not force):
            raise Exception("No such fileGrp: %s" % USE)

        file_dirs = []
        if recursive:
            for f in self.mets.find_files(fileGrp=USE):
                self.remove_file(f, force=force, keep_file=keep_files, page_recursive=page_recursive, page_same_group=page_same_group)
                if f.local_filename:
                    file_dirs.append(path.dirname(f.local_filename))

        self.mets.remove_file_group(USE, force=force)

        # PLEASE NOTE: this only removes directories in the workspace if they are empty
        # and named after the fileGrp which is a convention in OCR-D.
        with pushd_popd(self.directory):
            if Path(USE).is_dir() and not listdir(USE):
                Path(USE).rmdir()
            if file_dirs:
                for file_dir in set(file_dirs):
                    if Path(file_dir).is_dir() and not listdir(file_dir):
                        Path(file_dir).rmdir()


    def rename_file_group(self, old, new):
        """
        Rename a METS `fileGrp`.

        Arguments:
            old (string): `@USE` of the METS `fileGrp` to rename
            new (string): `@USE` of the METS `fileGrp` to rename as
        """
        log = getLogger('ocrd.workspace.rename_file_group')

        if old not in self.mets.file_groups:
            raise ValueError("No such fileGrp: %s" % old)
        if new in self.mets.file_groups:
            raise ValueError("fileGrp already exists %s" % new)

        with pushd_popd(self.directory):
            # create workspace dir ``new``
            log.info("mkdir %s" % new)
            if not Path(new).is_dir():
                Path(new).mkdir()
            url_replacements = {}
            log.info("Moving files")
            for mets_file in self.mets.find_files(fileGrp=old, local_only=True):
                new_url = sub(r'^%s/' % old, '%s/' % new, mets_file.url)
                url_replacements[mets_file.url] = new_url
                # move file from ``old`` to ``new``
                move(mets_file.url, new_url)
                # change the url of ``mets:file``
                mets_file.url = new_url
            # change file paths in PAGE-XML imageFilename and filename attributes
            for page_file in self.mets.find_files(mimetype=MIMETYPE_PAGE, local_only=True):
                log.info("Renaming file references in PAGE-XML %s" % page_file)
                pcgts = page_from_file(page_file)
                changed = False
                for old_url, new_url in url_replacements.items():
                    if pcgts.get_Page().imageFilename == old_url:
                        changed = True
                        log.info("Rename pc:Page/@imageFilename: %s -> %s" % (old_url, new_url))
                        pcgts.get_Page().imageFilename = new_url
                for ai in pcgts.get_Page().get_AllAlternativeImages():
                    for old_url, new_url in url_replacements.items():
                        if ai.filename == old_url:
                            changed = True
                            log.info("Rename pc:Page/../AlternativeImage: %s -> %s" % (old_url, new_url))
                            ai.filename = new_url
                if changed:
                    log.info("PAGE-XML changed, writing %s" % (page_file.local_filename))
                    with open(page_file.local_filename, 'w', encoding='utf-8') as f:
                        f.write(to_xml(pcgts))
            # change the ``USE`` attribute of the fileGrp
            self.mets.rename_file_group(old, new)
            # Remove the old dir
            log.info("rmdir %s" % old)
            if Path(old).is_dir() and not listdir(old):
                Path(old).rmdir()

    def add_file(self, file_grp, content=None, **kwargs):
        """
        Add a file to the :py:class:`ocrd_models.ocrd_mets.OcrdMets` of the workspace.
        
        Arguments:
            file_grp (string): `@USE` of the METS `fileGrp` to add to
        Keyword Args:
            content (string|bytes): optional content to write to the file
                in the filesystem
            **kwargs: See :py:func:`ocrd_models.ocrd_mets.OcrdMets.add_file`
        Returns:
            a new :py:class:`ocrd_models.ocrd_file.OcrdFile` 
        """
        log = getLogger('ocrd.workspace.add_file')
        log.debug(
            'outputfile file_grp=%s local_filename=%s content=%s',
            file_grp,
            kwargs.get('local_filename'),
            content is not None)
        if 'pageId' not in kwargs:
            raise ValueError("workspace.add_file must be passed a 'pageId' kwarg, even if it is None.")
        if content is not None and 'local_filename' not in kwargs:
            raise Exception("'content' was set but no 'local_filename'")
        if self.overwrite_mode:
            kwargs['force'] = True

        with pushd_popd(self.directory):
            if 'local_filename' in kwargs:
                # If the local filename has folder components, create those folders
                local_filename_dir = kwargs['local_filename'].rsplit('/', 1)[0]
                if local_filename_dir != kwargs['local_filename'] and not Path(local_filename_dir).is_dir():
                    makedirs(local_filename_dir)
                if 'url' not in kwargs:
                    kwargs['url'] = kwargs['local_filename']

            #  print(kwargs)
            ret = self.mets.add_file(file_grp, **kwargs)

            if content is not None:
                with open(kwargs['local_filename'], 'wb') as f:
                    if isinstance(content, str):
                        content = bytes(content, 'utf-8')
                    f.write(content)

        return ret

    def save_mets(self):
        """
        Write out the current state of the METS file to the filesystem.
        """
        log = getLogger('ocrd.workspace.save_mets')
        log.info("Saving mets '%s'", self.mets_target)
        if self.automatic_backup:
            WorkspaceBackupManager(self).add()
        with atomic_write(self.mets_target) as f:
            f.write(self.mets.to_xml(xmllint=True).decode('utf-8'))

    def resolve_image_exif(self, image_url):
        """
        Get the EXIF metadata about an image URL as :py:class:`ocrd_models.ocrd_exif.OcrdExif`

        Args:
            image_url (string) : `@href` (path or URL) of the METS `file` to inspect

        Returns:
            :py:class:`ocrd_models.ocrd_exif.OcrdExif`
        """
        if not image_url:
            # avoid "finding" just any file
            raise Exception("Cannot resolve empty image path")
        f = next(self.mets.find_files(url=image_url), OcrdFile(None, url=image_url))
        image_filename = self.download_file(f).local_filename
        ocrd_exif = exif_from_filename(image_filename)
        return ocrd_exif

    @deprecated(version='1.0.0', reason="Use workspace.image_from_page and workspace.image_from_segment")
    def resolve_image_as_pil(self, image_url, coords=None):
        """
        Resolve an image URL to a `PIL.Image`.

        Arguments:
            image_url (string): `@href` (path or URL) of the METS `file` to retrieve
        Keyword Args:
            coords (list) : Coordinates of the bounding box to cut from the image

        Returns:
            Full or cropped `PIL.Image`

        """
        return self._resolve_image_as_pil(image_url, coords)

    def _resolve_image_as_pil(self, image_url, coords=None):
        if not image_url:
            # avoid "finding" just any file
            raise Exception("Cannot resolve empty image path")
        log = getLogger('ocrd.workspace._resolve_image_as_pil')
        f = next(self.mets.find_files(url=image_url), OcrdFile(None, url=image_url))
        image_filename = self.download_file(f).local_filename

        with pushd_popd(self.directory):
            pil_image = Image.open(image_filename)
            pil_image.load() # alloc and give up the FD

        # Pillow does not properly support higher color depths
        # (e.g. 16-bit or 32-bit or floating point grayscale),
        # clipping its dynamic range to the lower 8-bit in
        # many operations (including paste, putalpha, ImageStat...),
        # even including conversion.
        # Cf. Pillow#3011 Pillow#3159 Pillow#3838 (still open in 8.0)
        # So to be on the safe side, we must re-quantize these
        # to 8-bit via numpy (conversion to/from which fortunately
        # seems to work reliably):
        if (pil_image.mode.startswith('I') or
            pil_image.mode.startswith('F')):
            arr_image = np.array(pil_image)
            if arr_image.dtype.kind == 'i':
                # signed integer is *not* trustworthy in this context
                # (usually a mistake in the array interface)
                log.debug('Casting image "%s" from signed to unsigned', image_url)
                arr_image.dtype = np.dtype('u' + arr_image.dtype.name)
            if arr_image.dtype.kind == 'u':
                # integer needs to be scaled linearly to 8 bit
                # of course, an image might actually have some lower range
                # (e.g. 10-bit in I;16 or 20-bit in I or 4-bit in L),
                # but that would be guessing anyway, so here don't
                # make assumptions on _scale_, just reduce _precision_
                log.debug('Reducing image "%s" from depth %d bit to 8 bit',
                          image_url, arr_image.dtype.itemsize * 8)
                arr_image = arr_image >> 8 * (arr_image.dtype.itemsize-1)
                arr_image = arr_image.astype(np.uint8)
            elif arr_image.dtype.kind == 'f':
                # float needs to be scaled from [0,1.0] to [0,255]
                log.debug('Reducing image "%s" from floating point to 8 bit',
                          image_url)
                arr_image *= 255
                arr_image = arr_image.astype(np.uint8)
            pil_image = Image.fromarray(arr_image)

        if coords is None:
            return pil_image

        # FIXME: remove or replace this by (image_from_polygon+) crop_image ...
        log.debug("Converting PIL to OpenCV: %s", image_url)
        color_conversion = COLOR_GRAY2BGR if pil_image.mode in ('1', 'L') else  COLOR_RGB2BGR
        pil_as_np_array = np.array(pil_image).astype('uint8') if pil_image.mode == '1' else np.array(pil_image)
        cv2_image = cvtColor(pil_as_np_array, color_conversion)

        poly = np.array(coords, np.int32)
        log.debug("Cutting region %s from %s", coords, image_url)
        region_cut = cv2_image[
            np.min(poly[:, 1]):np.max(poly[:, 1]),
            np.min(poly[:, 0]):np.max(poly[:, 0])
        ]
        return Image.fromarray(region_cut)

    def image_from_page(self, page, page_id,
                        fill='background', transparency=False,
                        feature_selector='', feature_filter=''):
        """Extract an image for a PAGE-XML page from the workspace.

        Args:
            page (:py:class:`ocrd_models.ocrd_page.PageType`): a PAGE `PageType` object
            page_id (string): its `@ID` in the METS physical `structMap`
        Keyword Args:
            fill (string): a `PIL` color specifier
            transparency (boolean): whether to add an alpha channel for masking
            feature_selector (string): a comma-separated list of `@comments` classes
            feature_filter (string): a comma-separated list of `@comments` classes            

        Extract a `PIL.Image` from ``page``, either from its `AlternativeImage`
        (if it exists), or from its `@imageFilename` (otherwise). Also crop it,
        if a `Border` exists, and rotate it, if any `@orientation` angle is
        annotated.

        If ``feature_selector`` and/or ``feature_filter`` is given, then
        select/filter among the `@imageFilename` image and the available
        AlternativeImages the richest one which contains all of the selected,
        but none of the filtered features (i.e. `@comments` classes), or
        raise an error.

        (Required and produced features need not be in the same order, so
        ``feature_selector`` is merely a mask specifying Boolean AND, and
        ``feature_filter`` is merely a mask specifying Boolean OR.)

        If the chosen image does not have the feature `"cropped"` yet, but
        a `Border` exists, and unless `"cropped"` is being filtered, then crop it.
        Likewise, if the chosen image does not have the feature `"deskewed"` yet,
        but an `@orientation` angle is annotated, and unless `"deskewed"` is being
        filtered, then rotate it. (However, if `@orientation` is above the
        [-45°,45°] interval, then apply as much transposition as possible first,
        unless `"rotated-90"` / `"rotated-180"` / `"rotated-270"` is being filtered.)

        Cropping uses a polygon mask (not just the bounding box rectangle).
        Areas outside the polygon will be filled according to ``fill``:

        - if `"background"` (the default),
          then fill with the median color of the image;
        - otherwise, use the given color, e.g. `"white"` or `(255,255,255)`.

        Moreover, if ``transparency`` is true, and unless the image already
        has an alpha channel, then add an alpha channel which is fully opaque
        before cropping and rotating. (Thus, unexposed/masked areas will be
        transparent afterwards for consumers that can interpret alpha channels).

        Returns:
            a tuple of
             * the extracted `PIL.Image`,
             * a `dict` with information about the extracted image:
               - `"transform"`: a `Numpy` array with an affine transform which
                   converts from absolute coordinates to those relative to the image,
                   i.e. after cropping to the page's border / bounding box (if any)
                   and deskewing with the page's orientation angle (if any)
               - `"angle"`: the rotation/reflection angle applied to the image so far,
               - `"features"`: the `AlternativeImage` `@comments` for the image, i.e.
                 names of all applied operations that lead up to this result,
             * an :py:class:`ocrd_models.ocrd_exif.OcrdExif` instance associated with 
               the original image.

        (The first two can be used to annotate a new `AlternativeImage`,
         or be passed down with :py:meth:`image_from_segment`.)

        Examples:

         * get a raw (colored) but already deskewed and cropped image::

           page_image, page_coords, page_image_info = workspace.image_from_page(
                 page, page_id,
                 feature_selector='deskewed,cropped',
                 feature_filter='binarized,grayscale_normalized')
        """
        log = getLogger('ocrd.workspace.image_from_page')
        page_image_info = self.resolve_image_exif(page.imageFilename)
        page_image = self._resolve_image_as_pil(page.imageFilename)
        page_coords = dict()
        # use identity as initial affine coordinate transform:
        page_coords['transform'] = np.eye(3)
        # interim bbox (updated with each change to the transform):
        page_bbox = [0, 0, page_image.width, page_image.height]
        page_xywh = {'x': 0, 'y': 0,
                     'w': page_image.width, 'h': page_image.height}

        border = page.get_Border()
        # page angle: PAGE @orientation is defined clockwise,
        # whereas PIL/ndimage rotation is in mathematical direction:
        page_coords['angle'] = -(page.get_orientation() or 0)
        # map angle from (-180,180] to [0,360], and partition into multiples of 90;
        # but avoid unnecessary large remainders, i.e. split symmetrically:
        orientation = (page_coords['angle'] + 45) % 360
        orientation = orientation - (orientation % 90)
        skew = (page_coords['angle'] % 360) - orientation
        skew = 180 - (180 - skew) % 360 # map to [-45,45]
        page_coords['angle'] = 0 # nothing applied yet (depends on filters)
        log.debug("page '%s' has %s orientation=%d skew=%.2f",
                  page_id, "border," if border else "", orientation, skew)

        # initialize AlternativeImage@comments classes as empty:
        page_coords['features'] = ''
        best_image = None
        alternative_images = page.get_AlternativeImage()
        if alternative_images:
            # (e.g. from page-level cropping, binarization, deskewing or despeckling)
            best_features = set()
            auto_features = {'cropped', 'deskewed', 'rotated-90', 'rotated-180', 'rotated-270'}
            # search to the end, because by convention we always append,
            # and among multiple satisfactory images we want the most recent,
            # but also ensure that we get the richest feature set, i.e. most
            # of those features that we cannot reproduce automatically below
            for alternative_image in alternative_images:
                features = alternative_image.get_comments()
                if not features:
                    log.warning("AlternativeImage %d for page '%s' does not have any feature attributes",
                                alternative_images.index(alternative_image) + 1, page_id)
                    features = ''
                featureset = set(features.split(','))
                if (all(feature in featureset
                        for feature in feature_selector.split(',') if feature) and
                    not any(feature in featureset
                            for feature in feature_filter.split(',') if feature) and
                    len(featureset.difference(auto_features)) >= \
                    len(best_features.difference(auto_features))):
                    best_features = featureset
                    best_image = alternative_image
            if best_image:
                log.debug("Using AlternativeImage %d %s for page '%s'",
                          alternative_images.index(best_image) + 1,
                          best_features, page_id)
                page_image = self._resolve_image_as_pil(best_image.get_filename())
                page_coords['features'] = best_image.get_comments() # including duplicates

        # adjust the coord transformation to the steps applied on the image,
        # and apply steps on the existing image in case it is missing there,
        # but traverse all steps (crop/reflect/rotate) in a particular order:
        # - existing image features take priority (in the order annotated),
        # - next is cropping (if necessary but not already applied),
        # - next is reflection (if necessary but not already applied),
        # - next is rotation (if necessary but not already applied).
        # This helps deal with arbitrary workflows (e.g. crop then deskew,
        # or deskew then crop), regardless of where images are generated.
        alternative_image_features = page_coords['features'].split(',')
        for duplicate_feature in set([feature for feature in alternative_image_features
                                      # features relevant in reconstructing coordinates:
                                      if (feature in ['cropped', 'deskewed', 'rotated-90',
                                                      'rotated-180', 'rotated-270'] and
                                          alternative_image_features.count(feature) > 1)]):
            log.error("Duplicate feature %s in AlternativeImage for page '%s'",
                      duplicate_feature, page_id)
        for i, feature in enumerate(alternative_image_features +
                                    (['cropped']
                                     if (border and
                                         not 'cropped' in alternative_image_features and
                                         not 'cropped' in feature_filter.split(','))
                                     else []) +
                                    (['rotated-%d' % orientation]
                                     if (orientation and
                                         not 'rotated-%d' % orientation in alternative_image_features and
                                         not 'rotated-%d' % orientation in feature_filter.split(','))
                                     else []) +
                                    (['deskewed']
                                     if (skew and
                                         not 'deskewed' in alternative_image_features and
                                         not 'deskewed' in feature_filter.split(','))
                                     else []) +
                                    # not a feature to be added, but merely as a fallback position
                                    # to always enter loop at i == len(alternative_image_features)
                                    ['_check']):
            # image geometry vs feature consistency can only be checked
            # after all features on the existing AlternativeImage have
            # been adjusted for in the transform, and when there is a mismatch,
            # additional steps applied here would only repeat the respective
            # error message; so we only check once at the boundary between
            # existing and new features
            # FIXME we should check/enforce consistency when _adding_ AlternativeImage
            if (i == len(alternative_image_features) and
                not (page_xywh['w'] - 2 < page_image.width < page_xywh['w'] + 2 and
                     page_xywh['h'] - 2 < page_image.height < page_xywh['h'] + 2)):
                log.error('page "%s" image (%s; %dx%d) has not been cropped properly (%dx%d)',
                          page_id, page_coords['features'],
                          page_image.width, page_image.height,
                          page_xywh['w'], page_xywh['h'])
            name = "%s for page '%s'" % ("AlternativeImage" if best_image
                                         else "original image", page_id)
            # adjust transform to feature, and ensure feature is applied to image
            if feature == 'cropped':
                page_image, page_coords, page_xywh = _crop(
                    log, name, border, page_image, page_coords,
                    fill=fill, transparency=transparency)
            elif feature == 'rotated-%d' % orientation:
                page_image, page_coords, page_xywh = _reflect(
                    log, name, orientation, page_image, page_coords, page_xywh)
            elif feature == 'deskewed':
                page_image, page_coords, page_xywh = _rotate(
                    log, name, skew, border, page_image, page_coords, page_xywh,
                    fill=fill, transparency=transparency)

        # verify constraints again:
        if not all(feature in page_coords['features']
                   for feature in feature_selector.split(',') if feature):
            raise Exception('Found no AlternativeImage that satisfies all requirements ' +
                            'selector="%s" in page "%s"' % (
                                feature_selector, page_id))
        if any(feature in page_coords['features']
               for feature in feature_filter.split(',') if feature):
            raise Exception('Found no AlternativeImage that satisfies all requirements ' +
                            'filter="%s" in page "%s"' % (
                                feature_filter, page_id))
        page_image.format = 'PNG' # workaround for tesserocr#194
        return page_image, page_coords, page_image_info

    def image_from_segment(self, segment, parent_image, parent_coords,
                           fill='background', transparency=False,
                           feature_selector='', feature_filter=''):
        """Extract an image for a PAGE-XML hierarchy segment from its parent's image.

        Args:
            segment (object): a PAGE segment object
            (i.e. :py:class:`ocrd_models.ocrd_page.TextRegionType`
             or :py:class:`ocrd_models.ocrd_page.TextLineType`
             or :py:class:`ocrd_models.ocrd_page.WordType`
             or :py:class:`ocrd_models.ocrd_page.GlyphType`)
           parent_image (PIL.Image): image of the segment's parent
           parent_coords (dict): a `dict` with information about ``parent_image``:
               - `"transform"`: a `Numpy` array with an affine transform which
                 converts from absolute coordinates to those relative to the image,
                 i.e. after applying all operations (starting with the original image)
               - `"angle"`: the rotation/reflection angle applied to the image so far,
               - `"features"`: the `AlternativeImage` `@comments` for the image, i.e.
                 names of all operations that lead up to this result, and
        Keyword Args:
            fill (string): a `PIL` color specifier
            transparency (boolean): whether to add an alpha channel for masking
            feature_selector (string): a comma-separated list of `@comments` classes
            feature_filter (string): a comma-separated list of `@comments` classes            
        
        Extract a `PIL.Image` from ``segment``, either from `AlternativeImage`
        (if it exists), or producing a new image via cropping from ``parent_image``
        (otherwise). Pass in ``parent_image`` and ``parent_coords`` from the result
        of the next higher-level of this function or from :py:meth:`image_from_page`.

        If ``feature_selector`` and/or ``feature_filter`` is given, then
        select/filter among the cropped ``parent_image`` and the available
        `AlternativeImage`s the richest one which contains all of the selected,
        but none of the filtered features (i.e. `@comments` classes), or
        raise an error.

        (Required and produced features need not be in the same order, so
        ``feature_selector`` is merely a mask specifying Boolean AND, and
        ``feature_filter`` is merely a mask specifying Boolean OR.)

        Cropping uses a polygon mask (not just the bounding box rectangle).
        Areas outside the polygon will be filled according to ``fill``:

        - if `"background"` (the default),
          then fill with the median color of the image;
        - otherwise, use the given color, e.g. `"white"` or `(255,255,255)`.

        Moreover, if ``transparency`` is true, and unless the image already
        has an alpha channel, then add an alpha channel which is fully opaque
        before cropping and rotating. (Thus, unexposed/masked areas will be
        transparent afterwards for consumers that can interpret alpha channels).

        When cropping, compensate any `@orientation` angle annotated for the
        parent (from parent-level deskewing) by rotating the segment coordinates
        in an inverse transformation (i.e. translation to center, then passive
        rotation, and translation back).

        Regardless, if any `@orientation` angle is annotated for the segment
        (from segment-level deskewing), and the chosen image does not have
        the feature `"deskewed"` yet, and unless `"deskewed"` is being filtered,
        then rotate it - compensating for any previous `"angle"`. (However,
        if `@orientation` is above the [-45°,45°] interval, then apply as much
        transposition as possible first, unless `"rotated-90"` / `"rotated-180"` /
        `"rotated-270"` is being filtered.)

        Returns:
            a tuple of
             * the extracted `PIL.Image`,
             * a `dict` with information about the extracted image:
               - `"transform"`: a `Numpy` array with an affine transform which
                   converts from absolute coordinates to those relative to the image,
                   i.e. after applying all parent operations, and then cropping to
                   the segment's bounding box, and deskewing with the segment's
                   orientation angle (if any)
               - `"angle"`: the rotation/reflection angle applied to the image so far,
               - `"features"`: the `AlternativeImage` `@comments` for the image, i.e.
                 names of all applied operations that lead up to this result.

        (These can be used to create a new `AlternativeImage`, or passed down
         for :py:meth:`image_from_segment` calls on lower hierarchy levels.)

        Examples:

         * get a raw (colored) but already deskewed and cropped image::

           image, xywh = workspace.image_from_segment(region,
                 page_image, page_xywh,
                 feature_selector='deskewed,cropped',
                 feature_filter='binarized,grayscale_normalized')
        """
        log = getLogger('ocrd.workspace.image_from_segment')
        # note: We should mask overlapping neighbouring segments here,
        # but finding the right clipping rules can be difficult if operating
        # on the raw (non-binary) image data alone: for each intersection, it
        # must be decided which one of either segment or neighbour to assign,
        # e.g. an ImageRegion which properly contains our TextRegion should be
        # completely ignored, but an ImageRegion which is properly contained
        # in our TextRegion should be completely masked, while partial overlap
        # may be more difficult to decide. On the other hand, on the binary image,
        # we can use connected component analysis to mask foreground areas which
        # originate in the neighbouring regions. But that would introduce either
        # the assumption that the input has already been binarized, or a dependency
        # on some ad-hoc binarization method. Thus, it is preferable to use
        # a dedicated processor for this (which produces clipped AlternativeImage
        # or reduced polygon coordinates).
        segment_image, segment_coords, segment_xywh = _crop(
            log, "parent image for segment '%s'" % segment.id,
            segment, parent_image, parent_coords,
            fill=fill, transparency=transparency)

        # Semantics of missing @orientation at region level could be either
        # - inherited from page level: same as line or word level (no @orientation),
        # - zero (unrotate page angle): different from line or word level (because
        #   otherwise deskewing would never have an effect on lines and words)
        # The PAGE specification is silent here (but does generally not concern itself
        # much with AlternativeImage coordinate consistency).
        # Since our (generateDS-backed) ocrd_page supports the zero/none distinction,
        # we choose the former (i.e. None is inheritance).
        if 'orientation' in segment.__dict__ and segment.get_orientation() is not None:
            # region angle: PAGE @orientation is defined clockwise,
            # whereas PIL/ndimage rotation is in mathematical direction:
            angle = -segment.get_orientation()
            # @orientation is always absolute; if higher levels
            # have already rotated, then we must compensate:
            angle -= parent_coords['angle']
            # map angle from (-180,180] to [0,360], and partition into multiples of 90;
            # but avoid unnecessary large remainders, i.e. split symmetrically:
            orientation = (angle + 45) % 360
            orientation = orientation - (orientation % 90)
            skew = (angle % 360) - orientation
            skew = 180 - (180 - skew) % 360 # map to [-45,45]
            log.debug("segment '%s' has orientation=%d skew=%.2f",
                      segment.id, orientation, skew)
        else:
            orientation = 0
            skew = 0
        segment_coords['angle'] = parent_coords['angle'] # nothing applied yet (depends on filters)

        # initialize AlternativeImage@comments classes from parent, except
        # for those operations that can apply on multiple hierarchy levels:
        segment_coords['features'] = ','.join(
            [feature for feature in parent_coords['features'].split(',')
             if feature in ['binarized', 'grayscale_normalized',
                            'despeckled', 'dewarped']])

        best_image = None
        alternative_images = segment.get_AlternativeImage()
        if alternative_images:
            # (e.g. from segment-level cropping, binarization, deskewing or despeckling)
            best_features = set()
            auto_features = {'cropped', 'deskewed', 'rotated-90', 'rotated-180', 'rotated-270'}
            # search to the end, because by convention we always append,
            # and among multiple satisfactory images we want the most recent,
            # but also ensure that we get the richest feature set, i.e. most
            # of those features that we cannot reproduce automatically below
            for alternative_image in alternative_images:
                features = alternative_image.get_comments()
                if not features:
                    log.warning("AlternativeImage %d for segment '%s' does not have any feature attributes",
                                alternative_images.index(alternative_image) + 1, segment.id)
                    features = ''
                featureset = set(features.split(','))
                if (all(feature in featureset
                        for feature in feature_selector.split(',') if feature) and
                    not any(feature in featureset
                            for feature in feature_filter.split(',') if feature) and
                    len(featureset.difference(auto_features)) >= \
                    len(best_features.difference(auto_features))):
                    best_features = featureset
                    best_image = alternative_image
            if best_image:
                log.debug("Using AlternativeImage %d %s for segment '%s'",
                          alternative_images.index(best_image) + 1,
                          best_features, segment.id)
                segment_image = self._resolve_image_as_pil(alternative_image.get_filename())
                segment_coords['features'] = best_image.get_comments() # including duplicates

        alternative_image_features = segment_coords['features'].split(',')
        for duplicate_feature in set([feature for feature in alternative_image_features
                                      # features relevant in reconstructing coordinates:
                                      if (feature in ['deskewed', 'rotated-90',
                                                      'rotated-180', 'rotated-270'] and
                                          alternative_image_features.count(feature) > 1)]):
            log.error("Duplicate feature %s in AlternativeImage for segment '%s'",
                      duplicate_feature, segment.id)
        for i, feature in enumerate(alternative_image_features +
                                    (['rotated-%d' % orientation]
                                     if (orientation and
                                         not 'rotated-%d' % orientation in alternative_image_features and
                                         not 'rotated-%d' % orientation in feature_filter.split(','))
                                     else []) +
                                    (['deskewed']
                                     if (skew and
                                         not 'deskewed' in alternative_image_features and
                                         not 'deskewed' in feature_filter.split(','))
                                     else []) +
                                    # not a feature to be added, but merely as a fallback position
                                    # to always enter loop at i == len(alternative_image_features)
                                    ['_check']):
            # image geometry vs feature consistency can only be checked
            # after all features on the existing AlternativeImage have
            # been adjusted for in the transform, and when there is a mismatch,
            # additional steps applied here would only repeat the respective
            # error message; so we only check once at the boundary between
            # existing and new features
            # FIXME we should enforce consistency here (i.e. split into transposition
            #       and minimal rotation, rotation always reshapes, rescaling never happens)
            # FIXME: inconsistency currently unavoidable with line-level dewarping (which increases height)
            if (i == len(alternative_image_features) and
                not (segment_xywh['w'] - 2 < segment_image.width < segment_xywh['w'] + 2 and
                     segment_xywh['h'] - 2 < segment_image.height < segment_xywh['h'] + 2)):
                log.error('segment "%s" image (%s; %dx%d) has not been cropped properly (%dx%d)',
                          segment.id, segment_coords['features'],
                          segment_image.width, segment_image.height,
                          segment_xywh['w'], segment_xywh['h'])
            name = "%s for segment '%s'" % ("AlternativeImage" if best_image
                                            else "parent image", segment.id)
            # adjust transform to feature, and ensure feature is applied to image
            if feature == 'rotated-%d' % orientation:
                segment_image, segment_coords, segment_xywh = _reflect(
                    log, name, orientation, segment_image, segment_coords, segment_xywh)
            elif feature == 'deskewed':
                segment_image, segment_coords, segment_xywh = _rotate(
                    log, name, skew, segment, segment_image, segment_coords, segment_xywh,
                    fill=fill, transparency=transparency)

        # verify constraints again:
        if not all(feature in segment_coords['features']
                   for feature in feature_selector.split(',') if feature):
            raise Exception('Found no AlternativeImage that satisfies all requirements' +
                            'selector="%s" in segment "%s"' % (
                                feature_selector, segment.id))
        if any(feature in segment_coords['features']
               for feature in feature_filter.split(',') if feature):
            raise Exception('Found no AlternativeImage that satisfies all requirements ' +
                            'filter="%s" in segment "%s"' % (
                                feature_filter, segment.id))
        segment_image.format = 'PNG' # workaround for tesserocr#194
        return segment_image, segment_coords

    # pylint: disable=redefined-builtin
    def save_image_file(self, image,
                        file_id,
                        file_grp,
                        page_id=None,
                        mimetype='image/png',
                        force=False):
        """Store an image in the filesystem and reference it as new file in the METS.

        Args:
            image (PIL.Image): derived image to save
            file_id (string): `@ID` of the METS `file` to use
            file_grp (string): `@USE` of the METS `fileGrp` to use
        Keyword Args:
            page_id (string): `@ID` in the METS physical `structMap` to use
            mimetype (string): MIME type of the image format to serialize as
            force (boolean): whether to replace any existing `file` with that `@ID`
        
        Serialize the image into the filesystem, and add a `file` for it in the METS.
        Use a filename extension based on ``mimetype``.

        Returns:
            The (absolute) path of the created file.
        """
        log = getLogger('ocrd.workspace.save_image_file')
        if not force and self.overwrite_mode:
            force = True
        image_bytes = io.BytesIO()
        image.save(image_bytes, format=MIME_TO_PIL[mimetype])
        file_path = str(Path(file_grp, '%s%s' % (file_id, MIME_TO_EXT[mimetype])))
        out = self.add_file(
            ID=file_id,
            file_grp=file_grp,
            pageId=page_id,
            local_filename=file_path,
            mimetype=mimetype,
            content=image_bytes.getvalue(),
            force=force)
        log.info('created file ID: %s, file_grp: %s, path: %s',
                 file_id, file_grp, out.local_filename)
        return file_path

def _crop(log, name, segment, parent_image, parent_coords, op='cropped', **kwargs):
    segment_coords = parent_coords.copy()
    # get polygon outline of segment relative to parent image:
    segment_polygon = coordinates_of_segment(segment, parent_image, parent_coords)
    # get relative bounding box:
    segment_bbox = bbox_from_polygon(segment_polygon)
    # get size of the segment in the parent image after cropping
    # (i.e. possibly different from size before rotation at the parent, but
    #  also possibly different from size after rotation below/AlternativeImage):
    segment_xywh = xywh_from_bbox(*segment_bbox)
    # crop, if (still) necessary:
    if (not isinstance(segment, BorderType) or # always crop below page level
        not op in parent_coords['features']):
        if isinstance(segment, BorderType):
            log.info("Cropping %s", name)
            segment_coords['features'] += ',' + op
        # create a mask from the segment polygon:
        segment_image = image_from_polygon(parent_image, segment_polygon, **kwargs)
        # crop to bbox:
        segment_image = crop_image(segment_image, box=segment_bbox)
    else:
        segment_image = parent_image
    # subtract offset from parent in affine coordinate transform:
    # (consistent with image cropping)
    segment_coords['transform'] = shift_coordinates(
        parent_coords['transform'],
        np.array([-segment_bbox[0],
                  -segment_bbox[1]]))
    return segment_image, segment_coords, segment_xywh

def _reflect(log, name, orientation, segment_image, segment_coords, segment_xywh):
    # Transpose in affine coordinate transform:
    # (consistent with image transposition or AlternativeImage below)
    transposition = {
        90: Image.ROTATE_90,
        180: Image.ROTATE_180,
        270: Image.ROTATE_270
    }.get(orientation) # no default
    segment_coords['transform'] = transpose_coordinates(
        segment_coords['transform'], transposition,
        np.array([0.5 * segment_xywh['w'],
                  0.5 * segment_xywh['h']]))
    segment_xywh['w'], segment_xywh['h'] = adjust_canvas_to_transposition(
        [segment_xywh['w'], segment_xywh['h']], transposition)
    segment_coords['angle'] += orientation
    # transpose, if (still) necessary:
    if not 'rotated-%d' % orientation in segment_coords['features']:
        log.info("Transposing %s by %d°", name, orientation)
        segment_image = transpose_image(segment_image, transposition)
        segment_coords['features'] += ',rotated-%d' % orientation
    return segment_image, segment_coords, segment_xywh

def _rotate(log, name, skew, segment, segment_image, segment_coords, segment_xywh, **kwargs):
    # Rotate around center in affine coordinate transform:
    # (consistent with image rotation or AlternativeImage below)
    segment_coords['transform'] = rotate_coordinates(
        segment_coords['transform'], skew,
        np.array([0.5 * segment_xywh['w'],
                  0.5 * segment_xywh['h']]))
    segment_xywh['w'], segment_xywh['h'] = adjust_canvas_to_rotation(
        [segment_xywh['w'], segment_xywh['h']], skew)
    segment_coords['angle'] += skew
    # deskew, if (still) necessary:
    if not 'deskewed' in segment_coords['features']:
        log.info("Rotating %s by %.2f°", name, skew)
        segment_image = rotate_image(segment_image, skew, **kwargs)
        segment_coords['features'] += ',deskewed'
        if (segment and
            (not isinstance(segment, BorderType) or # always crop below page level
             'cropped' in segment_coords['features'])):
            # re-crop to new bbox (which may deviate
            # if segment polygon was not a rectangle)
            segment_image, segment_coords, segment_xywh = _crop(
                log, name, segment, segment_image, segment_coords,
                op='recropped', **kwargs)
    elif (segment and
          (not isinstance(segment, BorderType) or # always crop below page level
           'cropped' in segment_coords['features'])):
        # only shift coordinates as if re-cropping
        _, segment_coords, segment_xywh = _crop(
            log, name, segment, segment_image, segment_coords,
            op='recropped', **kwargs)
    return segment_image, segment_coords, segment_xywh
