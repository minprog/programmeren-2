# title

Python strings kennen een methode `title()`. Hier vind je de [officiële documentatie](https://docs.python.org/3/library/stdtypes.html#str.title).

Implementeer de volgende functie in een bestand genaamd `title.py`:

    def title(string: str) -> str:
        """
        Return a titlecased version of the string where words start with an
        uppercase character and the remaining characters are lowercase.

        The algorithm uses a simple language-independent definition of a word
        as groups of consecutive letters. The definition works in many
        contexts but it means that apostrophes in contractions and possessives
        form word boundaries, which may not be the desired result.
        """

## Testen

Schrijf in een apart bestand `test_title.py` minimaal vier tests (vier aparte test functies) voor de functie `title`.