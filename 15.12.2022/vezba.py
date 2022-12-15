# PROIZVOD - naziv, opis, cena
# KORPA - spisak_proizvoda, ukupna_cena

class Proizvod:
    def __init__(self, naziv, opis, cena):
        self.naziv = naziv
        self.opis = opis
        self.cena = cena

class Korpa:
    def __init__(self, spisak_proizvoda):
        self.spisak_proizvoda = spisak_proizvoda # svojstvo 1
        res = 0
        for pr in spisak_proizvoda:
            res += pr.cena
        self.ukupna_cena = res                   # svojstvo 2

pr1 = Proizvod("Patike", "Fudbalske patike", 27000)
pr2 = Proizvod("Patike", "Kosarkaske patike", 15000)
pr3 = Proizvod("Papuce", "Cross", 5000)

lista_pr = []
lista_pr.append(pr2)
lista_pr.append(pr1)
lista_pr.append(pr3)

korpa = Korpa(lista_pr)
print(korpa.ukupna_cena)
