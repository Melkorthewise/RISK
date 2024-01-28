# Import the necessary libraries.
import random
import json

# Import the data from Gebiedskaarten.json
with open("Gebiedskaarten.json", "r") as data:
    gebiedskaarten = json.load(data)["gebiedskaarten"]

# print(type(gebiedskaarten), gebiedskaarten)

# De mogelijke kleuren voor de legers.
kleuren = ["blauw", "geel", "groen", "oranje", "paars", "rood"]

def kleuren_kiezen():
    kleuren_spelers = []

    while kleuren_spelers == []:
        kleur = input("Welke kleur zou je willen zijn?\n>>> ")

        for x in kleuren: # Checken of de kleur een mogelijkheid is.
            if kleur.lower() == x:
                kleuren_spelers.append(kleur.lower())
                kleuren.remove(kleur.lower())

    for x in range(2): # Kleuren voor de bot en het neutrale leger kiezen.
        kleur = kleuren[random.randint(0, len(kleuren) - 1)]
        kleuren_spelers.append(kleur)
        kleuren.remove(kleur)

    return kleuren_spelers


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

