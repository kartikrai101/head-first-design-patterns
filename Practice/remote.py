from commands import Command, NoCommand
from typing import List


class Remote:
    on_commands: List[Command] = []
    off_commands: List[Command] = []

    def __init__(self):
        for i in range(0, 7):
            self.on_commands[i] = NoCommand()
            self.off_commands[i] = NoCommand()

    def set_command(self, slot_number: int, on_cmd: Command, off_cmd: Command):
        self.on_commands[slot_number] = on_cmd
        self.off_commands[slot_number] = off_cmd

    def push_on_btn(self, slot_number: int):
        self.on_commands[slot_number].execute()

    def push_off_btn(self, slow_number: int):
        self.off_commands[slow_number].execute()