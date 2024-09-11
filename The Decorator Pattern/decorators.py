from abc import abstractmethod
from beverages import Beverage


# create abstract Decorator class
class Decorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass


# create concrete decorators (condiments)
class Mocha(Decorator):
    beverage: Beverage = None  # this will act as a pointer to the beverage that will be wrapped inside this decorator

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.20


class Milk(Decorator):
    beverage: Beverage = None

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Milk"

    def cost(self):
        return self.beverage.cost() + 0.10


class Soy(Decorator):
    beverage: Beverage = None

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.30


class Whip(Decorator):
    beverage: Beverage

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.15