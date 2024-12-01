import random

class opzet:
    def __init__(self):
        pass

    def tabel(self, landen):
        self.landen = landen
        spelers = []
        length = 0

        for x in range(len(self.landen)):
            for y in landen[x]:
                # print(y)
                # print(landen[x][y]["speler"])
                spelers.append(landen[x][y]['speler'])
                break

            for y in landen[x]:
                if len(y) > length:
                    length = len(y)

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

                print(y, end="")
                for z in range(length - len(y)):
                    print(" ", end="")
                print(" | ", end="")

                print(landen[x][y]['continent'], end="")
                for z in range(lengths[1] - len(landen[x][y]['continent'])):
                    print(" ", end="")
                print(" | ", end="")

                print(landen[x][y]['speler'], end="")
                for z in range(lengths[2] - len(landen[x][y]['speler'])):
                    print(" ", end="")
                print(" | ", end="")

                print(landen[x][y]['aantal_troepen'], end="")
                for z in range(lengths[3] - len(str(landen[x][y]['aantal_troepen']))):
                    print(" ", end="")
                print(" |")
        
        print("+", end="")

        for x in lengths:
            for y in range(x + 2):
                print("-", end="")

            print("+", end="")
            
        print()

    def dobbelen(self, troepen):
        self.dobbel = []

        for x in range(troepen):
            self.dobbel.append(random.randint(1, 6))

        return self.dobbel