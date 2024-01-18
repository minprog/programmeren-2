## isalpha

Python strings kennen de methodes `isalpha()`, `islower()` en `isupper()`. Hier vind je de officiële documentatie van [isalpha](https://docs.python.org/3/library/stdtypes.html#str.isalpha), [islower](https://docs.python.org/3/library/stdtypes.html#str.islower) en [isupper](https://docs.python.org/3/library/stdtypes.html#str.isupper).

Implementeer de volgende functies in een bestand genaamd `isalpha.py`:

    def isalpha(string: str) -> bool:
        """
        Return True if all characters in the string are alphabetic
        and there is at least one character, False otherwise.
        """

    def islower(string: str) -> bool:
        """
        Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.
        """

    def isupper(string: str) -> bool:
        """
        Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.
        """

> `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`

## Testen

Schrijf in een apart bestand `test_isalpha.py` minimaal negen tests in totaal (negen aparte test functies) voor de functies `isalpha`, `islower` en `isupper`.