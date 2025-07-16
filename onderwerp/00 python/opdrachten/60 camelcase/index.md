# camelCase

Schrijf een programma `camelcase.py` dat camelCase convert naar snake_case en andersom. Het programma moet als volgt werken:

    $ python3 camelcase.py
    openFile
    open_file
    
    $ python3 camelCase.py
    open_file
    openFile

Met de volgende eisen:

* De invoer van het programma is altijd één woord.
* Bij een mix van underscores (`_`) en hoofdletters converteert het programma altijd naar snake_case. Zo wordt `open_someFile`: `open_some_file`.

Implementeer en gebruik in je programma de volgende functie:

    def convert(name: str) -> str:
        pass

## Testen

Schrijf in een apart bestand `test_camelcase.py` minimaal vier tests (vier aparte test functies) voor de functie `convert`.