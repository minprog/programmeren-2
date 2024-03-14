# pytest

`pytest` is een populair Python framework voor het schrijven van tests. In een latere module gaan we uitgebreid in op het schrijven van tests en `pytest`. Hier volgt alleen een korte introductie met het broodnodige voor de introductie module.

`pytest` is naast een framework ook een programma dat je aanroept met: `pytest test_naam_van_test_bestand.py`. De naam van de testbestanden beginnen altijd met `test_`. Schrijf je bijvoorbeeld tests voor een programma genaamd `add.py`, dan zou een logische naam voor het testbestand zijn: `test_add.py`.

In het testbestand, bijvoorbeeld `test_add.py`, schrijf je tests. Dit zijn losse functies die `pytest` zal zien als aparte tests. Zo'n testfunctie ziet er vaak zo uit:

    def test_add_positive_numbers():
        assert add(3, 7) == 10

Ook hier begint de naam van iedere testfunctie met `test_`. Vervolgens is het slim om een beschrijvende functienaam te kiezen op basis van wat er wordt getest. In de functie zelf schrijf je testcode om je echte code te testen. Vaak is dat een zelfgeschreven functie aanroepen met een bepaalde input en een bepaalde output verwachten. Dat verwachten gaat door middel van het Python keyword `assert`. `assert` is als een if-statement, het kijkt of de uitkomst van de conditie `True` of `False` is. Het verschil is dat `assert` een error opgooit (`AssertionError`) als de conditie `False` oplevert. Eigenlijk dus, de conditie moet `True` zijn anders stopt het programma.

Omdat de testcode in een ander bestand staat (bijvoorbeeld `test_add.py`), zul je de functies uit je echte bestand (bijvoorbeeld `add.py`) moeten importeren. Dat kan op verschillende manieren, maar ook zo:

    from add import add

De regel hierboven lees je als: uit de module add (`add.py`) importeer de functie `add()`. Na deze import regel is de functie `add()` beschikbaar.

Vervolgens kan je de tests runnen met `pytest test_add.py`. Een mogelijk uitkomst is:

    =================== test session starts ====================
    platform darwin -- Python 3.12.1, pytest-7.4.0, pluggy-1.2.0
    rootdir: /Users/foo/programmeren_2/add
    collected 1 item                            

    test_add.py .                                         [100%]

    ==================== 1 passed in 0.00s =====================

Dit betekent dat alle tests, in dit geval één, zijn geslaagd. Natuurlijk kan het ook zo zijn dat een test faalt, maar dat zie je vanzelf.