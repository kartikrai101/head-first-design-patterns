from ducks import Quackable, MallardDuck, RedHeadDuck, DuckCall, RubberDuck
from goose import Goose, GooseAdapter
from duckDecorators import QuackCounter


class DuckSimulator:
    def simulate_duck(self, duck: Quackable):
        duck.quack()

    def simulate(self):
        quack_counter_wrapper: QuackCounter
        mallard_duck: Quackable = QuackCounter(MallardDuck())
        redhead_duck: Quackable = QuackCounter(RedHeadDuck())
        duck_call: Quackable = QuackCounter(DuckCall())
        rubber_duck: Quackable = QuackCounter(RubberDuck())
        goose: Goose = Goose()
        goose_duck: Quackable = GooseAdapter(goose)

        print("----------------------------------- Duck Simulator(With Decorator) -----------------------------------")

        self.simulate_duck(mallard_duck)
        self.simulate_duck(redhead_duck)
        self.simulate_duck(duck_call)
        self.simulate_duck(rubber_duck)
        self.simulate_duck(goose_duck)