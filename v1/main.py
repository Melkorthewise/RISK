# Importeer de benodigde libraries
from termcolor import colored # Voor de kleuren in de terminal
from prettytable import PrettyTable # Om de waardes in een tabel in de terminal te kunnen zetten.

import threading
import queue
import pygame
import time
import os
import json # Om de kaarten te kunnen lezen.
import random

# Importeer de andere python bestanden
from actions import dobbelstenen, plaatsen, verplaatsen, aanvallen
from begin import begin_spel3, legers
from gebiedskaarten import landen_verdelen, tabel, tabel_speler

# tabel1 = PrettyTable()

# Gebiedskaarten bestand openen en data lezen.
with open("Gebiedskaarten.json", "r") as data:
    gebiedskaarten = json.load(data)

# Aantal spelers (tijdig op 2, later terug naar 0), gekozen kleuren, kleuren legers, beurt
spelers = 2
kleuren_spelers = []
kleuren_legers = {
    "blauw": "#71baf6", 
    "geel": "#f5d953", 
    "groen": "#588c60",
    "oranje": "#df7d41",
    "paars": "#588c60",
    "rood": "#ef3740",
}

landen = []
# gespeelde_troepen = {}

landen_speler1 = []
landen_speler2 = []
landen_speler3 = []
landen_speler4 = []
landen_speler5 = []
landen_speler6 = []

# Troepen met de bijhorende waarde.
infanterie = 1
cavalerie = 5
artillerie = 10

# Gebieden
gebieden = 42
continenten = 6

# Waardes van de continenten
N_Amerika = 5
Z_Amerika = 2
Europa = 5
Afrika = 3
Azie = 7
Oceanie = 2

print("\nWelkom bij RISK!")

# while True:
#     spelers = int(input("Wat is het aantal spelers dat meedoen?\n>>> "))

#     if spelers <= 5 and spelers != 0 and spelers != 1 and spelers != None:
#         check = input("Ter bevestiging. Er spelen {} spelers, is dit correct? ".format(spelers))
#         if check == "ja":
#             break
#     else:
#         print("Voer een geldig aantal spelers in. Er kunnen 2 t/m 5 spelers meedoen.\n")

print("Er zijn {} spelers.\n".format(spelers))

print("Welke versie willen jullie spelen?")
print("----------------------------------------------")

if spelers == 2:
    print(colored("Spel 1. RISK met Missiekaarten (3-5 spelers)", "grey", attrs=["dark"]))
    print(colored("Spel 2. Klassiek RISK (3-5 spelers)", "grey", attrs=["dark"]))
    print("Spel 3. RISK voor 2 spelers")
    print(colored("Spel 4: HOOFDKWARTIER RISK (3-5 spelers)", "grey", attrs=["dark"]))
    print("----------------------------------------------\n")

    print("Doordat er 2 spelers zijn, wordt er automatisch Spel 3. gespeeld.")

    kleuren_spelers = begin_spel3()

    # print(kleuren_spelers)

    print("De landen van elke speler zijn hieronder in de tabel te zien. Beide spelers mogen om de beurt op elk van hun landen één Infanterie zetten, speler 1 mag beginnen. Daarna als dat gebeurt is, doe je hetzelfde bij het 'neutrale' leger (Speler 3).")

    landen = landen_verdelen(len(kleuren_spelers))

    landen_speler1 = landen[0]
    landen_speler2 = landen[1]
    landen_speler3 = landen[2]

    tabel(landen)

    # print(gebiedskaarten["gebiedskaarten"][0]["locatie"])
    # print(eval(gebiedskaarten["gebiedskaarten"][0]["locatie"]))

    #input("Wanneer jullie op elk land één troep hebben staan, mag je op enter drukken.")
        
    print("\nAls elk gebied op het bord bezet is, mogen jullie om de beurt je overige troepen: zet twee troepen op één of twee gebieden die je bezet, todat je startvoorraad van 40 Infanterie op is.")
    print("Zet vervolgens om de beurt één neutrale troep op een neutraal gebied naar keuze. Probeer ze zodanig te plaatsen dat je je tegenstander waar mogelijk hindert. Ga zo verder totdat alle 40 neutrale Infanterie speelstukken geplaatst zijn.")
    print("Als alle 40 Infanterie speelstukken van de drie legers zijn geplaatst.\n")

    # input("Druk enter om verder te gaan.\n")

