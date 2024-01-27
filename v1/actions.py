from os import error
import random
from gebiedskaarten import tabel_speler
import time
import json

with open("Gebiedskaarten.json", "r") as data:
    landen = json.load(data)


continenten = ["N_Amerika", "Z_Amerika", "Europa", "Afrika", "Azie", "Oceanie"]
veroverde_landen = []

punten = [5, 2, 5, 3, 7, 2]
aantal_landen = [9, 4, 7, 6, 12, 4]

sets = [] # Ingeleverde sets

def dobbelstenen(aantal):
    dobbel = []
    for x in range(aantal):
        dobbel.append(random.randint(1,6))
    return dobbel

def plaatsen(beurt, speler, landen):
    waar = []
    troepen = []
    check = []

    set_waarde = 4
    jokers = 0
    aantal = 0

    # Aantal troepen voor veroverde landen.
    for x in landen[speler]:
        aantal += 1

    aantal = int(aantal / 3)

    # Aantal troepen voor complete continenten.
    for y in continenten:
        totaal = 0
        for x in landen[speler]:
            if x[1]["continent"] == y:
                totaal += 1

        veroverde_landen.append(totaal)

    # Punten toerekenen voor de continenten.
    for x in range(6):
        if aantal_landen[x] == veroverde_landen[x]:
            aantal += punten[x]


    set = input("Wil je een set inleveren?\n>>> ")

    if set.lower() == "ja":
        set = []
        ingeleverd = False
        kaarten = 0

        print("\nWelke kaart heb je? Voer één kaart per keer in.")

        for x in range(3):
            while ingeleverd == False:
                kaart = input("Kaart {}. >>> ".format(kaarten + 1))
                
                if kaart.lower() == 'exit':
                    print("Set inleveren geannuleerd.\n")
                    ingeleverd = True
                    
                alle = 0

                if kaart.lower() == "joker":
                    if sets == []:
                        kaarten += 1
                        set.append(kaart.lower())
                        check.append("J")
                        if kaarten == 3:
                            ingeleverd = True
                            kaarten = 0
                        break
                    else:
                        for x in sets:
                            for y in x:
                                if kaart.lower() == y:
                                    print("Deze kaart is al ingeleverd in een eerdere set.\n")
                                    break
                                else:
                                    if jokers <= 1:
                                        kaarten += 1
                                        jokers += 1
                                        set.append(kaart.lower())
                                        check.append("J")
                                        if kaarten == 3:
                                            ingeleverd = True
                                            kaarten = 0
                                        break
                                    else:
                                        print("Alle jokers zijn al ingeleverd.\n")
                                        break
                else:
                    for x in range(6):
                        for land in landen[x]:
                            print(land, land[0])
                            #print(kaart.lower(), land["land"].lower())
                            if kaart.lower() == land[0].lower():
                                #print(sets)
                                if sets == []:
                                    kaarten += 1
                                    set.append(kaart.lower())
                                    check.append(land[1]["troep"])
                                    if kaarten == 3:
                                        ingeleverd = True
                                        kaarten = 0
                                    break
                                else:
                                    for x in sets:
                                        for y in x:
                                            if kaart.lower() == y:
                                                print("Deze kaart is al ingeleverd in een eerdere set.\n")
                                                break
                                            else:
                                                kaarten += 1
                                                set.append(kaart.lower())
                                                check.append(land[1]["troep"])
                                                if kaarten == 3:
                                                    ingeleverd = True
                                                    kaarten = 0
                                                break
                            else: # Even wat ruimte opvullen voor tegen de verwarring.
                                alle += 1
                                if alle == 42:
                                    print("Dit is geen correcte kaart. Voer een andere kaart in of voer 'exit' in om te stoppen.\n")
            
        if len(set) == 3:
            if ((check[0] == check[0] or check[0] == "J") and (check[1] == check[0] or check[1] == "J") and (check[2] == check[0] or check[2] == "J")):
                print("De set is ingeleverd.\n")
                sets.append(set)

                # print(aantal)
                aantal += set_waarde
                # print(aantal)

                if len(sets) <= 5:
                    set_waarde += 2
                else:
                    set_waarde += 5
                
            if ((check[0] == check[0] or check[0] == "J") and (check[1] != check[0] or check[1] == "J") and (check[2] != check[0] or check[2] == "J")):
                print("De set is ingeleverd.\n")
                sets.append(set)

                # print(aantal)
                aantal += set_waarde
                # print(aantal)

                if len(sets) <= 5:
                    set_waarde += 2
                else:
                    set_waarde += 5

    # Troepen plaatsen
    while True:
        if aantal > 0:
            tabel_speler(landen[speler], waar, troepen, beurt)

            print("Je mag deze beurt {} troepen plaatsen.".format(aantal))
            try:
                aantal_troepen = int(input("Hoeveel troepen wil je plaatsen?\n>>> "))

                if aantal_troepen <= aantal:

                    print("Waar wil je deze plaatsen? Je plaatst de troepen per land totdat je troepen op zijn.")
                    land = input(">>> ")

                    alle = 1

                    for x in landen[speler]:
                        try:
                            # print("Do or do not. There is no try.")
                            if (x[0] == land.title()):
                                if x[1]["speler"] == beurt:
                                    waar.append(land)
                                    troepen.append(aantal_troepen)

                                    aantal -= aantal_troepen

                                    alle = 0
                                    break
                            else:
                                alle += 1
                                if alle == 42:
                                    print("Je bezit dit land niet.\n")
                        except KeyError:
                            print("{0} is niet een van jouw landen.".format(waar))
                else:
                    print("Je hebt niet genoeg troepen om te plaatsen.\n")
            except ValueError:
                print("Dit is geen geldig aantal troepen.\n")
        else:
            # print(waar, troepen)
            return waar, troepen

