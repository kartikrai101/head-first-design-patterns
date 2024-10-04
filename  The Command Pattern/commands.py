from abc import ABC, abstractmethod
from receivers import Light, Stereo


# create the command interface class
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# create concrete command for LIGHT ON action
class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


# create concrete command for LIGHT OFF action
class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()