import random
from abc import ABC, abstractmethod


# ==============================
# CLASA ABSTRACTĂ ENTITATE ECOSISTEM
# ==============================
class EntitateEcosistem(ABC):
    def __init__(self, nume, energie, x, y, rata_supravietuire):
        self.nume = nume
        self.energie = energie
        self.x = x
        self.y = y
        self.rata_supravietuire = rata_supravietuire

    @abstractmethod
    def actioneaza(self):
        pass

    def reproduce(self):
        print(f"{self.nume} se reproduce.")


# ==============================
# CLASA PLANTĂ
# ==============================
class Planta(EntitateEcosistem):
    def __init__(self, nume, energie, x, y, rata_crescut):
        super().__init__(nume, energie, x, y, rata_crescut)

    def actioneaza(self):
        self.energie += self.rata_supravietuire
        print(f"{self.nume} crește și câștigă {self.rata_supravietuire} energie.")

    def reproduce(self):
        if self.energie > 50:
            print(f"{self.nume} s-a reprodus.")


# ==============================
# CLASA ABSTRACTĂ ANIMAL
# ==============================
class Animal(EntitateEcosistem, ABC):
    def __init__(self, nume, energie, x, y, viteza, tip_hrana):
        super().__init__(nume, energie, x, y, rata_supravietuire=0)
        self.viteza = viteza
        self.tip_hrana = tip_hrana

    @abstractmethod
    def mananca(self, prada):
        pass

    def deplaseaza(self):
        self.x += random.randint(-self.viteza, self.viteza)
        self.y += random.randint(-self.viteza, self.viteza)
        print(f"{self.nume} s-a deplasat la ({self.x}, {self.y}).")

    def actioneaza(self):
        self.deplaseaza()
        self.energie -= 1  # Animalele consumă energie la fiecare pas.
        print(f"{self.nume} a pierdut 1 energie, energie rămasă: {self.energie}")


# ==============================
# CLASA ERBIVOR
# ==============================
class Erbivor(Animal):
    def __init__(self, nume, energie, x, y, viteza):
        super().__init__(nume, energie, x, y, viteza, "plante")

    def mananca(self, planta):
        if isinstance(planta, Planta):
            self.energie += planta.energie
            planta.energie = 0
            print(f"{self.nume} a mâncat {planta.nume} și a câștigat {planta.energie} energie.")


# ==============================
# CLASA CARNIVOR
# ==============================
class Carnivor(Animal):
    def __init__(self, nume, energie, x, y, viteza):
        super().__init__(nume, energie, x, y, viteza, "animale")

    def mananca(self, prada):
        if isinstance(prada, Animal) and prada != self:
            self.energie += prada.energie
            prada.energie = 0
            print(f"{self.nume} a vânat {prada.nume} și a câștigat {prada.energie} energie.")


# ==============================
# CLASA OMNIVOR
# ==============================
class Omnivor(Animal):
    def __init__(self, nume, energie, x, y, viteza):
        super().__init__(nume, energie, x, y, viteza, "plante si animale")

    def mananca(self, entitate):
        if isinstance(entitate, (Planta, Animal)) and entitate != self:
            self.energie += entitate.energie
            entitate.energie = 0
            print(f"{self.nume} a mâncat {entitate.nume} și a câștigat {entitate.energie} energie.")


# ==============================
# CLASA ECOSISTEM
# ==============================
class Ecosistem:
    def __init__(self, latime, inaltime):
        self.latime = latime
        self.inaltime = inaltime
        self.entitati = []

    def adauga_entitate(self, entitate):
        self.entitati.append(entitate)
        print(f"{entitate.nume} a fost adăugat la ecosistem.")

    def elimina_entitate(self, entitate):
        if entitate in self.entitati:
            self.entitati.remove(entitate)
            print(f"{entitate.nume} a fost eliminat din ecosistem.")

    def simuleaza_pasu(self):
        print("\n=== PASUL DE SIMULARE ===")
        for entitate in self.entitati:
            entitate.actioneaza()
            if entitate.energie <= 0:
                print(f"{entitate.nume} a murit.")
                self.elimina_entitate(entitate)

    def raport_final(self):
        print("\n=== RAPORT FINAL ===")
        populatii = {}
        for entitate in self.entitati:
            tip_entitate = type(entitate).__name__
            if tip_entitate not in populatii:
                populatii[tip_entitate] = 0
            populatii[tip_entitate] += 1
        for tip, numar in populatii.items():
            print(f"Populația de {tip}: {numar}")


# ==============================
# SCENARII DE TESTARE
# ==============================
def testeaza_simulare():
    # Crearea ecosistemului
    ecosistem = Ecosistem(latime=20, inaltime=20)

    # Adaugarea plantelor
    planta1 = Planta(nume="Planta1", energie=30, x=5, y=5, rata_crescut=10)
    planta2 = Planta(nume="Planta2", energie=50, x=10, y=10, rata_crescut=5)

    # Adaugarea animalelor
    erbivor1 = Erbivor(nume="Iepure1", energie=40, x=3, y=3, viteza=2)
    carnivor1 = Carnivor(nume="Lup1", energie=70, x=8, y=8, viteza=3)
    omnivor1 = Omnivor(nume="Urs1", energie=80, x=12, y=12, viteza=2)

    # Adaugarea entitatilor la ecosistem
    ecosistem.adauga_entitate(planta1)
    ecosistem.adauga_entitate(planta2)
    ecosistem.adauga_entitate(erbivor1)
    ecosistem.adauga_entitate(carnivor1)
    ecosistem.adauga_entitate(omnivor1)

    # Simularea pasilor de ecosistem
    while True:
        print("\nApasă ENTER pentru a avansa la următorul pas de simulare (sau scrie 'stop' pentru a opri).")
        comanda = input()
        if comanda.lower() == 'stop':
            break
        ecosistem.simuleaza_pasu()

    # Raport final
    ecosistem.raport_final()


# Execută testarea
if __name__ == "__main__":
    testeaza_simulare()