else:
    print("Spel 1. RISK met Missiekaarten (3-5 spelers) \nSpel 2. Klassiek RISK (3-5 spelers)", colored("\nSpel 3. RISK voor 2 spelers", "grey", attrs=["dark"]), "\nSpel 4: HOOFDKWARTIER RISK (3-5 spelers)")

    versie = input(">>> ")

pygame.init()
#pygame.font.init()

flags = pygame.SCALED | pygame.RESIZABLE

screen = pygame.display.set_mode((1140, 734), flags)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans MS', 20)

pygame.display.set_caption("RISK")

bg = pygame.image.load(os.path.join("images", "map3.jpg"))

actie = [2]
speler = 0
beurt = kleuren_spelers[speler]


playing = True
invoer = True

user_input_queue = queue.Queue()
processing_event = threading.Event()

for x in range(len(kleuren_spelers)):
    z = 0
    for y in landen[x]:
        land = y[0], {"continent": y[1]["continent"], "troep": y[1]["troep"], "locatie": y[1]["locatie"], "grenzen": y[1]["grenzen"], "speler": kleuren_spelers[x], "aantal_troepen": 1},
        #land = {y["land"]:[{"speler": kleuren_spelers[x], "aantal_troepen": 1}]}

        landen[x][z] = land
        
        z += 1

