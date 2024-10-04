from abc import ABC, abstractmethod
from receivers import Light, Stereo, Fan, FancyFan


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


# ------------------------------------ concrete command for FANCY FAN HIGH action -----------------------------------
class FancyFanHighCommand(Command):
    fancy_fan: FancyFan
    prev_speed: int  # local state to keep track of the previous speed of the fan

    def __init__(self, fancy_fan: FancyFan):
        self.fancy_fan = fancy_fan

    def execute(self):
        # before we change the speed of the fan, we need to record its previous speed, so we'll be able to undo it
        self.prev_speed = self.fancy_fan.get_speed()
        self.fancy_fan.high()

    def undo(self):
        if self.prev_speed == self.fancy_fan.HIGH:
            self.fancy_fan.high()
        elif self.prev_speed == self.fancy_fan.MEDIUM:
            self.fancy_fan.medium()
        elif self.prev_speed == self.fancy_fan.LOW:
            self.fancy_fan.low()
        elif self.prev_speed == self.fancy_fan.OFF:
            self.fancy_fan.off()
        print(f'The previous speed was: {self.prev_speed}')
        print(f'The new speed is: {self.fancy_fan.get_speed()}')


# ------------------------------------ concrete command for FANCY FAN LOW action -----------------------------------
class FancyFanLowCommand(Command):
    fancy_fan: FancyFan
    prev_speed: int  # local state to keep track of the previous speed of the fan

    def __init__(self, fancy_fan: FancyFan):
        self.fancy_fan = fancy_fan

    def execute(self):
        # before we change the speed of the fan, we need to record its previous speed, so we'll be able to undo it
        self.prev_speed = self.fancy_fan.get_speed()
        self.fancy_fan.low()

    def undo(self):
        print(f'The current speed is: {self.fancy_fan.get_speed()}')
        if self.prev_speed == self.fancy_fan.HIGH:
            self.fancy_fan.high()
        elif self.prev_speed == self.fancy_fan.MEDIUM:
            self.fancy_fan.medium()
        elif self.prev_speed == self.fancy_fan.LOW:
            self.fancy_fan.low()
        elif self.prev_speed == self.fancy_fan.OFF:
            self.fancy_fan.off()
        print(f'The new speed after undo is: {self.fancy_fan.get_speed()}')