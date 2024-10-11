from abc import ABC, abstractmethod


#  ---------------------------------- The Template Class  ----------------------------------------
class CaffeineBeverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling the water...")

    def pour_in_cup(self):
        print("Pouring the coffee in cup...")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        print("Adding sugar and milk to the coffee!")


#  ---------------------- creating the coffee class using template CaffeineBeverage class  --------------------
class Coffee(CaffeineBeverage):
    def brew(self):
        print("Brewing the coffee grinds...")

    def add_condiments(self):
        print("Adding sugar and milk to the coffee!")


# ---------------------- creating the tea class using template CaffeineBeverage class ------------------------
class Tea(CaffeineBeverage):
    def brew(self):
        print("Putting the tea bag in the hot water...")

    def add_condiments(self):
        print("Adding lemon to the prepared tea!")