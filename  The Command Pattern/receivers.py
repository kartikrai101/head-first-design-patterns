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
    def on(self):
        print("Turning on the stereo!")

    def off(self):
        print("Turning off the stereo!")

    def set_cd(self):
        print("Setting up the CD inside the stereo...")

    def set_dvd(self):
        print("Setting up the DVD inside the stereo...")

    def setRadio(self):
        print("Setting up the radio...")

    def set_volume(self):
        print("Setting up the stereo volume...")


class Fan:
    fan_type: str

    def __init__(self, fan_type: str):
        self.fan_type = fan_type

    def on(self):
        print(f"Turning on the {self.fan_type} fan")

    def off(self):
        print(f'Turning off the {self.fan_type} fan')

