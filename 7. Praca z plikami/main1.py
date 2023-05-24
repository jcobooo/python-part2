import random
from os import path

dir_path = path.dirname(__file__)
imiona_file = "imiona.txt"
data_path = path.join(dir_path, imiona_file)

with open(data_path, "r", encoding="utf-8") as f:
    imiona= f.readlines()

dir_path = path.dirname(__file__)
nazwiska_file = "nazwiska.txt"
data_path = path.join(dir_path, nazwiska_file)

with open(data_path, "r", encoding="utf-8") as f:
    nazwiska = f.readlines()

def generate_combinations(imiona, nazwiska, liczba_kombinacji):
    combinations = set()
    
    while len(combinations) < liczba_kombinacji:
        imie = random.choice(imiona).strip()
        nazwisko = random.choice(nazwiska).strip()
        combinations.add((imie, nazwisko))
    
    return combinations

def save_combinations(combinations, kombinacje_file):
    with open(kombinacje_file, 'w') as file:
        for imie, nazwisko in combinations:
            file.write(f"{imie} {nazwisko}\n")

kombinacje_file = 'kombinacje.txt'

liczba_kombinacji = int(input("Podaj liczbę kombinacji do wygenerowania: "))

combinations = generate_combinations(imiona, nazwiska, liczba_kombinacji)
save_combinations(combinations, kombinacje_file)

print(f"Utworzono {len(combinations)} kombinacji imion i nazwisk. Zapisano do pliku {kombinacje_file}.")
