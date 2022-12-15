import car
from car import *

# auto1 = Automobil()
# print(auto1.marka, auto1.marka, auto1.godiste, auto1.alu_felne)

class Automobil:
    
    alu_felne = False

    broj_tockova = 4 # staticko svojstvo
    
    def __init__(self, marka, model, godiste, alu_felne=False):
        print("Pravim automobil")
        self.marka     = marka
        self.model     = model
        self.godiste   = godiste
        self.alu_felne = alu_felne
        
a = Automobil("Citroen", "C4", 2018)

#Osoba
# ime, preizme, godine

class Osoba:
    def __init__(self, ime, prezime, godiste, boja_kose=False):
        print("Profil osobe: ")
        self.ime = ime
        self.prezime = prezime
        self.godiste = godiste
        self.boja_kose = boja_kose
    
    def obojena_kosa(self):
        if self.boja_kose == True:
            print("Prirodna")
        else:
           self.boja_kose = False
           print("Neprirodna")
        
b = Osoba("Stevan", "Cudar", 1984)
print(b.godiste)
b.obojena_kosa()

