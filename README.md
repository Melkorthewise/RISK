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

## Componenten van een Neural Network

- **Lagen**: De bouwstenen van het netwerk waar informatie wordt verwerkt. Elke laag bevat neuronen die berekeningen uitvoeren op de ontvangen data.
- **Neuronen**: Kunstmatige eenheden geïnspireerd door biologische neuronen. Ze ontvangen input van eerdere lagen, passen gewichten en biases toe, en activeren een functie om een output te produceren.
- **Gewichten en Biases**: Leerbare parameteres die de sterkte van verbindingen tussen neuronen bepalen en de output beïnvloeden.
- **Activatiefunctie**: Deze functie voegt non-lineariteit toe aan het netwerk, waardoor het complexe patronen kan leren. Sigmoid, ReLU en tanh zijn veelgebruikte functies.

## Betrokken stappen:
1. **Netwerkarchitectuur definiëren**: Bepaal het aantal lagen, neuronen per laag en activeringsfuncties.
2. **Gewichten en Biases initialiseren**: Initialiseer deze parameters willekeurig.
3. **Voortwaartse propagatie**: Geef de invoerdata door het netwerk laag per laag, waarbij gewichten, biases en activeringsfuncties worden toegepast.
4. **Verlies berekenen**: Vergelijk de output van het netwerk met de gewenste output (grondwaarheid) om de fout te meten.
5. **Backpropogatie**: Gebruik de kettingregel om de gradiënten van de verliesfunctie te berekenen met betrekking tot de gewichten en biases.
6. **Gewichten en Biases bijwerken**: Pas de gewichten en baises aan op basis van de berekende gradiënten met behulp van een optimalisatiealgoritme zoals gradiëntendaling.
7. **Herhaal**: Herhaal stappen 3-6 voor meerdere trainingsperiodes totdat het netwerk convergeert of een bevredigend prestatatieniveau bereikt.

## Integratie in je spel:

- **Netwerk voor trainen**: Train het netwerk op een relevante dataset voordat je het in je spel integreert. Deze dataset moet de situaties weerspiegelen die je game-AI tegenkomt.
- **Invoer en uitvoer**: Definieer de invoerdata die het netwerk van de spelomgeving ontvangt (bijv. spelstatus, speleracties) en de gewenste output die het moet produceren (bijv. beslissingen over besturing, strategische zetten).
- **Inferentie**: Gebruik het netwerk na het trainen om voorspellingen te doen tijdens het spelen door de huidige spelstatus als invoer te geven en de gesuggereerde actie als output te verkrijgen.

## Opbouw

### Eerste Neuronen

De eerste neuronen in een neuraal netwerk zijn simpelweg **wiskundige functies** die input (data) omzetten in output. In de praktijk worden ze geprogrammeerd als kleine "programma's" in code. De basisfunctie van een neuron is:

```
def neuron(input, weights, bias):
    # Berken de activatie van het neuron
    activation = sum(input * weights) + bias

    # Pas de activatiefunctie toe
    output = sigmoid(activation)

    return output
```

### Laagstructuur:

Een laag in een neuraal netwerk is een verzameling van neuronen die allemaal dezelfde input ontvangen en onafhankelijk van elkaar hun output berekenen. De neuronen in een laag zijn met elkaar verbonden via gewichten.

#### Meerdere Neuronen in één Laag:

Wanneer je meerdere neuronen in één laag hebt, kan het netwerk complexere patronen in de data leren. Elk neuron kan zich specialiseren in het detecteren van een specifiek kenmerk in de input. De outputs van de neuronen in de laag worden vervolgens gecombineerd om de input voor de volgende laag te vormen.

#### Programmeren van Meerdere Neuronen:

In code worden neuronen in een laag meestal geprogrammeerd als een lus die over de input itereert. Voor lek element in de input wordt de neuronenfunctie aangeroepen met de bijbehorende gewichten en bias. De outputs van alle neuronen in de laag worden vervolgens verzameld in een array.




---
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

## Trainen

