from abc import ABC, abstractmethod
from observers import Observer


# interface for the display element
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):
    temperature = 0.0
    humidity = 0.0
    pressure = 0.0

    def update(self, temperature: float, pressure: float, humidity: float):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

    def display(self):
        # this function will display the most updated values of the weather measurements
        print(f'Temperature: {self.temperature}')
        print(f'Pressure: {self.pressure}')
        print(f'Humidity: {self.humidity}%')