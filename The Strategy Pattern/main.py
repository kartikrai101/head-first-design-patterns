from context import MallardDuck
from strategies import FastFly, NoFly


def main():
    # create an instance of Mallard Duck
    mallard_duck = MallardDuck()
    mallard_duck.display()
    mallard_duck.swim()
    mallard_duck.quack()
    mallard_duck.fly()

    # change the fly behavior dynamically at runtime
    mallard_duck.set_fly_behavior(FastFly())
    mallard_duck.fly()

    # change the fly behavior dynamically at runtime
    mallard_duck.set_fly_behavior(NoFly())
    mallard_duck.fly()


if __name__ == "__main__":
    main()