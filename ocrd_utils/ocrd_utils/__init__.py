"""
Utility functions and constants usable in various circumstances.

* ``coordinates_of_segment``, ``coordinates_for_segment``

    These functions convert polygon outlines for PAGE elements on all hierarchy
    levels below page (i.e. region, line, word, glyph) between relative coordinates
    w.r.t. a corresponding image and absolute coordinates w.r.t. the top-level image.
    This includes rotation and offset correction, based on affine transformations.
    (Used by ``Workspace`` methods ``image_from_page`` and ``image_from_segment``)

* ``rotate_coordinates``, ``shift_coordinates``, ``transpose_coordinates``, ``transform_coordinates``

    These backend functions compose affine transformations for reflection, rotation
    and offset correction of coordinates, or apply them to a set of points. They can be
    used to pass down the coordinate system along with images (both invariably sharing
    the same operations context) when traversing the element hierarchy top to bottom.
    (Used by ``Workspace`` methods ``image_from_page`` and ``image_from_segment``).

* ``rotate_image``, ``crop_image``, ``transpose_image``

    These PIL.Image functions are safe replacements for the ``rotate``, ``crop``, and
    ``transpose`` methods.

* ``image_from_polygon``, ``polygon_mask``

    These functions apply polygon masks to PIL.Image objects.

* ``xywh_from_points``, ``points_from_xywh``, ``polygon_from_points`` etc.

   These functions have the syntax ``X_from_Y``, where ``X``/``Y`` can be

    * ``bbox`` is a 4-tuple of integers x0, y0, x1, y1 of the bounding box (rectangle)

      (used by PIL.Image)
    * ``points`` a string encoding a polygon: ``"0,0 100,0 100,100, 0,100"``

      (used by PAGE-XML)
    * ``polygon`` is a list of 2-lists of integers x, y of points forming an (implicitly closed) polygon path: ``[[0,0], [100,0], [100,100], [0,100]]``

      (used by opencv2 and higher-level coordinate functions in ocrd_utils)
    * ``xywh`` a dict with keys for x, y, width and height: ``{'x': 0, 'y': 0, 'w': 100, 'h': 100}``

      (produced by tesserocr and image/coordinate recursion methods in ocrd.workspace)
    * ``x0y0x1y1`` is a 4-list of strings ``x0``, ``y0``, ``x1``, ``y1`` of the bounding box (rectangle)

      (produced by tesserocr)
    * ``y0x0y1x1`` is the same as ``x0y0x1y1`` with positions of ``x`` and ``y`` in the list swapped

* ``is_local_filename``, ``safe_filename``, ``abspath``, ``get_local_filename``

    FS-related utilities

* ``is_string``, ``membername``, ``concat_padded``, ``nth_url_segment``, ``remove_non_path_from_url``, ``parse_json_string_with_comments``, ``parse_json_string_or_file``, ``set_json_key_value_overrides``, ``assert_file_grp_cardinality``, ``make_file_id``

    String and OOP utilities

* ``MIMETYPE_PAGE``, ``EXT_TO_MIME``, ``MIME_TO_EXT``, ``VERSION``

    Constants

* ``logging``, ``setOverrideLogLevel``, ``getLevelName``, ``getLogger``, ``initLogging``

    Exports of ocrd_utils.logging

* ``deprecated_alias``

    Decorator to mark a kwarg as deprecated
"""

from .constants import (
    VERSION,
    MIMETYPE_PAGE,
    EXT_TO_MIME,
    MIME_TO_EXT,
    PIL_TO_MIME,
    MIME_TO_PIL,
    REGEX_PREFIX,
    LOG_FORMAT,
    LOG_TIMEFMT)

from .deprecate import (
    deprecated_alias)

from .image import (
    adjust_canvas_to_rotation,
    adjust_canvas_to_transposition,
    bbox_from_points,
    bbox_from_polygon,
    bbox_from_xywh,
    coordinates_for_segment,
    coordinates_of_segment,
    crop_image,
    image_from_polygon,
    points_from_bbox,
    points_from_polygon,
    points_from_x0y0x1y1,
    points_from_xywh,
    points_from_y0x0y1x1,
    polygon_from_bbox,
    polygon_from_points,
    polygon_from_x0y0x1y1,
    polygon_from_xywh,
    polygon_mask,
    rotate_coordinates,
    rotate_image,
    shift_coordinates,
    transform_coordinates,
    transpose_coordinates,
    transpose_image,
    xywh_from_bbox,
    xywh_from_points,
    xywh_from_polygon)

from .introspect import (
    set_json_key_value_overrides,
    membername)

from .logging import (
    logging,
    getLogger,
    getLevelName,
    initLogging,
    setOverrideLogLevel)

from .os import (
    abspath,
    pushd_popd,
    unzip_file_to_dir)

from .str import (
    assert_file_grp_cardinality,
    concat_padded,
    equals_or_regex_matches,
    get_local_filename,
    is_local_filename,
    is_string,
    make_file_id,
    nth_url_segment,
    parse_json_string_or_file,
    parse_json_string_with_comments,
    remove_non_path_from_url,
    safe_filename)
