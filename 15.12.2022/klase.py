# marka,model, godiste ,parkiran
class Automobil:
    def __init__(self, marka, model, godiste, parkiran=False):
        self.marka = marka
        self.model = model
        self.godiste = godiste
        self.parkiran = parkiran
    def informacije(self): #instancni metod
        status = "Parkiran" if self.parkiran else "U Pokretu"
        return f"Marka: {self.marka}\nModel:  {self.model}\nGodiste: {self.godiste}\n{status}"

    staticmethod
    def info_o_automobilima(): #staticki metod
        print("Automobili imaju 4 tocka")
        print("Najcesce se registruju jednom godisnje")

    # parkiraj - proveri da li je auto parkiran
    # svojstvo parkiran prebaciti u True
    def parkiraj(self):
        if self.parkiran == True:
            print("Vec ste parkirani")
        else:
            self.parkiran
            print("Parkirani ste")

automobil1 = Automobil("Citroen", "C5", 2021, True)
# "Marka: Citroen"
print(f"Marka: {automobil1.marka}")
print(f"Model: {automobil1.model}")
print(automobil1.informacije())

automobil2 = Automobil("FOrd", "Focus", 2020)
print(automobil2.informacije())

Automobil.info_o_automobilima()
automobil1.parkiraj()
automobil2.parkiraj()


