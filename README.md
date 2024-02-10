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

## Score berekenen

Er zijn verschillende manieren om data een score te geven. Een eenvoudige methode is om een gewogen som te gebruiken van de verschillende factoren die je belangrijk vindt. Stel je wilt de volgende factoren meenemen:

    Aantal aangrenzende gebieden (A)
    Continentbonus (B)
    Aantal troepen van de speler (S)
    Aantal troepen van de bot (B)

Dan kun je de volgende formule gebruiken om een score te berekenen voor elk gebied:

    Score = A * w_A + B * w_B + S * w_S - B * w_B

De w_ variabelen zijn gewichten die je aan elke factor kunt toekennen. Hoe belangrijker een factor is, hoe hoger het gewicht. Je kunt de gewichten aanpassen aan je eigen speelstijl en strategie.

Een voorbeeld:

Stel je wilt gebieden met veel buren en een continentbonus prioriteren. Je kunt de volgende gewichten gebruiken:

    w_A = 2
    w_B = 3
    w_S = 1
    w_B = 1

Een gebied met 4 buren, een continentbonus en 2 troepen van de speler zou dan de volgende score krijgen:

    Score = 4 * 2 + 3 * 1 + 2 * 1 - 0 * 1 = 11

Een gebied met 3 buren, geen continentbonus, 1 troep van de speler en 3 troepen van de bot zou dan de volgende score krijgen:

    Score = 3 * 2 + 0 * 1 + 1 * 1 - 3 * 1 = 5

In dit voorbeeld heeft het eerste gebied een hogere score, dus dat zou je prioriteit moeten zijn om troepen te plaatsen.

Naast deze eenvoudige methode zijn er ook meer geavanceerde technieken om data een score te geven. Je kunt bijvoorbeeld machine learning gebruiken om een model te trainen dat de scores voorspelt op basis van de data.

Het is belangrijk om te experimenteren met verschillende methoden om te zien wat het beste werkt voor jouw bot. De beste methode hangt af van de factoren die je belangrijk vindt en de speelstijl van je tegenstander.

Belangrijk is dat je de scores gebruikt om een beslissing te nemen. Je kunt bijvoorbeeld de gebieden met de hoogste scores sorteren en je troepen op die gebieden plaatsen. Je kunt de scores ook gebruiken om te bepalen welke gebieden je moet aanvallen of verdedigen.

1. Definieer de wiskundige formulering van het netwerk:
    - **Aantal neuronen in de input laag:** Aantal factoren die je wilt gebruiken (4 in dit voorbeeld)
    - **Aantal neuronen in de verborgen laag:** Kies een nummer, 10 is een gebruikelijke waarde
    - **Aantal neuronen in de output laag:** 1 (de score)
    - **Activatiefunctie:** Kies een activatiefunctie voor de neuronen, zoals ReLU of sigmoid
    - **Verliesfunctie:** Kies een verliesfunctie, zoals Mean Squared Error (MSE)
    - **Optimizers:** Kies een optimizer, zoals Adam

2. Implementeer de forward pass:
    - Bereken de activatie van de neuronen in de verborgen laag
    - Bereken de activatie van de neuronen in de output laag

3. Implementeer de backward pass:
    - Bereken de gradiënt van de verliesfunctie met betrekking tot de gewichten van het netwerk
    - Update de gewichten van het netwerk met behulp van de optimizer

4. Train het netwerk:
    - Herhaal de forward en backward pass totdat het netwerk geconvergeerd is

5. Voorspel de scores:
    - Gebruik de forward pass om de scores van de gebieden te voorspellen

Dit is een basisimplementatie van een neuraal netwerk. Je kunt de implementatie aanpassen door verschillende optimzers, activatiefuncties, en verliesfuncties te gebruiken.

Enkele tips:
- Gebruik NumPy voor de matrixberekeningen.
- Implementeer batch training om de efficiëntie te verhogen.
- Gebruik een valideringsset om te voorkomen dat het netwerk overfit.



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