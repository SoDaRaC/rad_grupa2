# tip (string) broj korisnika(int) mockup (bool) preuzeta za rad (bool)
class Aplikacija:
    def __init__(self, tip, broj_korisnika, mockup, preuzeta_za_rad):
        self.tip = tip
        self.broj_korisnika = broj_korisnika
        self.mockup = mockup
        self.preuzeta_za_rad = preuzeta_za_rad

app1 = Aplikacija("web aplikacija", 50,  True , False)
app2 = Aplikacija("iOS aplikacija", 1500, False, False)
app3 = Aplikacija("Android aplikacija", 1800, True, False)

class Firma:
    def __init__(self,naziv,broj_zaposlenih,registrovana = False):
        self.naziv = naziv
        self.broj_zaposlenih = broj_zaposlenih
        self.registrovana = registrovana

    def zaposli_nove(self, broj_novih):
        if broj_novih <= 0:
            print("Prosledite broj veci od 0")
        else:
            self.broj_zaposlenih += broj_novih
            print(f"Zaposleno je novih {broj_novih}, trenutni broj je {self.broj_zaposlenih}")
        # broj zaposlenih > = broj_otpustenih
        pass
    def otpusti_ljude(self, broj_otpustenih):
        if broj_otpustenih > self.broj_zaposlenih or broj_otpustenih < 0:
            print("Previse za otpustanje")
        else:
            self.broj_zaposlenih -= broj_otpustenih
            print(f"Otpusteno je = {broj_otpustenih}, trenutni broj je {self.broj_zaposlenih}")
    # da li aplikacija ima mockup i ako nema ,ne uzimam projekat
    def preuzmi_projekat(self, projekat):
        if projekat.mockup:
            print(f"Preuzet je projekat {projekat.tip}")
            projekat.preuzet_za_rad = True
        else:
            print("Donesite i mockup")
           

moja_firma = Firma("IT Akademija", 300, True)
moja_firma.zaposli_nove(10)
print(moja_firma.broj_zaposlenih)  
moja_firma.otpusti_ljude(50)
moja_firma.preuzmi_projekat(app3)
print(app3.preuzeta_za_rad)


        
        