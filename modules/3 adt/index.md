# ADT

Deze module gaat over *abstract data types* ofwel ADTs. In deze inleiding leggen we uit wat een ADT is zonder voorbeelden te geven. Het kan goed zijn dat je de uitleg hieronder niet direct begrijpt. Het is daarom zinvol de uitleg later in de module nogmaals te lezen en te checken of je het dan wel begrijpt.

Een abstract datatype beschrijft een datatype vanuit de **operaties** die je erop moet kunnen uitvoeren. Als je deze operaties en het bijbehorende gedrag vastlegt, kun je al redeneren over de mogelijkheden die zo'n datatype je biedt als programmeur. Nog sterker, als je de operaties definieert dan kun je in principe al code schrijven die gebruik maakt van zo'n datatype, zonder dat je verdere afspraken hoeft te maken over de details. Een ADT is dus geen code, maar een afspraak (contract) over de mogelijkheden die het datatype biedt.

De details van de implementatie worden in het contract (of de beschrijving) van een ADT geheel weggelaten. Men kan in principe een ADT implementeren op een willekeurige manier, zolang alle verplichte operaties maar ondersteund worden met de juiste pre- en postcondities. In de praktijk zullen ADTs vaak op een specifieke manier geïmplementeerd worden, omdat men heeft ontdekt dat de operaties op één manier zeer efficiënt kunnen werken, terwijl de ADT als deze op een andere manier wordt geïmplementeerd nodeloos traag is of andere beperkingen kent.

Daarna gaan we kijken naar *container classes* in Python en hoe die zijn opgebouwd. Inmiddels ben je bekend met o.a. `list` en `dict` in Python. In deze module ga je deze datastructuren zelf implementeren op verschillende manieren en onderzoeken wat de voordelen en nadelen zijn van de implementaties. Het doel is een goed begrip opbouwen hoe de datastructuren in elkaar steken en waarom.

## Leerdoelen

Je gaat in deze module:

- Goed begrijpen wat een ADT is
- Enkele basisvoorbeelden van ADT's leren kennen
- Ervaren hoe je classes en objecten kunt gebruiken voor het implementeren van ADT's
- Leren kiezen voor de juiste datastructuur
- Verschillende list-implementaties in Python implementeren en onderzoeken
- Verschillende dictionary-implementaties in Python implementeren en onderzoeken

## Puntentelling

Voor ieder complete en goedwerkende opdracht:

- Twee implementaties: 2 punten indien helemaal zorgvuldig gedaan met zinvolle tests die allerlei gebruiksscenario's van de class testen
- List structures: 2 punten
- Dict structures: 2 punten

Er zijn geen deelpunten mogelijk.

Er is daarnaast één opdracht met een *: Priority Queue. Deze opdracht telt apart mee. Lever je deze goedwerkend in, dan is dat twee extra punten. Zie ook studiewijzer voor uitleg over * opdrachten.
