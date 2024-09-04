from abc import ABC, abstractmethod


# interface for the subject (publisher)
class Subject(ABC):
    @abstractmethod
    def register_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observer(self):
        pass


# interface for the observer (subscriber)
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


# interface for the display element
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