def verplaatsen(speler, landen):
    waarvandaan = []
    hoeveel = []
    waarnaartoe = []

    print("Nu gaan we de troepen verplaatsen. Je mag troepen verplaatsen van één land naar één ander land. Er moet minimaal 1 troep achterblijven.")
    while True:
        check = input("Wil je troepen verplaatsen?\n>>> ")
        if check.lower() == "nee":
            break
        try:
            waarvandaan = input("Van welk land wil je je troepen verplaatsen?\n>>> ")

            # print(landen)

            for x in landen:
                # print(x[0], waarvandaan.title(), "\n", x[1], "\n")
                if x[0] == waarvandaan.title():
                    # print(x[0], "\n")
                    print(x, "\n", x[1]["aantal_troepen"])
                    if x[1]["aantal_troepen"] > 1:
                        while True:
                            try:
                                hoeveel = int(input("Hoeveel troepen wil je van dit land verplaatsen? Je kunt er maximaal {} verplaatsen.\n>>> ".format(x[1]["aantal_troepen"] - 1)))

                                if (x[1]["aantal_troepen"] - 1) >= hoeveel >= 0:
                                    break
                                else:
                                    print("Je kunt niet zoveel troepen verplaatsen.")
                            except ValueError:
                                print("Dit is geen geldig aantal troepen.")
                            
                        while True:
                            try:
                                waarnaartoe = input("Naar welk land wil je de troepen verplaatsen?\n>>> ")

                                if x[1]["speler"] == speler:
                                    if x[0] == waarvandaan.title():
                                        # print(x["land"])
                                        for y in x[1]["grenzen"]:
                                            if y == waarnaartoe:
                                                return waarvandaan, waarnaartoe, hoeveel
                                            else:
                                                print("Deze landen grenzen niet aan elkaar.\n")
                                else:
                                    print("{0} is niet een van jouw landen.\n".format(waarnaartoe))
                            except ValueError:
                                print("Dit is geen geldig land.")
                    else:
                        print("Dit land heeft geen genoeg troepen.\n")
                        break
                # else:
                #     print("{0} is niet een van jouw landen.".format(waarvandaan))
        except KeyError or ValueError:
            print("Dit is geen geldig land.")

def aanvallen(aanvaller, landen):
    # print(aanvaller, gespeelde_troepen, landen)

    aanvallen = True
    kaart = False

    troepen_a = 0
    troepen_v = 0

    while aanvallen:
        check = input("Weet je zeker dat je wilt aanvallen?\n>>> ")
        if check.lower() == "nee":
            break
        try:
            waarvandaan = input("Met welk land zou je willen aanvallen?\n>>> ")

            for x in landen:
                for y in x:
                    if y[0] == waarvandaan.title() and y[1]["speler"] == aanvaller:
                        while True:
                            try:
                                hoeveel = int(input("Hoeveel troepen wil je gebruiken om aan te vallen? Je kunt er maximaal {} gebruiken.\n>>> ".format(y[1]["aantal_troepen"] - 1)))

                                if (y[1]["aantal_troepen"] - 1) >= hoeveel >= 0:
                                    troepen_a += hoeveel
                                    break
                            except ValueError:
                                print("Dit is geen geldig aantal troepen.")
                    elif y[0] == waarvandaan.title() and y[1]["speler"] != aanvaller:
                        print("{0} is niet een van jouw landen.".format(waarvandaan))
                    
                    break
            
            while True:
                try:
                    waarnaartoe = input("Welk land zou je willen aanvallen?\n>>> ")

                    for x in landen:
                        for y in x:
                            if y[0] == waarnaartoe.title() and y[1]["speler"] != aanvaller:
                                if waarvandaan.title() in y[1]["grenzen"]: # Kijken of de landen (waarvandaan en waarnaartoe) aan elkaar grenzen.
                                    troepen_v += y[1]["aantal_troepen"]

                                    print("{} heeft {} troepen en {} heeft {} troepen.\n".format(waarvandaan, troepen_a, waarnaartoe, troepen_v))

                                    while True:
                                        rood = []
                                        blauw = []

                                        if troepen_a >= 3:
                                            rood += dobbelstenen(3)
                                        elif troepen_a < 3:
                                            rood += dobbelstenen(hoeveel)
                                        if troepen_v > 2:
                                            blauw += dobbelstenen(2)
                                        elif troepen_v < 2:
                                            blauw += dobbelstenen(1)

                                        rood.sort(reverse=True)
                                        blauw.sort(reverse=True)

                                        print("{} heeft {} gegooid.".format(aanvaller, rood))
                                        print("{} heeft {} gegooid.\n".format(y[1]["speler"], blauw))

                                        for x in range(len(blauw)):
                                            if blauw[x] >= rood[x]:
                                                troepen_a -= 1
                                            elif rood[x] > blauw[x]:
                                                troepen_v -= 1
                                            
                                            if troepen_v == 0 or troepen_a == 0:
                                                return waarvandaan, waarnaartoe, troepen_a, hoeveel
                                            else:
                                                check = input("Wil je doorgaan met aanvallen?\n>>> ")
                                                print()

                                                if check.lower() == "nee":
                                                    return waarvandaan, waarnaartoe, troepen_a, hoeveel
                                            
                                        
                                            
                                        
                                else:
                                    print("Deze landen grenzen niet aan elkaar.")


                            elif y[0] == waarnaartoe.title() and y[1]["speler"] == aanvaller:
                                print("Dit is een van jou eigen landen.")
                                
                except KeyError or ValueError:
                    print("Dit is geen geldig land of dit is een van je eigen landen.")
            
            break

        except KeyError or ValueError:
            print("Dit is geen geldig land.")