1. Gebruik verschillende bots:
    Ontwikkel of verzamel verschillende bots met verschillende strategieën en speelvaardigheden.
    Laat de bot tegen verschillende bots spelen om te leren van hun verschillende sterke en zwakke punten.

2. Menselijke input toevoegen:
    Laat de bot af en toe tegen menselijke spelers spelen om te leren van hun tactieken en strategieën.
    Implementeer een "teaching" -functie waar spelers de bot kunnen corrigeren of feedback kunnen geven na een spel.

3. Gebruik gevarieerde trainingsdata:
    Train de bot op een dataset van spelresultaten van zowel menselijke als bot-spellen.
    Voeg data toe van professionele Risk-spelers of toernooien om de bot te leren van de beste spelers ter wereld.
    
4. Beperk overfitting:
    Zorg ervoor dat de trainingsdata gevarieerd genoeg is om te voorkomen dat de bot zich overspecialiseert in één strategie.
    Implementeer technieken zoals regularisatie om overfitting te verminderen.

5. Continueer de ontwikkeling:
    Blijf de bot updaten met nieuwe data, strategieën en technieken.
    Experimenteer met verschillende trainingsmethoden en parameters om de prestaties van de bot te optimaliseren.

Extra tips:
    Gebruik een "elo"-systeem: Implementeer een elo-systeem om de vaardigheid van de bot te meten en te matchen met tegenstanders van vergelijkbaar niveau.
    Analyseer spelresultaten: Analyseer de spelresultaten van de bot om te identificeren waar verbetering nodig is.
    Visualiseer de leercurve: Visualiseer de voortgang van de bot tijdens het trainen om te zien hoe de vaardigheid verbetert.

## Uit welke onderdelen zou ik het neurale netwerk kunnen opbouwen?
1. **Inputlaag:**
    - De inputlaag ontvangt de data die het netwerk zal gebruiken om een voorspelling te doen. In dit geval kunnen de data bestaan uit factoren zoals:
        + Landbouwgebieden
        + Troepensterkte
        + Continentbonus
        + Aantal omringende landen
        + Aantal omringende vijandige troepen
        + Aantal eigen troepen in het land

2. **Verborgen lagen:**
    - Verborgen lagen bestaan uit neuronen die de input verwerken en transformeren.
    - Het aantal verborgen lagen en neuronen per laag hangt af van de complexiteit van de taak.
    - Meestal worden **Recurrent Neural Networks (RNNs)** of **Convolutional Neural Networks (CNNs)** gebruikt voor dit soort taken.

3. **Outputlaag:**
    -  De outputlaag produceert de voorspelling van het netwerk.
    - In dit geval kan de outputlaag een classificatie zijn (bijv. "verover land" of "niet veroveren land") of een regressiewaarde (bijv. "kans op succes bij aanval").

4. **Activatiefuncties:**
    - Activatiefuncties bepalen hoe de neuronen in het netwerk reageren op de input.
    - ReLU, Sigmoid en Tanh zijn veelgebruikte activatiefuncties.

5. **Verliesfunctie:**
    - De verliesfunctie bepaalt de fout van de voorspelling van het netwerk.
    - Mean Squared Error (MSE) en Croos-Entropy zijn veelgebruikte verliesfuncties.

6. **Optimizer:**
    - De optimizer past de gewichten van het netwerk aan om de verliesfunctie te minimaliseren.
    - Adam, SGD, en RMSProp zijn veelgebruikte optimizers.

**Extra onderdelen:**
- **Batch normalisatie:** Verbetert de stabiliteit van het trainingsproces.
- **Dropout:** Voorkomt overfitting door willekeurig neuronen te deactiveren tijdens training.
- **Regularisatie:** Voegt straffen toe aan de gewichten van het netwerk om overfitting te verminderen.

**Van input tot output:**
1. De inputdata wordt gepresenteerd aan de inputlaag.
2. De neuronen in de verborgen laag(en) verwerken de input en transformeren deze.
3. De outputlaag produceert de voorspelling van het netwerk.
4. De verliesfunctie berekent de fout van de voorspelling.
5. De optimizer past de gewichten van het netwerk aan om de verliesfunctie te minimaliseren.

















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