# lower en upper

Python strings kennen de methodes `lower()` en `upper()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.upper).

Implementeer de volgende functies in een bestand genaamd `lower.py`:

    def lower(string: str) -> str:
        """
        Return a copy of the string with all the cased
        characters converted to lowercase.
        """

    def upper(string: str) -> str:
        """
        Return a copy of the string with all the cased
        characters converted to uppercase.
        """

> `.isalpha()` is een handige methode om hier te gebruiken. Deze kan je zo aanroepen: `"hello".isalpha()`, of als je een variabele (bijvoorbeeld `name`) hebt: `name.isalpha()`.

## Testen

Schrijf in een apart bestand `test_lower.py` minimaal vier tests in totaal (vier aparte test functies) voor de functies `lower` en `upper`. Deze functies beloven één aspect te veranderen, namelijk alle "cased characters" te converteren. Impliciet zit daarin ook de andere belofte: de rest van de karakters wordt ongemoeid gelaten. Dat zijn twee gevallen om te testen:

* Zijn alle "cased characters" nu een kleine letter / hoofdletter geworden?
* Staan alle niet "cased characters" nog goed in de string?

> Voor het testen zijn de methodes `.isupper()` en `.islower()` waarschijnlijk handig om te gebruiken.