from distutils.spawn import find_executable as which # pylint: disable=import-error,no-name-in-module

from ocrd_models import ValidationReport

from .workspace_validator import WorkspaceValidator
from .parameter_validator import ParameterValidator

class OcrdWfValidator():

    def __init__(self):
        pass

    def validate(self, wf, workspace, overwrite=False, page_id=None):
        report = ValidationReport()
        report.merge_report(self.is_resolveable(wf))
        report.merge_report(self.is_consistent(wf, workspace, overwrite=overwrite, page_id=page_id))
        if not report.is_valid:
            raise Exception(report.errors)
        return report

    def is_resolveable(self, wf):
        report = ValidationReport()
        for step in wf.steps:
            report.merge_report(self.step_is_resolveable(step))
        return report

    def is_consistent(self, wf, workspace, overwrite=False, page_id=None):
        report = ValidationReport()
        prev_output_file_grps = workspace.mets.file_groups

        first_task = wf.steps[0]

        # first task: check input/output file groups from METS
        WorkspaceValidator.check_file_grp(workspace, first_task.input_file_grps, '' if overwrite else first_task.output_file_grps, page_id, report)

        prev_output_file_grps += first_task.output_file_grps
        for task in wf.steps[1:]:
            report.merge_report(self.step_is_consistent(task))
            # check either existing fileGrp or output-file group of previous task matches current input_file_group
            for input_file_grp in task.input_file_grps:
                if not input_file_grp in prev_output_file_grps:
                    report.add_error("Input file group not contained in METS or produced by previous steps: %s" % input_file_grp)
            if not overwrite:
                WorkspaceValidator.check_file_grp(workspace, [], task.output_file_grps, page_id, report)
            # TODO disable output_file_grps checks once CLI parameter 'overwrite' is implemented
            # XXX Thu Jan 16 20:14:17 CET 2020 still not sufficiently clever.
            #  if len(prev_output_file_grps) != len(set(prev_output_file_grps)):
            #      report.add_error("Output file group specified multiple times: %s" % 
            #          [grp for grp, count in Counter(prev_output_file_grps).items() if count >= 2])
            prev_output_file_grps += task.output_file_grps
        if not report.is_valid:
            raise Exception("Invalid task sequence input/output file groups: %s" % report.errors)
        return report
        return report

    def step_is_resolveable(self, step):
        report = ValidationReport()
        if not which(step.executable):
            report.add_error("Unresolveable! Executable not found in PATH: %s" % step.executable)
            return report
        # TODO uncomment and adapt once OCR-D/spec#121 lands
        # # make implicit input/output groups explicit by defaulting to what is
        # # provided in ocrd-tool.json
        # actual_output_grps = [*self.ocrd_tool_json['output_file_grp']]
        # for i, grp in enumerate(self.output_file_grps):
            # actual_output_grps[i] = grp
        # self.output_file_grps = actual_output_grps
        # actual_input_grps = [*self.ocrd_tool_json['input_file_grp']]
        # for i, grp in enumerate(self.input_file_grps):
            # actual_input_grps[i] = grp
        # self.input_file_grps = actual_input_grps
        param_validator = ParameterValidator(step.ocrd_tool_json)
        report = param_validator.validate(step.parameters)
        return report

    def step_is_consistent(self, step):
        report = ValidationReport()
        if not step.input_file_grps:
            report.add_error("Inconsistent: Task must have input file group")
        # TODO remove once OCR-D/spec#121 lands
        if 'output_file_grp' in step.ocrd_tool_json and not step.output_file_grps:
            report.add_error("Inconsistent: Processor requires output_file_grp but none was provided.")
        return report
