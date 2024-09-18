from abc import ABC, abstractmethod
from pizza import Pizza, CheesePizza, PepperoniPizza, ClamPizza
from ingredient_factories import IngredientsFactory, NYIngredientsFactory, ChicagoIngredientsFactory


# ----------------------------------- abstract pizza store -----------------------------------
class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str):
        pizza: Pizza

        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


#  ----------------------------------- concrete pizza stores -----------------------------------
class NYPizzaStore(PizzaStore):
    pizza: Pizza
    factory: IngredientsFactory

    def __init__(self):
        self.factory = NYIngredientsFactory()

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            self.pizza = CheesePizza(self.factory)
            self.pizza.set_name('NY Cheese Pizza')
        elif pizza_type == 'clam':
            self.pizza = ClamPizza(self.factory)
            self.pizza.set_name('NY Clam Pizza')
        elif pizza_type == 'pepperoni':
            self.pizza = PepperoniPizza(self.factory)
            self.pizza.set_name('NY Pepperoni Pizza')
        else:
            print('Sorry. We do not make that pizza YET ;)')

        return self.pizza


class ChicagoPizzaStore(PizzaStore):
    pizza: Pizza
    factory: IngredientsFactory

    def __init__(self):
        self.factory = ChicagoIngredientsFactory()

    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == 'cheese':
            self.pizza = CheesePizza(self.factory)
            self.pizza.set_name('Chicago Cheese Pizza')
        elif pizza_type == 'clam':
            self.pizza = ClamPizza(self.factory)
            self.pizza.set_name('Chicago Clam Pizza')
        elif pizza_type == 'pepperoni':
            self.pizza = PepperoniPizza(self.factory)
            self.pizza.set_name('Chicago Pepperoni Pizza')
        else:
            print('Sorry. We do not make that pizza YET ;)')

        return self.pizza