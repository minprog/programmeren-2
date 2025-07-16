# split

Python strings kennen een methode `split()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.split).

Implementeer de volgende functie in een bestand genaamd `split.py`:

    def split(string: str, sep: str, maxsplit: int=-1) -> list[str]:
        """
        Return a list of the words in the string, using sep as the delimiter
        string. If maxsplit is given at most maxsplit splits are done (thus,
        the list will have at most maxsplit+1 elements). If maxsplit is not
        specified or -1, then there is no limit on the number of splits
        (all possible splits are made).

        Consecutive delimiters are not grouped together and
        are deemed to delimit empty strings (for example, split('1,,2', ',')
        returns ['1', '', '2']). The sep argument may consist of multiple
        characters (for example, split('1<>2<>3', '<>') returns
        ['1', '2', '3']). Splitting an empty string with a specified separator
        returns [''].
        """

> Let op, de gevraagde implementatie is anders dan de implementatie van Python. Hier is `sep` geen optioneel argument en `sep` is altijd een `str`.

## Testen

Schrijf in een apart bestand `test_split.py` minimaal zes tests (zes aparte test functies) voor de functie `split`. Dit is een functie met veel mogelijke combinaties van input. Kies de zes tests als volgt:

* De tests voeren gezamenlijk zoveel mogelijk code uit, het zogenaamde "test coverage". Praktisch iedere regel code wordt uitgevoerd door de tests.
* Kies voor belangrijke of wellicht verassende edge cases. Hier hebben tests ook een documentatie functie, je legt vast wat een functie moet doen met een eigennaardige input.