"""
Technical image metadata
"""

from math import sqrt
from io import BytesIO
from subprocess import run, PIPE
from distutils.spawn import find_executable as which
from ocrd_utils import getLogger

class OcrdExif():
    """Represents technical image metadata.

    Members:

    - `width` / `height`: pixel dimensions
    - `photometricInterpretation`: pixel type/depth, e.g.
      '1' for b/w,
      'L' for 8-bit grayscale,
      'RGB' for 24-bit truecolor,
      'I' for 32-bit signed integer grayscale,
      'F' for floating-point grayscale
      (see PIL concept `mode`)
    - `resolution` / `xResolution` / `yResolution`: pixel density
    - `resolutionUnit`: unit of measurement (either `inches` or `cm`)

    """

    def __init__(self, img):
        """
        Arguments:
            img (PIL.Image): PIL image technical metadata is about.
        """
        #  print(img.__dict__)
        self.width = img.width
        self.height = img.height
        self.photometricInterpretation = img.mode
        self.n_frames = img.n_frames if 'n_frames' in img.__dict__ else 1
        for prop in ['compression', 'photometric_interpretation']:
            setattr(self, prop, img.info[prop] if prop in img.info else None)
        if img.filename:
            ret = run(['identify', '-format', r'%[resolution.x] %[resolution.y] %U', img.filename], check=False, stderr=PIPE, stdout=PIPE)
        else:
            with BytesIO() as bio:
                img.save(bio, format=img.format)
                ret = run(['identify', '-format', r'%[resolution.x] %[resolution.y] %U', '/dev/stdin'], check=False, stderr=PIPE, stdout=PIPE, input=bio.getvalue())
        if ret.returncode:
            stderr = ret.stderr.decode('utf-8')
            if not which('identify'):
                raise Exception("The 'identify' command is not available. Install with 'sudo apt install imagemagick'")
            if 'no decode delegate for this image format' in stderr:
                getLogger('ocrd_exif').warning("ImageMagick does not support the '%s' image format. ", img.format)
            else:
                getLogger('ocrd_exif').error("identify exited with non-zero %s: %s", ret.returncode, stderr)
            self.xResolution = self.yResolution = 1
            self.resolutionUnit = 'inches'
        else:
            tokens = ret.stdout.decode('utf-8').split(' ', 3)
            self.xResolution = max(int(float(tokens[0])), 1)
            self.yResolution = max(int(float(tokens[1])), 1)
            self.resolutionUnit = 'inches' if tokens[2] == 'undefined' else \
                                  'cm' if tokens[2] == 'PixelsPerCentimeter' else \
                                  'inches'
        self.resolution = round(sqrt(self.xResolution * self.yResolution))

    def to_xml(self):
        """
        Serialize all properties as XML
        """
        ret = '<exif>'
        for k in self.__dict__:
            ret += '<%s>%s</%s>' % (k, self.__dict__[k], k)
        ret += '</exif>'
        return ret
