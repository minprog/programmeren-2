## Kenteken

Schrijf een programma `kenteken.py` dat controleert of het kenteken van personenauto's aan de eisen van [RDW](https://www.rdw.nl/particulier/voertuigen/auto/de-kentekenplaat/cijfers-en-letters-op-de-kentekenplaat) voldoet. Specifiek de volgende eisen:

* Voor personenauto’s zijn de volgende medeklinkers toegestaan als eerste letter: G, H, J, K, L, N, P, R, S, T, X en Z. 
* Een kenteken is altijd in één van de volgende vormen:
    * 99-XX-XX
    * 99-XXX-9
    * 9-XXX-99
    * XX-999-X
    * X-999-XX
* De volgende lettercombinaties zijn verboden: PVV, SGP, VVD, FVD en BBB

Het programma moet als volgt werken:

    $ python3 kenteken.py
    13ghj8
    ja

    $ python3 kenteken.py
    13ahj8
    nee

    $ python3 kenteken.py
    J-321-AB
    ja

Met de volgende eisen:

* Het programma moet case-insensitive werken.
* Het programma moet ongevoelig zijn voor strepen (`-`) in het kenteken.

Implementeer en maak gebruik van de volgende functie:

    def check_kenteken(kenteken: str) -> bool:
        pass

## Testen

Schrijf in een apart bestand `test_kenteken.py` minimaal zes tests (zes aparte test functies) voor de functie `check_kenteken`.