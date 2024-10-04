# here we will have different appliance classes
class Light:
    def on(self):
        print("Turned on the light!")

    def off(self):
        print("Turned off the light!")


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