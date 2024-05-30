import random
import time

class Homar:
    def __init__(self, id, lungime, valoare):
        self.id = id
        self.lungime = lungime
        self.valoare = valoare

def valoareaPerUnitate(homar):
    return homar.valoare / (homar.lungime * 1.0)

def sortareHomari(homari):
    homari.sort(key=valoareaPerUnitate, reverse=True)

def repartizareHomari(homari, dimensiunePlasa):
    dimensiunePlasaMomentan = dimensiunePlasa
    valoarePlasa = 0.0

    for homar in homari:
        if homar.lungime <= dimensiunePlasaMomentan:
            print(f"\nA fost ales Homarul nr.{homar.id}, cu valoarea:{homar.valoare} si lungimea:{homar.lungime}")
            valoarePlasa += homar.valoare
            dimensiunePlasaMomentan -= homar.lungime

    print(f"\nValoarea maxima obtinuta: {valoarePlasa}")

def generareHomarii(noHomari):
    homari = []
    for i in range(noHomari):
        id = i
        lungime = random.randint(1, 500)
        valoare = random.randint(1, 500)
        homari.append(Homar(id, lungime, valoare))
    return homari

def generateNumbers():
    return random.randint(1, 10000)

def main():
    random.seed(time.time())
    start_time = time.time()
    
    noHomari = generateNumbers()
    dimensiunePlasa = generateNumbers()
    
    homari = generareHomarii(noHomari)

    print(f"  Numarul de homari: {noHomari}\n  Marimea plasei: {dimensiunePlasa}")
    print("\n==== Homari selectati====")
    
    sortareHomari(homari)
    repartizareHomari(homari, dimensiunePlasa)
    
    elapsed_time = time.time() - start_time
    print(f"\nElapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
