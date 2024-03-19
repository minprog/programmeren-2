# pytest

`pytest` is een populair Python framework voor het schrijven van tests. In een latere module gaan we uitgebreid in op het schrijven van tests en `pytest`. Hier volgt alleen een korte introductie met het broodnodige voor de introductie module.

`pytest` is naast een framework ook een programma dat je aanroept met: `pytest test_naam_van_test_bestand.py`. De naam van de testbestanden beginnen altijd met `test_`. Schrijf je bijvoorbeeld tests voor een programma genaamd `add.py`, dan zou een logische naam voor het testbestand zijn: `test_add.py`.

In het testbestand, bijvoorbeeld `test_add.py`, schrijf je tests. Dit zijn losse functies die `pytest` zal zien als aparte tests. Zo'n testfunctie ziet er vaak zo uit:

    def test_add_positive_numbers():
        assert add(3, 7) == 10

Ook hier begint de naam van iedere testfunctie met `test_`. Vervolgens is het slim om een beschrijvende functienaam te kiezen op basis van wat er wordt getest. In de functie zelf schrijf je testcode om je echte code te testen. Vaak is dat een zelfgeschreven functie aanroepen met een bepaalde input en een bepaalde output verwachten. Dat verwachten gaat door middel van het Python keyword `assert`. `assert` is als een if-statement, het kijkt of de uitkomst van de conditie `True` of `False` is. Het verschil is dat `assert` een error opgooit (`AssertionError`) als de conditie `False` oplevert. Eigenlijk dus, de conditie moet `True` zijn, want anders stopt het programma.

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

## Waar schrijf je tests voor?

Tot nu toe heb je waarschijnlijk veel code handmatig getest. Door bijvoorbeeld een programma of een functie uit te voeren met bepaalde input en te kijken wat de output is. Op zich geheel logisch, want terwijl je aan het programmeren bent weet je wat de functie moet doen en kan je makkelijk even nagaan of die functie het ook daadwerkelijk doet. Dit werkt, totdat programma's groter worden, of misschien ga je samenwerken, of schrijf je code binnen een groter bestaand project. Al heel snel wordt het onmogelijk om de code nog met de hand te testen. Daarom beginnen we direct met het schrijven van tests binnen dit vak. Maar wat zijn nou goede tests?

Alles testen is vaak ondoenlijk. Het is te veel werk om ieder mogelijke input te contoleren. Dus is het taak om te kiezen voor representatieve en interessante gevallen. Dat kiezen, dat vraagt wat ervaring en een kritische houding. Stel we schrijven een functie om te kijken of een getal deelbaar is door een ander getal:

    is_deelbaar(noemer: float, deler: float) -> bool:

Aan de ene kant hebben we normale input en normale verwachte output. Bijvoorbeeld:

1. testcases voor deelbare getallen, zoals `9` en `3`, en `4` en `2`. De functie zou dan `True` moeten geven
2. testcases voor ondeelbare getallen, zoals `7` en `2`. De functie moet dan `False` geven.

Ook zijn er zogenaamde "edge cases" (randgevallen). Interessante gevallen, bijvoorbeeld:

1. Is `0` deelbaar door een ander getal?
2. Wat gebeurt er als je probeert te delen door `0`?

Voor ieder van de hierboven genoemde gevallen is een eigen test, een eigen testfunctie, op zijn plaats. Je ziet al dat de gekozen tests hierboven sterk afhangen van het soort probleem dat de functie oplost. Om goede tests te kiezen moet je dus ook goed begrijpen wat je gaat testen. Om die reden is het slim om gelijk tests te schrijven, terwijl je nog met je neus in de code zit.

> Let op, in een latere module gaan we dieper in op het schrijven van tests. Tot die tijd is het voor de opdrachten voldoende om enkel normale input en normale output te testen.