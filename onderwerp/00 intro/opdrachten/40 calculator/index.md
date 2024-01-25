# Calculator

Schrijf een programma `calculator.py` dat gebruikers een formule laat intikken en het programma rekent vervolgens de uitkomst uit. De calculator moet de volgende operaties ondersteunen:

* `+`
* `-`
* `*`
* `/`

Verder zijn er de volgende eisen:

* De invoer van het programma is altijd één formule in de vorm `a op b` waar `a` en `b` getallen zijn en `op` een operator. Bijvoorbeeld: `3 + 7`.
* Het antwoord moet geprint worden als kommagetal.
* Het programma moet om kunnen gaan met negatieve getallen.

Het programma moet als volgt werken:

    $ python3 calculator.py
    3 + 7
    10

Implementeer en gebruik de volgende functie in het programma:

    def calculate(formula: str) -> float:
        pass

> `eval()` en `exec()` mogen niet worden gebruikt.

## Testen

Schrijf in een apart bestand `test_calculator.py` minimaal vier tests (vier aparte test functies) voor de functie `calculate`.
