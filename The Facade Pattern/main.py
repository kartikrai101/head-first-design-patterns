# we will use our facade to watch the movie simple way by simply calling the methods on our facade object
from facade import HomeTheaterFacade
from devices import Amplifier, Tuner, DvdPlayer, CdPlayer, Projector, TheaterLights, Screen, PopcornPopper


def main():
    # instantiating our theater components
    amp: Amplifier = Amplifier()
    tuner: Tuner = Tuner()
    dvd: DvdPlayer = DvdPlayer()
    cd: CdPlayer = CdPlayer()
    projector: Projector = Projector()
    lights: TheaterLights = TheaterLights()
    screen: Screen = Screen()
    popper: PopcornPopper = PopcornPopper()

    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, lights, screen, popper)

    # now, let's simply watch a nice movie
    home_theater.watch_movie("Social Network")

    # let's turn off our home theater
    home_theater.end_movie()


if __name__ == "__main__":
    main()