# slice

Python strings en lists kennen ook slicing. Hier vind je een korte uitleg op [Stack Overflow](https://stackoverflow.com/a/509295).

Implementeer de volgende functie in een bestand genaamd `slice.py`:

    def slice(string: str, start: int=0, end: int|None=None) -> str:
        """
        Returns the substring of string between index start (inclusive)
        and end (exclusive).
        start is 0 if not given, and end is len(string) if not given.
        Both start and end can be any number between -len(string)
        and len(string) - 1
        """

> Implementeer de functie **zonder gebruik te maken van slicing**.

> De functie `slice()` heeft zogenaamde optionele argumenten. Deze functie kan je met of zonder de argumenten aanroepen, bijvoorbeeld: `slice("hello")`, `slice("hello", 2)`, `slice("hello", 2, -1)`, `slice("hello", end=3)` 

> `None` is de niks waarde in Python. Gebruik de `is` operator om te vergelijken met `None`, bijvoorbeeld `if end is None:`. 

## Testen

Schrijf in een apart bestand `test_slice.py` minimaal zes tests in totaal (zes aparte test functies) voor de functie `slice`.