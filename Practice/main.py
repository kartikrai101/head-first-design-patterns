from ducks import MallardDuck, ToyDuck, SuperDuck, Duck
from behaviors import SuperQuackBehavior, FastFlyBehavior


def main():
    mallard_duck: Duck = MallardDuck()
    toy_duck: Duck = ToyDuck()
    super_duck: Duck = SuperDuck()

    mallard_duck.perform_fly()
    mallard_duck.swim()
    mallard_duck.perform_quack()

    mallard_duck.set_fly_behavior(FastFlyBehavior())
    mallard_duck.set_quack_behavior(SuperQuackBehavior())
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()


if __name__ == "__main__":
    main()