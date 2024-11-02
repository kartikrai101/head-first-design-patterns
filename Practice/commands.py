from abc import ABC, abstractmethod
from receivers import CeilingFan, KitchenLight, FancyFan, Stereo, GarageDoor


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    def execute(self):
        print("No command has been executed here!")

    def undo(self):
        print("Cannot undo anything here!")


# ------------------------------- Concrete ON commands ---------------------------------------------
class CeilingFanOnCommand(Command):
    fan: CeilingFan = None

    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()


class FancyFanOnCommand(Command):
    fan: FancyFan = None
    prev_speed = int

    def __init__(self, fan: FancyFan):
        self.fan = fan

    def execute(self):
        self.fan.get_speed()
        self.fan.on()

    def undo(self):
        if self.prev_speed == self.fan.HIGH:
            self.fan.high()
        elif self.prev_speed == self.fan.MEDIUM:
            self.fan.mid()
        elif self.prev_speed == self.fan.LOW:
            self.fan.low()
        elif self.prev_speed == self.fan.OFF:
            self.fan.off()


class KitchenLightOnCommand(Command):
    light: KitchenLight = None

    def __init__(self, light: KitchenLight):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class StereoOnCommand(Command):
    stereo: Stereo = None

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.insert_cd()
        self.stereo.set_base()
        self.stereo.set_volume()

    def undo(self):
        self.stereo.off()


class GarageDoorOnCommand(Command):
    door: GarageDoor = None

    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.open()
        self.door.turn_light_on()

    def undo(self):
        self.door.turn_light_off()
        self.door.close()


# ------------------------------- Concrete OFF commands ---------------------------------------------
class CeilingFanOffCommand(Command):
    fan: CeilingFan = None

    def __init__(self, fan: CeilingFan):
        self.fan = fan

    def execute(self):
        self.fan.off()

    def undo(self):
        self.fan.on()


class FancyFanOffCommand(Command):
    fan: FancyFan = None

    def __init__(self, fan: FancyFan):
        self.fan = fan

    def execute(self):
        self.fan.off()

    def undo(self):
        self.fan.on()
        self.fan.mid()


class KitchenLightOffCommand(Command):
    light: KitchenLight = None

    def __init__(self, light: KitchenLight):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class StereoOffCommand(Command):
    stereo: Stereo = None

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.insert_cd()
        self.stereo.set_base()
        self.stereo.set_volume()


class GarageDoorOffCommand(Command):
    door: GarageDoor = None

    def __init__(self, door: GarageDoor):
        self.door = door

    def execute(self):
        self.door.turn_light_off()
        self.door.close()

    def undo(self):
        self.door.open()
        self.door.turn_light_on()