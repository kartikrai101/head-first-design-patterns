from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack Quack!!")

    def fly(self):
        print("I am a Mallard Duck and I can fly")


class WildTurkey(Turkey):
    def gobble(self):
        print("I am a turkey. I don't Quack, I rather gobble!!")

    def fly(self):
        print("I can also fly though!")


# adapter class
class TurkeyAdapter(Duck):
    turkey: Turkey

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def fly(self):
        self.turkey.fly()

    def quack(self):
        self.turkey.gobble()


def main():
    duck1 = MallardDuck()
    turkey1 = WildTurkey()

    # Now I want to create a duck object out of the turkey object
    duck_from_turkey = TurkeyAdapter(turkey1)
    duck_from_turkey.quack()


if __name__ == "__main__":
    main()