# Abstract data types

Deze module gaat over *abstracte datatypen* ofwel ADTs. In deze inleiding leggen we uit wat een ADT is zonder voorbeelden te geven. Het kan goed zijn dat je de uitleg hieronder niet direct begrijpt. Het is daarom zinvol de uitleg later in de module nogmaals te lezen en te checken of je het dan wel begrijpt.

Een abstract datatype beschrijft een datatype vanuit de **operaties** die je erop moet kunnen uitvoeren. Als je deze operaties en het bijbehorende gedrag vastlegt, kun je al redeneren over de mogelijkheden die zo'n datatype je biedt als programmeur. Nog sterker, als je de operaties definieert dan kun je in principe al code schrijven die gebruik maakt van zo'n datatype, zonder dat je verdere afspraken hoeft te maken over de details. Een ADT is dus geen code, maar een afspraak (contract) over de mogelijkheden die het datatype biedt.

De details van de implementatie worden in het contract (of de beschrijving) van een ADT geheel weggelaten. Men kan in principe een ADT implementeren op een willekeurige manier, zolang alle verplichte operaties maar ondersteund worden met de juiste pre- en postcondities. In de praktijk zullen ADTs vaak op een specifieke manier geïmplementeerd worden, omdat men heeft ontdekt dat de operaties op één manier zeer efficiënt kunnen werken, terwijl de ADT als deze op een andere manier wordt geïmplementeerd nodeloos traag is of andere beperkingen kent.

## Leerdoelen

- Goed begrijpen wat een ADT is
- Enkele basisvoorbeelden van ADT's leren kennen
- Ervaren hoe je classes kunt gebruiken voor het implementeren van ADT's
- Leren kiezen voor de juiste datastructuur
- Verschillende list-implementaties in Python implementeren en onderzoeken
- Verschillende dictionary-implementaties in Python implementeren en onderzoeken

## Puntentelling

Voor iedere complete en goedwerkende opdracht:

Game of Cards
: 2 punten

Testen met twee implementaties
: 2 punten indien helemaal zorgvuldig gedaan met zinvolle tests die allerlei gebruiksscenario's van de class testen

Er zijn geen deelpunten mogelijk.

## Steropdracht

Wat is er mis met Cash*
: 2 punten in totaal
    - Bij deze opdracht krijg je 1/6 punt per goede oplossing, met een maximum van 2 punten.
