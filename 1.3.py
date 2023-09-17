while True:
    #Zadání jména
    jmeno = input("Ahoj jak se jmenuješ? ")

    #Ověření jména
    odpoved = input(f"Opravdu se jmenuješ: {jmeno}? (ano/ne) ")

    #Kontrola odpovědi
    if odpoved.lower() == 'ano':
        print(f"Ahoj, {jmeno}! Sbohem.")
        break
    elif odpoved.lower() == 'ne':
        print("Zkus to znovu.")
    else:
        print("Prosím zadej 'ano' nebo 'ne'.")

