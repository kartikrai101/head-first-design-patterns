from abc import ABC, abstractmethod
from typing import List


# create abstract class for ingredients factory that will be responsible for creating all tne pizza ingredients
class IngredientsFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> List[Veggies]:
        pass

    @abstractmethod
    def create_clams(self) -> Clams:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass


# create concrete ingredient factories
class NYIngredientsFactory(IngredientsFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_clams(self) -> Clams:
        return FreshClams()

    def create_veggies(self) -> List[Veggies]:
        return [Garlic(), Onion(), Mushroom()]


class ChicagoIngredientsFactory(IngredientsFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozarellaCheese()

    def create_clams(self) -> Clams:
        return FrozenClams()

    def create_veggies(self) -> List[Veggies]:
        return [Olive(), Onion(), Spinach()]