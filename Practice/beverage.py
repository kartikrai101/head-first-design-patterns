from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def boil(self):
        print("Water is boiling...")

    def pour_into_cup(self):
        print("Pouring the drink in cup...")

    @abstractmethod
    def add_condiments(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    def prepare(self):
        self.boil()
        self.brew()
        self.add_condiments()
        self.pour_into_cup()


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Brewing the coffee beans...")

    def add_condiments(self):
        print("Adding sugar and milk...")


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping tea leaves...")

    def add_condiments(self):
        print("Adding lemon and sugar...")