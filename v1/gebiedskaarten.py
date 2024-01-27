import json
import random

from prettytable import PrettyTable # Om de waardes in een tabel in de terminal te kunnen zetten.

tabel1 = PrettyTable()
tabel2 = PrettyTable()

s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []

with open("Gebiedskaarten.json", "r") as data:
    gebiedskaarten = json.load(data)

# print(landen)
# print(landen["gebiedskaarten"])
    
# print("Er zijn: ", len(landen["gebiedskaarten"]), "landen.")
    
def landen_verdelen(spelers):
    kaarten = 0

    if spelers == 3:
        kaarten = 42 / spelers
        #print(int(kaarten), "kaarten per persoon")

    for x in gebiedskaarten["gebiedskaarten"]:
        while True:
            y = random.randint(1, 6)

            if (y == 1 or y == 7) and len(s1) != kaarten: # Speler 1
                s1.append((x, gebiedskaarten["gebiedskaarten"][x]))
                break
            elif (y == 2 or y == 8) and len(s2) != kaarten: # Speler 2
                s2.append((x, gebiedskaarten["gebiedskaarten"][x]))
                break
            elif (y == 3 or y == 9) and len(s3) != kaarten: # Speler 3
                s3.append((x, gebiedskaarten["gebiedskaarten"][x]))
                break
            else:
                y = random.randint(1, 6)

            # Voor als er meer dan 3 spelers nodig zijn.
            if (y == 4 or y == 10) and len(s1) != kaarten and spelers == 4: # Speler 4
                s1.append((x, gebiedskaarten["gebiedskaarten"][x]))
                break
            else:
                y = random.randint(1, 3)

            if (y == 5 or y == 11) and len(s2) != kaarten and spelers == 5: # Speler 5
                s2.append((x, gebiedskaarten["gebiedskaarten"][x]))
                break
            else:
                y = random.randint(1, 3)

            if (y == 6 or y == 12) and len(s3) != kaarten and spelers == 6: # Speler 6
                s3.append((x, gebiedskaarten["gebiedskaarten"][x]))
                break
            else:
                y = random.randint(1, 6)

    # print("\nSpeler 1: ", len(s1), s1)
    # print("\nSpeler 2: ", len(s2), s2)
    # print("\nSpeler 3: ", len(s3), s3)
    # print("\nSpeler 4: ", len(s4), s4)
    # print("\nSpeler 5: ", len(s5), s5)
    # print("\nSpeler 6: ", len(s6), s6)
    # print()
                
    # s1.sort(key=lambda x: x)
    # s2.sort(key=lambda x: x)
    # s3.sort(key=lambda x: x)
    # s4.sort(key=lambda x: x)
    # s5.sort(key=lambda x: x)
    # s6.sort(key=lambda x: x)

    return s1, s2, s3, s4, s5, s6
    

def tabel(landen):
    # Tabel speler 1
    tabel1.field_names = ["Speler", "Land", "Continent", "Troep"]
    tabel1.align["Speler"] = "l"
    tabel1.align["Land"] = "l"
    tabel1.align["Continent"] = "l"

    y = 0

    for x in landen[0]:
        if y == len(landen[0]) - 1:
            tabel1.add_row(["Speler 1", x[0], x[1]["continent"], x[1]["troep"]], divider=True)
            y = 0
        else:
            tabel1.add_row(["Speler 1", x[0], x[1]["continent"], x[1]["troep"]])
        y += 1

    for x in landen[1]:
        if y == len(landen[1]):
            tabel1.add_row(["Speler 2", x[0], x[1]["continent"], x[1]["troep"]], divider=True)
            y = 0
        else:
            tabel1.add_row(["Speler 2", x[0], x[1]["continent"], x[1]["troep"]])
        y += 1

    for x in landen[2]:
        if y == len(landen[2]):
            tabel1.add_row(["Speler 3", x[0], x[1]["continent"], x[1]["troep"]], divider=True)
            y = 1
        else:
            tabel1.add_row(["Speler 3", x[0], x[1]["continent"], x[1]["troep"]])
        y += 1

    for x in landen[3]:
        if y == len(landen[3]):
            tabel1.add_row(["Speler 4", x[0], x[1]["continent"], x[1]["troep"]], divider=True)
            y = 0
        else:
            tabel1.add_row(["Speler 4", x[0], x[1]["continent"], x[1]["troep"]])
        y += 1
    
    for x in landen[4]:
        if y == len(landen[4]):
            tabel1.add_row(["Speler 5", x[0], x[1]["continent"], x[1]["troep"]], divider=True)
            y = 0
        else:
            tabel1.add_row(["Speler 5", x[0], x[1]["continent"], x[1]["troep"]])
        y += 1
    
    for x in landen[5]:
            tabel1.add_row(["Speler 6", x[0], x[1]["continent"], x[1]["troep"]])

    print(tabel1)

def tabel_speler(landen, waar, troepen, speler):

    tabel2.clear_rows()

    if troepen != []:
        tabel2.field_names = [("Land van {}".format(speler)), "Extra troepen"]
        tabel2.align["Land van {}".format(speler)] = "l"
        
        for x in range(len(waar)):
            for y in landen:
                if y[0] == waar[x]:
                    tabel2.add_row([y[0], troepen[x]])
                else:
                    tabel2.add_row([y[0], "0"])
    else:
        tabel2.field_names = ["Land van {}".format(speler)]
        tabel2.align["Land van {}".format(speler)] = "l"

        for x in landen:
            tabel2.add_row([x[0]])

    print(tabel2)