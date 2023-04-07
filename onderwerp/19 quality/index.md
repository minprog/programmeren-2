# Codekwaliteit

Herschrijf je code voor Schuifpuzzel en Hangman en zorg dat ze meer in lijn zijn met de Python-standaarden en in het algemeen een hogere leesbaarheid en begrijpelijkheid hebben door beter op te delen en te vereenvoudigen.

## Individuele opdracht

Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand of iets anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

## Kwaliteit

Jouw code heeft een zekere [kwaliteit](https://en.wikipedia.org/wiki/Zen_and_the_Art_of_Motorcycle_Maintenance). Kwaliteit is nogal een ongrijpbaar begrip. Het is echter heel gebruikelijk om kwaliteit begrijpelijk te maken door gebruik te maken van heuristieken (versimpelde uitleg) of metrieken (versimpelde metingen). Als je ergens een getal of een label op kunt plakken, dan kun je makkelijker communiceren over de waarde van iets.

In de softwarebusiness hebben we hetzelfde probleem. Code kan totaal chaotisch zijn, maar wat moet je verbeteren? Code kan een "je ne sais quoi" overzichtelijkheid hebben, maar wat maakt nou dat het zo geweldig makkelijk te begrijpen is? De oorzaak zit 'm vaak in meerdere factoren die elkaar beïnvloeden.

Voor het verbeteren of onder controle houden van de kwaliteit van software gebruiken we ook heuristieken en metrieken. Heuristieken zijn bijvoorbeeld "functies die een superkorte naam hebben". Als je die op een rijtje kan zetten weet je waar je moet kijken voor verbetering. Of je hebt een lijst van "plekken waar de indentatie niet klopt met hoe dit normaal hoort in Python". Makkelijk opgelost. Misschien helpt het om de totale kwaliteit te verhogen.

Metrieken kunnen zijn hoeveel functies je hebt in één bestand, hoeveel methodes in één class. Of, zoals hieronder, hoeveel beslissingen in één functie worden genomen. Als die metriek hoog uitvalt, is dat misschien een kandidaat voor verbetering.

Kortom, we gebruiken bij het programmeren vaak tools die helpen "problemen" in onze code te vinden. De code is dan misschien bug-free, maar hij kan wel *beter*.

## Flake8

Flake8 is een tool die een aantal andere tools combineert om problemen in code te vinden. De tools zijn heel erg gericht op de "conventies" die gelden in de Python-wereld. In tegenstelling tot veel andere talen heeft de Python-community een sterke ["hoe hoort het eigenlijk"](https://nl.wikipedia.org/wiki/Hoe_hoort_het_eigenlijk)-mentaliteit. Dat kan erg prettig zijn omdat het structuur geeft... je hoeft niet alles zelf te bedenken.

**Instructies:**

1. Installeer Flake8: `pip3 install flake8`.

2. Gebruik de tool om je 21/Deck/Card te controleren op "violations" van de regels (`flake8 *.py` bijvoorbeeld).

3. Je vindt [hier](https://flake8.pycqa.org/en/latest/user/error-codes.html) en [hier](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes) de mogelijke error codes.

Ga nog niet verbeteren, maar lees eerst alle instructies hieronder.

## Cyclomatic complexity

[Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity), of ook McCabe's complexity, is een metriek waarmee de fundamentele complexiteit van stukjes code (functies) zichtbaar kan worden gemaakt. We gaan daarbij uit van de "routes" die je door de code kunt lopen als je deze traceert vanaf de start.

In de basis is het vrij simpel: elke **beslissing** maakt de functie complexer. Een if/else-statement zorgt voor een verdubbeling van de mogelijke routes waarmee je door de code kunt lopen. Je hoeft de theorie niet supernauwkeurig te begrijpen om de metriek te kunnen gebruiken. Vaak kun je intuïtief zien waarom een functie als complex wordt bestempeld.

**Instructies:**

1. Installeer radon: <https://pypi.org/project/radon/>

2. Gebruik de tool om je programma's te controleren op complexiteit. Probeer te achterhalen waarom je code op bepaalde punten erg complex is geworden. Kijk of je vereenvoudigingen ziet, of dat je aparte functies kunt definiëren voor bepaalde delen.

## Verbeteren (de echte opdracht)

1. Doe op basis van de output van de tools hierboven een verbetering in je code. Dat kan van alles zijn!

2. Documenteer heel nauwkeurig welke verandering je hebt gedaan. Maak een document, beschrijf de wijziging in woorden en voeg screenshots in van het stukje code vóór en na de verandering. De screenshots mogen alleen van het stukje code zijn dat veranderd is. Als je grote screenshots gebruikt wordt je inzending helaas afgekeurd omdat het dan niet goed na te kijken is.

3. Ga naar stap 1 tenzij je al 20 keer bij stap 3 bent geweest.

Zo heb je 20 verbeteringen gedaan en nauwkeurig gedocumenteerd. Als je een aantal dezelfde verbeteringen doet op verschillende stukjes code, geef dit dan op als één stap.

De tests die je eerder hebt geschreven zou je niet met Radon moeten controleren. Flake8 zou wel nuttig kunnen zijn.
