import math
import matplotlib.pyplot as plt


def sieb_des_eratosthenes(start, end):
    kmax = math.ceil(math.sqrt(end))
    prim = []
    gestrichen = [False] * end
    for teiler in range(2, kmax):  # über alle Teiler iterieren
        if not gestrichen[teiler]:  # wenn Teiler nicht schon gestrichen (z.B. 2 ==> 4)
            for zahl in range(teiler**2, end, teiler):  # für alle Zahlen die in "Multiplikationsreihe" des Teilers liegen
                # print(zahl)
                gestrichen[zahl] = True  # Zahl streichen

    for i in range(start, end):
        if not gestrichen[i]:
            prim.append(i)
    return prim


for i in range(2, 1000000, 100000):

    primzahlen = sieb_des_eratosthenes(i, i + 100000)
    print(len(primzahlen))


