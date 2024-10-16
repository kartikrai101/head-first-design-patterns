from typing import List
from menuItem import MenuItem


# define class for Diner Menu
class DinerMenu:
    menu_items: List[MenuItem] = []

    def __init__(self):
        self.add_item("Paneer Platter", "Tawa Paneer with Naan or Rice, Salad, Pickle, Dessert of the day", 70.0, True)
        self.add_item("Non-Veg Platter", "Butter Chicken with Naan or Rice, Salad, Soft drink", 90.0, False)
        self.add_item("Chinese Platter", "Triple Fried Rice, Manchurian Gravy/Dry, Soft drink of choice", 80.0, True)
        self.add_item("Healthy Platter", "Steamed Rice, Lettuce, Black Beans, Sour Cream, Corn, Mushrooms, Cheese, Fried Potato, Lime", 110.0, True)

    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        new_item = MenuItem(name, desc, price, is_veg)
        self.menu_items.append(new_item)

    def get_menu_items(self):
        return self.menu_items


# define class for Breakfast Menu
class BreakfastMenu:
    menu_items: List[MenuItem] = []

    def __init__(self):
        self.add_item("Healthy Start", "Overnight Oats Bowl/Omelette, Fruit Bowl, Banana Shake ", 70.0, True)
        self.add_item("Indian Plate", "Poha with lime and peanuts, Ginger Tea", 50.0, True)
        self.add_item("English Breakfast", "Pancake with Strawberry/Blueberry, Coffee", 60.0, True)
        self.add_item("Light Plate", "Peanut Butter and Brown Bread, Coffee/Chai", 40.0, True)

    def add_item(self, name: str, desc: str, price: float, is_veg: bool):
        new_item = MenuItem(name, desc, price, is_veg)
        self.menu_items.append(new_item)

    def get_menu_items(self):
        return self.menu_items