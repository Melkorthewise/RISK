from opzet import opzet

class functies:
    def __init__(self, kleuren):
        self.kleuren = kleuren
    
    def leger_kiezen(self, spelers):
        legers = []

        for x in range(spelers):
            leger = input(f"Welk leger zou jij (Speler {x + 1}) willen zijn? \n>>> ")

            if leger in self.kleuren:
                legers.append(leger)

        return legers
    
    def landen_verdelen(self):
        # TODO
        pass
    
    def troepen_verdelen(self, landen, troepen, legers):
        self.troepen = [troepen, troepen, troepen]
        self.legers = legers
        self.landen = landen

        for x in range(troepen):
            for y in range(len(self.legers)):
                while True:
                    print(f"Speler {self.legers[y]}", self.troepen[y])
                    naar = input("Op welk land zou je een troep willen neerzetten? \n>>> ")

                    if naar in landen[y]:
                        self.landen[y][naar]['aantal_troepen'] += 1
                        self.troepen[y] -= 1
                        break
                    else:
                        print("Dit is niet een van jouw landen\n")

            opzet().tabel(landen)

        return self.landen