# find

Python strings kennen een methode `find()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.find).

Implementeer de volgende functie in een bestand genaamd `find.py`:

    def find(string: str, sub: str, start: int|None=None, end: int|None=None) -> int:
        """
        Return the lowest index in the string where substring sub is found
        within the slice s[start:end]. Optional arguments start and end are
        interpreted as in slice notation. Return -1 if sub is not found.
        """

## Testen

Schrijf in een apart bestand `test_find.py` minimaal zes tests (zes aparte test functies) voor de functie `find`.