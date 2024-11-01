from pizza import Pizza, ClamPizza, CheesePizza, NonVegPizza


# here we will create our factory that will be responsible for creating pizza instances for us
class SimplePizzaFactory:
    def create_pizza(self, pizza_type: str):
        pizza: Pizza = None

        # the issue with the following part of the code is that it is open for modification and every time we need to make or add new pizzas, we need to modify this code
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == "non-veg":
            pizza = NonVegPizza()

        return pizza