from abc import ABC, abstractmethod
from typing import List


# interface for the observer (subscriber)
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, pressure: float, humidity: float):
        pass