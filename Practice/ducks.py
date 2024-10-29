from abc import ABC, abstractmethod
from behaviors import FlyBehavior, QuackBehavior, DefaultFlyBehavior, DefaultQuackBehavior, SuperQuackBehavior, FastFlyBehavior, NoFlyBehavior, SqueakBehavior


class Duck(ABC):
    _fly_behavior: FlyBehavior = DefaultFlyBehavior()
    _quack_behavior: QuackBehavior = DefaultQuackBehavior()

    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior, duck_type: str):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior
        self._duck_type = duck_type

    def swim(self) -> None:
        print('La la la la.... It is a beautiful day!')

    def display(self):
        print(f"Hey! I am a {self._duck_type} duck :)")

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def set_fly_behavior(self, behavior: FlyBehavior):
        self._fly_behavior = behavior

    def set_quack_behavior(self, behavior: QuackBehavior):
        self._quack_behavior = behavior


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(DefaultFlyBehavior(), DefaultQuackBehavior(), 'Mallard')


class ToyDuck(Duck):
    def __init__(self):
        super().__init__(NoFlyBehavior(), SqueakBehavior(), 'Toy')


class SuperDuck(Duck):
    def __init__(self):
        super().__init__(FastFlyBehavior(), SuperQuackBehavior(), 'Super')