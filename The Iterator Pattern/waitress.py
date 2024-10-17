from typing import List
from menus import BreakfastMenu, DinerMenu, CafeMenu, Menu
from iterators import Iterator


# the waitress is expected to print the breakfast menu or the diner menu without having to consult with the cook
class Waitress:
    menu_list: List[Menu] = []

    def __init__(self, menus: List[Menu]):
        self.menu_list = menus

    def print_menu(self):
        for menu in self.menu_list:
            menu_iterator = menu.create_iterator()
            self.display_menu(menu_iterator)

    def display_menu(self, itr: Iterator):
        while itr.has_next():
            item = itr.next()
            print(f"Name: {item.get_name()}")
            print(f"Description: {item.get_description()}")
            print(f"Price: {item.get_price()} \n")
