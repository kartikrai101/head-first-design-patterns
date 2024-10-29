from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str

    def __init__(self, desc: str):
        self.description = desc

    @abstractmethod
    def cost(self):
        pass

    def get_description(self):
        return self.description


# concrete beverage classes
class HouseBlend(Beverage):
    def __init__(self):
        super().__init__('House Blend')

    def cost(self):
        return 1.25


class Espresso(Beverage):
    def __init__(self):
        super().__init__('Espresso')

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        super().__init__('Decaf')

    def cost(self):
        return 0.75


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__('Dark Roast')

    def cost(self):
        return 1.50