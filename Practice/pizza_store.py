from abc import ABC, abstractmethod


class PizzaStore(ABC):
    pizza: Pizza

    @abstractmethod
    def create_pizza(self, pizza_type: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        # this method will ask the create pizza factory method to create a pizza for it
        self.pizza = self.create_pizza(pizza_type)

        # now that we have the pizza, we can start doing our pizza operations and return it at the end
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza


# create concrete pizza stores
class NYPizzaStore(PizzaStore):
    pizza: Pizza

    def create_pizza(self, pizza_type: str) -> Pizza:
        # using conditions, create the required pizza instance and return it
        if pizza_type == 'cheese':
            self.pizza = NYCheesePizza()
        elif pizza_type == 'veggie':
            self.pizza = NYVeggiePizza()
        else:
            print("We don't serve that pizza, YET ;)")

        return self.pizza


class ChicagoPizzaStore(PizzaStore):
    pizza: Pizza

    def create_pizza(self, pizza_type: str) -> Pizza:
        # using conditions, create the required pizza instance and return it
        if pizza_type == 'cheese':
            self.pizza = ChicagoCheesePizza()
        elif pizza_type == 'veggie':
            self.pizza = ChicagoVeggiePizza()
        else:
            print("We don't serve that pizza, YET ;)")

        return self.pizza