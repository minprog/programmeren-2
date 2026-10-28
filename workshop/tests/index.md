# Workshop: Testen van andermans code

In deze workshop test je code die iemand anders heeft geschreven. Je krijgt steeds dertien uitwerkingen van dezelfde opdracht, en precies één daarvan is correct. Het is aan jou en je team om te bewijzen welke dat is, en bij de andere twaalf aan te tonen *waarom* ze fout zijn. Je kijkt daarbij niet zozeer naar hoe de code werkt, maar naar wat de code doet: je schrijft tests die het gedrag van buitenaf vastleggen.

## Waar gaat het over?

Het testen van je eigen code is lastig, maar het testen van andermans code is misschien nog wel lastiger. Bedenk maar eens te bedenken op welke manieren iets fout kan gaan, zonder dat je zelf de code hebt geschreven of begrijpt. Dat ga je bij deze workshop doen.

## Opbouw

1. [Many submissions of cash](/workshop/tests/tests): de uitwerkingen van `number_of_coins`, een functie die munten telt. Je schrijft een `test_cash.py` waarin elke foute uitwerking door minstens één test wordt ontmaskerd.
2. [merge_intervals](/workshop/tests/merge): nu een functie die overlappende tijdsblokken samenvoegt. 

## Werkwijze

1. Lees de opdracht goed en bedenk **zonder code te lezen** welke situaties je zou willen testen: normale gevallen, grensgevallen en foute invoer.
2. Download de distributiecode en schrijf je eerste tests. Draai ze met `pytest --path submissions/1/cash.py` om te zien of ze slagen of falen op één uitwerking.
3. Gebruik `run_tests.py` om alle dertien uitwerkingen in één keer te testen, en kijk welke tests op welke uitwerking falen.
4. Bij een uitwerking die nog nergens op faalt: kijk wat die doet bij situaties die je nog niet getest hebt, en schrijf een test die het verschil laat zien. Pas als je echt vastzit loont het om de code zelf te lezen.
5. Schrijf je bevindingen op in het verslag: voor elke uitwerking of die correct is, en zo niet, welke test dat bewijst.

## Puntentelling

De workshop is onderdeel van de module [Abstract data types](/onderwerp/adt). Het aftekenen gebeurt handmatig door de docent aan het einde van de workshop, de automatische checks tellen niet mee voor de punten. Niet alles hoeft af tijdens de workshop.
