from ducks import Quackable


# create a decorator class that will act as a wrapper for ducks to add additional functionalities to the ducks
class QuackCounter(Quackable):
    # we need to have a reference to the duck that this decorator is wrapping
    duck: Quackable
    number_of_quacks: int

    def __init__(self, duck: Quackable):
        self.duck = duck

    def quack(self):
        self.duck.quack()
        self.number_of_quacks += 1

    def get_quacks(self):
        return self.number_of_quacks