import random
import time
class Team:
    def __init__(self, naziv_tima):
        self.naziv = naziv_tima

class Score:
    domaci = 0
    gosti = 0

class Match:      #    Team   Team  Int    Score 
    def __init__(self, tim1, tim2, minuti, score):
        self.domaci = tim1
        self.gosti = tim2
        self.minuti = minuti
        self.score = score

    def start(self):
        print("Zapoceta je utakmica")
        while True:

            # self.score.domaci = random.randint(0, 10)
            # self.score.gosti = random.randint(0, 10)
            nas_broj_tim_1 = 5
            nas_broj_tim_2 = 7

            if nas_broj_tim_1 == random.randint(0, 10):
                self.score.domaci +=1
                self.score.gosti +=0

            if nas_broj_tim_2 == random.randint(0, 10):
                self.score.gosti +=1
                self.score.domaci +=0

            print(f"{self.domaci.naziv} - {self.gosti.naziv}")
            print(f"{self.score.domaci} - {self.score.gosti}")

            time.sleep(0.5)

            self.minuti += 1

            if self.minuti >=90:
                print("Utakmica je gotova")
                return

tim1 = Team("Crvena Zvezda")
tim2 = Team("Partizan")

utakmica = Match(tim1, tim2, 0, Score())
utakmica.start()