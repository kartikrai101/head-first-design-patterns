class CeilingFan:
    def on(self):
        print("Switching on the ceiling fan.")

    def off(self):
        print("Switching off the ceiling fan.")


class KitchenLight:
    def on(self):
        print("Switching on the Kitchen Light.")

    def off(self):
        print("Switching off the Kitchen Light.")


class FancyFan:
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0
    speed: int
    location: str

    def __init__(self, location: str):
        self.location = location

    def on(self):
        print(f"Switching on the Fancy Fan in {self.location}")

    def off(self):
        self.speed = self.OFF
        print(f"Switching off the Fancy Fan in {self.location}.")

    def high(self):
        self.speed = self.HIGH

    def mid(self):
        self.speed = self.MEDIUM

    def low(self):
        self.speed = self.LOW

    def get_speed(self):
        return self.speed


class Stereo:
    def on(self):
        print("Switching on the stereo.")

    def off(self):
        print("Switching off the stereo.")

    def set_volume(self):
        print("Setting up the volume of stereo...")

    def insert_cd(self):
        print("Inserting the CD in stereo...")

    def set_base(self):
        print("Setting up the base...")


class GarageDoor:
    def open(self):
        print("Opening the garage door.")

    def close(self):
        print("Closing the garage door.")

    def turn_light_on(self):
        print("Turning the garage lights on.")

    def turn_light_off(self):
        print("Turning the garage lights off.")