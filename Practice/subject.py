from abc import ABC, abstractmethod
from typing import List
from observer import Observer


class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Subject):
    observers: List[Observer] = []
    temperature: float = 0.0
    humidity: float = 0.0
    pressure: float = 0.0

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        for ob in self.observers:
            if ob is observer:
                self.observers.remove(ob)
                return

        print("The given observer is has not subscribed yet :(")

    def measurements_changed(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.pressure = pressure
        self.humidity = humidity
        self.notify_observers()

    def notify_observers(self):
        for ob in self.observers:
            ob.update(self.temperature, self.pressure, self.humidity)