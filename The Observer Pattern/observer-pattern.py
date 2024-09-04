from abc import ABC, abstractmethod
from typing import List


# interface for the observer (subscriber)
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, pressure: float, humidity: float):
        pass


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


# interface for the display element
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
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


# Concrete observer for first Display Screen
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


# main function for demo
def main():
    weatherStation = WeatherStation()
    currentConditionDisplay = CurrentConditionsDisplay()

    currentConditionDisplay.display()

    # let's make the currentConditionDisplay as an observer to our subject
    weatherStation.register_observer(currentConditionDisplay)
    weatherStation.measurements_changed(32.3, 2.45, 63)
    currentConditionDisplay.display()


if __name__ == "__main__":
    main()