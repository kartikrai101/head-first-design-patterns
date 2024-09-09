from abc import ABC, abstractmethod
from typing import List
from observers import Observer


# create an interface for the subject
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


# create a concrete Subject - WeatherStation
class WeatherStation(Subject):
    temperature = 0.0
    pressure = 0.0
    humidity = 0.0
    observers: List[Observer] = []

    def current_temperature(self) -> float:
        return self.temperature

    def current_pressure(self):
        return self.pressure

    def current_humidity(self):
        return self.humidity

    def add_observer(self, observer: Observer):
        # append this observer to the list of observers if it is not present already
        is_present = False
        for ob in self.observers:
            if ob == observer:
                is_present = True
                break

        if not is_present:
            self.observers.append(observer)
        else:
            print('Observer already subscribed to the Subject!')

    def remove_observer(self, observer: Observer):
        for ob in self.observers:
            if ob == observer:
                self.observers.remove(ob)
                break

        print('Successfully removed the observer.')

    def notify_observer(self):
        # this method shall call the update method of all the observers to update the readings
        for ob in self.observers:
            ob.update(self.temperature, self.pressure, self.humidity)

    def measurements_changed(self, temperature: float, pressure: float, humidity: float) -> bool:
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        print('Updated the measurements at Weather Station.')
        self.notify_observer()
        return True