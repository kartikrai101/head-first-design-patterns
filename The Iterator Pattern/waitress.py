from menus import BreakfastMenu, DinerMenu
from iterators import Iterator


# the waitress is expected to print the breakfast menu or the diner menu without having to consult with the cook
class Waitress:
    diner_menu: DinerMenu
    breakfast_menu: BreakfastMenu

    def __init__(self, diner_menu: DinerMenu, breakfast_menu: BreakfastMenu):
        self.diner_menu = diner_menu
        self.breakfast_menu = breakfast_menu

    def print_menu(self):
        diner_menu_it = self.diner_menu.create_iterator()
        breakfast_menu_it = self.breakfast_menu.create_iterator()
        print("---------------------- Here's our today's special BREAKFAST MENU: ---------------------- \n")
        self.display_menu(breakfast_menu_it)
        print("---------------------- Here's our today's special LUNCH MENU: ---------------------- \n")
        self.display_menu(diner_menu_it)

    def display_menu(self, itr: Iterator):
        while itr.has_next():
            item = itr.next()
            print(f"Name: {item.get_name()}")
            print(f"Description: {item.get_description()}")
            print(f"Price: {item.get_price()} \n")
