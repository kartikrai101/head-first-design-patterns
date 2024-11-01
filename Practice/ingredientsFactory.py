from abc import ABC, abstractmethod
from ingredients import NYDough, NYClam, NYSauce, NYCheese, NYPepperoni, ChicagoClam, ChicagoDough, ChicagoSauce, ChicagoPepperoni, ChicagoCheese


class IngredientsFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass


class NYIngredientsFactory(IngredientsFactory):
    def create_dough(self):
        return NYDough()

    def create_cheese(self):
        return NYCheese()

    def create_clam(self):
        return NYClam()

    def create_pepperoni(self):
        return NYPepperoni()

    def create_sauce(self):
        return NYSauce()


class ChicagoIngredientsFactory(IngredientsFactory):
    def create_dough(self):
        return ChicagoDough()

    def create_cheese(self):
        return ChicagoCheese()

    def create_clam(self):
        return ChicagoClam()

    def create_pepperoni(self):
        return ChicagoPepperoni()

    def create_sauce(self):
        return ChicagoSauce()