from abc import ABC, abstractmethod


# we create a Quackable interface
class Quackable(ABC):

    @abstractmethod
    def quack(self):
        pass


# create concrete ducks
class MallardDuck(Quackable):
    def quack(self):
        print("Quack")


class RedHeadDuck(Quackable):
    def quack(self):
        print("Quack")


class DuckCall(Quackable):
    def quack(self):
        print("Kwak")


class RubberDuck(Quackable):
    def quack(self):
        print("Squeak")