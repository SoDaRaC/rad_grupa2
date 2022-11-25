import random

kurs = "Python Fundamentals"
print(kurs)

a = 10
b = 5

print(a + b)

rezultat_sabiranja = a + b
print(rezultat_sabiranja)

print("Oduzimanje:", a - b)
print("Mnozenje:", a* b)
print("Deljenje:", a / b)

print("Celobrojno deljenje:", a // b)
print(10 // 3)
print(10 / 3)

print(a ** 2) # a * a
print(a ** 3) # a * a * a

# 10 / 3 = 3
# 3*3 = 9
# 9 + 1 = 10

print(10 % 3)
print(5 % 2)
print(8 % 2)

print(-a)

godine = 25
#godine + 1

godine = godine + 1

godine += 1

print(godine)

godine -= 5
print(godine)

godine *= 2
print(godine)

godine /= 2
print(godine)

godine //= 2
print(godine)

broj1 = 15
broj2 = 20

print("Zbir:", broj1 + broj2)

# broj1 = input("Unesite prvi broj: ")
# print(broj1)

# broj2 = input("Unesite drugi broj: ")
# print(broj2)

# print("Rezultat je:", broj1 + broj2)

# poluprecnik = float(input("Unesite poluprecnik: "))
# pi = 3.14

# povrsina = poluprecnik ** 2 * pi
# print("Povrsina kruga je:", povrsina)

# unos = input("Unesi nesto...")

# print(unos.isnumeric())

stara_kilaza = 80
nova_kilaza = 99

print(stara_kilaza > nova_kilaza)
print(stara_kilaza < nova_kilaza)

print(nova_kilaza != 100)
print(stara_kilaza <= 80)

username = "test"
password = "abc123"

print(username == "test")
print(password == "abc123")

godine = 20
print(godine >= 16)

# broj = int(input("Unestie broj: "))

# provera = broj % 2

# print("Paran broj?", provera == 0)

# korisnik = int(input("Unesite broj: "))
# racunar = random.randint(1, 10)

# print("Korisnik:", korisnik)
# print("Racunar:", racunar)
# print("Pogodak:", korisnik == racunar)


automobil = 0
cilj = 50

print(automobil >= cilj)
automobil += 10
print(automobil >= cilj)

automobil += 20
print(automobil >= cilj)

automobil += 25
print(automobil >= cilj)

provera_imena = True #ime == sacuvano_ime
provera_sifre = False #sifra == sacuvana_sifra

print(provera_imena or provera_sifre)

lepo_vreme = False
print(not lepo_vreme)

# python 2022

kurs = input("Unesite kurs:")
generacija = int(input("Generacija:"))

odobreno = kurs == "python" and generacija == 2022
print(odobreno) 

