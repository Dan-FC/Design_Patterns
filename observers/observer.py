from abc import ABC, abstractmethod

# Observable
class CountryInput:
    def __init__(self):
        self._observers = []
        self._country = ""

    def add_observer(self, observer):
        self._observers.append(observer)

    def set_country(self, country):
        self._country = country
        self._notify_observers()

    def get_country(self):
        return self._country

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._country)

# Observer
class CountryObserver(ABC):
    @abstractmethod
    def update(self, country):
        pass

# Ejemplo de observador
class LoggerObserver(CountryObserver):
    def update(self, country):
        print(f"[Logger] El país ha cambiado a: {country}")
