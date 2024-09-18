from abc import ABC, abstractmethod
from typing import List
from ingredients import Dough, Sauce, Cheese, Veggies, Clams, Pepperoni
from ingredient_factories import IngredientsFactory


# abstract pizza class
class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    cheese: Cheese
    veggies: List[Veggies]
    clams: Clams
    pepperoni: Pepperoni

    @abstractmethod
    def prepare(self) -> None:
        pass

    def bake(self):
        print(f'Baking the {self.name} pizza at 350 for 20 minutes...')

    def cut(self):
        print(f'Cutting the pizza...')

    def box(self):
        print('Packing your pizza to take away!')

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


# concrete pizzas
class CheesePizza(Pizza):
    factory: IngredientsFactory

    def __init__(self, ingredient_factory: IngredientsFactory):
        self.factory = ingredient_factory

    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        self.dough = self.factory.create_dough()
        self.cheese = self.factory.create_cheese()
        self.sauce = self.factory.create_sauce()


class ClamPizza(Pizza):
    factory: IngredientsFactory

    def __init__(self, ingredient_factory: IngredientsFactory):
        self.factory = ingredient_factory

    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        self.dough = self.factory.create_dough()
        self.cheese = self.factory.create_cheese()
        self.sauce = self.factory.create_sauce()
        self.clams = self.factory.create_clams()


class PepperoniPizza(Pizza):
    factory: IngredientsFactory

    def __init__(self, ingredient_factory: IngredientsFactory):
        self.factory = ingredient_factory

    def prepare(self) -> None:
        print(f'Preparing {self.name}')
        self.dough = self.factory.create_dough()
        self.cheese = self.factory.create_cheese()
        self.sauce = self.factory.create_sauce()
        self.pepperoni = self.factory.create_pepperoni()