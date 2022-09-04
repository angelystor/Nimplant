from mythic_payloadtype_container.MythicCommandBase import *
import json

class KillArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = []

    async def parse_arguments(self):
        pass


class KillCommand(CommandBase):
    cmd = "kill"
    needs_admin = False
    help_cmd = "kill [pid]"
    description = "Kill a process specified by PID."
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_remove_file = False
    is_upload_file = False
    author = "@NotoriousRebel"
    argument_class = KillArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass