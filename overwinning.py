
class voorwaarden:
    def __init__(self, legers, gamemode, landen):
        self.legers = legers
        self.gamemode = gamemode
        self.landen = landen

        if self.gamemode == "Klassiek RISK":
            self.world_domination()

    def world_domination(self):
        # Wanneer 1 speler alle landen bezit heeft diegene gewonden
        for x in range(len(self.landen)):
            if len(self.landen[x]) == 42:
                print(f"Speler {self.legers[x]} heeft gewonnen.")