from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def display(self):
        pass


class ClamPizza(Pizza):
    def display(self):
        print('I am a clam pizza!')


class PepperoniPizza(Pizza):
    def display(self):
        print('I am a Pepperoni pizza!')


class CheesePizza(Pizza):
    def display(self):
        print('I am a cheese pizza!')


class SimplePizzaFactory:
    def create_pizza(self, pizza_type: str):
        pizza: Pizza = None

        if pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'pepperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'cheese':
            pizza = CheesePizza()

        return pizza


class PizzaStore:
    factory: SimplePizzaFactory

    def __init__(self, pizza_factory: SimplePizzaFactory):
        self.factory = pizza_factory

    def order_pizza(self, pizza_type: str) -> 'Pizza':
        pizza: Pizza

        pizza = self.factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza