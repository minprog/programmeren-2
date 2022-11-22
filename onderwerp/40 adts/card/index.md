# Testen met twee implementaties

In deze opdracht ga je tests schrijven voor de `Card`-class uit het boek en daarna een *tweede* implementatie maken van de `Card`-class. De bedoeling is dat één set tests goed werkt met beide implementaties.

1. Neem de `Card`-class uit paragraaf 2.3 van het boek in een file `card.py` (download [card.py](card.py) en [printcards.py](printcards.py)).

2. Schrijf unit tests voor de class `Card` in een file `test_card.py`. Net als in eerdere modules gebruiken wij de module `pytest` om te testen. Bedenk hoe de class gebruikt kan worden en schrijf diverse tests.

3. Pas daarna de `Card`-class aan zodat deze gebruik maakt van de alternatieve implementatie zoals beschreven in paragraaf 2.3.3 van het boek (sla een nieuwe versie op!). De tests moeten exact zo blijven werken als ze zijn en dat betekent dat je ook niets kunt veranderen aan welke methods er zijn in de `Card`-class en welke argumenten ze meekrijgen.

4. Gebruik dan de tests die je hebt geschreven om te controleren of jouw nieuwe implementatie nog steeds precies zo werkt (functioneel is) als de oorspronkelijke versie uit het boek. Je kunt daarmee aantonen dat de beide implementaties van deze Card ADT **compatibel** zijn. Mocht je nog fouten vinden, pas je nieuwe implementatie dan aan.

Hiermee laat je zien dat het mogelijk is om één ADT te gebruiken met verschillende invullingen van de details van de implementatie.

## Inleveren

Lever hieronder zowel je nieuwe implementatie als de tests in.
