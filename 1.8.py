# Funkce pro výpočet mocniny bez použití operátoru "**"
def vypocet_mocniny(zaklad, mocnitel):
    vysledek = 1
    for _ in range(mocnitel):
        vysledek *= zaklad
    return vysledek

# Získání vstupu od uživatele pro základ a mocnitel
zaklad = float(input("Zadej základ mocniny: "))
mocnitel = int(input("Zadej kladný a nenulový mocnitel: "))

# Kontrola základu a mocnitele
if mocnitel < 1:
    print("Mocnitel musí být kladný a nenulový.")
else:
    # Výpočet a výpis výsledku
    vysledek = vypocet_mocniny(zaklad, mocnitel)
    print(f"{zaklad}^{mocnitel} = {vysledek}")