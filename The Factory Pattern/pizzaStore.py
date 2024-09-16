from abc import ABC, abstractmethod
from pizza import NYPepperoniPizza, NYCheesePizza, NYVeggiePizza, ChicagoCheesePizza, ChicagoVeggiePizza, ChicagoPepperoniPizza, Pizza


# create the abstract pizza store
class PizzaStore(ABC):
    @abstractmethod  # This is the factory method
    def create_pizza(self, pizza_type: str):
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza: Pizza

        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


# create concrete pizza stores
class NYPizzaStore(PizzaStore):
    pizza: Pizza

    def create_pizza(self, pizza_type: str):
        if pizza_type == 'cheese':
            pizza = NYCheesePizza()
        elif pizza_type == 'veggie':
            pizza = NYVeggiePizza()
        elif pizza_type == 'pepperoni':
            pizza = NYPepperoniPizza()
        else:
            print("Sorry! We don't serve that pizza YET ;)")

        return self.pizza


class ChicagoPizzaStore(PizzaStore):
    pizza: Pizza

    def create_pizza(self, pizza_type: str):
        if pizza_type == 'cheese':
            pizza = ChicagoCheesePizza()
        elif pizza_type == 'veggie':
            pizza = ChicagoVeggiePizza()
        elif pizza_type == 'pepperoni':
            pizza = ChicagoPepperoniPizza()
        else:
            print("Sorry! We don't serve that pizza YET ;)")

        return pizza
