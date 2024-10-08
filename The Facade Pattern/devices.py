# this file contains various individual device classes that are required in a home theater
class Screen:
    def up(self):
        print("Turning up the theater screen...")

    def down(self):
        print("Turning down the theater screen...")


class PopcornPopper:
    def on(self):
        print("Turning on the popcorn machine.")

    def off(self):
        print("Turning off the popcorn machine")

    def pop(self):
        print("Popping the popcorns....")


class TheaterLights:
    def on(self):
        print("Turning on the theater lights.")

    def off(self):
        print("Turning off the theater lights.")

    def dim(self):
        print("Dimming the theater lights...")


class Tuner:
    amplifier: "Amplifier"

    def on(self):
        print("Turning on the tuner")

    def off(self):
        print("Turning off the tuner")

    def set_am(self):
        print("Setting up the AM")

    def set_fm(self):
        print("Setting up the FM")

    def set_freqency(self, freq: int):
        print(f"Setting up the frequency to {freq}")


class CdPlayer:
    amplifier: "Amplifier"

    def on(self):
        print("Turning on the CD Player.")

    def off(self):
        print("Turning off the CD Player.")

    def eject(self):
        print("Ejecting the CD...")

    def pause(self):
        print("Pausing the show.")

    def play(self):
        print("Playing the show.")

    def stop(self):
        print("Stopped the show.")


class DvdPlayer:
    amplifier: "Amplifier"

    def on(self):
        print("Turning on the CD Player.")

    def off(self):
        print("Turning off the CD Player.")

    def eject(self):
        print("Ejecting the CD...")

    def pause(self):
        print("Pausing the show.")

    def play(self):
        print("Playing the show.")

    def stop(self):
        print("Stopped the show.")

    def set_surround_sound(self):
        print("Setting up the Surround Sound feature...")

    def set_two_channel_audio(self):
        print("Activating the two channel audio...")


class Projector:
    dvd_player: DvdPlayer

    def on(self):
        print("Turning on the projector")

    def off(self):
        print("Turning off the projector")

    def tv_mode(self):
        print("Turning on TV Mode on the projector")

    def wide_screen_mode(self):
        print("Turning on Wide Screen Mode on the projector")


class Amplifier:
    tuner: Tuner
    dvd_player: DvdPlayer
    cd_player: CdPlayer
    mode = None

    def __init__(self, tuner, dvd_player, cd_player):
        self.tuner = tuner
        self.dvd_player = dvd_player
        self.cd_player = cd_player

    def on(self):
        print("Tuning on the amplifier")

    def off(self):
        print("Turning off the amplifier")

    def set_cd(self):
        print("Setting up the CD mode for the amplifier")
        self.cd_player.on()

    def set_dvd(self):
        print("Setting up the DVD mode for the amplifier")
        self.dvd_player.on()

    def set_stereo_sound(self):
        print("Setting up stereo sound for the amplifier")

    def set_surround_sound(self):
        print("Setting up the surround sound for the amplifier")

    def set_tuner(self):
        print("Setting up the tuner")
        self.tuner.on()

    def set_volume(self):
        print("Setting up the volume")
