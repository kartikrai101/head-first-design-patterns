from devices import Amplifier, Tuner, DvdPlayer, CdPlayer, Projector, TheaterLights, Screen, PopcornPopper


class HomeTheaterFacade:
    amp: Amplifier
    tuner: Tuner
    dvd: DvdPlayer
    cd: CdPlayer
    projector: Projector
    lights: TheaterLights
    screen: Screen
    popper: PopcornPopper

    def __init__(self, amp: Amplifier, tuner: Tuner, dvd: DvdPlayer, cd: CdPlayer, projector: Projector, lights: TheaterLights, screen: Screen, popper: PopcornPopper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper

    def watch_movie(self, movie: str):
        print("Getting ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd(self.dvd)
        self.amp.set_surround_sound()
        self.amp.set_volume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print("Shutting down the movie theater...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()