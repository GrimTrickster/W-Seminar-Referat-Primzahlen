from sympy import isprime
import time
import math
from colorama import Style
from colorama import Fore


input_zahl = None


def _ist_primzahl(zahl):
    kmax = math.ceil(math.sqrt(zahl))  # kmax = Wurzel aus zu prüfender Zahl
    if len(range(2, kmax)) == 0:
        kmax += 1
    for k in range(2, kmax):  # über alle möglichen Teiler iterieren
        if zahl % k == 0 and k != zahl:  # kein Rest
            return False
    return True  # in Schleife keinen Teiler gefunden


def sympy_test(zahl):
    start_time = time.time()

    prim = isprime(zahl)  # Sympy Methode

    end_time = time.time()
    elapsed_time = end_time - start_time
    return prim, elapsed_time


def own_test(zahl):
    start_time = time.time()

    prim = _ist_primzahl(zahl)  # eigener Algorithmus

    end_time = time.time()
    elapsed_time = end_time - start_time
    return prim, elapsed_time


while input_zahl != 0:
    try:
        input_zahl = int(input(f"{Style.RESET_ALL}\n\nBitte zu prüfenden Exponenten eingeben: "))
        M = 2 ** input_zahl - 1
        print(f"Testing Number: {M}")

        print("\n\n-----------------------------------------------------------------------")
        print(f"{Fore.GREEN}SYMPY:")
        sympy_prim, sympy_time = sympy_test(M)
        print(f"Ist eine Primzahl: {sympy_prim}; errechnet in {sympy_time}")
        print(f"{Style.RESET_ALL}-----------------------------------------------------------------------")

        print(f"{Fore.RED}Eigener Algorithmus:")
        try:
            own_prim, own_time = own_test(M)
            print(f"Ist eine Primzahl: {own_prim}; errechnet in {own_time}")
        except OverflowError as error:
            print("Mersenne Zahl zu hoch für eigenen Algorithmus 😒:")
            print(error)
    except ValueError as error:
        print(error)
        print("Bitte Zahl eingeben")


# Test Numbers: 2281 (Robinson 1952); 11213 (Gillies 1963); 19937 (Tuckerman 1971)
