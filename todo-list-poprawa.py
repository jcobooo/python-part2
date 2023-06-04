import json

def dodaj_zadanie(zadania, tytul, opis, termin):
    zadanie = {
        'id': len(zadania) + 1,
        'tytul': tytul,
        'opis': opis,
        'termin': termin
    }
    zadania.append(zadanie)
    print("Dodano nowe zadanie.")

def wyswietl_zadanie(zadanie, pokaz_opis=False):
    print("ID:", zadanie['id'])
    print("Tytuł:", zadanie['tytul'])
    print("Termin:", zadanie['termin'])
    if pokaz_opis:
        print("Opis:", zadanie['opis'])

def usun_zadanie(zadania, zadanie_id):
    for zadanie in zadania:
        if zadanie['id'] == zadanie_id:
            zadania.remove(zadanie)
            print("Usunięto zadanie o ID:", zadanie_id)
            return
    print("Nie znaleziono zadania o podanym ID.")

def aktualizuj_zadanie(zadania, zadanie_id, tytul=None, opis=None, termin=None):
    for zadanie in zadania:
        if zadanie['id'] == zadanie_id:
            if tytul:
                zadanie['tytul'] = tytul
            if opis:
                zadanie['opis'] = opis
            if termin:
                zadanie['termin'] = termin
            print("Zaktualizowano zadanie o ID:", zadanie_id)
            return
    print("Nie znaleziono zadania o podanym ID.")

def zapisz_do_pliku(zadania, nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        json.dump(zadania, plik)
    print("Zadania zostały zapisane do pliku:", nazwa_pliku)

def odczytaj_z_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            return json.load(plik)
    except FileNotFoundError:
        return []

def wypisz_zadania(zadania):
    if not zadania:
        print("Brak zapisanych zadań.")
    else:
        for zadanie in zadania:
            wyswietl_zadanie(zadanie)

def menu():
    zadania = odczytaj_z_pliku('zadania.json')

    wypisz_zadania(zadania)

    while True:
        print("\n===== MENADŻER ZADAŃ =====")
        print("1. Dodaj nowe zadanie")
        print("2. Wyświetl zadania")
        print("3. Usuń zadanie")
        print("4. Aktualizuj zadanie")
        print("5. Zapisz zadania do pliku")
        print("6. Wyjdź z programu")

        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            tytul = input("Podaj tytuł zadania: ")
            opis = input("Podaj opis zadania: ")
            termin = input("Podaj termin wykonania zadania: ")
            dodaj_zadanie(zadania, tytul, opis, termin)
        elif wybor == '2':
            wypisz_zadania(zadania)
        elif wybor == '3':
            zadanie_id = int(input("Podaj ID zadania do usunięcia: "))
            usun_zadanie(zadania, zadanie_id)
        elif wybor == '4':
            zadanie_id = input("Podaj ID zadania do aktualizacji: ")
            if zadanie_id.isdigit():
                zadanie_id = int(zadanie_id)
                tytul = input("Podaj nowy tytuł zadania (jeśli bez zmian, pozostaw puste): ")
                opis = input("Podaj nowy opis zadania (jeśli bez zmian, pozostaw puste): ")
                termin = input("Podaj nowy termin wykonania zadania (jeśli bez zmian, pozostaw puste): ")
                aktualizuj_zadanie(zadania, zadanie_id, tytul, opis, termin)
            else:
                print("Podano nieprawidłowe ID zadania.")
        elif wybor == '5':
            zapisz_do_pliku(zadania, 'zadania.json')
        elif wybor == '6':
            zapisz_do_pliku(zadania, 'zadania.json')
            break
        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")

menu()
