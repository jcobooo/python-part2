class Czytelnik:
    def __init__(self, imie, nazwisko, numer_karty):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_karty = numer_karty

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}. Mój numer karty to {self.numer_karty}.")

czytelnik1 = Czytelnik("Jan", "Kowalski", 1234)
czytelnik2 = Czytelnik("Anna", "Nowak", 5678)

czytelnik1.przedstaw_sie()
czytelnik2.przedstaw_sie()