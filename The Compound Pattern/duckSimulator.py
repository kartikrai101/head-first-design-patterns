from ducks import Quackable, MallardDuck, RedHeadDuck, DuckCall, RubberDuck
from goose import Goose, GooseAdapter
from duckDecorators import QuackCounter
from duckFactory import AbstractDuckFactory


class DuckSimulator:
    def simulate_duck(self, duck: Quackable):
        duck.quack()

    def simulate(self, duck_factory: AbstractDuckFactory):
        mallard_duck: Quackable = duck_factory.create_mallard_duck()
        redhead_duck: Quackable = duck_factory.create_redhead_duck()
        duck_call: Quackable = duck_factory.create_duck_call()
        rubber_duck: Quackable = duck_factory.create_rubber_duck()
        goose: Goose = Goose()
        goose_duck: Quackable = GooseAdapter(goose)

        print("----------------------------------- Duck Simulator: With Duck Factory -----------------------------------")

        self.simulate_duck(mallard_duck)
        self.simulate_duck(redhead_duck)
        self.simulate_duck(duck_call)
        self.simulate_duck(rubber_duck)
        self.simulate_duck(goose_duck)