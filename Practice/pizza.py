from abc import ABC, abstractmethod
from ingredients import Sauce, Dough, Cheese, Clam, Pepperoni
from ingredientsFactory import NYIngredientsFactory, ChicagoIngredientsFactory, IngredientsFactory


class Pizza(ABC):
    name: str = ""
    sauce: Sauce = None
    dough: Dough = None
    cheese: Cheese = None
    clam: Clam = None
    pepperoni: Pepperoni = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Baking your pizza...")

    def cut(self):
        print("Cutting your pizza...")

    def box(self):
        print("Packing your pizza...")

    @abstractmethod
    def get_description(self):
        pass


class CheesePizza(Pizza):
    ingredient_factory: IngredientsFactory

    def __init__(self, factory: IngredientsFactory):
        self.ingredient_factory = factory

    def prepare(self):
        print("Preparing: " + self.get_name())
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        self.clam = self.ingredient_factory.create_clam()


class VeggiePizza(Pizza):
    ingredient_factory: IngredientsFactory

    def __init__(self, factory: IngredientsFactory):
        self.ingredient_factory = factory

    def prepare(self):
        print("Preparing: " + self.get_name())
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        self.clam = self.ingredient_factory.create_clam()


class IndianPizza(Pizza):
    ingredient_factory: IngredientsFactory

    def __init__(self, factory: IngredientsFactory):
        self.ingredient_factory = factory

    def prepare(self):
        print("Preparing: " + self.get_name())
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        self.clam = self.ingredient_factory.create_clam()