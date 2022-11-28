import math


def sieb_des_eratosthenes(start, end):
    kmax = math.ceil(math.sqrt(end))
    prim = []
    gestrichen = [False] * end  # Liste für alle Zahlen erstellen
    for teiler in range(start, kmax):  # über alle Teiler iterieren
        if not gestrichen[teiler]:  # wenn Teiler nicht schon gestrichen (z.B. 2 ==> 4)
            for zahl in range(teiler**2, end, teiler):  # für alle Zahlen die in "Multiplikationsreihe" des Teilers liegen
                # print(zahl)
                gestrichen[zahl] = True  # Zahl streichen

    for i in range(2, end):
        if not gestrichen[i]:
            prim.append(i)
    return prim


primzahlen = sieb_des_eratosthenes(2, 100000)
print(primzahlen)
