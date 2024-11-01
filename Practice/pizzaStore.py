from pizza import Pizza
from abc import ABC, abstractmethod
from pizza import CheesePizza, VeggiePizza, IndianPizza
from ingredientsFactory import IngredientsFactory, NYIngredientsFactory, ChicagoIngredientsFactory


class PizzaStore(ABC):
    def order_pizza(self, pizza_type: str):
        pizza: Pizza
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    # all the object creation part has been handed over to a factory method create_pizza()
    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass


class NYPizzaStore(PizzaStore):
    ingredients_factory: IngredientsFactory = NYIngredientsFactory

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'veggie':
            return VeggiePizza(self.ingredients_factory)
        elif pizza_type == 'indian':
            return IndianPizza(self.ingredients_factory)
        elif pizza_type == 'cheese':
            return CheesePizza(self.ingredients_factory)
        else:
            print("We do not serve that pizza yet!")


class ChicagoPizzaStore(PizzaStore):
    ingredients_factory: IngredientsFactory = ChicagoIngredientsFactory

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'veggie':
            return VeggiePizza(self.ingredients_factory)
        elif pizza_type == 'indian':
            return IndianPizza(self.ingredients_factory)
        elif pizza_type == 'cheese':
            return CheesePizza(self.ingredients_factory)
        else:
            print("We do not serve that pizza yet!")