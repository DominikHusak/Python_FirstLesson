# Získání vstupu od uživatele
den = int(input("Zadej den narození: "))
mesic = int(input("Zadej měsíc narození: "))
rok = int(input("Zadej rok narození: "))

# Vytvoření formátovaného řetězce s datem narození
datum_narozeni = f"{den}.{mesic}.{rok}"

# Výpis datumu narození
print("Datum narození:", datum_narozeni)