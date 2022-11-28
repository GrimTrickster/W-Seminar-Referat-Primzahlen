import math

input_zahl = None


def ist_primzahl(zahl):
    kmax = math.ceil(math.sqrt(zahl))  # kmax = Wurzel aus zu prüfender Zahl
    if len(range(2, kmax)) == 0:
        kmax += 1
    for k in range(2, kmax):  # über alle möglichen Teiler iterieren
        if zahl % k == 0 and k != zahl:  # kein Rest
            return False, zahl
    return True, zahl  # in Schleife keinen Teiler gefunden


while input_zahl != 0:
    try:
        input_zahl = int(input("Bitte zu prüfende Zahl eingeben: "))
        print(ist_primzahl(input_zahl))
    except ValueError:
        print("Bitte Zahl eingeben")

