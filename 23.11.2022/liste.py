osoba = ["Sofija", 25, "plava", False]

for indeks in range(len(osoba)):
    print(osoba[indeks])

              # "Sofija", 25, "plava", False
for osobina in osoba:
    print(osobina)

voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana","mandarina", "lubenica", "krastavac"]

for stavka in voce_i_povrce:
    print(stavka)

# for i in range(len(voce_i_povrce)):
#     print(voce_i_povrce[i])

for i in range(len(voce_i_povrce)):
    print("Na indeksu:", i, "nalazi se", voce_i_povrce[i])


for indeks, vrednost in enumerate(voce_i_povrce):
    print("Indeks:", indeks, "Stavka:", vrednost)


automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo"]

# Pozicija: 0 Auto: Citroen
for pozicija, auto in enumerate(automobili):
    print("Pozicija:", pozicija, "Auto:", auto)

for pozicija, auto in enumerate(automobili):
    if len(auto) ==3:
        print(auto)

#prosirenje ponude
automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3] = "Kia Sportage"

del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)
automobili.pop(0)
print(automobili)

automobili[0]
broj_opela = 0
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("Evo ga Opel")
        broj_opela += 1
print("Imam ",broj_opela, "Na placu")

automobili.clear()
print(automobili)

prazan_plac = []
#
automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot", "Audi"]

automobili_akcija = []
for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])

print(automobili_akcija)

automobili_akcija = automobili[1:4]
print(automobili_akcija)

#lista
# prazne liste,parni neparni
# for
# %
# if else

brojevi = [3,7,1,9,2,4,5,12]
parni = []
neparni = []

for broj in brojevi:
    parni.append(broj if broj % 2 == 0 else neparni.append(broj))
    # if broj % 2 == 0:
    #     parni.append(broj)
    # else:
    #     neparni.append(broj)

print(parni,neparni)