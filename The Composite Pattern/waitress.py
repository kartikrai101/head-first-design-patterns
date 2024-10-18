from menuComponent import MenuComponent


class Waitress:
    all_menus: MenuComponent  # root node of the tree

    # the waitress will expect a root node from where you want it to print the menu
    def __init__(self, menus: MenuComponent):
        self.all_menus = menus

    def print_menu(self):
        self.all_menus.print()