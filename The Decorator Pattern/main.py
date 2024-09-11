from beverages import HouseBlend, DarkRoast, Espresso
from decorators import Mocha, Milk, Soy, Whip


def main():
    # create a beverage
    drink1 = HouseBlend()
    print(drink1.cost())
    drink2 = DarkRoast()
    print(drink2.cost())
    drink3 = Espresso()
    print(drink3.cost())

    # add mocha in drink1
    modified_drink1 = Mocha(drink1)
    # get the new description
    print(modified_drink1.get_description())
    # get new cost of the drink
    print(modified_drink1.cost())

    # add Soy and Mocha in drink2
    modified_drink2 = Soy(Mocha(drink2))
    # get the new description
    print(modified_drink2.get_description())
    # get new cost of the drink
    print(modified_drink2.cost())

    # add milk and whip in drink3
    modified_drink3 = Whip(Milk(drink3))
    # get the new description
    print(modified_drink3.get_description())
    # get new cost of the drink
    print(modified_drink3.cost())


if __name__ == "__main__":
    main()