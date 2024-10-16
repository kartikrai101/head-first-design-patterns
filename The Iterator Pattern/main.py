from menus import DinerMenu, BreakfastMenu
from waitress import Waitress


def main():
    diner_menu = DinerMenu()
    breakfast_menu = BreakfastMenu()

    waitress = Waitress(diner_menu, breakfast_menu)
    waitress.print_menu()


if __name__ == "__main__":
    main()