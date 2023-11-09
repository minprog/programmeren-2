# Structures

Deze module gaat over structuren die je kunt bouwen met objecten. We hebben eerder al kennis gemaakt met ADT's die de werking van een enkele class voorschrijven. In deze module ga je twee generieke ADT's leren kennen: de stack en de queue. Beide hebben allerlei toepassingen in het programmeren van efficiënte algoritmen. Daarnaast kun je classes zo inrichten dat je netwerken van objecten kunt bouwen. Uit Programmeren 1 ken je al de "linked list", die je ook met Python classes kunt maken. En we werken toe naar grafen, waar elk object naar verschillende andere objecten kan wijzen. De opdracht Adventure gebruikt dit idee om een netwerk van "kamers" op te bouwen waar je als speler doorheen kunt lopen.

## Leerdoelen

Je gaat in deze module:

- Leren over references naar objecten
- Linked list bouwen met objects, net zoals met structs in C
- Specialistische ADTs implementeren (Stacks and Queues)

## Lesstof

Uit het boek lees je hoofdstuk 4 tot je het zo goed mogelijk begrijpt.

- 4.1 Overview
- 4.2 Python memory model
- 4.3 Linked implementation of lists

En dan hoofdstuk 5 tot je het zo goed mogelijk begrijpt.

- 5.1 Overview
- 5.2 Stacks
- 5.3 Queues
- 5.4 Queue implementations

## Puntentelling

- 2 punten voor een goed uitgevoerde Palindrome-oefening (geen deelpunten)

- tot 10 punten voor Adventure, afhankelijk van hoe ver je komt met de implementatie en de wijze waarop je het geleerde uit Programmeren 2 toepast in deze implementatie

    - eerste 7 punten zijn op basis van percentage checks die lukken en uitvoering volgens de opdracht (zonder uitzondering)

    - overige 3 punten voor de kwaliteit van de uitvoering:

        - 1 punt voor degelijke uitvoering waar basis op orde is: docstrings, relevante pre- en postconditions met af en toe assertions, type hints die goedgekeurd worden volgens `mypy --strict`

        - 2 punten voor een zeer goede uitvoering waar voldaan is aan de eisen voor 1 punt, maar waar ook zinvolle tests aanwezig zijn voor alle classes die zinvol testbaar zijn (het is aan jou om uit te zoeken welke tests, de assistenten mogen hier niet bij helpen)

        - 3 punten voor een uitzonderlijk goede uitvoering waar voldaan is aan de eisen voor 2 punten, maar waar het (class)design substantieel ook is aangepast waardoor de code overzichtelijker wordt (met nadrukkelijke eis dat de checks nog slagen; assistenten mogen op geen enkele manier helpen met redesign, wel met debugging natuurlijk)

## Extra onderwerp

Als laatste onderdeel van deze module staat de opdracht "Profiling". Deze is 3 punten waard binnen de cursus en telt gewoon mee. De opdracht is wel gemarkeerd als extra onderwerp omdat de rest van de cursus niet bouwt op deze kennis. Als je een opdracht moet overslaan is deze opdracht een goede keuze. Je mist daarmee dan wel enkele punten.
