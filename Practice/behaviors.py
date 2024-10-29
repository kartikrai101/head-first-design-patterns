from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class DefaultFlyBehavior(FlyBehavior):
    def fly(self):
        print("Hey there, I can fly.")


class NoFlyBehavior(FlyBehavior):
    def fly(self):
        print("I cannot fly!")


class FastFlyBehavior(FlyBehavior):
    def fly(self):
        print("Zoooooooooooo..............ooooooooooooooppp!")


class DefaultQuackBehavior(QuackBehavior):
    def quack(self):
        print("Quack! Quack! Quack!")


class SqueakBehavior(QuackBehavior):
    def quack(self):
        print("Squeak! Squeak! Squeak!")


class SuperQuackBehavior(QuackBehavior):
    def quack(self):
        print("QUACK!!! QUACK!!! QUACK!!!")