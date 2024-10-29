from abc import ABC, abstractmethod
import random

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
    def __init__(self, machine):
        self.gumball_machine = machine

    def insert_quarter(self):
        print("You inserted a quarter in the Gumball Machine.")
        self.gumball_machine.set_state(self.gumball_machine.get_has_quarter_state())

    def eject_quarter(self):
        print("You have not inserted any quarter yet!")

    def turn_crank(self):
        print("You need to insert a quarter to turn the crank!")

    def dispense(self):
        print("You need to insert a quarter, then pull the crank to dispense a gumball.")


# HasQuarter State class
class HasQuarterState(State):
    def __init__(self, machine):
        self.gumball_machine = machine

    def insert_quarter(self):
        print("You have already inserted a quarter in machine.")

    def eject_quarter(self):
        print("Returning your inserted quarter...")
        self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())

    def turn_crank(self):
        print("Turning the crank to dispense a gumball for you...")
        chance = not random.randint(1, 100)
        if chance <= 10 and self.gumball_machine.get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine.get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_state())

    def dispense(self):
        print("No Gumball dispensed.")


# SoldState State class
class SoldState(State):
    def __init__(self, machine):
        self.gumball_machine = machine

    def insert_quarter(self):
        print("Please wait, we are already giving you a gumball.")

    def eject_quarter(self):
        print("Sorry, you already turned the crank!")

    def turn_crank(self):
        print("Turning twice will not get you another gumball :=)")

    def dispense(self):
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() > 0:
            self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
        else:
            print("Oops, out of gumballs!")
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())


# SoldOut State class
class SoldOutState(State):
    def __init__(self, machine):
        self.gumball_machine = machine

    def insert_quarter(self):
        print("Sorry, we are all sold out for now!")

    def eject_quarter(self):
        print("You have not inserted a quarter yet.")

    def turn_crank(self):
        print("You need to insert a quarter first.")

    def dispense(self):
        print("Cannot dispense without pulling the crank.")


# WinnerState class
class WinnerState(State):
    def __init__(self, machine):
        self.gumball_machine = machine

    def insert_quarter(self):
        print("Please wait, we are already giving you a gumball.")

    def eject_quarter(self):
        print("Sorry, you already turned the crank!")

    def turn_crank(self):
        print("Turning twice will not get you another gumball :=)")

    def dispense(self):
        print("You are a WINNER!!! You get 2 gumballs for the price of one!")
        self.gumball_machine.release_ball()
        if self.gumball_machine.get_count() == 0:
            self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())
        else:
            self.gumball_machine.release_ball()
            if self.gumball_machine.get_count() > 0:
                self.gumball_machine.set_state(self.gumball_machine.get_no_quarter_state())
            else:
                self.gumball_machine.set_state(self.gumball_machine.get_sold_out_state())