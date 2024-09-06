from abc import ABC, abstractmethod


# The abstract FlyBehaviour class
class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass


# Concrete flying classes
class NoFly(FlyBehaviour):
    def fly(self):
        print("This duck cannot fly! Don't try to kill it :=)")


class FastFly(FlyBehaviour):
    def fly(self):
        print("Zoooooooooooooooooooooooooooooooooooooooooooo................ooooooom")


# The abstract QuackBehaviour class
class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass


# Concrete quack classes
class NoQuack(QuackBehaviour):
    def quack(self):
        print("This duck cannot speak you dummy!")


class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak! Squeak! Squeak!")


class Quack(QuackBehaviour):
    def quack(self):
        print('Quack, Quack! Quack, Quack!')


# The main Duck class
class Duck:
    def __init__(self, fly_behaviour: FlyBehaviour, quack_behaviour: QuackBehaviour):
        self.flyBehaviour = fly_behaviour
        self.quackBehaviour = quack_behaviour

    def swim(self):
        print('The duck is swimming now...')

    @abstractmethod
    def display(self):
        pass

    def set_fly_behaviour(self, fb: FlyBehaviour):
        self.flyBehaviour = fb

    def set_quack_behaviour(self, qb: QuackBehaviour):
        self.quackBehaviour = qb

    def perform_quack(self):
        self.quackBehaviour.quack()

    def perform_fly(self):
        self.flyBehaviour.fly()


# concrete ducks
class MallardDuck(Duck):
    def __init__(self):
        self.quack = NoQuack()
        self.fly = NoFly()
        super().__init__(self.fly, self.quack)

    def display(self):
        print('You are watching a Mallard Duck! It can swim, quack, and fly as well!')


# main function
def main():
    duck1 = MallardDuck()
    duck1.display()
    duck1.swim()
    duck1.perform_fly()
    duck1.perform_quack()

    # use the setter function to provide a fly type and a quack type to this duck
    duck1.set_fly_behaviour(FastFly())
    duck1.set_quack_behaviour(Squeak())

    duck1.perform_fly()
    duck1.perform_quack()


if __name__ == "__main__":
    main()