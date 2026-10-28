# Workshop: Cyclomatic Complexity

In deze workshop leer je code te herkennen die te ingewikkeld is en haal je die stap voor stap uit elkaar. Als maat gebruiken we de [Cyclomatic Complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) (ook wel McCabe's complexiteit): het aantal verschillende routes door een stuk code. Je krijgt vier programma's die werken, maar waarvan de code een rommeltje is. Jouw taak is steeds hetzelfde: maak de code overzichtelijker, zonder dat het programma iets anders gaat doen.

## Opbouw

1. [Hangman](/workshop/cc/hangman): een spel in één grote functie. Hier leg je de basis: wat is Cyclomatic Complexity, hoe meet je het met `flake8`, en hoe breek je een functie op.
2. [Bioscoop](/workshop/cc/cinema): een kassa met veel losse beslissingen. Je oefent met herhaalde code en met `dict`s en tuples in plaats van lange `if`/`elif`-ketens.
3. [Tekstanalyse](/workshop/cc/text): een programma dat een bestand verwerkt met lussen binnen lussen. Je oefent met het verdelen van lussen over functies.
4. [Vier op een rij](/workshop/cc/connect4): een spel verspreid over twee bestanden. Hier is functies opknippen niet genoeg, je moet ook slimmer naar de data kijken.

Begin dus met Hangman. Daar staat ook de uitleg over Cyclomatic Complexity en `flake8`, die je bij de andere opdrachten opnieuw nodig hebt.

## Werkwijze

Bij iedere opdracht werk je op dezelfde manier:

1. Kopieer de code van de opdracht naar je eigen bestand(en) en draai het programma, zodat je weet hoe het werkt.
2. Meet de complexiteit met `flake8` en kijk welke functies te ingewikkeld zijn.
3. Pas de code aan, één functie per keer, en test na elke stap of het programma nog precies hetzelfde doet.
4. Lever in. De checks controleren of de output nog klopt en of de complexiteit van elke functie niet hoger dan 3 is.

## Puntentelling

De workshop is onderdeel van de module [Collections en Complexiteit](/onderwerp/collections). Het aftekenen gebeurt handmatig door de docent aan het einde van de workshop, de automatische checks tellen niet mee voor de punten. Niet alles hoeft af tijdens de workshop.