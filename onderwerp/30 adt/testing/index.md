# Testen met twee implementaties

In deze opdracht ga je tests schrijven voor de `Card`-class uit het boek en daarna een *tweede* implementatie maken van de `Card`-class. De bedoeling is dat één set tests goed werkt met beide implementaties.

1.  Neem de `Card`-class uit paragraaf 2.3 van het boek in een file `card_original.py` (download [card_original.py](card_original.py)).

2.  Schrijf tests voor de class `Card` in een file `test_card.py`.

    - Bovenaan de file zet je `from card_original import Card`. Net als in eerdere modules gebruiken wij de module `pytest` om te testen.

    - Bedenk hoe de class gebruikt kan worden en schrijf tests die diverse gebruiksscenario's controleren. Bijvoorbeeld het aanmaken van een `Card`-object en dan met `suit_name()` opvragen van de naam. En misschien een andere test voor het aanmaken van een `Card`-object voor een *andere* kaart. Enzovoort.

    - Zorg dat tests op zichzelf staan. Maak geen variabele in de ene test om die in de andere te gebruiken. Maak *zeker* geen globale variabelen aan die in meerdere tests gebruikt worden.

    - Test **geen** interne implementatiedetails! Dat is precies waar de opdracht over gaat. Je gaat dus niet kijken of een waarde goed zit opgeslagen in een variabele in het object, maar je kunt wél een methode aanroepen om te kijken of die een juist "antwoord" geeft.

    - Probeer zo compleet mogelijk alle combinaties van functie-aanroepen te testen, maar probeer tegelijk herhaling van soortgelijke tests te voorkomen. Dit is een balans die je moet vinden.

3.  Pas nu de `Card`-class aan zodat deze gebruik maakt van de alternatieve implementatie zoals beschreven in paragraaf 2.3.3 van het boek (sla een nieuwe versie op als `new_card.py`!).

    Je alternatieve implementatie heeft niet meer de instance variables `_rank_num` en `_suit_char` , dus je moet deze regels verwijderen uit de __init__:

        self.rank_num = rank
        self.suit_char = suit

    Vervolgens voeg je een andere instance variable toe op basis van de ideeën uit paragraaf 2.3.3, die je daarna in de rest van de methodes gebruikt.

4. Uiteindelijk moeten en kunnen de tests exact zo blijven werken als ze zijn, omdat er niets zal veranderen aan welke methods er zijn in de `Card`-class en welke argumenten ze meekrijgen. In andere woorden, de interface blijft helemaal hetzelfde als de oorspronkelijke `Card`-class. 

    Maar: mocht door het testen juist blijken dat je iets verkeerd aan het testen was, dan mag je natuurlijk wel de test veranderen! Zolang de tests maar blijven werken op zowel de oude als de nieuwe implementatie.

    Om beide implementaties tegelijk te kunnen testen, zonder daarvoor al je test code te moeten copy-pasten, gebruiken we een handige feature van pytest: een zogenaamde parametrized fixture. Neem daarvoor onderstaande code over en zet deze bovenin `test_card.py`

        from new_card import Card as NewCard
        from original_card import Card as OriginalCard

        import pytest

        @pytest.fixture(params=[NewCard, OriginalCard])
        def Card(request):
            return request.param

    In het kort, de eerste twee regels importeren beide `Card` classes en geven ze tactisch even een andere naam: `NewCard` en `OriginalCard`. Vervolgens wordt er een fixture aangemaakt met een speciale syntax. Het belangrijke hier is het woord `params` dat een lijst van waardes accepteert, in ons geval de twee verschillende classes. Dit gaat ervoor zorgen dat iedere test die deze fixture genaamd `Card` gebruikt twee keer wordt uitgevoerd, één keer voor `NewCard` en één keer voor `OriginalCard`. 

    Om de `Card` fixture te gebruiken voeg je een parameter genaamd `Card` toe aan iedere test functie. Bijvoorbeeld:

        def test_suit_name(Card):
            assert Card(1, "s").suit_name() == "Spades"

    Door dit te doen wordt test_suit_name automatisch twee keer uitgevoerd. De ene keer heeft `Card` de waarde `NewCard`, de volgende keer `OriginalCard`.

    Na deze aanpassingen te hebben gedaan, gebruik je je tests om te controleren of jouw nieuwe implementatie nog steeds precies zo werkt (functioneel is) als de oorspronkelijke versie uit het boek. Je kunt daarmee aantonen dat de beide implementaties van deze Card ADT **compatibel** zijn. Mocht je nog fouten vinden, pas je nieuwe implementatie dan gerust aan.

<details markdown="1"><summary markdown="span">Fixtures?</summary>
pytest heeft als test framework een boel features om testen makkelijker te maken. Een veel voorkomend probleem in testen is dat er een aantal zaken in orde moeten zijn voordat je iets kan testen. Bijvoorbeeld bij deze opdracht moet je vaak een kaart aanmaken en vervolgens kan je eigenschappen van de kaart bekijken. Dat valt relatief mee, maar naar mate programma's groter worden wordt die aanmaakstap ook steeds groter. Want, om bijvoorbeeld een pak kaarten (een `Deck`) te testen moet je eigenlijk alle 52 kaarten aanmaken en vervolgens een `Deck` en dan pas kan je een keertje testen. Als iedere test die code moet bevatten, wordt de testcode al snel groter en ingewikkelder dan de te testen code...

Onder andere hiervoor heeft pytest zogenaamde `fixture`s. Dit zijn functies die je zelf moet schrijven voor het opzetten van een test-situatie. Dit kan bijvoorbeeld het aanmaken van een `Card` zijn, of een `Deck`, of een bestandje `cards.txt`, of een verbinding met een database maken. Als je een fixture hebt geschreven, kan je die vervolgens in je tests gebruiken. Bijvoorbeeld zo:

    @pytest.fixture
    def ace_of_spades(Card):
        return Card(1, 's')

    def test_suit_name(ace_of_spades):
        assert ace_of_spades.suit_name() == "Spades"

Zie <https://docs.pytest.org/en/stable/how-to/fixtures.html#how-to-fixtures> voor een uitgebreidere uitleg en meer voorbeelden. 

</details>

## Inleveren

Lever hieronder de oude en de nieuwe implementatie, en ook de bijbehorende tests in.
Zorg dat bij het inleveren `from card import Card` bovenaan je testfile staat, zodat de **nieuwe** implementatie wordt gebruikt voor testen.
