# the menu component is the interface which the compositeMenu and menuItems will implement
# Composite Menu -> These are the non-leaf nodes of the object tree that we are creating through this pattern
# Menu Items -> These are the leaf nodes of the object tree which means that they have no children components
# We define all the functions of MenuComponent class and give them some default behavior because there are some methods
# that are irrelevant for a MenuItems, i.e., leaf nodes (like add, remove, get_child) and there are some methods that are irrelevant
# for the CompositeMenu nodes (like get_price, is_veg) but we want both of them to have a common interface

from abc import ABC, abstractmethod


class MenuComponent(ABC):
    # ------------------- methods that will be overridden by all the CompositeMenu nodes ----------------------
    def add(self, component: 'MenuComponent'):
        raise NotImplementedError("This operation is not supported!")

    def remove(self, component: 'MenuComponent'):
        raise NotImplementedError("This operation is not supported!")

    def get_child(self, i: int) -> 'MenuComponent':
        raise NotImplementedError("This operation is not supported!")

    #  ------------------------- methods that will be overridden by all MenuItem nodes -------------------------
    def get_name(self) -> str:
        raise NotImplementedError("This operation is not supported!")

    def get_description(self) -> str:
        raise NotImplementedError("This operation is not supported!")

    def get_price(self) -> float:
        raise NotImplementedError("This operation is not supported!")

    def is_veg(self) -> bool:
        raise NotImplementedError("This operation is not supported!")

    # the print() method needs to be implemented by both the types of nodes
    def print(self):
        raise NotImplementedError("This operation is not supported!")