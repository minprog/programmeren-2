# replace

Python strings kennen een methode `replace()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.replace).

Implementeer de volgende functie in een bestand genaamd `replace.py`:

    def replace(string: str, old: str, new: str, count: int=-1) -> str:
        """
        Return a copy of the string with all occurrences of substring old
        replaced by new. If the optional argument count is given, only the
        first count occurrences are replaced.
        """

## Testen

Schrijf in een apart bestand `test_replace.py` minimaal vier tests (vier aparte test functies) voor de functie `replace`.