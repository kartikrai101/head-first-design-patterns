from typing import List
from menuComponent import MenuComponent


class Menu(MenuComponent):
    menu_components: List[MenuComponent]
    name: str
    description: str

    def __init__(self, name: str, desc: str):
        self.name = name
        self.description = desc
        self.menu_components = []

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def add(self, component: 'MenuComponent'):
        self.menu_components.append(component)

    def remove(self, component: 'MenuComponent'):
        self.menu_components.remove(component)

    def get_child(self, i: int) -> 'MenuComponent':
        return self.menu_components[i]

    def print(self):
        # print the name and description of this menu, then call the print method for all the sub-menus
        print(f"{self.get_name().upper()} || {self.get_description()}")
        print("-----------------------------------------------------------------------------------------")

        menu_iterator = iter(self.menu_components)
        while True:
            try:
                item = next(menu_iterator)
                item.print()
            except StopIteration:
                break