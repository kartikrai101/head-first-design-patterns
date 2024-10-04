from typing import List
from commands import Command


# here we will implement the invoker of our system, the Remote Control
class RemoteControl:
    onCommands: List[Command]
    offCommands: List[Command]

    def __init__(self):
        no_command: Command = NoCommand()
        for i in range(0, 7):
            self.onCommands[i] = no_command
            self.offCommands[i] = no_command

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.onCommands[slot] = on_command
        self.offCommands[slot] = off_command

    def on_button_pushed(self, slot: int):
        self.onCommands[slot].execute()

    def off_button_pushed(self, slot: int):
        self.offCommands[slot].execute()