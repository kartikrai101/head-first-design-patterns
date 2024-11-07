from abc import ABC, abstractmethod
from ducks import Quackable, MallardDuck, RedHeadDuck, RubberDuck, DuckCall
from duckDecorators import QuackCounter


# now we will create an abstract factory to create multiple types of ducks
class AbstractDuckFactory(ABC):
    @abstractmethod
    def create_mallard_duck(self):
        pass

    @abstractmethod
    def create_redhead_duck(self):
        pass

    @abstractmethod
    def create_duck_call(self):
        pass

    @abstractmethod
    def create_rubber_duck(self):
        pass


# create a duck factory that will implement the AbstractDuckFactory class
class DuckFactory(AbstractDuckFactory):
    def create_rubber_duck(self):
        return RubberDuck()

    def create_duck_call(self):
        return DuckCall()

    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedHeadDuck()


# create a Counting Duck Factory
class CountingDuckFactory(AbstractDuckFactory):
    def create_redhead_duck(self):
        return QuackCounter(RedHeadDuck())

    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())