from abc import ABC, abstractmethod


# create an interface for the observers
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, pressure: float, humidity: float):
        pass