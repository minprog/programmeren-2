# Type hints toevoegen

Herschrijf je code voor Schuifpuzzel en Hangman en voeg type hints toe.

## Individuele opdracht

Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand of iets anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

## Type checking

Python zelf controleert nooit types. Niet vooraf en niet tijdens het runnen van je programma. Als je een bug hebt, word je dus ook niet beschermd door je typehints, en de code zal nog altijd op hetzelfde punt crashen.

Met de aparte tool `mypy` kun je de typehints echter heel strikt controleren, wat je zal helpen fouten te vinden voordat je je code uitvoert. Installeer `mypy` als volgt:

    $ pip3 install mypy

Afhankelijk van je besturingssysteem en installatie kan het zijn dat je het commando `pip` of zelfs `python -m pip` moet gebruiken.

## Controleer je type hints

Je kunt je code controleren op type hints door `mypy` te runnen:

    mypy --strict mario.py

Of om alle bestanden in de huidige map te controleren:

    mypy --strict .

## Submit

Je kunt hieronder je aangepaste programma's insturen.
