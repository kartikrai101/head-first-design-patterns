from abc import ABC, abstractmethod
from menuItem import MenuItem
from typing import List


# create the iterator interface
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# define the iterator class for the Diner Menu
class DinerMenuIterator(Iterator):
    menu_items: List[MenuItem] = []
    position: int = 0

    def __init__(self, items: List[MenuItem]):
        self.menu_items = items

    def next(self):
        menu_item: MenuItem = self.menu_items[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        if self.position >= len(self.menu_items) or self.menu_items[self.position] is None:
            return False
        else:
            return True


# define the iterator class for the Breakfast Menu
class BreakfastMenuIterator(Iterator):
    menu_items: List[MenuItem] = []
    position: int = 0

    def __init__(self, items: List[MenuItem]):
        self.menu_items = items

    def next(self):
        menu_item: MenuItem = self.menu_items[self.position]
        self.position += 1
        return menu_item

    def has_next(self):
        if self.position >= len(self.menu_items) or self.menu_items[self.position] is None:
            return False
        else:
            return True