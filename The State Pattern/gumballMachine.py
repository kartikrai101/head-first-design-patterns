class GumballMachine:
    # define values for describing different states the machine can be in
    NO_QUARTER: int = 0
    HAS_QUARTER: int = 1
    SOLD: int = 2
    SOLD_OUT: int = 3

    state: int  # current state of the gumball machine
    gumballs: int  # count of gumballs in machine at any point of time

    def __init__(self, gumballs: int):
        self.gumballs = gumballs
        self.state = self.NO_QUARTER

    def set_state(self, new_state: NO_QUARTER | HAS_QUARTER | SOLD | SOLD_OUT):
        self.state = new_state