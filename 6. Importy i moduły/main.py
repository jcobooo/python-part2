#kalkulator
print("KALKULATOR")
 
import mod

mod.dodawanie 
mod.dzielenie
mod.mnozenie
mod.odejmowanie

wyjscie = False
while wyjscie == False:
 
    print("::Menu::")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    print("5 - potegowanie")
    print("6 - wyjscie")
 
    choice = input("Wybierz (1/2/3/4/5/6):")
 
    if choice == '6':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (1/2/3/4/5/6):")
 
    x= float(input("Podaj liczbe: "))
    y = float(input("Podaj liczbe: "))
 
    if choice == '1':
         print(x,"+",y,"=", mod.dodawanie(x,y))
 
    elif choice == '2':
        print(x,"-",y,"=", mod.odejmowanie(x,y))
 
    elif choice == '3':
         print(x,"*",y,"=", mod.mnozenie(x,y))
 
    elif choice == '4':
         print(x,"/",y,"=", mod.dzielenie(x,y))
 
    else:
     print("Wybraleś nieistniejącą opcje!")
