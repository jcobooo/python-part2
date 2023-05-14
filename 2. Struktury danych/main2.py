slowo = input("Podaj słowo: ")

odwrocone_slowo = slowo[::-1]

if odwrocone_slowo == slowo:
    print("Palindrom.")
else:
    print("Podane słowo nie jest palindromem.")
