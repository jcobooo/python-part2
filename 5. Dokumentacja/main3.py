print("KALKULATOR")

def dodawanie(x: float, y: float) -> float:
   """Dodaje dwie cyfry"""
   return x + y

def odejmowanie(x: float, y: float) -> float:
   """Odejmuje dwie cyfry"""
   return x - y

def mnozenie(x: float, y: float) -> float:
   """Mnozy dwie cyfry"""
   return x * y

def dzielenie(x: float, y: float) -> float:
   """Dzieli dwie cyfry"""
   return x / y


wyjscie: bool = False
while wyjscie == False:

    print("::Menu::")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    print("5 - wyjscie")

    choice: str = input("Wybierz:")

    if choice == '6':
        pytanie: str = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (1/2/3/4/5/6):")

    x: float = float(input("Podaj liczbe: "))
    y: float = float(input("Podaj liczbe: "))

    if choice == '1':
         print(x, "+", y, "=", dodawanie(x, y))

    elif choice == '2':
        print(x, "-", y, "=", odejmowanie(x, y))

    elif choice == '3':
         print(x, "*", y, "=", mnozenie(x, y))

    elif choice == '4':
         print(x, "/", y, "=", dzielenie(x, y))

    else:
     print("Wybraleś nieistniejącą opcje!")
