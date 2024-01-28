# Import the necessary libraries.
import json

# Import my own necessary libraries.
from begin import kleuren_kiezen, landen_verdelen


# Define variables
aantal_spelers = 3
kleuren_legers = {
    "blauw": "#71baf6",
    "geel": "#f5d953",
    "groen": "#588c60",
    "oranje": "#df7d41",
    "paars": "#588c60",
    "rood": "#ef3740",
}

aantal_troepen = []

# Begin van het spel
print("Welkom bij RISK!")

kleuren_spelers = kleuren_kiezen()

# print(f"Jij bent leger {kleuren_spelers[0]}. De tegenstander is leger {kleuren_spelers[1]} en het neutrale leger is leger {kleuren_spelers[2]}.")

landen = landen_verdelen()

for x in range(aantal_spelers):
    z = 0
    for y in landen[x]:
        land = y[0], {"continent": y[1]["continent"], "troep": y[1]["troep"], "locatie": y[1]["locatie"], "grenzen": y[1]["grenzen"], "speler": kleuren_spelers[x], "aantal_troepen": 1},
        #land = {y["land"]:[{"speler": kleuren_spelers[x], "aantal_troepen": 1}]}

        landen[x][z] = land
        
        z += 1

for x in landen:
    for y in x:
        print(y)
    print()