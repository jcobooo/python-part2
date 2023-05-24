from os import path

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

with open(data_path, "r", encoding="utf-8") as f:
    file_lines = f.read()

def policz_slowa(file_lines):
    slowa = file_lines.split()
    ilosc_slow = len(slowa)
    return ilosc_slow

def statystyki_liter(file_lines):
    slowa = file_lines.split()
    statystyki = {}
    for slowo in slowa:
            litery = file_lines.strip().split()
            for litera in litery:
                if litera:
                    ostatnia = litera[-1].lower()
                    statystyki[ostatnia] = statystyki.get(ostatnia, 0) + 1
    return statystyki


ilosc_slow = policz_slowa(file_lines)
print("Ilość słów:", ilosc_slow)

statystyki = statystyki_liter(file_lines)
print("Statystyki liter:")
for litera, ilosc in statystyki.items():
    print(f"Litera '{litera}': {ilosc}")