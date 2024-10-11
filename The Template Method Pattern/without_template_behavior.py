# here we will implement the coffee and tea class without the help of the template class
class Coffee:
    def prepare(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self):
        print("Boiling the water...")

    def brew_coffee_grinds(self):
        print("Brewing the coffee grinds...")

    def pour_in_cup(self):
        print("Pouring the coffee in cup...")

    def add_sugar_and_milk(self):
        print("Adding sugar and milk to the coffee!")


class Tea:
    def prepare(self):
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def boil_water(self):
        print("Boiling the water...")

    def steep_tea_bag(self):
        print("Putting the tea bag in the hot water...")

    def pour_in_cup(self):
        print("Pouring the coffee in cup...")

    def add_lemon(self):
        print("Adding lemon to the prepared tea!")