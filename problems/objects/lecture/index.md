# Lecture: Object-oriented programming

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_3m9duva2&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_0fj1ulvm)

You might have a look at [this video](https://www.youtube.com/watch?v=apACNr7DC_s) if you need an alternate source.


## Notes

Onderstaande lecture notes zijn nog in bewerking!


## Voorgeschiedenis

Objectgeoriënteerd programmeren begint bij Sketchpad, een programma om figuren op het scherm te tekenen. En nu nemen we dat redelijk voor lief, maar in 1963 was dat een bijzonder innovatieve stap. Er kon met een  soort lichtpen direct  op het scherm  getekend worden en van de punten die aangetipt worden  kon men "polygonen"  maken.

De programmeertaal Simula is de  andere kant van het verhaal. Dat is de eerste programmeertaal waarin "klassen" en eigenschappen van objecten omschreven konden worden, en zo konden programmeerproblemen waarin veel objecten een rol speelden beter beschreven worden, en korter.

Dit is Omnigraffle, een programma om diagrammen te maken met figuren, teksten en andere objecten. Hier hebben we drie figuren getekend: twee rechthoeken en een cirkel. Die rechthoeken, die hebben allebei eigenschappen: breedte, hoogte, en coördinaten. Breedte en hoogte is steeds hetzelfde, de coördinaten verschillen. Ook de cirkel heeft dezelfde breedte en hoogte, maar andere coördinaten. En een cirkel wordt natuurlijk op een andere manier getekend. Voor de cirkel voegen we ook nog een schaduw toe. Dan zie je rechts in de balk, zie je dat je de eigenschappen kan aanpassen.

## Objecten en classes

Op de achtergrond heeft zo'n programma natuurlijk een catalogus van objecten in het geheugen zitten. Dit zijn ze op een wat meer abstracte manier: drie objecten met hun eigenschappen. En als het programma deze objecten zou inladen, dan zou het die op precies dezelfde manier weer kunnen tekenen op het scherm.

De stap die we nu gaan maken, is dat we deze objecten gaan onderscheiden in "classes". Want een rechthoek wordt natuurlijk heel anders getekend dan een cirkel. Zo zeggen we dat rectangle1 en rectangle2 van het type Rectangle zijn, en circle1 is van het type Circle. Rectangle en Circle zijn dus de twee classes waar het hier om gaat.

Objecten bestaan in het geheugen  van het programma. Die worden gebruikt om wat er op dit moment op het scherm staat te kunnen representeren. "Classes" is een construct wat eigenlijk vooral bestaat in programmacode. Die definiëren wat voor soort eigenschappen zo'n object zou kunnen hebben. Hier staat bijvoorbeeld dat een rechthoek een breedte, hoogte, x, y  en een schaduw kan hebben, en een cirkel kan ook ook een breedte, een hoogte, een x, een y en een schaduw hebben.

## Classes in Python

Goed, hoe ziet een klasse eruit in Python? Dit is de simpelste die je kan definiëren: "class", en dan de naam van de klasse, Circle, en dan "pass".

    def Circle:
        pass

Pass betekent eigenlijk "sla deze regel over," dus dit is een lege klasse. We kunnen een klasse ook instantiëren, we kunnen objecten maken ván die klasse. En dat betekent dat we "Circle", de naam van de klasse geven en dan ronde haken. En dan wordt er een nieuw object gemaakt in het geheugen.

    circle1 = Circle()

In dit geval geven we het object ook een naam, door de naam op te geven en dan =. Zo kunnen we er nog eentje maken. En, zoals je ziet, er wordt echt een ander object aangemaakt: elke keer als je de naam  van de klasse geeft en met de ronde haken aangeeft dat er een nieuw object gemaakt moet worden. In dit geval krijgt die ook een andere naam.

    circle2 = Circle()

## Attributen

Als we een object hebben, dan kunnen we attributen toekennen. We maken een nieuw rechthoek-object, en dan zeggen we: oké, dit rechthoek-object heeft een breedte, een hoogte, een x en een y.

    >>> rectangle1 = Rectangle()
    >>> rectangle1.width = 85

We kunnen ook nog een tweede rechthoek-object aanmaken, en ook daar zeggen we: deze heeft een breedte, een hoogte, en x en een y.

## Verantwoordelijkheden

Naast eigenschappen kunnen in een klasse ook verantwoordelijkheden gedefinieerd worden. In dit geval kunnen we bijvoorbeeld van een  rechthoek de oppervlakte uitrekenen, maar ook van een cirkel kunnen we de oppervlakte uitrekenen. En zoals je weet zijn dat twee heel verschillende formules.

Objecten kunnen dus niet alleen dingen opslaan, maar ze kunnen ook dingen *doen*, en dat is hun "verantwoordelijkheid". Wat ze kunnen doen, dat staat in de klasse gedefinieerd. Laten we bijvoorbeeld een "area"-functie  toevoegen aan de Rectangle-klasse en die zegt gewoon: dat is "mijn" breedte maal "mijn" hoogte.

En daar komt het woord "self" in voor, en dat betekent zoveel als "gebruik hier het object waar het nu over gaat". Als ik bijvoorbeeld op rectangle1 "area" aanroep, dan willen we natuurlijk van rectangle1 ook daarvoor de breedte en de hoogte gebruiken. Dan krijgen we het goeie antwoord.

## Initializer

Soms willen definiëren dat een klasse niet kan bestaan zonder een aantal eigenschappen en daarvoor kun je een speciale methode aanmaken: de initializer. Die schrijf je zo met twee underscores, "init" en dan nog twee underscores. En in de initializer kun je zeggen: oké, self.width is 10 voor een nieuwe rechthoek self.height is ook 10, en we hebben coördinaten die op 0 komma 0 staan. Wat je ziet dan, als je een nieuwe rectangle aanmaakt, is dat deze initializer meteen wordt uitgevoerd en dat er dus ook meteen attributen bestaan. Maar die kun je nog steeds overschrijven. Je kan rectangle2 aanmaken en dan eigenschappen overschrijven.

We kunnen ook zeggen: een initializer heeft een aantal parameters nodig. In dit geval willen we dat, wie een rectangle aanmaakt, ook verplicht is om te specificeren wat de breedte, de hoogte, de x- en de y-coördinaat zijn. Als we dan proberen een rectangle te maken zonder die op te geven, dan geeft Python een "TypeError". Maar als we wel de vier coördinaten opgeven, dan worden die meteen mooi meegenomen en ingesteld. Wat je ziet is dat hier ook weer "self" wordt gebruikt om, van het Rectangle- object dat we aan het maken zijn, een aantal eigenschappen in te stellen.

Hier zie je een Rectangle-class waar in de initializer de breedte en de hoogte wél al worden gegeven, maar er is ook een methode `set_position` waarmee je de coördinaten kan opgeven.

Dit is een voorbeeld van een rectangle-klasse. Je ziet een initializer waar je vier waarden moét opgeven. Je bent verplicht om width, height, x en y in te vullen. Je ziet `set_position`, waarmee je een nieuwe locatie kan aangeven voor de rechthoek en je ziet "area", een methode die als taak heeft om de oppervlakte uit te rekenen.

Objecten van de rechthoek-klasse slaan dus vier belangrijke attributen op, kan de oppervlakte uitrekenen, en de code voor alle objecten is opgeslagen, is uitgetikt in één klasse. De klasse is de code die werkt op alle objecten van die klasse.

## Abstracte datatypes

Met classes kun je ook abstracte datatypes maken. Dat is één voorbeeld van waar je classes voor kan gebruiken. Je ziet hier een aantal voorbeelden die je misschien nog wel tegen gaat komen  en het abstracte datatype waar we nu mee gaan werken is een "queue". Een queue is een hele simpele: het is eigenlijk gewoon een soort lijst, en het idee is dat je aan de achterkant van de lijst dingen toevoegt, dat noemen we dan "back", en dat die er aan de voorkant altijd weer uit gaan. En er is geen andere mogelijkheid voor toevoegen en weghalen.

Je ziet in feite dat deze datastructuur veel minder flexibel is dan bijvoorbeeld een lijst. In een lijst kun je op redelijk willekeurige plekken dingen veranderen: je kan dingen aan de achterkant toevoegen, je kan dingen aan de voorkant toevoegen, en het idee van een Queue-klasse is juist dat het wat beperkt is, en op een bepaalde manier gebruikt hoort te worden.

Het voordeel is dat de interface dan vrij simpel kan blijven. Met de "interface" bedoelen we hoe de klasse gebruikt kan worden. In dit geval: we maken bijvoorbeeld een  nieuw Queue-object aan, en wat we dan willen doen is een getal "enqueuen", dus we kunnen q.enqueue met het getal 3. Dan willen misschien nog een getal erin zetten. En dan kunnen we bijvoorbeeld "dequeue" gebruiken om aan de andere kant van de lijst weer een getal of een ander object van de lijst af te halen.

Dus let nog even op wat hier gebeurt. We gaan aan de linkerkant van de queue, gaan we 3 toevoegen, daarna 1, en dan halen we één element uit de queue. Dat doen we aan de rechterkant en daar komt dus uit het element dat we als eerste hadden toegevoegd, namelijk 3, en dat noemen we first in first out. Er is een ander belangrijk datatype, en dat heet een "stack", en dat is juist last in first out. Dus nog even: de drie gaat erin, één gaat erin. Dat noemen we dan de achterkant, 3 staat aan de voorkant, en dat is dan ook degene die wordt ge-dequeued op het moment dat we dat vragen.

Goed, laten we een stukje van die klasse maken. We beginnen met class, Queue, pass. En dan neem ik even de test-code.

    q = ...

"q" is nieuwe queue, q.enqueue het getal 3, q.enqueue het getal 1, en dan printen we q.dequeue: het resultaat van de "dequeue"-operatie. Dit gaat nog niet werken, want de methoden "enqueue" en "dequeue" die we willen aanroepen, die zijn nog niet gedefinieerd. Dat gaan we nu doen. Ik kan pass weghalen... En dan gaan we enqueue definiëren en de-queue.

    def ...

Goed, zoals je misschien eerder al had gezien krijgt elke methode in een klasse "self" als eerste argument, en dat staat voor het object waar nu mee gewerkt wordt. In het geval van enqueue wilden we ook een andere parameter meegeven, namelijk het object, het element dat in de queue gezet moet worden.

## Encapsulation/lijst

Dan moeten we even na gaan denken over: wat is een queue eigenlijk, waar werken we mee? Ja, het is een soort lijst en de lijst is dan ook wel de meest voor de hand liggende manier om dingen op te slaan. En wat ik nu ga doen is een initializer definiëren voor de Queue-klasse die alvast een lijst klaarzet voor het geval we enqueue en dequeue gaan aanroepen. self.data is een lege lijst Goed. Wat betekent dan "en"queue? Nou, misschien zoiets als self punt data punt append... en dan moeten we het element erin zetten. Wat betekent dit: self.data is een lijst en als we dan append aanroepen dan wordt het aan de achterkant, dus de rechterkant, toegevoegd zoals je dat gewend bent van een lijst. Dat betekent dat bij "de"-queue moeten we juist aan de linkerkant iets weghalen. Hoe doen we dat? Dat doen we met "pop". Dat kun je vinden in de documentatie en dat kun je straks zien in de oefening over queues. Pop is een operatie die van een lijst een element opvraagt, en weghaalt, en in dit geval ook returnt, en onze dequeue-operatie moet dan het resultaat daarvan weer returnen naar wie de queue-operatie maar aan het gebruiken is.

Dus, we hebben een nieuwe functie die een lijst aanmaakt, we hebben een enqueue-functie die  een element toevoegt op de queue-manier en we hebben een dequeue-functie die een element weghaalt op de queue-manier. En als het goed is werkt ons voorbeeld nu ook wel. Inderdaad: 3.

Dus we maken zo'n diagram, net als we net hadden gedaan, met daar boven de naam van de klasse: Queue; een plek voor de attributen; en een plek voor de verantwoordelijkheden. In dit geval zijn de verantwoordelijkheden van de Queue het toevoegen en het weghalen van elementen.

## Encapsulation

Ik had het net al even over de lijst die in een queue zit. Dus in Python bouw je vaak je datastructuren op de datastructuren die Python zelf al aanbiedt. Je ziet er hier al een aantal: set, een tuple, een dict, een list... Wat is nou handig om te gebruiken?

* Een set is echt een hele snelle manier om willekeurig elementen toe te voegen en weer weg te halen. Het punt van een set is: de volgorde is niet gegarandeerd, en in een queue is volgorde juist heel belangrijk.

* Een tuple heb je misschien wel gezien en dat is een lijst-element waar je geen veranderingen in kan aanbrengen en bij een queue is dat juist heel belangrijk.

* Een dict is een beetje een rare keuze, want het is een mapping van "keys" naar "values", en in dit geval is een queue eigenlijk niet aan mapping van keys naar values, maar gewoon en een rijtje getallen of andere objecten. Dit is dus geen voor de hand liggende keuze, alleen al omdat hij ook niet geordend is.

* En dan blijft er van de standaard-datastructuren  toch vooral de lijst over, die ietsjes langzamer is soms met het toevoegen en verwijderen van elementen, maar wel precies aan alle voorwaarden voldoet om een queue mee te kunnen implementeren. Je kan dan dingen toevoegen aan het einde en bijvoorbeeld weghalen aan het begin, of andersom.

Daarom vullen we hier nu data in als een lege lijst-element  in het diagram.

## Privé-variabelen

Het is je misschien al opgevallen dat ik een underscore gebruik bij data, en dat is om te laten zien dat het een privé-element is, dat het niet van buitenaf aangepast moet worden. Je moet de queue alleen maar aanpassen door "enqueue" en "dequeue" aan te roepen en dat is ook het sterke van een abstracte datastructuur, dat je geacht wordt om die dingen te gebruiken, en dan zorgt de datastructuur ervoor dat de queue ook echt als een queue blijft werken.

## UML

Het diagram dat ik nu aan het gebruiken ben, en wat we eigenlijk al vanaf het begin gebruiken is UML: unified modeling language. En dit is een klassediagram, en een klasse ziet er dus zo uit: in het eerste blok heb je de klasse-naam, Queue in dit geval.

Dan heb je een blokje, daarin staan de verschillende attributen. In dit geval staat er een privé-attribuut, dat zou ik ook weg kunnen laten. Maar bijvoorbeeld bij de rechthoek-klasse zou je zien dat daar bijvoorbeeld de breedte en de hoogte gedefinieerd staan.

In het onderste blokje staan de verantwoordelijkheden van het geheel, oftewel de methodes die je kan definiëren. En de twee blokjes onder de naam noem je samen de "members" van de klasse: de onderdelen.

## Cards

Een ander voorbeeld is een kaartspel. Dat zijn objecten die in de echte wereld ook voor kunnen komen en die we kunnen beschrijven met classes. In dit geval hebben we een "Card"-klasse waarin één enkele speelkaart wordt beschreven en we hebben een "Deck"-klasse waarin een compleet kaartspel van 52 kaarten wordt beschreven.

### Data class

Card zou er bijvoorbeeld zo uit kunnen zien. We hebben een suit, een value:  een kleur en een waarde, en dan een description-methode. Description zou er uit kunnen zien als hier op het scherm. Card is een data-klasse. Dat betekent dat we eigenlijk geen  interessante methodes hebben die we  kunnen implementeren, maar alleen attributen, die we van buitenaf kunnen aanpassen, dus we kunnen een kaart maken en we kunnen de suit en de value  instellen.

### Full class

De Deck-klasse heeft juist geen attributen, maar een heleboel methods, in dit geval om te schudden (`shuffle`), om een kaart af te geven (`deal`) en wederom de description. Deze klasse is dus helemaal encapsulated, dat betekent dat we niet van buitenaf kunnen zien hoe het Deck kaarten wordt opgeslagen en we kunnen niet zien wat de volgorde is.

We kunnen eigenlijk alleen maar praten over de acties die de klasse voor ons kan verzorgen: maak een nieuw Deck kaarten, schud het en geef een kaart, en geef nog een kaart, en geef nog een kaart precies als je het in het echt ook zou doen.

## Implementation details

Maar hoe zou een Deck kaarten dan geïmplementeerd moeten worden? Wat voor Python-datastructuur zouden  we hiervoor gebruiken? Bij een kaartspel is volgorde in zekere zin wel belangrijk, want je schudt het, maar daarna moet het wel in volgorde blijven, dus een set valt wederom af. Er worden steeds kaarten afgegeven, dus een tuple valt ook af.. Dict is wederom "unordered" en niet echt een logische keuze.. en een lijst is de handige keuze, omdat het op volgorde staat.

## Relaties

Goed, Game of Cards.. zo ziet het eruit. De Card-klasse, de Deck-klasse, en we laten ook zien dat.. in een kaartspel zitten veel kaarten. "Has many relation". En dat is een relatie die je kunt specificeren in een klassediagram door een pijl te zetten en een omschrijving van wat de relatie is.

Er zijn een aantal standaardrelaties die je kunt beschrijven, maar je kunt het ook zelf verzinnen, om duidelijk te maken wat er aan de hand is en hoe het gebruikt  moet worden.

## Abstractie

In bovenstaande en andere voorbeelden hebben we het vaak over objecten uit de "echte wereld". Vergeet niet dat we daarbij ook altijd een heleboel informatie weglaten, zoals bijvoorbeeld:

- Kaarten in een kaartspel hebben altijd een zeker ontwerp op de achterkant staan. Het uiterlijk van de kaarten is echter niet relevant voor de werking van kaartspelletjes, dus die laten we nu weg.

- Als je een kaartspel speelt in het echt, dan wil je vaak meerdere keren spellen. Zodra het spel afgelopen is verzamel je alle kaarten, schud je ze, en dan kan het opnieuw beginnen. In code kun je dan net zo goed een "nieuw" kaartspel aanmaken en het oude weggooien.

Zo zijn er allerlei overwegingen om elementen van de echte wereld wel of niet op te nemen in het model dat je met code aan het bouwen bent. En je zult soms ook weer aanpassingen gaan maken aan je classes om nieuwe toepassingen mogelijk te maken. Maar uiteindelijk blijven je classes altijd een abstractie van de werkelijkheid.

## Conclusie

Objectgeoriënteerd programmeren heeft nog een heleboel andere aspecten, maar die heb je niet nodig op dit moment. Belangrijk is dat je weet:

- hoe je methodes kan schrijven, 
- hoe methodes iets te maken hebben met de verantwoordelijkheden van classes en objecten, 
- wat het verschil is tussen een klasse en een object, en
- hoe je "self" moet gebruiken.
