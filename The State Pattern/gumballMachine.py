from states import State, NoQuarterState, HasQuarterState, SoldState, SoldOutState, WinnerState


class GumballMachine:
    def __init__(self, gumballs: int):
        self.no_quarter_state = NoQuarterState(self)
        self.has_quarter_state = HasQuarterState(self)
        self.sold_state = SoldState(self)
        self.sold_out_state = SoldOutState(self)
        self.winner_state = WinnerState(self)

        self.gumballs = gumballs
        if gumballs > 0:
            self.state = self.no_quarter_state
        else:
            self.state = self.sold_out_state

    def set_state(self, new_state: State):
        self.state = new_state

    def insert_quarter(self):
        self.state.eject_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()

    def release_ball(self):
        print("A gumball is coming out of the slot for you...")
        if self.gumballs != 0:
            self.gumballs -= 1

    # getter methods
    def get_count(self) -> int:
        return self.gumballs

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_no_quarter_state(self):
        return self.no_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_winner_state(self):
        return self.winner_state

    # display methods
    def print_current_state(self):
        if self.state == self.no_quarter_state:
            print("Current State: No Quarter")
        elif self.state == self.has_quarter_state:
            print("Current State: Has Quarter")
        elif self.state == self.sold_state:
            print("Current State: Sold")
        elif self.state == self.sold_out_state:
            print("Current State: Sold Out")
        else:
            print("Current State: Winner!")