import math
from abc import ABC, abstractmethod


class Figura(ABC):
    def __init__(self):
        self._pole = None
        self._obwod = None

    @abstractmethod
    def oblicz_pole(self):
        pass

    @abstractmethod
    def oblicz_obwod(self):
        pass

    def wyswietl_informacje(self):
        print("Pole:", self._pole)
        print("Obwod:", self._obwod)


class Kwadrat(Figura):
    def __init__(self, bok):
        super().__init__()
        self._bok = bok

    def oblicz_pole(self):
        self._pole = self._bok * self._bok

    def oblicz_obwod(self):
        self._obwod = 4 * self._bok


class Kolo(Figura):
    def __init__(self, promien):
        super().__init__()
        self._promien = promien

    def oblicz_pole(self):
        self._pole = math.pi * self._promien * self._promien

    def oblicz_obwod(self):
        self._obwod = 2 * math.pi * self._promien


kwadrat = Kwadrat(5)
kwadrat.oblicz_pole()
kwadrat.oblicz_obwod()
kwadrat.wyswietl_informacje()

print()

kolo = Kolo(3)
kolo.oblicz_pole()
kolo.oblicz_obwod()
kolo.wyswietl_informacje()