#Vytvářením funkc začínáme slovem "def" (definujeme funkci) a následně název funkce
#V závorkách nalezneme parametry funkce
#Parametry voláme jako proměnou ve funkci, aniž bychom inicializovali proměnou
#Pokud funkci zavoláme a zadáme její parametry, funkce je převezme.

def scitani(a, b):
    #Zde vidíme, jak do vysledek ukládáme a+b, což jsou naše proměné v parametru
    #Pokud do parametru funkce zadáme například - scitani(promena1, promena2), 
    #Přemění se nám promena1 - a, promena2 - b, hodnota která byla v proměné bude zachovaná
    #Příklad - Pokud promena1 je 5 a promena2 je 3, bude a = 5 a b = 3 
    vysledek = a+b

    #Return je vrácení hodnoty z vyhodnocení funkce. Respektive nám vrací výsledek
    return vysledek
    
#Proměné které inicializujeme
#Defaultně, se proměná ukládá v datovém typu string
promena1 = input("Zadejte proměnou 1: ")
promena2 = input("Zadejte proměnou 2: ")

#Přetypování ze stringu na integer
promena1 = int(promena1)
promena2 = int(promena2)

#Zde voláme funkci, kterou jsme si vytvořili, do funkce zadáme následně parametry
#Funkce se zde zavolá a vykoná příkaz, který je uvnitř funkce
#Funkce nám vrátí výsledek a uloží se do proměný
vysledek = scitani(promena1, promena2)

#Pokud chci kombinovat v printu více datových typů, oddělím je čárkou ","
print("Výsledek je: ", vysledek)
