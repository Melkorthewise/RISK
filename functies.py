continenten = ["N_Amerika", "Z_Amerika", "Europa", "Afrika", "Azie", "Oceanie"]
veroverde_landen = []

punten = [5, 2, 5, 3, 7, 2]
aantal_landen = [9, 4, 7, 6, 12, 4]

def continentbonus(landen):
    continentbonussen = []

    for x in continenten:
        totaal = 0
        for y in landen[1]:
            if y[1]["continent"] == x:
                totaal += 1
        veroverde_landen.append(totaal)

    for x in range(len(aantal_landen)):
        if aantal_landen[x] == veroverde_landen[x]:
            continentbonussen.append(punten[x])
        elif aantal_landen[x] != veroverde_landen[x]:
            continentbonussen.append(0)

    print("Continentbonus:", continentbonussen)

    return continentbonussen

