from abc import ABC, abstractmethod
from gumballMachine import GumballMachine


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


# NoQuarter State class
class NoQuarterState(State):
    gumball_machine: GumballMachine

    def insert_quarter(self):
        print("You inserted a quarter in the Gumball Machine.")
        self.gumball_machine.set_state(self.gumball_machine.HAS_QUARTER)

    def eject_quarter(self):
        print("You have not inserted any quarter yet!")

    def turn_crank(self):
        print("You need to insert a quarter to turn the crank!")

    def dispense(self):
        print("You need to insert a quarter, then pull the crank to dispense a gumball.")