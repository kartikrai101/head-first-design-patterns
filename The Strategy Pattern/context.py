from abc import ABC, abstractmethod
from strategies import FlyBehavior, QuackBehavior, DefaultFly, DefaultQuack, FastFly, NoFly, SqueakQuack


# abstract context class
class Duck(ABC):
    # instance variables that will act as pointers to concrete strategies
    _flyBehaviour = DefaultFly()
    _quackBehavior = DefaultQuack()

    def __init__(self, duck_type: str):
        self.duck_type = duck_type

    def swim(self) -> None:
        print('La la la la.... It is a beautiful day!')

    def display(self) -> None:
        print(f'Hello there! I am a {self.duck_type} duck!')

    def quack(self) -> None:
        self._quackBehavior.quack()

    def fly(self) -> None:
        self._flyBehaviour.fly()

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self._flyBehaviour = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self._quackBehavior = quack_behavior


# concrete duck classes
class CommonDuck(Duck):
    def __init__(self):
        super().__init__('Newbie')


class MallardDuck(Duck):
    def __init__(self):
        super().__init__('Mallard')


class RubberDuck(Duck):
    def __init__(self):
        super().__init__('Rubber')