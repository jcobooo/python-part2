print("KALKULATOR")

def dodawanie(x, y):
   return x + y

def odejmowanie(x, y):
   return x - y

def mnozenie(x, y):
   return x * y

def dzielenie(x, y):
   try:
       return x / y
   except ZeroDivisionError:
       print("Nie można dzielić przez zero!")
       return None


wyjscie = False
while not wyjscie:

    print("::Menu::")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    print("5 - wyjscie")

    choice = input("Wybierz:")

    if choice == '5':
        wyjscie = True
        print('Koniec programu!')
        exit()

    elif choice == '1' or choice == '2' or choice == '3' or choice == '4':
        try:
            x = float(input("Podaj liczbę: "))
            y = float(input("Podaj liczbę: "))

            if choice == '1':
                print(x, "+", y, "=", dodawanie(x, y))

            elif choice == '2':
                print(x, "-", y, "=", odejmowanie(x, y))

            elif choice == '3':
                print(x, "*", y, "=", mnozenie(x, y))

            elif choice == '4':
                wynik = dzielenie(x, y)
                if wynik is not None:
                    print(x, "/", y, "=", wynik)

        except ValueError:
            print("Podano nieprawidłową liczbę!")

    else:
        print("Wybrałeś nieistniejącą opcję!")