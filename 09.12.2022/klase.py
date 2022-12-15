class Osoba:
    ime = ""
    prezime = ""
    godine = 0


osoba1 = Osoba()
osoba1.ime = "Sofija"
osoba1.prezime = "Sofilic"
osoba1.godine = 25

# print(osoba1.ime, osoba1.prezime, osoba1.godine)

osoba2 = Osoba()
osoba2.ime = "Milovan"
osoba2.prezime = "Ciric"
osoba2.godine = 30

# print(osoba2.ime, osoba2.prezime, osoba2.godine)

pristutni = [osoba1, osoba2]

for o in pristutni:
    print(f"Ime: {o.ime}")
    print(f"Prezime: {o.prezime}")
    print(o.godine)



    
        