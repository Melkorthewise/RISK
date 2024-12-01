# RISK (Dutch)
Het doel van dit project is om een werkende versie te krijgen van het bordspel RISK. Het is dan ook de bedoeling dat je tegen bots kunt spelen.

## Kiezen leger en plaatsen troepen
1. ~~Spel is voor 2 spelers(, gebruiker en bot)~~
2. ~~De gebruiker kiest een kleur en de bot en het neutrale leger krijgen beide één van de overige kleuren.~~
3. ~~Alle legers beginnen met 40 troepen.~~
4. De landen worden over de legers verdeeld, zodat alle legers 14 landen hebben.
5. Dan worden een voor een de troepen op de gekregen landen gezet, zodat er op elk land één troep staat.
6. ~~De rest van de troepen worden nu verdeeld, probeer de tegenstander te hinderen met de plaatsing van de troepen.~~

## Nieuwe troepen pakken
1. ~~Je krijgt minimaal 3 troepen.~~
2. ~~Tel het aantal landen en deel dat door drie, rond af naar beneden.~~
3. (Extra troepen voor de bezeten continenten, of voor ingeleverde setjes)

## Aanvallen
1. ~~Besluiten of er wordt aangevallen.~~
2. ~~Je mag een gebied alleen aanvallen als het grenst aan een van jou gebieden.~~
3. ~~Je mag maar één tegelijk aanvallen.~~
4. ~~Je moet altijd ten minste twee troepen hebben in het gebied van waaruit je aanvalt.~~
5. ~~Na je eerste aanval, mag je blijven aanvallen totdat je alle vijandelijke troepen in het gebied verslagen hebt, of je aanval verschuiven naar een ander gebied. Je mag in één beurt zo vaak aanvallen als je wilt.~~

## Troepen verdelen (AI)

Aatal variabelen per land, om rekening mee te houden:
- Aantal aangrenzende landen, van bot en van tegenstanders.
- Aantal troepen om het land heen van de speler.
- Aantal troepen om het land heen van de tegenstander.
- Aantal troepen op het land zelf.
- Hoeveel landen liggen er op hetzelfde continent.

Als je gaat kijken naar of er landen om het land heen liggen van de speler zelf en dat zijn er geen dan heeft dit geen invloed op een berekening, want het rekent dan met 0. Het zou misschien een idee zijn om te kijken hoeveel landen er dan niet van de speler zijn, want wanneer dit variabel 0 is maakt dat niet uit want dan is het land veilig.

## ChatGPT Advies
### 1. Define the Game Logic

First, you need to define the rules and mechanics of Risk. This includes:
- Initial Setup (distributing territories and armies)
- Turn sequence (reinforcements, attack, fortification)
- Combat mechanics (dice rolls, army losses)
- Win conditions