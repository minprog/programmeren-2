# Workshop: Wat is er mis met Cash

In deze workshop test je code die iemand anders heeft geschreven. Je krijgt dertien uitwerkingen van dezelfde opdracht, en precies één daarvan is correct. Het is aan jou en je team om te bewijzen welke dat is, en bij de andere twaalf aan te tonen *waarom* ze fout zijn. Je kijkt daarbij niet naar hoe de code werkt, maar naar wat de code doet: je schrijft tests die het gedrag van buitenaf vastleggen.

## Waar gaat het over?

Studenten kregen de opdracht een functie `number_of_coins` te schrijven, die uitrekent hoeveel munten er nodig zijn om een bedrag te wisselen:

    print(number_of_coins(41, [25, 10, 5, 1]))  # prints 4

Dat lijkt simpel, maar er zijn veel randgevallen: negatieve bedragen, munten van waarde 0, floats in plaats van integers, een bedrag dat niet exact te wisselen is, een lijst met munten in willekeurige volgorde. Elke foute uitwerking mist een ander randgeval. Een goede testsuite denkt van tevoren aan zulke gevallen en weet ze allemaal te vangen.

## Opbouw

1. [Many submissions of cash](/workshop/cash/tests): je krijgt de dertien uitwerkingen en wat hulpcode om ze in één keer te testen. Je schrijft een `test_cash.py` waarin elke foute uitwerking door minstens één test wordt ontmaskerd, en je beschrijft in een kort verslag per uitwerking wat er mis is.

## Werkwijze

1. Lees de opdracht goed en bedenk **zonder code te lezen** welke situaties je zou willen testen: normale gevallen, grensgevallen en foute invoer.
2. Download de distributiecode en schrijf je eerste tests. Draai ze met `pytest --path submissions/1/cash.py` om te zien of ze slagen of falen op één uitwerking.
3. Gebruik `run_tests.py` om alle dertien uitwerkingen in één keer te testen, en kijk welke tests op welke uitwerking falen.
4. Bij een uitwerking die nog nergens op faalt: kijk wat die doet bij situaties die je nog niet getest hebt, en schrijf een test die het verschil laat zien. Pas als je echt vastzit loont het om de code zelf te lezen.
5. Schrijf je bevindingen op in het verslag: voor elke uitwerking of die correct is, en zo niet, welke test dat bewijst.

Verdeel het werk in je team, maar bespreek je tests onderling. Een test die een collega bedenkt is vaak een randgeval dat jij vergeten was.

## Puntentelling

De workshop is onderdeel van de module [Abstract data types](/onderwerp/adt). Het aftekenen gebeurt handmatig door de docent aan het einde van de workshop, de automatische checks tellen niet mee voor de punten. Niet alles hoeft af tijdens de workshop.
