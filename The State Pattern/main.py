# while creating a state machine, the first thing that we do is:
# 1. We collect all the possible states in which the machine can exist in
# 2. We collect all the possible actions that can be performed on the machine in one state to move it to another possible state
from gumballMachine import GumballMachine


def main():
    machine = GumballMachine(10)

    machine.insert_quarter()
    machine.eject_quarter()
    machine.insert_quarter()
    machine.turn_crank()


if __name__ == "__main__":
    main()