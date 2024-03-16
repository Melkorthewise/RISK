from RISKbot import *
from functies import continentbonus, tabel

import numpy as np
import random
import json

with open("Gebiedskaarten.json", "r") as data:
    gebiedskaarten = json.load(data)["gebiedskaarten"]

kleuren = ["blauw", "geel", "groen", "oranje", "paars", "rood"]
kleuren_legers = []

def kleuren_kiezen():
    while True:
        keuze = input("Welke kleur zou je willen zijn?\n>>> ")

        if keuze.lower() in kleuren:
            kleuren_legers.append(keuze.lower())
            kleuren.remove(keuze.lower())

            for x in range(2):
                y = random.randint(1, (len(kleuren) - 1))
                kleuren_legers.append(kleuren[y])
                kleuren.remove(kleuren[y])

            return kleuren_legers

def landen_verdelen():
    player1 = []
    player2 = []
    player3 = []

    shuffled_keys = random.sample(list(gebiedskaarten.keys()), len(gebiedskaarten))
    landen = {key: gebiedskaarten[key] for key in shuffled_keys}

    for x in landen:
        while True:
            y = random.randint(1, 100)

            if y % 3 == 0 and len(player1) != 14: # Speler 1
                player1.append((x, landen[x]))
                break
            elif y % 3 == 1 and len(player2) != 14: # Speler 2
                player2.append((x, landen[x]))
                break
            elif len(player3) != 14: # Speler 3
                player3.append((x, landen[x]))
                break

    return player1, player2, player3

def troepen_verdelen(landen, kleuren_spelers, automatisch):
    risk = RiskNet()

    overige_troepen = [26, 26, 26] # 40 - 14

    running = True

    while overige_troepen != [0, 0, 0]:
        print(f"{kleuren_spelers[0]} heeft {overige_troepen[0]} troepen, {kleuren_spelers[1]} heeft {overige_troepen[1]} troepen en {kleuren_spelers[2]} heeft {overige_troepen[2]} troepen.")

        if overige_troepen[0] != 0 and automatisch == 0:  
            while running:
                try:
                    print(f"{kleuren_spelers[0].title()} is aan de beurt.")
                    keuze = input("Waar zou je troepen willen plaatsen?\n>>> ")

                    for x in landen[0]:
                        if x[0] == keuze.title():
                            landen[0][landen[0].index(x)][1]["aantal_troepen"] += 1
                            overige_troepen[0] -= 1
                            break
                    else:
                        print(f"{keuze.title()} is niet een van jouw landen.")

                    break

                except KeyError:
                    pass

        elif overige_troepen[0] != 0 and automatisch == 1:
            keuze_bot = risk.formule_troepen_plaatsen(landen, kleuren_spelers, 0)
            landen[0][landen[0].index(keuze_bot)] = keuze_bot
            overige_troepen[0] -= 1

        if overige_troepen[1] != 0:
            keuze_bot = risk.formule_troepen_plaatsen(landen, kleuren_spelers, 1)
            landen[1][landen[1].index(keuze_bot)] = keuze_bot
            overige_troepen[1] -= 1

        if overige_troepen[2] != 0:
            landen[2][random.randint(0, 13)][1]["aantal_troepen"] += 1
            overige_troepen[2] -= 1

        # tabel(landen)
        input()

    return landen

# TODO def missiekaarten():