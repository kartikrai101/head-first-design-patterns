from beverage import Beverage
from abc import ABC, abstractmethod


class Decorator(Beverage):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Mocha(Decorator):
    beverage: Beverage = None

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()


class Soy(Decorator):
    beverage: Beverage = None

    def __init__(self, bev: Beverage):
        self.beverage = bev

    def cost(self):
        return 0.30 + self.beverage.cost()

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"


class Milk(Decorator):
    beverage: Beverage = None

    def __init__(self, bev: Beverage):
        self.beverage = bev

    def cost(self):
        return 0.25 + self.beverage.cost()

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Milk"