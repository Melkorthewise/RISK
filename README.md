# RISK (Dutch)
Het doel van dit project is om een werkende versie te krijgen van het bordspel RISK met de Go language.

# Folder logic
```
/game-project
│
├── /cmd                 # Main entry point for the game
│   └── /client          # Client-side logic (main.go)
│
├── /pkg                 # Core game logic and reusable code
│   ├── /game            # Core game rules (gameplay logic, mechanics, etc.)
│   ├── /utils           # Utility functions (helpers, logging, etc.)
│   └── /models          # Data structures, entities (e.g., players, objects)
│
├── /assets              # Game assets (images, sounds, etc.)
│
├── /scripts             # Dev scripts for building or running the game
│
├── /test                # Unit tests
│
├── go.mod               # Go module definition
└── README.md            # Project overview and instructions
```
# Kiezen leger en plaatsen troepen
1. Spel is voor 2 spelers
2. `De gebruikers kiezen een kleur rest van de legers krijgen een kleur toegewezen.`
3. Alle legers beginnen met 40 troepen.
4. De landen worden over de legers verdeeld, zodat alle legers 14 landen hebben.
5. Dan worden een voor een de troepen op de gekregen landen gezet, zodat er op elk land een troep staat.
6. De rest van de troepen worden nu verdeeld, probeer de tegenstander te hinderen met de plaatsing van de troepen.

# Voorbeeld troepen verdelen in Python
```
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
```
