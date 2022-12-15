def digitron(broj1, broj2, operacija):
    if operacija == "+":
        print(broj1 + broj2)
        return broj1 + broj2
    elif operacija == "-":
        print(broj1 - broj2)
        return broj1 - broj2
    elif operacija == "*":
        print(broj1 * broj2)
        return broj1 * broj2
    elif operacija == "/":
        print(broj1 / broj2)
        return broj1 / broj2
    else:
        print("Pogresna operacija")

rezultat = digitron(10, 5, "+")
#rezultat_sabiranja
print(rezultat)
rezultat_oduzimanja = digitron(10, 5, "-")

brojevi = [1, 2, 3]
broj_clanova = len(brojevi)

print(broj_clanova)


# ime = input("Unesite ime: ")
# prezime = input("Unesite prezime: ")
# godina = input("Godina (21, 22, 23...): ")

# korisnicko_ime = ""

# def kreiraj_kor_ime(ulaz_ime, ulaz_prezime, ulaz_godina):
#     kor_ime = f"ita{ulaz_godina}.{ulaz_ime.lower()}{ulaz_prezime.lower()}"
#     print("Uspesno kreirano kor ime!")
#     return kor_ime

# korisnicko_ime = kreiraj_kor_ime(ime, prezime, godina)

# print("Prikupljeni podatci o korisniku:")
# print(ime, prezime, korisnicko_ime)

# funkcija - menjacnica
# parametri - eur
# POVRATNA VREDNOST: rezultat u dinarima

# racunanje eur * 117

# dobijeni_dinari = ....

# def menjacnica(eur):
#     dinari = eur * 117
#     return dinari

# dobijeni_dinari = menjacnica(int(input("Unesite vrednost u evrima: ")))
# print("Rezultat:", dobijeni_dinari)

# registracija
# licna karta,cist automobil, saobracajna
# registrovana kola "Uspesno!" "Neuspesno, dodjite opet"

# def registracija(licna_karta,cist_auto, saobracajna):
#     if cist_auto == False or licna_karta == False or saobracajna == False:
#         return "Neuspesno, dodjite opet!"
    
#     else:
#         return "Uspesno"

# print(registracija(True, True, False))

# funkcijja - bankomat
# parametri - stanje, zeljeni_iznos
# stanje >= zeljeni_iznos -> "Uspesno izvrseno, stanje: ???"
# -> Neuspesno! stanje: ???

def bankomat(stanje, zeljeni_iznos):
    if stanje >= zeljeni_iznos:
        return f"Uspesno!!! Novo stanje je:{stanje - zeljeni_iznos}"
    else:
        return "Neuspesno"

print(bankomat(500, 200))
rezultat = bankomat(100, 80)
print(rezultat)

def registracija(*dokumenti):
    print("Doneli ste dokumenta:")
    print(dokumenti)
    print(dokumenti[0])
    print(type(dokumenti))
registracija("vozacka dozvola", "obavio tehnicki pregled", "licna karta")

def upis(**podaci):
    print("Uneli ste podatke")
    print(podaci["ime"])
    print(type(podaci))
    

upis(ime="Aleksandra", prezime="Lazarevic", ustanova="ita")

def skolovanje(predavac_predaje):
    print("Skolska godina je u toku..")
    print("Ucionica A22")
    # Odavde nastupa predavac
    predavac_predaje()

def predavac_vm():
    print("Uvod u mreze")
    print("Danas radimo novu temu")
    print("Da li ste igrali LOL?")

def predavac_al():
    print("Opet imamo predavanje sredom")
    print("Radimo funkcije")

def predavac_vn():
    print("Krecemo sa kurskom HTML i CSS")

skolovanje(predavac_vm)   


def priprema_obroka(spremanje):
    print("Dolazak u kuhinju")
    print("Perem ruke")
    #priprema obroka...
    spremanje()
    print("Perem sudove")

def dorucak():
    print("Idem po burek")
    print("To je to od kuvanja")

def rucak():
    print("Pohovanje")
    print("Restovan krompir")

def vecera():
    print("Tunjevina salata")
    print("Sladoled")

priprema_obroka(dorucak)

res = lambda a, b: a + b
res(10, 5)

# def tajmer(sekunde):
#     print(sekunde)
#     sekunde -= 1
#     if sekunde > 0:
#         tajmer(sekunde)
    
# tajmer(10)

def provera(funkcija):
    def unutrasnja_funkcija(a, b):
        if b == 0:
           print("Nije dozvoljeno deljenje sa nulom")
           return
        funkcija(a, b)
    return unutrasnja_funkcija


@provera
def deljenje(a, b):
    print(a/b)

deljenje(10, 5)

def brojevi():
    yield 1
    yield 2
    yield 3

dobijeni_broj = brojevi()
print(dobijeni_broj)
print(next(dobijeni_broj))
print(next(dobijeni_broj))
print(next(dobijeni_broj))






        
    

    
