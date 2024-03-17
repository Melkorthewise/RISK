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

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def neuron(self, input, weights, bias):
        # Bereken de activatie van het neuron
        activation = sum(input * weights) + bias

        # Pas de activatiefunctie toe
        output = self.sigmoid(activation)

        return output

    def formule_troepen_plaatsen(self, landen, kleuren_spelers, speler): # speler begint bij 0
        self.landen = landen
        self.kleuren_spelers = kleuren_spelers

        self.score = None
        self.land = None

        # Er is een percentage aan landen dat een persoon per continent kan hebben.
        # Dit moet ook meegerekend worden in de berekening.
        # Bijvoorbeeld 1 land hebben in Australie is meer waard dan 1 land in Azie.
        self.Continentbonus, self.veroverde_landen = continentbonus(self.landen)

        for x in self.landen[speler]:
            self.A = len(x[1]["grenzen"])

            y = self.continenten.index(x[1]["continent"])
            self.C = self.Continentbonus[y]

            self.aantal = self.aantal_landen[y]
            # print("aantal", self.aantal)

            self.S = 0
            self.B = 0
            self.L = x[1]["aantal_troepen"]

            # Kijken naar de omliggende landen naar hoeveel troepen daar staan van de tegenstanders
            for a in x[1]["grenzen"]:
                for y in range(len(self.kleuren_spelers)):
                    for z in self.landen[y]:
                        # print(z[0], x[0])
                        if z[0] == a and z[1]["speler"] != x[1]["speler"]:
                            self.S += z[1]["aantal_troepen"]

                        elif z[0] == a and z[1]["speler"] == x[1]["speler"] and z[0] != x[0]:
                            self.B += z[1]["aantal_troepen"]

            self.Z = self.aantal_landen[self.continenten.index(x[1]["continent"])]
            self.G = self.veroverde_landen[self.continenten.index(x[1]["continent"])]
            self.P = self.punten[self.continenten.index(x[1]["continent"])]

            # Weights voor alle variabelen
            self.w_A = 1 # A is het aantal omliggende landen
            self.w_C = 1 # C is de continentbonus
            self.w_S = 1 # S zijn de troepen van de speler om het land heen
            self.w_B = 1 # B zijn de troepen van de bot om het land heen
            self.w_L = 1 # L is de troepen in het land zelf

            # TODO formule aanpassen zodat het minder voorkomt dat er twee landen zijn met dezelfde score
            score = self.A * self.w_A + self.C * self.w_C + self.S * self.w_S  - (self.B * self.w_B + self.L * self.w_L)

            # score = self.sigmoid(score)

            print(score, x[0], self.A, self.C, self.S, self.B, self.L, "\n")
            
            if self.score == None or score > self.score:
                self.score = score
                self.land = x

        self.land[1]["aantal_troepen"] += 1

        print("Score:", self.score, "Land: ", self.land)
        print("Aantal landen:", self.aantal_landen)
        print("Veroverde landen:", self.veroverde_landen)
        print("Continentbonus:", self.Continentbonus, "\n")

        return self.land