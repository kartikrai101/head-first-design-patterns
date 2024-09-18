from abc import ABC, abstractmethod


# Here we will define classes for all the ingredients that we are using in the ingredient factories

# --------------------------- Abstract classes for ingredients ---------------------------
class Dough(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Sauce(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Cheese(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Clams(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Pepperoni(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Veggies(ABC):
    @abstractmethod
    def get_name(self):
        pass


#  --------------------------- Concrete dough classes ---------------------------
class ThinCrustDough(Dough):
    def get_name(self):
        return "Thin Crust"


class ThickCrustDough(Dough):
    def get_name(self):
        return "Thick Crust"


#  --------------------------- Concrete sauce classes ---------------------------
class MarinaraSauce(Sauce):
    def get_name(self):
        return "Marinara"


class PlumTomatoSauce(Sauce):
    def get_name(self):
        return "Plum Tomato"


#  --------------------------- Concrete cheese classes ---------------------------
class ReggianoCheese(Cheese):
    def get_name(self):
        return "Reggiano"


class MozarellaCheese(Cheese):
    def get_name(self):
        return "Mozarella"


#  --------------------------- Concrete clams classes  ---------------------------
class FreshClams(Clams):
    def get_name(self):
        return "Fresh Clams"


class FrozenClams(Clams):
    def get_name(self):
        return "Frozen Clams"


#  --------------------------- Concrete pepperoni classes ---------------------------
class SlicedPepperoni(Pepperoni):
    def get_name(self):
        return "Sliced Pepperoni"


#  --------------------------- Concrete veggies classes ---------------------------
class Onion(Veggies):
    def get_name(self):
        return "Onion"


class Garlic(Veggies):
    def get_name(self):
        return "Garlic"


class Mushroom(Veggies):
    def get_name(self):
        return "Mushroom"


class Olive(Veggies):
    def get_name(self):
        return "Olive"


class Spinach(Veggies):
    def get_name(self):
        return "Spinach"