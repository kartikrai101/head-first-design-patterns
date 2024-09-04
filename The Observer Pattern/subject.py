from abc import ABC, abstractmethod
from typing import List
from observers import Observer


# interface for the subject (publisher)
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concrete subject
class WeatherStation(Subject):
    observers: List[Observer] = []
    temperature = 0.0
    humidity = 0.0
    pressure = 0.0

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        for ob in self.observers:
            if ob is observer:
                self.observers.remove(ob)
                return
        # if the passed observer is not found, we display the error message
        print('The provided observer was not found :(')

    def notify_observers(self):
        # notify the observers of current measurements whenever this method is called
        for observer in self.observers:
            observer.update(self.temperature, self.pressure, self.humidity)

    def get_temperature(self):
        return self.temperature

    def get_pressure(self):
        return self.pressure

    def get_humidity(self):
        return self.humidity

    def measurements_changed(self, temp: float, pressure: float, humidity: float):
        self.temperature = temp
        self.pressure = pressure
        self.humidity = humidity

        # call the notify method after updating the measurements
        self.notify_observers()