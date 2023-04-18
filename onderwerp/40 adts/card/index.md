# Testen met twee implementaties

In deze opdracht ga je tests schrijven voor de `Card`-class uit het boek en daarna een *tweede* implementatie maken van de `Card`-class. De bedoeling is dat één set tests goed werkt met beide implementaties.

1.  Neem de `Card`-class uit paragraaf 2.3 van het boek in een file `card_original.py` (download [card.py](card.py) en [printcards.py](printcards.py)).

2.  Schrijf unit tests voor de class `Card` in een file `test_card.py`.

    - Bovenaan de file zet je `from test_card import Card`. Net als in eerdere modules gebruiken wij de module `pytest` om te testen.

    - Bedenk hoe de class gebruikt kan worden en schrijf tests die diverse gebruiksscenario's controleren. Zorg dat tests op zichzelf staan. Je kunt bijvoorbeeld een test schrijven om te kijken of het lukt een nieuwe `Card` aan te maken. Maar als je een test maakt om te kijken of het lukt om de `suitName` op te vragen, maak dan in dezelfde test eerst een nieuwe `Card` aan en vraag daarvan de `suitName` op.

    - Probeer zo compleet mogelijk alle combinaties van functie-aanroepen te testen, maar probeer tegelijk herhaling van soortgelijke tests te voorkomen. Dit is een balans die je moet vinden.

3.  Pas nu de `Card`-class aan zodat deze gebruik maakt van de alternatieve implementatie zoals beschreven in paragraaf 2.3.3 van het boek (sla een nieuwe versie op!). De tests moeten exact zo blijven werken als ze zijn en dat betekent dat je ook niets mag veranderen aan welke methods er zijn in de `Card`-class en welke argumenten ze meekrijgen.

4.  Gebruik dan de tests die je hebt geschreven om te controleren of jouw nieuwe implementatie nog steeds precies zo werkt (functioneel is) als de oorspronkelijke versie uit het boek. Je kunt daarmee aantonen dat de beide implementaties van deze Card ADT **compatibel** zijn. Mocht je nog fouten vinden, pas je nieuwe implementatie dan aan.

Hiermee laat je zien dat het mogelijk is om één ADT te definiëren en daarvan verschillende implementaties te bouwen. Doordat je ze met dezelfde tests kunt valideren toon je aan dat het dezelfde ADT is.

## Inleveren

Lever hieronder de oude en de nieuwe implementatie, en ook de bijbehorende tests in.
Zorg dat bij het inleveren `from card.py import Card` bovenaan je testfile staat, zodat de **nieuwe** implementatie wordt gebruikt voor testen.
