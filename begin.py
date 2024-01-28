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