continenten = ["N_Amerika", "Z_Amerika", "Europa", "Afrika", "Azie", "Oceanie"]

punten = [5, 2, 5, 3, 7, 2]
aantal_landen = [9, 4, 7, 6, 12, 4]

def continentbonus(landen):
    continentbonussen = []
    veroverde_landen = []

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

    # print("Continentbonus:", continentbonussen)
    # print("Veroverde landen:", veroverde_landen, "\n")

    return continentbonussen, veroverde_landen

def tabel(landen):
    spelers = []
    length = 0

    for x in range(len(landen)):
        for y in landen[x]:
            # print(y[1]["speler"])
            spelers.append(y[1]["speler"])
            break

        for y in landen[x]:
            if len(y[0]) > length:
                length = len(y[0])

    lengths = [length, len("Continent"), len("Speler"), len("Aantal troepen")]

    print("+", end="")

    for x in lengths:
        for y in range(x + 2):
            print("-", end="")

        print("+", end="")

    print()

    print("| ", end="") # TODO Kijken of dit korter kan.
    print("Landen", end="")
    for y in range(length - len("Landen")):
        print(" ", end="")
    print(" | ", end="")

    print("Continent", end="")
    print(" | ", end="")

    print("Speler", end="")
    for y in range(lengths[2] - len("Speler")):
        print(" ", end="")
    print(" | ", end="")

    print("Aantal troepen", end="")
    print(" |")

    for x in range(len(landen)):
        print("+", end="")

        for y in lengths:
            for z in range(y + 2):
                print("-", end="")

            print("+", end="")
            
        print()

        for y in landen[x]: # TODO Kijken of dit korter kan.
            print("| ", end="")

            print(y[0], end="")
            for z in range(length - len(y[0])):
                print(" ", end="")
            print(" | ", end="")

            print(y[1]["continent"], end="")
            for z in range(lengths[1] - len(y[1]["continent"])):
                print(" ", end="")
            print(" | ", end="")

            print(y[1]["speler"], end="")
            for z in range(lengths[2] - len(y[1]["speler"])):
                print(" ", end="")
            print(" | ", end="")

            print(y[1]["aantal_troepen"], end="")
            for z in range(lengths[3] - len(str(y[1]["aantal_troepen"]))):
                print(" ", end="")
            print(" |")
    
    print("+", end="")

    for x in lengths:
        for y in range(x + 2):
            print("-", end="")

        print("+", end="")
        
    print()