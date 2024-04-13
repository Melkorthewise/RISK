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
    # player1 = []
    # player2 = []
    # player3 = []

    # shuffled_keys = random.sample(list(gebiedskaarten.keys()), len(gebiedskaarten))
    # landen = {key: gebiedskaarten[key] for key in shuffled_keys}

    # for x in landen:
    #     while True:
    #         y = random.randint(1, 100)

    #         if y % 3 == 0 and len(player1) != 14: # Speler 1
    #             player1.append((x, landen[x]))
    #             break
    #         elif y % 3 == 1 and len(player2) != 14: # Speler 2
    #             player2.append((x, landen[x]))
    #             break
    #         elif len(player3) != 14: # Speler 3
    #             player3.append((x, landen[x]))
    #             break

    # return player1, player2, player3

    landen = (
        [
            ('Alaska', {'continent': 'N_Amerika', 'troep': 'I', 'locatie': '(105, 120)', 'grenzen': ['Noordwestelijke Staten', 'Alberta', 'Kamtsjatka'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Peru', {'continent': 'Z_Amerika', 'troep': 'I', 'locatie': '(309, 508)', 'grenzen': ['Venezuela', 'Brazilie', 'Argentinie'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Argentinie', {'continent': 'Z_Amerika', 'troep': 'I', 'locatie': '(334, 596)', 'grenzen': ['Peru', 'Brazilie'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Scandinavie', {'continent': 'Europa', 'troep': 'C', 'locatie': '(588, 163)', 'grenzen': ['Ijsland', 'Rusland', 'Groot-Brittannie', 'Noord-Europa'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Rusland', {'continent': 'Europa', 'troep': 'C', 'locatie': '(684, 217)', 'grenzen': ['Scandinavie', 'Noord-Europa', 'Zuid-Europa', 'Oeral', 'Afghanistan', 'Midden-Oosten'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Groot-Brittannie', {'continent': 'Europa', 'troep': 'A', 'locatie': '(495, 255)', 'grenzen': ['Ijsland', 'Scandinavie', 'Noord-Europa', 'West-Europa'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Zuid-Europa', {'continent': 'Europa', 'troep': 'A', 'locatie': '(599, 326)', 'grenzen': ['Noord-Europa', 'West-Europa', 'Rusland', 'Midden-Oosten', 'Noord-Afrika', 'Egypte'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Egypte', {'continent': 'Afrika', 'troep': 'I', 'locatie': '(631, 438)', 'grenzen': ['Noord-Afrika', 'Zuid-Europa', 'Midden-Oosten', 'Oost-Afrika'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Siberie', {'continent': 'Azie', 'troep': 'C', 'locatie': '(849, 143)', 'grenzen': ['Oeral', 'China', 'Yakutsk', 'Irkoetsk', 'Mongolie'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Afghanistan', {'continent': 'Azie', 'troep': 'C', 'locatie': '(774, 283)', 'grenzen': ['Rusland', 'Midden-Oosten', 'Oeral', 'China', 'India'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Japan', {'continent': 'Azie', 'troep': 'A', 'locatie': '(1039, 277)', 'grenzen': ['Mongolie', 'Kamtsjatka'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('Midden-Oosten', {'continent': 'Azie', 'troep': 'I', 'locatie': '(707, 394)', 'grenzen': ['Zuid-Europa', 'Rusland', 'Afghanistan', 'India', 'Egypte', 'Oost-Afrika'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('India', {'continent': 'Azie', 'troep': 'C', 'locatie': '(835, 390)', 'grenzen': ['Midden-Oosten', 'Afghanistan', 'China', 'Zuidoost-Azie'], 'speler': 'blauw', 'aantal_troepen': 1}), 
            ('West-Australie', {'continent': 'Oceanie', 'troep': 'A', 'locatie': '(975, 637)', 'grenzen': ['Indonesie', 'Oost-Australie'], 'speler': 'blauw', 'aantal_troepen': 1}), 
        ],
        [
            ('Noordwestelijke Staten', {'continent': 'N_Amerika', 'troep': 'A', 'locatie': '(217, 121)', 'grenzen': ['Alaska', 'Alberta', 'Ontario', 'Groenland'], 'speler': 'groen', 'aantal_troepen': 1}),
            ('Groenland', {'continent': 'N_Amerika', 'troep': 'C', 'locatie': '(417, 86)', 'grenzen': ['Noordwestelijke Staten', 'Ontario', 'Oost-Canada', 'Ijsland'], 'speler': 'groen', 'aantal_troepen': 1}),  
            ('Ontario', {'continent': 'N_Amerika', 'troep': 'C', 'locatie': '(280, 196)', 'grenzen': ['Noordwestelijke Staten', 'Alberta', 'Groenland', 'Verenigde Staten (West)', 'Oost-Canada', 'Verenigde Staten (Oost)'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Verenigde Staten (West)', {'continent': 'N_Amerika', 'troep': 'A', 'locatie': '(215, 270)', 'grenzen': ['Alberta', 'Ontario', 'Verenigde Staten (Oost)', 'Centraal-Amerika'], 'speler': 'groen', 'aantal_troepen': 1}),
            ('Verenigde Staten (Oost)', {'continent': 'N_Amerika', 'troep': 'A', 'locatie': '(296, 284)', 'grenzen': ['Verenigde Staten (West)', 'Ontario', 'Oost-Canada', 'Centraal-Amerika'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Brazilie', {'continent': 'Z_Amerika', 'troep': 'A', 'locatie': '(382, 483)', 'grenzen': ['Venezuela', 'Peru', 'Argentinie', 'Noord-Afrika'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Ijsland', {'continent': 'Europa', 'troep': 'I', 'locatie': '(511, 169)', 'grenzen': ['Groenland', 'Groot-Brittannie', 'Scandinavie'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Noord-Afrika', {'continent': 'Afrika', 'troep': 'C', 'locatie': '(568, 465)', 'grenzen': ['Brazilie', 'West-Europa', 'Zuid-Europa', 'Egypte', 'Centraal-Afrika', 'Oost-Afrika'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Oost-Afrika', {'continent': 'Afrika', 'troep': 'I', 'locatie': '(680, 500)', 'grenzen': ['Noord-Afrika', 'Egypte', 'Centraal-Afrika', 'Midden-Oosten', 'Zuid-Afrika', 'Madagaskar'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Madagaskar', {'continent': 'Afrika', 'troep': 'C', 'locatie': '(729, 641)', 'grenzen': ['Zuid-Afrika', 'Oost-Afrika'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Kamtsjatka', {'continent': 'Azie', 'troep': 'I', 'locatie': '(1024, 116)', 'grenzen': ['Yakutsk', 'Irkoetsk', 'Mongolie', 'Japan', 'Alaska'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Irkoetsk', {'continent': 'Azie', 'troep': 'C', 'locatie': '(919, 195)', 'grenzen': ['Siberie', 'Yakutsk', 'Kamtsjatka', 'Mongolie'], 'speler': 'groen', 'aantal_troepen': 1}),
            ('Indonesie', {'continent': 'Oceanie', 'troep': 'A', 'locatie': '(931, 540)', 'grenzen': ['Zuidoost-Azie', 'Nieuw-Guinea', 'West-Australie'], 'speler': 'groen', 'aantal_troepen': 1}), 
            ('Oost-Australie', {'continent': 'Oceanie', 'troep': 'A', 'locatie': '(1052, 612)', 'grenzen': ['Nieuw-Guinea', 'West-Australie'], 'speler': 'groen', 'aantal_troepen': 1}), 
        ],
        [
            ('Alberta', {'continent': 'N_Amerika', 'troep': 'C', 'locatie': '(201, 187)', 'grenzen': ['Alaska', 'Noordwestelijke Staten', 'Ontario', 'Verenigde Staten (West)'], 'speler': 'paars', 'aantal_troepen': 1}),
            ('Oost-Canada', {'continent': 'N_Amerika', 'troep': 'C', 'locatie': '(355, 204)', 'grenzen': ['Groenland', 'Ontario', 'Verenigde Staten (Oost)'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Centraal-Amerika', {'continent': 'N_Amerika', 'troep': 'A', 'locatie': '(222, 350)', 'grenzen': ['Verenigde Staten (West)', 'Verenigde Staten (Oost)', 'Venezuela'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Venezuela', {'continent': 'Z_Amerika', 'troep': 'I', 'locatie': '(303, 422)', 'grenzen': ['Centraal-Amerika', 'Peru', 'Brazilie'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Noord-Europa', {'continent': 'Europa', 'troep': 'A', 'locatie': '(587, 262)', 'grenzen': ['Groot-Brittannie', 'Scandinavie', 'Rusland', 'West-Europa', 'Zuid-Europa'], 'speler': 'paars', 'aantal_troepen': 1}),
            ('West-Europa', {'continent': 'Europa', 'troep': 'A', 'locatie': '(518, 343)', 'grenzen': ['Groot-Brittannie', 'Noord-Europa', 'Zuid-Europa', 'Noord-Afrika'], 'speler': 'paars', 'aantal_troepen': 1}),
            ('Centraal-Afrika', {'continent': 'Afrika', 'troep': 'I', 'locatie': '(626, 550)', 'grenzen': ['Noord-Afrika', 'Oost-Afrika', 'Zuid-Afrika', 'Madagaskar'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Zuid-Afrika', {'continent': 'Afrika', 'troep': 'A', 'locatie': '(639, 639)', 'grenzen': ['Centraal-Afrika', 'Oost-Afrika', 'Madagaskar'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Oeral', {'continent': 'Azie', 'troep': 'C', 'locatie': '(794, 190)', 'grenzen': ['Rusland', 'Siberie', 'China', 'Afghanistan'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Yakutsk', {'continent': 'Azie', 'troep': 'C', 'locatie': '(931, 111)', 'grenzen': ['Siberie', 'Kamtsjatka', 'Irkoetsk'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('China', {'continent': 'Azie', 'troep': 'I', 'locatie': '(890, 332)', 'grenzen': ['Oeral', 'Siberie', 'Mongolie', 'India', 'Zuidoost-Azie', 'Afghanistan'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Mongolie', {'continent': 'Azie', 'troep': 'I', 'locatie': '(932, 274)', 'grenzen': ['Siberie', 'Irkoetsk', 'Japan', 'China'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Zuidoost-Azie', {'continent': 'Azie', 'troep': 'I', 'locatie': '(919, 425)', 'grenzen': ['India', 'China', 'Zuidoost-Azie', 'Indonesie'], 'speler': 'paars', 'aantal_troepen': 1}), 
            ('Nieuw-Guinea', {'continent': 'Oceanie', 'troep': 'I', 'locatie': '(1021, 511)', 'grenzen': ['Indonesie', 'Oost-Australie'], 'speler': 'paars', 'aantal_troepen': 1}), 
        ]
    )

    return landen

def troepen_verdelen(landen, kleuren_spelers, automatisch):
    risk = RiskNet()

    overige_troepen = [26, 26, 26] # 40 - 14 ! Niet vergeten terug te veranderen

    running = True

    while overige_troepen != [0, 0, 0]:
        print(f"{kleuren_spelers[0]} heeft {overige_troepen[0]} troepen, {kleuren_spelers[1]} heeft {overige_troepen[1]} troepen en {kleuren_spelers[2]} heeft {overige_troepen[2]} troepen. \n")

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
            # keuze_bot = risk.formule_troepen_plaatsen(landen, kleuren_spelers, 1)
            # landen[1][landen[1].index(keuze_bot)] = keuze_bot
            overige_troepen[1] -= 1

        if overige_troepen[2] != 0:
            # landen[2][random.randint(0, 13)][1]["aantal_troepen"] += 1
            overige_troepen[2] -= 1

        # tabel(landen)
        # input()

    return landen



# TODO def missiekaarten():