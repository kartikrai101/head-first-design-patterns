from abc import ABC, abstractmethod


class Sauce(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Cheese(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Clam(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Pepperoni(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Dough(ABC):
    @abstractmethod
    def get_name(self):
        pass


class NYSauce(Sauce):
    def get_name(self):
        return "NY Sauce"


class ChicagoSauce(Sauce):
    def get_name(self):
        return "Chicago Sauce"


class NYDough(Dough):
    def get_name(self):
        return "NY Dough"


class NYPepperoni(Pepperoni):
    def get_name(self):
        return "NY Pepperoni"


class NYClam(Clam):
    def get_name(self):
        return "NY Clam"


class NYCheese(Cheese):
    def get_name(self):
        return "NY Cheese"


class ChicagoDough(Dough):
    def get_name(self):
        return "Chicago Dough"


class ChicagoPepperoni(Pepperoni):
    def get_name(self):
        return "Chicago Pepperoni"


class ChicagoClam(Clam):
    def get_name(self):
        return "Chicago Clam"


class ChicagoCheese(Cheese):
    def get_name(self):
        return "Chicago Cheese"