import io
import re

from .constants import OCRD_WF_SHEBANG
from .ocrd_wf_step import OcrdWfStep

class OcrdWf():

    def __init__(self, steps=None, assignments=None):
        self.steps = steps if steps else []
        self.assignments = assignments if assignments else {}

    @staticmethod
    def parse_file(fname):
        with io.open(fname, mode='r', encoding='utf-8') as f:
            return OcrdWf.parse(f.read())

    @staticmethod
    def parse(src):
        if src[0:len(OCRD_WF_SHEBANG)] != OCRD_WF_SHEBANG:
            raise ValueError("OCRD-WF does not begin with '%s'!" % OCRD_WF_SHEBANG)
        lines_wo_empty = []
        # remove empty lines
        for line in src.split("\n")[1:]:
            if not re.fullmatch(r'^\s*$', line):
                lines_wo_empty.append(line)
        # strip comments
        lines_wo_comment = []
        for line in lines_wo_empty:
            if not re.match(r"^\s*#", line):
                lines_wo_comment.append(line)
        lines_wo_continuation = []
        # line continuation
        n = 0
        while n < len(lines_wo_comment):
            continued_lines = 0
            while lines_wo_comment[n].endswith('\\'):
                lines_wo_comment[n] = re.sub(r"\s*\\$", "", lines_wo_comment[n])
                continued_lines += 1
                lines_wo_comment[n] += re.sub(r"^\s*", " ", lines_wo_comment[n + continued_lines])
            lines_wo_continuation.append(lines_wo_comment[n])
            n += 1 + continued_lines
        assignments = {}
        steps = []
        for line in lines_wo_continuation:
            if re.match(r'^[A-Za-z][A-Za-z0-9]*=', line):
                k, v = line.split('=', 2)
                assignments[k] = v
            else:
                steps.append(OcrdWfStep.parse(line))
        return OcrdWf(assignments=assignments, steps=steps)

    def __str__(self):
        ret = '%s\n' % OCRD_WF_SHEBANG
        for k in self.assignments:
            v = self.assignments[k]
            ret += '%s=%s\n' % (k, v)
        for step in self.steps:
            ret += '%s\n' % str(step)
        return ret
