# Object graphs

Je gaat hier grafen bouwen met hulp van classes: een uitbreiding van het idee van linked structures. De opdracht Adventure gebruikt dit idee om een netwerk van "kamers" op te bouwen waar je als speler doorheen kunt lopen. Maar kamers verwijzen niet alleen naar andere kamers: er zit nog een hoop meer in deze opdracht. Hiermee sluit je het vak Programmeren 2 af.

## Leerdoelen

- Uitgebreid ervaring opdoen met references van objecten naar objecten
- Een groot programma ontwikkelen dat uit diverse classes bestaat

## Puntentelling

Standaard kun je voor deze opdracht 9 punten krijgen:

Basis-Adventure
: tot 9 punten, afhankelijk van hoe ver je komt met de implementatie - het percentage geslaagde checks bepaalt het aantal punten

Daarnaast kun je nog 1, 2 of 3 extra punten ontvangen voor een uitwerking waarin de ideeën van het vak verwerkt zijn:

Docstrings, type hints
: 1 punt voor degelijke uitvoering waar basis op orde is: volledige docstrings, type hints die goedgekeurd worden volgens `mypy --strict`

Docstrings, type hints, tests
: 2 punten voor een zeer goede uitvoering waar voldaan is aan de eisen voor 1 punt, maar waar ook zinvolle `pytest` tests aanwezig zijn voor alle classes die zinvol testbaar zijn (het is aan jou om uit te zoeken welke tests, de assistenten mogen hier niet bij helpen).

Docstrings, type hints, tests, design
: 3 punten voor een uitzonderlijk goede uitvoering waar voldaan is aan de eisen voor 2 punten, maar waar het (class)design substantieel ook is aangepast waardoor de code overzichtelijker wordt (met nadrukkelijke eis dat de checks nog slagen; assistenten mogen op geen enkele manier helpen met redesign, wel met debugging natuurlijk). De cyclomatic complexity voor ieder deel moet 2 of lager zijn, dit wordt gemeten via `flake8 --max-complexity 2 --select=C *.py`
