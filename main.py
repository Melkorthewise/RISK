from begin import kleuren_kiezen, landen_verdelen, troepen_verdelen
from functies import continentbonus, tabel
from RISKbot import *
from acties import troepen_verplaatsen

import matplotlib.pyplot as plt
import pygame

# Variabelen
kleuren_legers = {
    "blauw": "#71baf6",
    "geel": "#f5d953",
    "groen": "#588c60",
    "oranje": "#df7d41",
    "paars": "#7f638c",
    "rood": "#ef3740",
}

kleuren_spelers = kleuren_kiezen()
print(type(kleuren_spelers), kleuren_spelers)
kleuren_spelers = ("blauw", "groen", "paars")

landen = landen_verdelen()

for x in range(len(kleuren_spelers)):
    z = 0
    for y in landen[x]:
        land = y[0], {"continent": y[1]["continent"], "troep": y[1]["troep"], "locatie": y[1]["locatie"], "grenzen": y[1]["grenzen"], "speler": kleuren_spelers[x], "aantal_troepen": 1},
        #land = {y["land"]:[{"speler": kleuren_spelers[x], "aantal_troepen": 1}]}

        landen[x][z] = land

        z += 1

# print(landen)

tabel(landen)

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1140, 734))
font = pygame.font.SysFont('Comic Sans MS', 20)

bg = pygame.image.load("images/kaart.jpg")
pygame.display.update()

landen = troepen_verdelen(landen, kleuren_spelers, 1) # 0 is speler, 1 is bot

# ? Plot van voor en na het verdelen van de overige troepen.

# TODO Kiezen of je met missiekaarten wilt spelen.

tabel(landen)

running = True
beurt = 0

# Begin spel
while running:

    pygame.display.set_caption("RISK - {} is aan de beurt".format(kleuren_spelers[beurt]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # De achtergrond tekenen op het scherm.
    screen.blit(bg, (0, 0))

    pygame.draw.circle(screen, kleuren_legers[kleuren_spelers[beurt]], (20, 20), 10)
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

    # Update het scherm.
    pygame.display.update()

    troepen_verplaatsen(landen, kleuren_spelers)