# isalpha

Python strings kennen de methodes `isalpha()`, `islower()` en `isupper()`. Hier vind je de officiële documentatie van [isalpha](https://docs.python.org/3/library/stdtypes.html#str.isalpha), [islower](https://docs.python.org/3/library/stdtypes.html#str.islower) en [isupper](https://docs.python.org/3/library/stdtypes.html#str.isupper).

Implementeer de volgende functies in een bestand genaamd `isalpha.py`:

    def isalpha(string: str) -> bool:
        """
        Return True if all characters in the string are alphabetic
        and there is at least one character, False otherwise.
        """

    def islower(string: str) -> bool:
        """
        Return True if all cased characters in the string are lowercase
        and there is at least one cased character, False otherwise.
        """

    def isupper(string: str) -> bool:
        """
        Return True if all cased characters in the string are uppercase
        and there is at least one cased character, False otherwise.
        """

> `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`

> **Let op!** Er zit een verschil tussen de verschillende functies. `isalpha` heeft tenminste **one character** nodig voor `True`. `islower` en `isupper` hebben daarentegen tenminste **one cased character** nodig.

## Testen

Schrijf in een apart bestand `test_isalpha.py` minimaal negen tests in totaal (negen aparte test functies) voor de functies `isalpha`, `islower` en `isupper`. Test voor iedere functie het volgende:

Alle mogelijke situaties waarin de functie `True` of `False` returned. Bijvoorbeeld voor `isalpha`:

- De situatie waarin de functie `True` returned: `"foo"`
- De situatie waarin de functie `False` returned vanwege een niet alfabetische letter: `"foo!"` 
- De situatie waarin de functie `False` returned vanwege het ontbreken van letters: `""`

Hoewel de functie in de laatste twee situaties dezelfde waarde (`False`) returned, is er echt een andere reden waarom deze waarde gereturned moet worden. Dat maakt het belangrijk om deze redenen in isolatie te testen. Op deze manier wordt de code die beide gevallen afhandeld uitgevoerd door de tests, en is daarmee de kans op een bug kleiner.