from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    name: str
    sauce: str
    dough: str
    toppings: List[str] = []

    def prepare(self):
        print(f"Preparing: {self.name} Pizza")
        print(f"Tossing dough...")
        print(f"Adding sauce...")
        print(f"Adding toppings...")
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print("Baking your pizza...")

    def cut(self):
        print("Cutting your pizza...")

    def box(self):
        print("Packing your pizza...")

    def get_name(self):
        return self.name


class CheesePizza(Pizza):
    def display(self):
        print("This is your ordered cheese pizza!")


class ClamPizza(Pizza):
    def display(self):
        print("This is your ordered clam pizza!")


class NonVegPizza(Pizza):
    def display(self):
        print("This is your ordered non-veg pizza!")