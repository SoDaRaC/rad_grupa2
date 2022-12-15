class Automobil:
    marka     = ""
    model     = ""
    godiste   = 0
    alu_felne = False

    broj_tockova = 4 # staticko svojstvo

    #metode
    def vozi(self):
        print("Auto je u pokretu")
        print(self.model)
    
    def postavi_felne(self):
        if self.alu_felne == True:
            print("Imate vec alu felne")
        else:
            self.alu_felne = True
            print("Postavljene su alu felne")

auto1 = Automobil() # objekat / instanca - instanciranje klase
auto1.marka = "Citroen"
auto1.model = "C3"
auto1.godiste = 2017
auto1.alu_felne = False
print(auto1.marka, auto1.model, auto1.godiste, auto1.alu_felne)

print(Automobil.broj_tockova)

auto1.vozi()

auto1.postavi_felne() # metoda automobila

#STRING tip
slova = "AbcD"
slova = str()

slova.upper() # metoda stringa
slova.lower()





