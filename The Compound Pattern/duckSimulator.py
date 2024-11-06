from ducks import Quackable, MallardDuck, RedHeadDuck, DuckCall, RubberDuck


class DuckSimulator:
    def simulate_duck(self, duck: Quackable):
        duck.quack()

    def simulate(self):
        mallard_duck: Quackable = MallardDuck()
        redhead_duck: Quackable = RedHeadDuck()
        duck_call: Quackable = DuckCall()
        rubber_duck: Quackable = RubberDuck()

        print("----------------------------------- Duck Simulator -----------------------------------")

        self.simulate_duck(mallard_duck)
        self.simulate_duck(redhead_duck)
        self.simulate_duck(duck_call)
        self.simulate_duck(rubber_duck)