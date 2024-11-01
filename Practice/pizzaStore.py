from pizza import Pizza
from abc import ABC, abstractmethod


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
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'veggie':
            return NYVeggiePizza()
        elif pizza_type == 'non-veg':
            return NYNonVegPizza()
        elif pizza_type == 'cheese':
            return NYCheesePizza()
        else:
            print("We do not serve that pizza yet!")


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'veggie':
            return ChicagoVeggiePizza()
        elif pizza_type == 'non-veg':
            return ChicagoNonVegPizza()
        elif pizza_type == 'cheese':
            return ChicagoCheesePizza()
        else:
            print("We do not serve that pizza yet!")