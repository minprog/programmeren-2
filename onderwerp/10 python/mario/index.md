# Mario

![](../../mario/less/pyramid.png)

In deze opdracht ga je Mario schrijven in Python. Gebruik de analyse die je eerder van Mario gemaakt hebt om snel te kunnen starten!

## Samenwerkopdracht

Bij deze opdracht is het helemaal prima om samen te werken met één of twee medestudenten. Zorg dat je gezamenlijk op één scherm kunt kijken en echt samen het probleem probeert op te lossen. Heeft iemand een goed idee, dan moet die zorgen dat de anderen het ook begrijpen. De bedoeling is dat alle samenwerkers evenveel hebben bijgedragen aan de opdracht. Iedereen levert uiteindelijk een eigen versie in.

## Gebruik

    $ python3 mario.py
    Height: 3
      ##
     ###
    ####
    $ python3 mario.py
    Height: -1
    Height: 24
    Height: 2
     ##
    ###

Op sommige systemen moet je `python mario.py` geven om je programma te starten.

## Specificatie

-   Schrijf een programma genaamd `~/problems/mario.py` dat een Mario-piramide tekent met gebruik van hash-tekens (`#`).

-   De gebruiker van het programma mag zelf de hoogte van de pyramide aangeven.

-   De hoogte van de pyramide mag niet groter dan 23 blokken hoog zijn, en niet kleiner dan 0. Wordt er een andere waarde ingevuld, dan moet je de gebruiker opnieuw om invoer vragen.

-   Je mag aannemen dat de gebruiker alleen integers invoert.

-   Maak je gebruik van de CS50 library, zoals in het college? Dan moet je deze eerst installeren. Dit doe je via het volgende commando:

        pip3 install cs50

## Tips

In het videocollege worden diverse tips gegeven over het printen van tekens op het scherm. Als je die combineert met je kennis van de oplossing in C dan zou je de opdracht moeten kunnen maken zonder verdere documentatie. Begrijp je iets niet uit het college, vraag dan gerust!

## Testen

    check50 -l minprog/checks/2022/mario/python
