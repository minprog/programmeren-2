# Many submissions of merge_intervals

Dit is een tweede ronde van dezelfde workshop, met een lastigere functie. Opnieuw krijg je dertien uitwerkingen, en opnieuw is er maar één correct. De uitwerkingen zijn nu in veel verschillende programmeerstijlen geschreven: functioneel, recursief, met een heap, met een object en een cache, enzovoort. Laat je daardoor niet afleiden: je test van buitenaf wat de functie doet, niet hoe.

Aan studenten is gevraagd de volgende functie te implementeren:

    def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """
        Given a list of closed intervals (start, end), merge all intervals
            that overlap or touch, and return the result as a list of tuples,
            sorted by start.
        Raises a ValueError if an interval ends before it starts.
        """

Bijvoorbeeld, een planning van bezette tijdsblokken:

    print(merge_intervals([(9, 12), (14, 16), (11, 13)]))  # prints [(9, 13), (14, 16)]

Om de opdracht verder af te bakenen is het volgende toegevoegd:

* Een interval `(start, end)` is een *gesloten* stuk van de getallenlijn, dus zowel `start` als `end` horen erbij. Het mag ook één punt zijn: `(5, 5)`.
* Intervallen die overlappen *of elkaar raken* worden samengevoegd: `(1, 3)` en `(3, 5)` worden `(1, 5)`.
* Intervallen die geen enkel punt gemeen hebben blijven los, ook als er maar een kleine ruimte tussen zit: `(1, 2)` en `(3, 4)` blijven twee intervallen.
* Het resultaat is een `list` van `tuple`s, gesorteerd op `start`, waarin geen twee intervallen elkaar overlappen of raken.
* De invoer kan in willekeurige volgorde staan, dubbele of geneste intervallen bevatten en negatieve getallen. Bij lege invoer is het resultaat een lege lijst.
* Als een interval eindigt voordat het begint (`start > end`), dan geeft de functie een `ValueError`.
* De functie mag de lijst die ze meekrijgt niet aanpassen.
* Je mag aannemen dat de invoer altijd een `list` van `tuple`s van twee integers is.

Aan het eind van de dag hebben dertien studenten hun werk ingeleverd. Je vindt alle dertien uitwerkingen in de map `submissions`. Welke van deze dertien uitwerkingen zijn fout, en waarom?

## Wat te doen

[Download de distributiecode](testing_merge.zip).

Schrijf unittests in Pytest voor deze opdracht. Zoek uit welke uitwerkingen correct of incorrect zijn. Als een uitwerking incorrect is, schrijf dan op waarom (zie het verslag hieronder). Lever al je unittests in, in een bestand genaamd `test_merge.py`, onderaan deze pagina.

## Een beetje hulp

Net als bij [Many submissions of cash](/workshop/tests/tests) hebben we scaffolding toegevoegd. Je vindt twee extra bestanden:

1. `conftest.py`. Dit bestand voegt een command line optie (`--path`) aan pytest toe en laadt de uitwerkingen van `merge_intervals` in. Deze worden doorgegeven aan elke unittest die om een `merge_intervals` fixture vraagt. Hierdoor kan je tests schrijven zoals:

        def test_something(merge_intervals):
            assert merge_intervals([(1, 4), (3, 6)]) == [(1, 6)]

    En deze zo draaien:

        pytest --path submissions/1/merge.py
        pytest --path submissions/1/merge.py --path submissions/2/merge.py

2. `run_tests.py`. Dit script draait pytest voor elke uitwerking in de map `submissions` en schrijft de uitvoer van de tests naar `outputs/1.txt` (voor elke uitwerking apart). Draai het zo:

        $ python3 run_tests.py
        Testing - submissions/1/merge.py => outputs/1.txt   | SUCCESS
        Testing - submissions/2/merge.py => outputs/2.txt   | FAILED
        Testing - submissions/3/merge.py => outputs/3.txt   | SUCCESS
        ...

## Wat gemoedsrust

* Je mag aannemen dat alle uitwerkingen deterministisch zijn, er zit geen randomness in.
* Je mag aannemen dat er geen oneindige loops bestaan.
* Je mag aannemen dat de code van de studenten niets kwaadaardigs bevat, dus je kunt het veilig op je eigen computer draaien.
* We zijn vrij zeker dat slechts **één** uitwerking correct is, maar je mag bewijzen dat we ongelijk hebben!
* De `12` incorrecte uitwerkingen zijn op fundamenteel verschillende manieren fout. Je zult waarschijnlijk minstens 12 testcases moeten schrijven.
* Sommige fouten vallen alleen op als je een functie *twee keer* aanroept, of als je kijkt naar wat er met de invoer gebeurt *nadat* de functie klaar is. Een test hoeft niet uit één `assert` te bestaan.

## Verslag

Schrijf in een verslag (`.pdf`) voor elk van de 13 uitwerkingen op of deze correct of incorrect is. Geef voor elke incorrecte uitwerking een onderbouwing: hoe weten we zonder twijfel dat die uitwerking inderdaad incorrect is? Je hebt bijvoorbeeld waarschijnlijk een testcase gevonden die heel specifiek fout gedrag laat zien.

Houd er rekening mee dat de foute uitwerkingen op fundamenteel verschillende manieren fout zijn, dus elke uitwerking vraagt om een andere redenering. Daarom moet je voor elke uitwerking aparte tests schrijven, maar wel alle tests in hetzelfde testbestand houden. Zo zie je dat elke test op een andere uitwerking afgaat.
