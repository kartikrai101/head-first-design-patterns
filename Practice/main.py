from beverage import Beverage, HouseBlend, Decaf, Espresso, DarkRoast
from decorators import Decorator, Milk, Soy, Mocha


def main():
    order1: Beverage = HouseBlend()
    order1_mod1 = Milk(order1)
    order1_mod2 = Soy(order1_mod1)

    print(order1_mod2.get_description())
    print(order1_mod2.cost())
    print(Mocha(order1_mod2).get_description())
    print(Mocha(order1_mod2).cost())


if __name__ == "__main__":
    main()