def get_user_input(actie, speler):
    invoer = True
    bezig = True

    troepen = []

    while invoer:
        if actie == [-1]: # Voor aanvallen
            land = aanvallen(beurt, landen)

            waarvandaan, waarnaartoe, troepen, hoeveel = land

            for x in landen:
                for y in x:
                    if waarvandaan in y and troepen == hoeveel:
                        y[1]["aantal_troepen"] -= troepen
                    elif waarvandaan in y and troepen == 0:
                        y[1]["aantal_troepen"] = troepen + 1
                    elif waarvandaan in y and troepen != hoeveel:
                        y[1]["aantal_troepen"] -= hoeveel

                    if waarnaartoe in y and troepen != 0:
                        y[1]["speler"] = beurt
                        y[1]["aantal_troepen"] = troepen

        elif actie == [-2]: # Voor verplaatsen
            troepen = verplaatsen(beurt, landen[speler])

            if troepen != None:
                for y in landen[speler]:
                    if y[0] == troepen[0]:
                        land = "{}".format(troepen[0])
                        y[1]["aantal_troepen"] = y[1]["aantal_troepen"] - troepen[2]
                    elif y[0] == troepen[1]:
                        land = "{}".format(troepen[1])
                        y[1]["aantal_troepen"] = y[1]["aantal_troepen"] + troepen[2]

            print("Einde beurt\n")

            if speler == (spelers - 1):
                speler = 0
                print("Next player's turn")
            else:
                speler += 1

            beurt = kleuren_spelers[speler]

            # Reset actie to 0 for the new player's turn
            if actie[0] != 1:
                actie[0] = 1

            invoer = False


        for x in range(len(kleuren_spelers)):
            troep = 0
            for y in landen[x]:
                for spelers in kleuren_spelers:
                    if y[1]["speler"] == spelers:
                        troep += y[1]["aantal_troepen"]

            troepen.append(40 - troep)

        while bezig:
            for spelers in range(len(kleuren_spelers)):
                if troepen[spelers] == 0:
                    print("{} heeft geen troepen meer. De volgende is aan de beurt.\n".format(kleuren_spelers[spelers]))
                else:
                    print("{} is aan de beurt om troepen te plaatsen.".format(kleuren_spelers[spelers]))

                    while True:
                        # print(troepen)
                        try:
                            hoeveel = int(input("Je hebt {} troepen om te plaatsen. Hoeveel troepen wil je plaatsen?\n>>> ".format(troepen[spelers])))
                                
                            while True:
                                try:
                                
                                    waarnaartoe = input("Naar welk land wil je de troepen plaatsen?\n>>> ")
                                    # print()

                                    # print(y, gespeelde_troepen[y][0])
                                    y = 0
                                    for x in landen[spelers]:
                                        if waarnaartoe.title() == x[0]:
                                            x[1]["aantal_troepen"] = x[1]["aantal_troepen"] + hoeveel

                                            troepen[spelers] = troepen[spelers] - hoeveel
                                            
                                            print()
                                            y = 0
                                        elif waarnaartoe.title() != x[0] and y == (40 / len(kleuren_spelers)):
                                            print("Dit is niet een van jou landen. Vul alstjeblieft een van jou landen in.\n")
                                            break

                                        y += 1
                                    
                                    break
                                except ValueError:
                                    print("Dit is geen geldig land.")
                                
                                    break
                        
                        except ValueError:
                            print("Dit is geen geldig aantal troepen.")
                            
                        break

                if all(item == 0 for item in troepen):
                    troepen = []
                    bezig = False

            actie = [1]

    while invoer:
        if actie[0] == 1:
            actie[0] += 1

            print("{} is aan de beurt.".format(beurt))

            troepen = plaatsen(beurt, speler, landen)

            for x in range(len(troepen[0])):
                for y in landen[speler]:
                    if y[0] == troepen[0][x]:
                        y[1]["aantal_troepen"] = y[1]["aantal_troepen"] + troepen[1][x]

        elif actie[0] > 1:
            actie[0] += 1

            print(beurt, "is aan de beurt.\n")
            print("-------------------------------------------------------------")
            print("Mogelijke acties:")
            print("- aanvallen (Aanvallen)")                    
            print("- verplaatsen (Troepen verplaatsen (einde van de beurt))")
            print("-------------------------------------------------------------")
            user_input = input("Wat zou je willen doen?\n>>> ")
            user_input_queue.put(user_input)

            processing_event.wait()
            processing_event.clear()

# Start een thread voor gebruikers input
input_thread = threading.Thread(target=get_user_input, args=(actie, speler,), daemon=True)
input_thread.start()

while playing:

    pygame.display.set_caption("RISK - {} is aan de beurt".format(beurt))

    # poll for events
    # pygame.QUIT event means the user clicked the X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        # if event.type == pygame.MOUSEBUTTONUP:
        #     pos = pygame.mouse.get_pos()

        #     print(pos)

    screen.blit(bg, (0, 0))

    pygame.draw.circle(screen, kleuren_legers[beurt], (20, 20), 10)
    text2 = font.render("1  = aantal legers", False, "#FFFFFF")
    screen.blit(text2, (16, 4))

    for x in range(len(kleuren_spelers)):
        for y in landen[x]:
            # print(type(y), y[1])
            pygame.draw.circle(screen, kleuren_legers[y[1]["speler"]], eval(y[1]["locatie"]), 10)

            # z = gespeelde_troepen.get(y["land"])
            tekst = "{}".format(y[1]["aantal_troepen"])

            (X, Y) = eval(y[1]["locatie"])

            text = font.render(tekst, False, "#FFFFFF")
            screen.blit(text, (X - 5, Y - 15))
    

    pygame.display.update()

    try:
        user_input = user_input_queue.get_nowait()
        print("User input:", user_input, "\n")

        if user_input.lower() == 'exit':
            playing = False

        elif user_input.lower() == 'aanvallen':
            actie = [-3]

        elif user_input.lower() == 'verplaatsen':
            actie = [-2]

        # Signal that processing is complete
        processing_event.set()

    except queue.Empty:
        pass


# Bestand sluiten
data.close()

pygame.quit()