# mypy

Python heeft optionele syntax voor het schrijven van zogenaamde `type hints`. In het kort, Python kent net zoals de meeste andere programmeertalen types zoals `int`, `float` en `str`. In tegenstelling tot bijvoorbeeld C heeft een variabele geen eigen type, maar alleen een type op basis van de waarde die wordt opgeslagen in de variabele. Zo kan éénzelfde variabele verschillende types opslaan, bijvoorbeeld zo:

    getal = 42
    getal = "hello world"

Dit betekent ook dat je aan de hand van een variabele alleen niet kunt afleiden wat erin is opgeslagen. Daarom bestaat er nu ook de mogelijkheid om dat type te hinten. Het ziet er als volgt uit:

    getal: int = 42

Type hints zorgen er ook voor dat een ander programma kan checken of de types kloppen in jouw code. Daardoor worden bugs een stuk sneller gevonden. `mypy` is zo'n typechecker voor Python. Je runt deze tool als volgt:

    mypy --strict

`mypy --strict` vereist dat je op bepaalde plekken type hints neerzet. Specifiek bij het definiëren van functies, bijvoorbeeld:

    def add(getal1, getal2):
        """verkeerd"""

    def add(getal1: int, getal2: int) -> int:
        """goed"""

En bij variabelen waar het type niet direct kan worden afgeleid. In veel gevallen kan het type wel worden afgeleid:

    foo = 7 # hier hoeft geen type hint, 7 is een int dus foo ook
    tekst = "hello world" # ook hier geen type hint nodig

Soms kan dat niet, bijvoorbeeld:

    getallen = [] # fout
    getallen: list[int] = [] # goed

In het geval hierboven is getallen een lege lijst. Daardoor weet `mypy` niet wat er in de lijst moet komen. `mypy` zal je dan ook vragen om een type hint toe te voegen.

Het type hint systeem van Python is vrij uitgebreid en dat behandelen we later in de cursus. Voor nu zijn de volgende details van belang:

* `int | None` betekent het type is of een `int` of de waarde `None` (niks)
* `list[int]` betekent een `list` van `int`s
* oudere versies van Python (Python 3.9 of eerder) hadden wisselende ondersteuning voor types. Zo moest je `List[int]` schrijven in plaats van `list[int]`, en `Optional[int]` in plaats van `int | None`. In deze cursus gebruiken we de nieuwe vorm.