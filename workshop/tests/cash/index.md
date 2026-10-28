# Many submissions of cash

Aan studenten is gevraagd de volgende functie te implementeren:

    def number_of_coins(change: int, coins: list[int]) -> int:
        """
        Given an amount of change in cents, and a list of coins in cents,
            calculate how many coins are needed to fulfill the change.
        Raises a TypeError in case floats are given instead of integers.
        Raises a ValueError in case of negative values, or coins of value 0.
        """

Bijvoorbeeld:

    print(number_of_coins(41, [25, 10, 5, 1])) # prints 4

Om de opdracht verder af te bakenen is het volgende toegevoegd:

* Je mag aannemen dat een greedy strategie (zoveel mogelijk wisselen met de grootste munt die nog past) altijd het juiste antwoord oplevert.
* Je mag aannemen dat de gebruiker nooit andere waardes invoert dan integers en floats.
* Je mag aannemen dat de gebruiker voor de munten altijd een `list` van integers of floats invoert.
* Als het bedrag niet exact gewisseld kan worden, geef dan zoveel mogelijk zonder het totaal te overschrijden. Als er bijvoorbeeld alleen kwartjes (25) zijn en het bedrag is 97, geef dan 3 kwartjes.

Aan het eind van de dag hebben dertien studenten hun werk ingeleverd. Je vindt alle dertien uitwerkingen in de map `submissions`. Dat laat ons met een uitdaging zitten: nakijken. Welke van deze dertien uitwerkingen zijn fout, en waarom?

## Wat te doen

[Download de distributiecode](testing_cash.zip).

Schrijf unittests in Pytest voor deze opdracht. Zoek uit welke uitwerkingen correct of incorrect zijn. Als een uitwerking incorrect is, schrijf dan op waarom (zie het verslag hieronder). Lever al je unittests in, in een bestand genaamd `test_cash.py`, onderaan deze pagina.

## Een beetje hulp

Voordat je meteen begint: we hebben wat scaffolding toegevoegd om je op weg te helpen. Je vindt twee extra bestanden:

1. `conftest.py`. Kort gezegd bevat dit bestand pytest-specifieke code die een command line optie (`--path`) aan pytest toevoegt en die paden gebruikt om de uitwerkingen van `number_of_coins` van de studenten in te laden. Deze uitwerkingen worden doorgegeven aan elke unittest die om een `number_of_coins` fixture vraagt. Hierdoor kan je tests schrijven zoals:


        def test_something(number_of_coins):
            assert number_of_coins(41, [25, 10, 5, 1]) == 4


    En deze zo draaien:

        pytest --path submissions/1/cash.py
        pytest --path submissions/1/cash.py --path submissions/2/cash.py

2. Dertien programma's is veel om te testen, en het is makkelijk om het overzicht kwijt te raken. `run_tests.py` helpt daarbij. Dit script draait pytest voor elke uitwerking in de map `submissions` en schrijft de uitvoer van de tests naar `outputs/1.txt` (voor elke uitwerking apart). Draai het zo:

        $ python3 run_tests.py
        Testing - submissions/1/cash.py => outputs/1.txt   | SUCCESS
        Testing - submissions/2/cash.py => outputs/2.txt   | FAILED
        Testing - submissions/3/cash.py => outputs/3.txt   | SUCCESS
        ...

## Wat gemoedsrust

* Je mag aannemen dat alle uitwerkingen deterministisch zijn, er zit geen randomness in.
* Je mag aannemen dat er geen oneindige loops bestaan.
* Je mag aannemen dat de code van de studenten niets kwaadaardigs bevat, dus je kunt het veilig op je eigen computer draaien.
* We zijn vrij zeker dat slechts **één** uitwerking correct is, maar je mag bewijzen dat we ongelijk hebben!
* De `12` incorrecte uitwerkingen zijn op fundamenteel verschillende manieren fout. Je zult waarschijnlijk minstens 12 testcases moeten schrijven.

## Verslag

Schrijf in een verslag (`.pdf`) voor elk van de 13 uitwerkingen op of deze correct of incorrect is. Geef voor elke incorrecte uitwerking een onderbouwing: hoe weten we zonder twijfel dat die uitwerking inderdaad incorrect is? Je hebt bijvoorbeeld waarschijnlijk een testcase gevonden die heel specifiek fout gedrag laat zien, op basis van hoe het programma getest wordt.

Houd er rekening mee dat de foute uitwerkingen op fundamenteel verschillende manieren fout zijn, dus elke uitwerking vraagt om een andere redenering. Daarom moet je voor elke uitwerking aparte tests schrijven, maar wel alle tests in hetzelfde testbestand houden. Zo zie je dat elke test op een andere uitwerking afgaat.
