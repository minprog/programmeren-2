# Structures

Deze module gaat over structuren die je kunt bouwen met objecten. We hebben eerder al kennis gemaakt met ADT's die de werking van een enkele class voorschrijven. In deze module ga je twee generieke ADT's leren kennen: de stack en de queue. Beide hebben allerlei toepassingen in het programmeren van efficiënte algoritmen. Daarnaast kun je classes zo inrichten dat je netwerken van objecten kunt bouwen. Uit Programmeren 1 ken je al de "linked list", die je ook met Python classes kunt maken. En we werken toe naar grafen, waar elk object naar verschillende andere objecten kan wijzen. De opdracht Adventure gebruikt dit idee om een netwerk van "kamers" op te bouwen waar je als speler doorheen kunt lopen.

## Leerdoelen

Je gaat in deze module:

- Leren over references naar objecten
- Specialistische ADTs implementeren (Stacks and Queues)
- Een groot programma ontwikkelen

## Puntentelling

- 2 punten voor een goed uitgevoerde Palindrome-oefening (geen deelpunten)

- tot 7 punten voor Adventure, afhankelijk van hoe ver je komt met de implementatie:
    - eerste 7 punten zijn op basis van percentage checks die lukken en uitvoering volgens de opdracht (zonder uitzondering)

Voor de wijze waarop je het geleerde uit Programmeren 2 toepast in deze implementatie kan je extra * punten behalen. Deze punten tellen apart mee, zie ook de studiewijzer. 

3 * punten voor de kwaliteit van de uitvoering:

    - 1 punt voor degelijke uitvoering waar basis op orde is: volledige docstrings, type hints die goedgekeurd worden volgens `mypy --strict`

    - 2 punten voor een zeer goede uitvoering waar voldaan is aan de eisen voor 1 punt, maar waar ook zinvolle `pytest` tests aanwezig zijn voor alle classes die zinvol testbaar zijn (het is aan jou om uit te zoeken welke tests, de assistenten mogen hier niet bij helpen).

    - 3 punten voor een uitzonderlijk goede uitvoering waar voldaan is aan de eisen voor 2 punten, maar waar het (class)design substantieel ook is aangepast waardoor de code overzichtelijker wordt (met nadrukkelijke eis dat de checks nog slagen; assistenten mogen op geen enkele manier helpen met redesign, wel met debugging natuurlijk). De cyclomatic complexity voor ieder deel moet 2 of lager zijn, dit wordt gemeten via `flake8 --max-complexity 2 --select=C *.py`
