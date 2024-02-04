# RISK (Dutch)

- Weer bij het begin beginnen, deze keer zo veel mogelijk eigen code gebruiken.
- Visueel voor later houden, eerst alleen tekst.
- Proberen een AI model er in te verwerken.

## Kiezen leger en plaatsen troepen

1. Spel is voor 2 spelers(, gebruiker en bot)
2. De gebruiker kiest een kleur en de bot en het neutrale leger krijgen beide één van de overige kleuren.
3. Alle legers beginnen met 40 troepen.
4. De landen worden over de legers verdeeld, zodat alle legers 14 landen hebben.
5. Dan worden een voor een de troepen op de gekregen landen gezet, zodat er op elk land één troep staat.
6. De rest van de troepen worden nu verdeeld, probeer de tegenstander te hinderen met de plaatsing van de troepen.

## Nieuwe troepen pakken

1. Je krijgt minimaal 3 troepen.
2. Tel het aantal landen en deel dat door drie, rond af naar beneden.
3. (Extra troepen voor de bezeten continenten)

## Aanvallen

1. Besluiten of er wordt aangevallen.
2. Je mag een gebied alleen aanvallen als het grenst aan een van jou gebieden.
3. Je mag maar één gebied tegelijk aanvallen.
4. Je moet altijd ten minste twee troepen hebben in het gebied van waaruit je aanvalt.
5. Na je eerste aanval, mag je blijven aanvallen totdat je alle vijandelijke troepen in het gebied verslagen hebt, of je aanval verschuiven naar een ander gebied. Je mag in één beurt zo vaak aanvallen als je wilt.

### Het gevecht

1. Pak eerst het aantal troepen waarmee je wil aanvallen en duw ze over de grens in het verdedigende gebied. (Je mag tot drie troepen gebruiken voor je aanval.) Er moet altijd ten minste één troep achterblijven om de wacht te houden.
2. (Nu kiest de verdediger of hij z'n gebied met één of twee troepen gaat verdedigen. Ongeacht het aantal troepen in het verdedigende gebied, verdedigen mag uitsluitend met één of twee troepen. In tegenstelling tot de aanvaller kan de verdediger ook zijn laatste troep voor het gevecht gebruiken. Hij hoeft geen bewaking achter te laten.)
3. Nu begint het gevecht. De aanvaller gooit één rode dobbelsteen voor elke aanvallende troep en de verdediger gooit één blauwe dobbelsteen voor elke verdedigende troep. Beide spelers moeten tegelijk gooien.
    - Leg de hoogste dobbelstenen tegen elkaar, hoogste wint. Bij gelijk spel wint de verdediger altijd.
    - De aanvaller kan met één worp nooit meer dan twee troepen verliezen.
    - Als de verdedigerd na de aanval nog één of meer troepen in het aangevallen gebied over heeft, dan gaan overlevende aanvallers terug naar het gebied van waaruit ze aanvielen. Maar de aanvaller mag, desgewenst, ook opnieuw aanvallen.

### Gebieden veroveren



# Neural Network (AI)

Het is belangrijk om de data die je hebt over de verschillende gebieden te gebruiken om te beslissen waar je troepen moet plaatsen. Je kunt de gebieden een score geven op basis van verschillende factoren, zoals:

- **Aantal aangrenzende gebieden:** Gebieden met meer buren zijn strategisch belangrijker, omdat ze meer mogelijkheden bieden voor aanvallen en verdedigen.
- **Continentbonussen:** Sommige continenten geven bonussen aan spelers die een meerderheid van de gebieden op dat continent bezitten.
- **Aantal troepen:** Gebieden met meer troepen zijn moeilijker te veroveren, maar bieden ook meer verdedigingskracht.
- **Troepen van de speler en de bot:** Je moet rekening houden met de troepenverdeling van zowel jou als de tegenstander.

Gebruik de scores van de gebieden om te bepalen waar je je troepen moet plaatsen. Gebieden met hogere scores zijn doorgaans strategisch waardevoller. Je kunt je strategie ook aanpassen aan de context van de game. Als je tegenstander bijvoorbeeld agressief speelt, moet je je misschien meer concentreren op het verdedigen van je gebieden.

Naast het gebruik van de data, zijn er nog andere dingen die je kunt doen om je Risk-bot te verbeteren:

- **Analyseer het gedrag van je tegenstander.** Observeer hoe je tegenstander speelt en pas je strategie daaraan aan.
- **Simuleer de uitkomsten van verschillende acties.** Dit kan je helpen om te beslissen wat de beste zet is in een bepaalde situatie.
- **Laat je bot leren van zijn ervaringen.** Door te analyseren wat er in het verleden is gebeurd, kan je bot zijn strategie in de toekomst verbeteren.

## Elementen voor de strategie
- Waarde Gebieden
- Risico Assessment
- Tegenstander Analyse
- Adaptive Learning





<!-- # Risk
De spelregels van het spel Risk. Het spel kan gespeeld worden van 2 tot 5 spelers.

# Inleiding
In RISK is het doel simpel: verover de gebieden van je vijanden door je troepen erheen te verplaatsen en het gevecht aan te gaan. Afhankelijk van wat je gooit met de dobbelstenen, versla je je vijand of je wordt zelf verslagen. Als je alle vijandelijke troepen in een gebied hebt vernietigd, heb je het gebied veroverd en je bent een stapje dichter bij de wereldheerschappij.

## Het gebruik van deze spelregels
Als je voor het eerst RISK speelt en je wil alles weten, begin dan op blz.3. Als je je meteen in de strijd wil storten en spelen, ga je naar blz.5.

### Er zijn vier maniern om te spelen:
RISK met Missiekaarten (blz. 5)
Klassiek RISK (blz. 12)
RISK voor 2 spelers (blz. 13)
Hoofdkwartier RISK (blz. 14)

### Inhoud
- Speelbord
- 5 legers met elk 40 infanterie, 12 cavalerie en 8 artillerie speelstukken
- 56 RISK kaarten
- 1 kartonnen doos
- 5 dobbelstenen
- 5 kartonnen legerkisten

# Zo ziet het spel eruit
## Het speelbord
Het speelbord is een wereldkaart met **42 gebieden**, verdeeld over **zes continenten**. (Elk continent heeft een andere kleur). De cijfers langs de randen van het vord geven aan hoeveel troepen je ontvangt voor elk setje kaarten dat je inruilt.

## De legers
Er zijn vijf complete legers die elk bestaan uit drie soorten speelstukken (troepen):

Infanterie (waarde: 1 troep), Cavalerie (waarde: 5 troepen) en Artillerie (waarde: 10 troepen)

Je begint het spel met Infanterie speelstukken, maar wanneer je meer troepen krijgt, kun je ruimte besparen door ze in te ruilen voor Cavalerie of Artillerie speelstukken.

## De dobbelstenen
Je gebruikt de rode als je aanvalt en de blauwe als je verdedigt.

## RISK kaarten
### 42 gebiedkaarten
Op elke kaart staat de naam van een gebied en een plaatje van Infanterie, Cavalerie of Artillerie.

### 2 'Jokers'
Op elke kaart staan alle drie de troepen.

### 12 Geheime Missiekaarten
Let op: de 12 Geheime Missiekaarten worden alleen gebruikt als je RISK met Missiekaarten speelt. Voor de andere manieren om RISK te soelen blijven de Geheime Missiekaarten uit het spel. -->