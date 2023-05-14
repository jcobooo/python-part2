import random

traf = int(input("Zgadnij liczbę od 0 do 100: "))
liczba = random.randrange(0, 100)
if traf==liczba:
    print("Zgadłeś! Wylosowana liczba to: "+liczba)
elif (traf>liczba):
    print("Liczba jest mniejsza")
else:
    print("Liczba jest większa")
    

