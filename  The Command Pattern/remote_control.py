from typing import List


# here we will implement the invoker of our system, the Remote Control
class RemoteControl:
    onCommands: List[Command]
    offCommands: List[Command]

    def __init__(self):
        noCommand: Command = NoCommand()
        for i in range(0, 7):
            self.onCommands[i] = noCommand
            self.offCommands[i] = noCommand

    def set_command(self, slot: int, onCommand: Command, offCommand: Command):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def on_button_pushed(self, slot: int):
        self.onCommands[slot].execute()

    def off_button_pushed(self, slot: int):
        self.offCommands[slot].execute()