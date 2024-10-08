from abc import ABC, abstractmethod


# interface for the observer (subscriber)
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, pressure: float, humidity: float):
        pass