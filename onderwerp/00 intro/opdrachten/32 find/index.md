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

Schrijf in een apart bestand `test_find.py` minimaal zes tests (zes aparte test functies) voor de functie `find`. Dit is een functie met veel mogelijke combinaties van input. Kies de zes tests als volgt:

* De tests voeren gezamenlijk zoveel mogelijk code uit, het zogenaamde "test coverage". Praktisch iedere regel code wordt uitgevoerd door de tests.
* Kies voor belangrijke of wellicht verassende edge cases. Hier hebben tests ook een documentatie functie, je legt vast wat een functie moet doen met een eigennaardige input.