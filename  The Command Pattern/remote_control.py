from typing import List
from commands import Command, NoCommand


# here we will implement the invoker of our system, the Remote Control
class RemoteControl:
    on_commands: List[Command]
    off_commands: List[Command]

    def __init__(self):
        # initialize the remote controller slots with NoCommand objects by default
        no_command: Command = NoCommand()
        self.on_commands = [no_command] * 7
        self.off_commands = [no_command] * 7

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_pushed(self, slot: int):
        self.off_commands[slot].execute()