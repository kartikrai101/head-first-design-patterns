# here we will have different receiver classes - Basically the appliances that we will be controlling
class Light:
    light_type: str

    def __init__(self, light_type: str):
        self.light_type = light_type

    def on(self):
        print(f"Turned on the {self.light_type} light!")

    def off(self):
        print(f"Turned off the {self.light_type} light!")


class Stereo:
    stereo_type: str

    def __init__(self, stereo_type: str):
        self.stereo_type = stereo_type

    def on(self):
        print(f"Turning on the {self.stereo_type} stereo!")

    def off(self):
        print(f"Turning off the {self.stereo_type} stereo!")

    def set_cd(self):
        print(f"Setting up the CD inside the {self.stereo_type} stereo...")

    def set_dvd(self):
        print(f"Setting up the DVD inside the {self.stereo_type} stereo...")

    def set_radio(self):
        print(f"Setting up the {self.stereo_type} radio...")

    def set_volume(self):
        print(f"Setting up the {self.stereo_type} stereo volume...")


class Fan:
    fan_type: str

    def __init__(self, fan_type: str):
        self.fan_type = fan_type

    def on(self):
        print(f"Turning on the {self.fan_type} fan")

    def off(self):
        print(f'Turning off the {self.fan_type} fan')


# a fan class that supports setting up different speeds of the fan
class FancyFan:
    fan_location: str
    speed: int = 0
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0

    def __init__(self, fan_location: str):
        self.fan_location = fan_location

    def high(self):
        self.speed = self.HIGH

    def low(self):
        self.speed = self.LOW

    def medium(self):
        self.speed = self.MEDIUM

    def off(self):
        self.speed = self.OFF
        print(f"Turned the {self.fan_location} off.")

    def get_speed(self) -> int:
        return self.speed