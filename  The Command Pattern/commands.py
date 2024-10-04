from abc import ABC, abstractmethod
from receivers import Light, Stereo, Fan


#  --------------------------------- create the command interface class ---------------------------------
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


#  --------------------------------- create a default NoCommand class ---------------------------------
class NoCommand(Command):
    def execute(self):
        print("No command has been initialized here yet!  :(")

    def undo(self):
        print("Nothing to undo here!")


#  --------------------------------- create concrete command for LIGHT ON action ---------------------------------
class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# --------------------------------- create concrete command for LIGHT OFF action -----------------------------------
class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# ------------------------------------ concrete command for FAN ON action -----------------------------------
class FanOnCommand(Command):
    fan: Fan

    def __init__(self, fan_type: Fan):
        self.fan = fan_type

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()


#  --------------------------------- concrete command for FAN OFF action ---------------------------------
class FanOffCommand(Command):
    fan: Fan

    def __init__(self, fan_type: Fan):
        self.fan = fan_type

    def execute(self):
        self.fan.off()

    def undo(self):
        self.fan.on()


#  --------------------------------- concrete command for STEREO ON WITH CD action ---------------------------------
class StereoOnWithCD(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume()

    def undo(self):
        self.stereo.off()


#  --------------------------------- concrete command for STEREO ON WITH DVD action ---------------------------------
class StereoOnWithDVD(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_dvd()
        self.stereo.set_volume()

    def undo(self):
        self.stereo.off()


#  --------------------------------- concrete command for STEREO OFF action ---------------------------------
class StereoOffCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume()