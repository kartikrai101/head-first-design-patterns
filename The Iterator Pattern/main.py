from menus import DinerMenu, BreakfastMenu, CafeMenu
from waitress import Waitress


def main():
    diner_menu = DinerMenu()
    breakfast_menu = BreakfastMenu()
    cafe_menu = CafeMenu()

    waitress = Waitress([diner_menu, breakfast_menu, cafe_menu])
    waitress.print_menu()


if __name__ == "__main__":
    main()