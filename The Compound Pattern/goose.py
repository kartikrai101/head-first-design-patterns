from ducks import Quackable


class Goose:
    def honk(self):
        print("Honk!")


# we need to create a Goose Adapter if we want to use goose as a duck
class GooseAdapter(Quackable):
    goose: Goose

    def __init__(self, goose: Goose):
        self.goose = goose

    def quack(self):
        self.goose.honk()