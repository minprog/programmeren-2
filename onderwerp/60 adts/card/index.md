# Testen met twee implementaties

In deze opdracht ga je tests schrijven voor de `Card`-class uit het boek en daarna een *tweede* implementatie maken van de `Card`-class. De bedoeling is dat één set tests goed werkt met beide implementaties.

1.  Neem de `Card`-class uit paragraaf 2.3 van het boek in een file `card_original.py` (download [card_original.py](card.py)).

2.  Schrijf unit tests voor de class `Card` in een file `test_card.py`.

    - Bovenaan de file zet je `from test_card import Card`. Net als in eerdere modules gebruiken wij de module `pytest` om te testen.

    - Bedenk hoe de class gebruikt kan worden en schrijf tests die diverse gebruiksscenario's controleren. Bijvoorbeeld het aanmaken van een `Card`-object en dan met `suitName` opvragen van de naam. En misschien een andere test voor het aanmaken van een `Card`-object voor een *andere* kaart. Enzovoort.

    - Zorg dat tests op zichzelf staan. Maak geen variabele in de ene test om die in de andere te gebruiken. Maak *zeker* geen globale variabelen aan die in meerdere tests gebruikt worden.

    - Beschrijf in de docstring bij de test wat je precies test.

    - Test **geen** interne implementatiedetails! Dat is precies waar de opdracht over gaat. Je gaat dus niet kijken of een waarde goed zit opgeslagen in een variabele in het object, maar je kunt wél een methode aanroepen om te kijken of die een juist "antwoord" geeft.

    - Probeer zo compleet mogelijk alle combinaties van functie-aanroepen te testen, maar probeer tegelijk herhaling van soortgelijke tests te voorkomen. Dit is een balans die je moet vinden.

3.  Pas nu de `Card`-class aan zodat deze gebruik maakt van de alternatieve implementatie zoals beschreven in paragraaf 2.3.3 van het boek (sla een nieuwe versie op als `card.py`!).

    Je alternatieve implementatie heeft niet meer de instance variables `rank_num` en `suit_char` , dus je moet deze regels verwijderen uit de __init__:

        self.rank_num = rank
        self.suit_char = suit

    Vervolgens voeg je een andere instance variable toe op basis van de ideeën uit paragraaf 2.3.3, die je vervolgens in de rest van de methodes gebruikt.

    Uiteindelijk moeten en kunnen de tests daarom exact zo blijven werken als ze zijn, omdat er niets zal veranderen aan welke methods er zijn in de `Card`-class en welke argumenten ze meekrijgen. Alleen de instance variables zullen veranderen en de code die daarmee werkt.

    Maar: mocht door het testen juist blijken dat je iets verkeerd aan het testen was, dan mag je natuurlijk wel de test veranderen! Zolang de tests maar blijven werken op zowel de oude als de nieuwe implementatie.

4.  Gebruik nu de tests om te controleren of jouw nieuwe implementatie nog steeds precies zo werkt (functioneel is) als de oorspronkelijke versie uit het boek. Je kunt daarmee aantonen dat de beide implementaties van deze Card ADT **compatibel** zijn. Mocht je nog fouten vinden, pas je nieuwe implementatie dan aan.

## Inleveren

Lever hieronder de oude en de nieuwe implementatie, en ook de bijbehorende tests in.
Zorg dat bij het inleveren `from card import Card` bovenaan je testfile staat, zodat de **nieuwe** implementatie wordt gebruikt voor testen.

Bij deze opdracht wordt niet gekeken naar gebruik van type hints.
