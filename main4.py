class Czytelnik:
    def __init__(self, imie, nazwisko, numer_karty):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__numer_karty = numer_karty

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.__imie} {self.__nazwisko}. Mój numer karty to {self.__numer_karty}.")

    def get_numer_karty(self):
        return self.__numer_karty


czytelnik1 = Czytelnik("Jan", "Kowalski", 1234)
czytelnik2 = Czytelnik("Anna", "Nowak", 5678)

print(czytelnik1.get_numer_karty())