import time

kleuren_spelers = [] # Later terug veranderen naar een lege array.
kleuren_legers = ["blauw", "geel", "groen", "oranje", "paars", "rood"]

def begin_spel3():
    print("Wat is de bedoeling?")
    print("Schakel je tegenstander uit door al zijn of haar gebieden te veroveren.\n")

    print("Gooi beide een dobbelsteen, degene met de hoogste waarde mag beginnen.")
    print("Jullie kiezen beide een kleur en samen kiezen jullie een kleur voor het 'neutrale' leger (speler 3).\n")
    print("De volgende kleuren zijn mogelijk: {}, {}, {}, {}, {} en {}.".format(kleuren_legers[0], kleuren_legers[1], kleuren_legers[2], kleuren_legers[3], kleuren_legers[4], kleuren_legers[5]))

    kleuren_spelers = legers(3)

    print("\nLeg 40 Infanterie speelstukken van ieder leger klaar. Dit is de startvoorraad troepen waarmee het spel begint.")

    return kleuren_spelers

def legers(spelers):
    y = 1
    for x in range(spelers):
        speler = input("Welke kleur is speler {}: ".format(y))
        kleuren_spelers.append(speler)

        y += 1
    
    return kleuren_spelers
