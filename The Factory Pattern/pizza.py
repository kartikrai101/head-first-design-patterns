from abc import ABC, abstractmethod
from typing import List


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]

    def prepare(self):
        print(f'Preparing {self.name}')
        print(f'Tossing dough...')
        print(f'Adding sauce...')
        print(f'Adding toppings: ')
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Packing the pizza in Kartik')

    def get_name(self):
        return self.name


# create concrete pizzas
class NYCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.sauce = "Marinara Sauce"
        self.dough = "Thin crust dough"

        self.toppings.append("Olives")


class NYVeggiePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Veggie Pizza"
        self.sauce = "Tango Sauce"
        self.dough = "Thin crust dough"

        self.toppings.append("Onion")


class NYPepperoniPizza(Pizza):
    def __init__(self):
        self.name = "NY Style Pepperoni Pizza"
        self.sauce = "SubChilli Sauce"
        self.dough = "Thin crust dough"

        self.toppings.append("Pepperoni")


class ChicagoCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Cheese and Sauce Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Mint")


class ChicagoVeggiePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Mint")


class ChicagoPepperoniPizza(Pizza):
    def __init__(self):
        self.name = "Chicago Pepperoni Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Mint")