from abc import ABC, abstractmethod
from typing import List
from menuItem import MenuItem
from iterators import BreakfastMenuIterator, DinerMenuIterator, Iterator, CafeMenuIterator


# define an interface for menus
class Menu(ABC):
    @abstractmethod
    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        pass

    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass


# define class for Diner Menu
class DinerMenu(Menu):
    menu_items: List[MenuItem] = []

    def __init__(self):
        self.add_item("Paneer Platter", "Tawa Paneer with Naan or Rice, Salad, Pickle, Dessert of the day", 70.0, True)
        self.add_item("Non-Veg Platter", "Butter Chicken with Naan or Rice, Salad, Soft drink", 90.0, False)
        self.add_item("Chinese Platter", "Triple Fried Rice, Manchurian Gravy/Dry, Soft drink of choice", 80.0, True)
        self.add_item("Healthy Platter", "Steamed Rice, Lettuce, Black Beans, Sour Cream, Corn, Mushrooms, Cheese, Fried Potato, Lime", 110.0, True)

    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        new_item = MenuItem(name, desc, price, is_veg)
        self.menu_items.append(new_item)

    def create_iterator(self) -> Iterator:
        new_iterator = DinerMenuIterator(self.menu_items)
        return new_iterator

    # in this method, we will use the inbuilt iterator class to return an iterator to our diner menu
    def create_iterator_using_inbuilt_iterator(self):
        return iter(self.menu_items)


# define class for Breakfast Menu
class BreakfastMenu(Menu):
    menu_items: List[MenuItem] = []

    def __init__(self):
        self.add_item("Healthy Start", "Overnight Oats Bowl/Omelette, Fruit Bowl, Banana Shake ", 70.0, True)
        self.add_item("Indian Plate", "Poha with lime and peanuts, Ginger Tea", 50.0, True)
        self.add_item("English Breakfast", "Pancake with Strawberry/Blueberry, Coffee", 60.0, True)
        self.add_item("Light Plate", "Peanut Butter and Brown Bread, Coffee/Chai", 40.0, True)

    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        new_item = MenuItem(name, desc, price, is_veg)
        self.menu_items.append(new_item)

    # this function will create an iterator for the Breakfast Menu and return that iterator to the caller
    def create_iterator(self) -> Iterator:
        new_iterator = BreakfastMenuIterator(self.menu_items)
        return new_iterator

    # in this method, we will use the inbuilt iterator class to return an iterator to our breakfast menu
    def create_iterator_using_inbuilt_iterator(self):
        return iter(self.menu_items)


# define class for Cafe Menu - Uses dict to store menu items {name: menu_item}
class CafeMenu(Menu):
    menu_items: dict

    def __init__(self):
        self.menu_items = {}

        self.add_item("Classic Indian", "Roti/Paranthe, Tadka Dal, Rice, Salad, Potato Sabzi, Rice", 120.0, True)
        self.add_item("Craving Platter", "Pizza of Choice, Soft Drink, Garic Bread, Fries", 100.0, True)
        self.add_item("Healthy Bowl", "Steamed Rice, Lettuce, Black Beans, Sour Cream, Corn, Mushrooms, Cheese, Fried Potato, Lime", 130.0, True)
        self.add_item("Non-Veg Plate", "Butter Chicken with Naan or Rice, Vinegar Onions, Soft drink", 120.0, False)

    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        new_item = MenuItem(name, desc, price, is_veg)
        self.menu_items[name] = new_item

    # method that returns iterator to traverse the menu_items dict
    def create_iterator(self):
        new_iterator = CafeMenuIterator(self.menu_items)
        return new_iterator