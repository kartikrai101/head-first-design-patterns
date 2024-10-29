from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, pressure: float, humidity: float):
        pass


class CurrentDisplayElement(Observer):
    temperature: float = 0.0
    pressure: float = 0.0
    humidity: float = 0.0

    def display(self):
        print(f"The current temperature is: {self.temperature}")
        print(f"The current pressure is: {self.pressure}")
        print(f"The current humidity is: {self.humidity}")

    def update(self, temp: float, pressure: float, humidity: float):
        self.pressure = pressure
        self.temperature = temp
        self.humidity = humidity