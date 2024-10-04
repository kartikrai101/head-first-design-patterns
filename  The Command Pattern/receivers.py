# here we will have different receiver classes - Basically the appliances
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

