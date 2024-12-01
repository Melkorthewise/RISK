from opzet import opzet

class actie:
    def __init__(self):
        self.continenten = ["N_Amerika", "Z_Amerika", "Europa", "Afrika", "Azie", "Oceanie"]

    def set_inleveren(self):
        # TODO
        pass

    def troepen_plaatsen(self, beurt, landen):
        troepen = len(landen[beurt]) // 3
        print(f"Je hebt {len(landen[beurt])} landen en mag dus {troepen} troepen plaatsen")

        while troepen > 0:
            land = input("Waar zou je troepen willen plaatsen? \n>>> ").capitalize()

            if land in landen[beurt]:
                try:
                    aantal = int(input(f"Hoeveel troepen zou je hier willen plaatsen? (Je hebt nog {troepen} troepen) \n>>> "))
                        
                    if aantal >= 0 and aantal <= troepen:
                        landen[beurt][land]['aantal_troepen'] += aantal
                        troepen -= aantal
                    else:
                        print("Dit is geen juist aantal troepen.")
                except ValueError:
                    print("Vul hier een getal in.")
            else:
                print("Dit is niet een van jouw landen.")

        return landen
                        
    def aanvallen(self, beurt, landen, legers):
        while True:
            try:
                beslissing = input("Wil je deze beurt aanvallen? (J/N) \n>>> ").capitalize()

                if beslissing == "J":
                    while True:
                        van = input("Met welk land wil je aanvallen? \n>>> ").capitalize()

                        if van in landen[beurt] and landen[beurt][van]["aantal_troepen"] > 1:
                            while True:
                                naar = input("Welk land zou je willen aanvallen? \n>>> ").capitalize()
                                for x in range(len(landen)):
                                    if naar in landen[x]:
                                        self.troepen_naar = landen[x][naar]["aantal_troepen"]
                                        print(f"{naar} heeft {self.troepen_naar} troep(en).")
                                        break

                                if naar not in landen[beurt] and naar in landen[beurt][van]["grenzen"]:
                                    troepen = landen[beurt][van]["aantal_troepen"]
                                    self.troepen_van = troepen - 1
                                    while True:
                                        try:
                                            aantal = int(input(f"Met hoeveel troepen wil je aanvallen? Je hebt {self.troepen_van} troepen beschikbaar. \n>>> "))
                                            if aantal > 0 and aantal <= (troepen - 1):

                                                dobbelstenen = opzet()
                                                
                                                if self.troepen_van >= 3:
                                                    dv = dobbelstenen.dobbelen(3)
                                                else:
                                                    dv = dobbelstenen.dobbelen(self.troepen_van)

                                                if self.troepen_naar >= 2:
                                                    dn = dobbelstenen.dobbelen(2)
                                                else:
                                                    dn = dobbelstenen.dobbelen(self.troepen_naar)

                                                dv.sort(reverse=True)
                                                dn.sort(reverse=True)
                                                
                                                # print(dv, dn, dv[0], dn[0])
                                                
                                                for x in range(len(dn)):
                                                    print(x)

                                                    if dv[x] <= dn[x]:
                                                        print(self.troepen_van)
                                                        self.troepen_van -= 1

                                                        print(f"{naar} heeft gewonnen, {van} heeft nu {self.troepen_van} troepen")

                                                        if self.troepen_van == 0:
                                                            print(f"Helaas, het is niet gelukt om {naar} te veroveren.")
                                                            # Update de troepen van beide landen
                                                            for x in range(len(landen)):
                                                                if naar in landen[x]:
                                                                    landen[x][naar]["aantal_troepen"] = self.troepen_naar
                                                                if van in landen[x]:
                                                                    landen[x][van]["aantal_troepen"] = self.troepen_van
                                                                    
                                                            return landen
                                                        
                                                    if dv[x] > dn[x]:
                                                        self.troepen_naar -= 1
                                                        print(f"{van} heeft gewonnen, {naar} heeft nu {self.troepen_naar} troepen")
                                                        if self.troepen_naar == 0:
                                                            print(f"Gefeliciteerd, je hebt {naar} veroverd.")
                                                            # Update de troepen en speler van het land
                                                            for x in range(len(landen)):
                                                                if naar in landen[x]:
                                                                    self.land = landen[x][naar]
                                                                    print(self.land)
                                                                    landen[x][naar]["speler"] = legers[beurt]
                                                                    landen[x][naar]["aantal_troepen"] = self.troepen_van
                                                                    landen[x].pop(naar)
                                                                    landen[beurt].update({naar: self.land})
                                                                    
                                                                    landen_sort = dict(sorted(landen[beurt].items(), key=lambda item: self.continenten.index(item[1]['continent'])))

                                                                    landen = (landen_sort, landen[1], landen[2])

                                                                if van in landen[x]:
                                                                    landen[x][van]["aantal_troepen"] -= self.troepen_van
                                                                    
                                                            return landen
                                                        
                                                einde = input("Wil je nog een keer aanvallen? (J/N) \n>>> ").capitalize()
                                                if einde == "N":
                                                    return landen
                                            else:
                                                print("Voer een geldig aantal troepen in.")
                                        except ValueError:
                                            print("Voer een geldig aantal troepen in.")
                                else:
                                    print("Dit is niet een geldig land.")
                        else:
                            print("Dit is niet een van jouw landen.")
                else:
                    return landen
            except ValueError:
                pass

    def zijn_verbonden(self, beurt, landen, start_land, doel_land):
        start_speler = beurt
        bezocht = set()
        queue = [start_land]

        while queue:
            huidig_land = queue.pop(0)

            if huidig_land == doel_land:
                return True
            
            bezocht.add(huidig_land)

            # Voeg niet-bezochte buurlanden van dezelfde speler toe aan de queue
            for buur in landen[beurt][huidig_land]['grenzen']:
                if buur not in bezocht and buur in landen[beurt]:
                    queue.append(buur)

                # print(buur, queue)

        return False

    # print("Je mag een keer troepen verplaatsen van één land naar één ander land die via grens of via andere landen aan elkaar grenzen.")
    def troepen_verplaatsen(self, beurt, landen, legers):
        self.landen = landen           

        while True:
            try:
                beslissing = input("Wil je deze beurt troepen verplaatsen (J/N) \n>>> ").capitalize()

                if beslissing.capitalize() == "J":
                    while True:
                        van = input("Van welk land zou je troepen willen verplaatsen? \n>>> ").capitalize()

                        if van in landen[beurt] and landen[beurt][van]["aantal_troepen"] > 1:
                            while True:
                                naar = input("Naar welk land zou je troepen willen verplaatsen? \n>>> ").capitalize()

                                resultaat = self.zijn_verbonden(beurt, landen, van, naar)
                                # if resultaat:
                                #     print(f"{van} en {naar} zijn verbonden en worden gecontroleerd door dezelfde speler.")
                                # else:
                                #     print(f"{van} en {naar} zijn niet verbonden of worden niet door dezelfde speler gecontroleerd.")

                                # TODO checken of het aangrenzend is aan elkaar
                                if naar in landen[beurt] and naar != van and resultaat == True:
                                    while True:
                                        try:
                                            aantal = int(input(f"Hoeveel troepen zou je willen verplaatsen? Je hebt {landen[beurt][van]["aantal_troepen"] - 1}. \n>>> "))

                                            if aantal > 0 and aantal <= (landen[beurt][van]["aantal_troepen"] - 1):
                                                landen[beurt][van]["aantal_troepen"] -= aantal
                                                landen[beurt][naar]["aantal_troepen"] += aantal

                                                return landen
                                            else:
                                                print("Voer een geldig aantal troepen in.")
                                        except ValueError:
                                            print("Voer een geldig aantal troepen in.")
                                else:
                                    print("Dit is niet een van jouw landen of de landen grenzen niet aan elkaar.")
                        else:
                            print("Dit is niet een van jouw landen.")
                else:
                    return landen
            except ValueError:
                pass 
