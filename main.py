from begin import kleuren_kiezen, landen_verdelen

# Variabelen
kleuren_legers = {
    "blauw": "#71baf6",
    "geel": "#f5d953",
    "groen": "#588c60",
    "oranje": "#df7d41",
    "paars": "#588c60",
    "rood": "#ef3740",
}

kleuren_spelers = kleuren_kiezen()
print(kleuren_spelers)

landen = landen_verdelen()

for x in range(len(kleuren_spelers)):
    z = 0
    for y in landen[x]:
        land = y[0], {"continent": y[1]["continent"], "troep": y[1]["troep"], "locatie": y[1]["locatie"], "grenzen": y[1]["grenzen"], "speler": kleuren_spelers[x], "aantal_troepen": 1},
        #land = {y["land"]:[{"speler": kleuren_spelers[x], "aantal_troepen": 1}]}

        landen[x][z] = land

        z += 1