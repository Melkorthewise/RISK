from variabelen import landen, kleuren_legers
from voorbereiding import functies
from beurt import actie
from opzet import opzet
from overwinning import voorwaarden

# Variabelen
gamemode = "Klassiek RISK"

spelers = 2 # 2 spelers, 1 neutraal leger
legers = []
kleuren = {
    "blauw": "#71baf6",
    "geel": "#f5d953",
    "groen": "#588c60",
    "oranje": "#df7d41",
    "paars": "#7f638c",
    "rood": "#ef3740",
}

landen = landen

voorwaarden(legers, gamemode, landen)

voorbereiding = functies(kleuren)

lijst_legers = voorbereiding.leger_kiezen(spelers)

for leger in lijst_legers:
    legers.append(leger)

# Bot en neutraal krijgen een kleur
legers.append('paars')

# Landen verdelen
troepen = 40 - 14 # * Tijdig, omdat er nu standaard landen worden verdeeld waar alle landen al 1 troep op zich hebben staan.
# TODO

# Landen verdelen in een tabel
opzet().tabel(landen)

# De rest van de troepen verdelen
# * TODO? voorbereiding.troepen_verdelen(landen, troepen, legers)

beurt = 0
acties = actie()
running = True

while running:
    print(f"{legers[beurt].capitalize()} is aan de beurt.")

    voorwaarden(legers, gamemode, landen)

    # 1. Nieuwe troepen pakken en op het bord plaatsen.
    landen = acties.troepen_plaatsen(beurt, landen)
    opzet().tabel(landen)

    voorwaarden(legers, gamemode, landen)

    # 2. Aanvallen (als je wilt).
    landen = acties.aanvallen(beurt, landen, legers)
    opzet().tabel(landen)

    voorwaarden(legers, gamemode, landen)

    # 3. Troepen verplaatsen (als je wilt).
    landen = acties.troepen_verplaatsen(beurt, landen, legers)
    opzet().tabel(landen)

    voorwaarden(legers, gamemode, landen)

    beurt = 1 if beurt == 0 else 0
