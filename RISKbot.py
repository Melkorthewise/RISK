from functies import continentbonus

import matplotlib.pyplot as plt
import numpy as np

class RiskNet:
    def __init__(self, landen, kleuren_spelers):
        self.landen = landen
        self.kleuren_spelers = kleuren_spelers

        self.continenten = ["N_Amerika", "Z_Amerika", "Europa", "Afrika", "Azie", "Oceanie"]
        self.lpc = [0, 0, 0, 0, 0, 0]
        self.aantal_landen = [9, 4, 7, 6, 12, 4]

        plt.bar(self.continenten, self.aantal_landen, color="#ccd0c8")

        for y in self.landen[1]:
            # print(y[1]["continent"])
            # self.continent.append(y[1]["continent"])

            z = self.continenten.index(y[1]["continent"])
            self.lpc[z] += 1

        # print(self.B)

        plt.bar(self.continenten, self.lpc)
        plt.show()


    def formule(self):
        self.score = 0

        for x in self.landen[1]:
            self.A = len(x[1]["grenzen"])
            self.C = continentbonus(self.landen)

            y = self.continenten.index(x[1]["continent"])
            self.Continentbonus = self.C[y]
                    

            # score = self.A * self.w_A + self.C * self.w_C + self.S + self.w_S - self.B * self.w_B

