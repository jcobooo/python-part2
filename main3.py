from random import randint

def zgadywanka():
    liczba = randint(0, 100)
    liczba_strzalow = 0
    odgadniete = False

    while not odgadniete:
        strzal = int(input("Podaj liczbę: "))
        liczba_strzalow += 1

        if strzal == liczba:
            print("Brawo! Odgadłeś liczbę {} po {} strzałach.".format(liczba, liczba_strzalow))
            break
        elif strzal < liczba:
            print("Szukana liczba jest większa.")
        else:
            print("Szukana liczba jest mniejsza.")

    odpowiedz = input("Czy chcesz zagrać jeszcze raz? (t/n) ")
    if odpowiedz.lower() == "t":
        zgadywanka()

zgadywanka()

    

