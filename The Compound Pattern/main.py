from duckSimulator import DuckSimulator
from duckFactory import CountingDuckFactory


def main():
    duck_simulator = DuckSimulator()
    duck_factory = CountingDuckFactory()
    duck_simulator.simulate(duck_factory)


if __name__ == "__main__":
    main()