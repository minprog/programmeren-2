## islower en isupper

Python strings kennen de methodes `islower()` en `isupper()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.isupper).

Implementeer de volgende functies in een bestand genaamd `iscase.py`:

    def islower(string: str) -> bool:
        """
        Return True if all cased characters in the string are lowercase and there is at least one cased character, False otherwise.
        """

    def isupper(string: str) -> bool:
        """
        Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.
        """

## Testen

Schrijf in een apart bestand `test_iscase.py` minimaal zes tests in totaal (zes aparte test functies) voor de functies `islower` en `isupper`.