from abc import ABC, abstractmethod


# create the command interface class
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# create concrete command for light on
class LightOnCommand(Command):
    light: Light