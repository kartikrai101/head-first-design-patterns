import array
from typing import List


# MenuItem class
class MenuItem:
    name: str
    description: str
    price: float
    is_veg: bool

    def __init__(self, name: str, desc: str, price: float, is_veg: bool):
        self.name = name
        self.description = desc
        self.price = price
        self.is_veg = is_veg

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_veg(self) -> bool:
        return self.is_veg


# Breakfast Menu Implementation -> uses List
class BreakfastMenu:
    menu_items: List[MenuItem] = []

    def __init__(self):
        self.add_item("Poha and Chai", "Light savoury poha with a kadak adrak chai!", 40.0, True)
        self.add_item("Peanut Butter and Brown Bread with Classic Coffee", "A meal for kick starting your day!", 45.0, True)
        self.add_item("Omlette and Orange Juice", "A meal for healthy start to your day!", 55.0, False)
        self.add_item("Healthy Bowl with Banana Shake", "The best start for a fantastic day!", 70, True)

    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        new_item = MenuItem(name, desc, price, is_veg)
        self.menu_items.append(new_item)

    def get_menu_items(self):
        return self.menu_items


# Let's create an iterator object that will iterate through the BreakfastMenu
def main():
    # create a BreakfastMenu object
    breakfast_menu = BreakfastMenu()
    it = iter()
