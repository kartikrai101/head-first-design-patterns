from abc import ABC, abstractmethod


# create abstract Beverage class
class Beverage(ABC):
    description = ""

    def __init__(self, description: str):
        self.description = description

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self):
        pass


# create concrete Beverages
class HouseBlend(Beverage):
    def __init__(self):
        super().__init__("Our House Blend coffee with just the taste that you need to get your day started with!")

    def cost(self) -> float:
        return 1.25


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__("Roasted and enriched with high textured coffee beans for coffee lovers!")

    def cost(self) -> float:
        return 2.55


class Decaf(Beverage):
    def __init__(self):
        super().__init__("Dont worry! You won't need to hold back on your caffeine with this one!")

    def cost(self) -> float:
        return 0.99


class Espresso(Beverage):
    def __init__(self):
        super().__init__("Even Sabrine Carpenter knows which one's the best ;)")

    def cost(self) -> float:
        return 1.15