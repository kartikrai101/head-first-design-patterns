from abc import ABC, abstractmethod


# strategy class for fly behavior
class FlyBehavior(ABC):
    def fly(self):
        pass


# strategy class for quack behavior
class QuackBehavior(ABC):
    def quack(self):
        pass


# concrete fly behavior classes
class DefaultFly(FlyBehavior):
    def fly(self):
        print('Flap! Flap! Flap!')


class FastFly(FlyBehavior):
    def fly(self):
        print("I'm fast af boi! Zoooooooo...................ooop!!!!")


class NoFly(FlyBehavior):
    def fly(self):
        print('Hey! Are you trying to kill me or what! I cannot fly!')


# concrete quack behavior classes
class DefaultQuack(QuackBehavior):
    def quack(self):
        print('Quack! Quack! Quack!')


class SqueakQuack(QuackBehavior):
    def quack(self):
        print('Squeak! Squeak! Squeak!')


class NoQuack(QuackBehavior):
    def quack(self):
        print('Sorry man! I cannot quack!')