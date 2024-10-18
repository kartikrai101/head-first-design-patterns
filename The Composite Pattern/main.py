from waitress import Waitress
from compositeMenu import Menu
from menuComponent import MenuComponent
from menuItem import MenuItem


def main():
    # let's create all the individual menu objects first
    breakfast_menu: MenuComponent = Menu("Today's Special Breakfast", "Start your day with a scrumptious meal!")
    lunch_menu: MenuComponent = Menu("Today's Special Lunch", "Let's fill up that tummy of yours!")
    dinner_menu: MenuComponent = Menu("Today's Special Dinner", "Exquisite dinner experience for today.")
    dessert_menu: MenuComponent = Menu("Today's Special Dessert", "There's always some room for dessert!")

    # defining the root component (node) of our tree
    all_menus: MenuComponent = Menu("All Menus", "Here are our today's specials")

    # add the different menus to the root node and the dessert menu to the dinner menu
    all_menus.add(breakfast_menu)
    all_menus.add(lunch_menu)
    all_menus.add(dinner_menu)

    # create menu items for different menus
    breakfast_menu_item1 = MenuItem("Healthy Start", "Overnight Oats Bowl/Omelette, Fruit Bowl, Banana Shake ", 70.0, True)
    breakfast_menu_item2 = MenuItem("Indian Plate", "Poha with lime and peanuts, Ginger Tea", 50.0, True)
    breakfast_menu_item3 = MenuItem("English Breakfast", "Pancake with Strawberry/Blueberry, Coffee", 60.0, True)
    breakfast_menu_item4 = MenuItem("Light Plate", "Peanut Butter and Brown Bread, Coffee/Chai", 40.0, True)

    lunch_menu_item1 = MenuItem("Paneer Platter", "Tawa Paneer with Naan or Rice, Salad, Pickle, Dessert of the day", 70.0, True)
    lunch_menu_item2 = MenuItem("Non-Veg Platter", "Butter Chicken with Naan or Rice, Salad, Soft drink", 90.0, False)
    lunch_menu_item3 = MenuItem("Chinese Platter", "Triple Fried Rice, Manchurian Gravy/Dry, Soft drink of choice", 80.0, True)
    lunch_menu_item4 = MenuItem("Healthy Platter", "Steamed Rice, Lettuce, Black Beans, Sour Cream, Corn, Mushrooms, Cheese, Fried Potato, Lime", 110.0, True)

    dinner_menu_item1 = MenuItem("Classic Indian", "Roti/Paranthe, Tadka Dal, Rice, Salad, Potato Sabzi, Rice", 120.0, True)
    dinner_menu_item2 = MenuItem("Craving Platter", "Pizza of Choice, Soft Drink, Garic Bread, Fries", 100.0, True)
    dinner_menu_item3 = MenuItem("Healthy Bowl", "Steamed Rice, Lettuce, Black Beans, Sour Cream, Corn, Mushrooms, Cheese, Fried Potato, Lime", 130.0,True)
    dinner_menu_item4 = MenuItem("Non-Veg Plate", "Butter Chicken with Naan or Rice, Vinegar Onions, Soft drink", 120.0, False)

    dessert_menu_item1 = MenuItem("Ice Cream", "Nutty Almond and Coffee flavour", 40, True)
    dessert_menu_item2 = MenuItem("Indian Classic", "Kesar Gulab Jamun, Rabri", 50, True)
    dessert_menu_item3 = MenuItem("Cheesecake", "Cheesecake New York Style", 90, True)

    # add the menu items to the different menus
    breakfast_menu.add(breakfast_menu_item1)
    breakfast_menu.add(breakfast_menu_item2)
    breakfast_menu.add(breakfast_menu_item3)
    breakfast_menu.add(breakfast_menu_item4)

    lunch_menu.add(lunch_menu_item1)
    lunch_menu.add(lunch_menu_item2)
    lunch_menu.add(lunch_menu_item3)
    lunch_menu.add(lunch_menu_item4)

    dinner_menu.add(dinner_menu_item1)
    dinner_menu.add(dinner_menu_item2)
    dinner_menu.add(dinner_menu_item3)
    dinner_menu.add(dinner_menu_item4)
    dinner_menu.add(dessert_menu)  # add the dessert menu as a sub-menu inside the dinner menu

    dessert_menu.add(dessert_menu_item1)
    dessert_menu.add(dessert_menu_item2)
    dessert_menu.add(dessert_menu_item3)

    # create a waitress instance
    waitress = Waitress(all_menus)
    waitress.print_menu()


if __name__ == "__main__":
    main()