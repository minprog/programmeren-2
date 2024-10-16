# split (real)

Python strings kennen een methode `split()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.split).

Implementeer de volgende functie in een bestand genaamd `split_real.py`:

    def split(string: str, sep: str|None=None, maxsplit: int=-1) -> list[str]:
        """
        Return a list of the words in the string, using sep as the delimiter
        string. If maxsplit is given at most maxsplit splits are done (thus,
        the list will have at most maxsplit+1 elements). If maxsplit is not
        specified or -1, then there is no limit on the number of splits
        (all possible splits are made).

        If sep is given, consecutive delimiters are not grouped together and
        are deemed to delimit empty strings (for example, split('1,,2', ',')
        returns ['1', '', '2']). The sep argument may consist of multiple
        characters (for example, split('1<>2<>3', '<>') returns
        ['1', '2', '3']). Splitting an empty string with a specified separator
        returns [''].

        If sep is not specified or is None, a different splitting algorithm
        is applied: runs of consecutive whitespace are regarded as a single
        separator, and the result will contain no empty strings at the start
        or end if the string has leading or trailing whitespace. Consequently,
        splitting an empty string or a string consisting of just whitespace
        with a None separator returns [].
        """

## Testen

Schrijf in een apart bestand `test_split_real.py` minimaal twaalf tests (twaalf aparte test functies) voor de functie `split`.