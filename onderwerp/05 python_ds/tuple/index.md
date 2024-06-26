# Tuple

Python heeft meerdere ingebouwde datastructuren, zo ook een `tuple`. Dit is een datastructuur met een aantal bijzondere eigenschappen:

- Een tuple is onveranderbaar, eenmaal aangemaakt is het niet meer aan te passen.
- Een tuple is bedoeld om een vast aantal items bij elkaar te houden, bijvoorbeeld paren.

In de basis is een tuple hetzelfde als een list. Ze kennen beide een volgorde en indices. Het grote verschil is dat een tuple niet aan te passen is.

Zo maak je een tuple aan:

    lege_tuple = ()
    coordinaten = (3, 7)

Zo haal je een waarde op een index op:

    coordinaten[0] # geeft 3

Zo voeg je twee tuples samen in een nieuwe derde tuple:

    coordinaten_3d = coordinaten + (4,)

Tuples worden vaak gebruikt om verschillende informatie bij elkaar te houden. Iedere index in een tuple kan zijn eigen type hebben, zo is het type van `coordinaten` hierboven: `tuple[int, int]`. Uit het type kan je ook gelijk opmaken hoeveel elemenenten er in de tuple zitten.

<details markdown="1"><summary markdown="span">`(4,)`</summary>
Tuples gebruiken ronde haakjes, maar die ronde haakjes worden al op veel plekken gebruikt in Python. Daarom is er wat syntax nodig om ambiguiteit te voorkomen:

    lege_tuple = ()
    de_integer_4 = (4) # dit is een integer 4 tussen haakjes, bijvoorbeeld in een berekening
    tuple_met_1_element = (4,) # de komma is expliciet nodig om er een tuple van te maken

</details>

<details markdown="1"><summary markdown="span">`(1, 2, 3)` versus `1, 2, 3`</summary>
De ronde haakjes zijn optioneel, ook in het geval van tuples. Zo is onderstaande code hetzelfde:

    getallen = (1, 2, 3)
    getallen = 1, 2, 3

In sommige gevallen zijn de haakjes nodig om onderscheid te maken, bijvoorbeeld in:

    print((1, 2, 3)) # dit print de tuple: (1, 2, 3)
    print(1, 2, 3) # dit print de getallen: 1 2 3

Het is dan ook gebruikelijk om wel de haakjes te gebruiken, zo voorkom je fouten.

</details>

<details markdown="1"><summary markdown="span">`tuple[int, ...]`</summary>
Hoewel je bij een tuple iedere plek een type kan geven, zijn er ook situaties waar dat niet kan. Bijvoorbeeld bij tuples van onbekende grootte. Zoals in het volgende geval:

    lijst_van_getallen = [1, 2, 3, 4, 5, 6, 7, 8]
    tuple_van_getallen = tuple(lijst_van_getallen)

In dit geval wordt het type van de tuple: `tuple[int, ...]`.

</details>

### max_and_index

Schrijf een functie `max_and_index` in een bestand genaamd `tuples.py` die van een lijst aan getallen de maximum waarde en de index van de maximum waarde teruggeeft.

    def max_and_index(numbers: list[float]) -> tuple[float, int]:
        """
        Returns the maximum number in numbers and the index of that number.
        """

<details markdown="1"><summary markdown="span">Meerdere waardes returnen</summary>
Ook in Python kan een functie maar één keer één waarde returnen. Toch kan je op deze manier twee waardes returnen:

    return max, index

Hoewel het lijkt alsof er hier twee waardes worden teruggeven, wordt er eigenlijk een tuple aangemaakt van `max` en `index`. De haakjes van een tuple zijn namelijk optioneel. Conventie is dan ook dat als een functie meerdere verschillende waardes moet returnen, dat dit via een tuple gebeurt.
</details>


### items

Python dicts kennen een methode `items`. Deze methode geeft alle items (de keys en values) van een dictionary als een lijst van paren. Ieder paar is een tuple met op de eerste plek de key, en op de tweede de value.

Implementeer de volgende functie in een bestand genaamd `tuples.py`:

    def items[KT, VT](dictionary: dict[KT, VT]) -> list[tuple[KT, VT]]:
        """
        Returns a list of key-value tuples of all items in the dictionary. 
        """

