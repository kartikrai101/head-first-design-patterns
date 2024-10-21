from abc import ABC, abstractmethod


# State Interface containing all the methods(actions) that all the concrete state classes need to define
class State(ABC):
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


#