import json

from ocrd.processor.base import run_cli
from ocrd.resolver import Resolver
from ocrd_utils import getLogger
from ocrd_validators import OcrdWfValidator
from ocrd_models import OcrdWf, OcrdWfStep

def run_tasks(mets, log_level, page_id, task_strs, overwrite=False):
    resolver = Resolver()
    workspace = resolver.workspace_from_url(mets)
    log = getLogger('ocrd.task_sequence.run_tasks')
    steps = [OcrdWfStep.parse(task_str) for task_str in task_strs]
    wf = OcrdWf(steps=steps)

    OcrdWfValidator().validate(wf, workspace, page_id=page_id, overwrite=overwrite)

    # Run the tasks
    for task in steps:

        log.info("Start processing task '%s'", task)

        # execute cli
        returncode, out, err = run_cli(
            task.executable,
            mets,
            resolver,
            workspace,
            log_level=log_level,
            page_id=page_id,
            overwrite=overwrite,
            input_file_grp=','.join(task.input_file_grps),
            output_file_grp=','.join(task.output_file_grps),
            parameter=json.dumps(task.parameters)
        )

        # check return code
        if returncode != 0:
           raise Exception("%s exited with non-zero return value %s. STDOUT:\n%s\nSTDERR:\n%s" % (task.executable, returncode, out, err))

        # reload mets
        workspace.reload_mets()

        # check output file groups are in mets
        for output_file_grp in task.output_file_grps:
            if not output_file_grp in workspace.mets.file_groups:
                raise Exception("Invalid state: expected output file group not in mets: %s\nSTDOUT:\n%s\nSTDERR:\n%s" % (output_file_grp, out, err))

        log.info("Finished processing task '%s'", task)
