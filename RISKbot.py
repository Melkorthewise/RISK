from functies import continentbonus

import matplotlib.pyplot as plt
import numpy as np

class RiskNet:
    def __init__(self):
        # self.landen = landen
        # self.kleuren_spelers = kleuren_spelers

        self.continenten = ["N_Amerika", "Z_Amerika", "Europa", "Afrika", "Azie", "Oceanie"]
        self.aantal_landen = [9, 4, 7, 6, 12, 4]
        self.punten = [5, 2, 5, 3, 7, 2]

        # plt.bar(self.continenten, self.aantal_landen, color="#ccd0c8")

        # plt.bar(self.continenten, self.lpc)
        # plt.show()

    def formule_troepen_plaatsen(self, landen, kleuren_spelers):
        self.landen = landen
        self.kleuren_spelers = kleuren_spelers

        self.score = 0
        self.land = None

        self.Continentbonus = continentbonus(self.landen)

        self.lpc = [0, 0, 0, 0, 0, 0]

        for y in self.landen[1]:
            z = self.continenten.index(y[1]["continent"])
            self.lpc[z] += 1

        for x in self.landen[1]:
            self.A = len(x[1]["grenzen"])

            y = self.continenten.index(x[1]["continent"])
            self.C = self.Continentbonus[y]

            self.aantal = self.aantal_landen[y]
            print("aantal", self.aantal)

            self.S = 0

            # Kijken naar de omliggende landen naar hoeveel troepen daar staan van de tegenstanders
            for a in x[1]["grenzen"]:
                for y in range(len(self.kleuren_spelers)):
                    for z in self.landen[y]:
                        # print(z[0], x[0])
                        if z[0] == a and z[1]["speler"] != self.kleuren_spelers[1]:
                            self.S += z[1]["aantal_troepen"]

            self.B = x[1]["aantal_troepen"]

            print(x[0], self.A, self.C, self.S, self.B)

            self.w_A = 1
            self.w_C = 2
            self.w_S = 3
            self.w_B = 4

            score = self.A * self.w_A + self.C * self.w_C + self.S + self.w_S - self.B * self.w_B

            print("Score:", score, "\n")
            
            if score > self.score:
                self.score = score
                self.land = x

        self.land[1]["aantal_troepen"] += 1

        print(self.score, self.land)
        print(self.aantal_landen)
        print(self.lpc)

        return self.land