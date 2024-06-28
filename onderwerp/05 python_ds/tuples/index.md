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

Zo pak je een tuple uit in meerdere variabelen (unpacking):

    x, y, z = coordinaten_3d

Tuples worden vaak gebruikt om verschillende stukken informatie bij elkaar te houden. Iedere index in een tuple kan namelijk zijn eigen type hebben. Zo is het type van `coordinaten` hierboven: `tuple[int, int]`. Uit het type kan je ook gelijk opmaken hoeveel elemenenten er in de tuple zitten.

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

**TODO** Schrijf een functie `max_and_index` in een bestand genaamd `tuples.py` die van een lijst aan getallen de maximum waarde en de index van de maximum waarde teruggeeft.

    def max_and_index(numbers: list[float]) -> tuple[float, int]:
        """
        Returns the first maximum number in numbers and the index of that number.
        Precondition: len(numbers) > 0
        """

**TODO** Schrijf minimaal vier pytest test in een bestand genaamd `test_tuples.py` voor deze functie.

<details markdown="1"><summary markdown="span">Meerdere waardes returnen</summary>
Ook in Python kan een functie maar één keer één waarde returnen. Toch kan je op deze manier twee waardes returnen:

    return max, index

Hoewel het lijkt alsof er hier twee waardes worden teruggeven, wordt er eigenlijk een tuple aangemaakt van `max` en `index`. De haakjes van een tuple zijn namelijk optioneel. Conventie is dan ook dat als een functie meerdere verschillende waardes moet returnen, dat dit via een tuple gebeurt.
</details>


### items

Python dicts kennen een methode `items`. Deze methode geeft alle items (de keys en values) van een dictionary als een lijst van paren. Ieder paar is een tuple met op de eerste plek de key, en op de tweede plek de bijbehorende value.

**TODO** Implementeer de volgende functie in een bestand genaamd `tuples.py`:

    def items[KT, VT](dictionary: dict[KT, VT]) -> list[tuple[KT, VT]]:
        """
        Returns a list of key-value tuples of all items in the dictionary. 
        """

**TODO** Schrijf minimaal vier pytest test in een bestand genaamd `test_tuples.py` voor deze functie.

### enumerate

Python kent een functie [enumerate](https://docs.python.org/3/library/functions.html#enumerate). Deze functie neemt een itereerbare verzameling als argument. Dit is bijvoorbeeld een list, set, tuple of dict. Een datastructuur waarmee je met een for-loop over kan itereren. De functie returned vervolgens een list met op iedere plek een tuple. Iedere tuple bestaat uit twee waardes: de index (beginnend bij 0) en de waarde op die index.

**TODO** Implementeer de volgende functie in een bestand genaamd `tuples.py`:

    from typing import Iterable

    def enumerate[T](values: Iterable[T]) -> list[tuple[int, T]]:
        """
        Returns a list of tuples. Each tuple is a pair of an
        index (starting at 0) and a value at that index in values.
        """

**TODO** Schrijf minimaal vier pytest test in een bestand genaamd `test_tuples.py` voor deze functie.
 
<details markdown="1"><summary markdown="span">enumerate in Python</summary>
Python kent maar één vorm van een for-loop, een zogenaamde for-each loop. Je leest hem eigenlijk als: voor ieder (for each) element in een verzameling van elementen, doe iets. Nu zijn er situaties waarin dit voldoet, en er zijn situaties waarin je expliciet de index van een element nodig hebt in plaats van het element zelf. Vaak zie je daarom deze twee loops:

    # itereer over alle elementen in elements
    for element in elements:
        ...

    # itereer over de indices van elements
    for i in range(len(elements)):
        ...

Maar wat nou als je zowel de index als het element wilt? Daar is `enumerate` handig voor. Namelijk als volgt:

    for i, element in enumerate(elements):
        ...

Hierboven wordt tuple-unpacking, het uitpakken van een tuple in meerdere variabelen, op dezelfde regel van de for-loop gedaan. Daardoor heb je in één klap een variabele `i` met de index en een variabele `element` met het element op die index.
</details>

<details markdown="1"><summary markdown="span">geen `len(Iterable)`?</summary>
Een `Iterable` belooft alleen maar dat je erover kan itereren. Dit type doet geen verdere beloftes. Zo ook niet dat er voor een `Iterable` een lengte bestaat, want er bestaan ook itereerbare types zonder lengte. Dit zijn bijvoorbeeld oneindige verzamelingen, of verzamelingen waarvan de lengte niet van te voren bekend is. Om deze reden kan je niet via `len()` de lengte van een `Iterable` nemen. 

<details markdown="1"><summary markdown="span">Voor de nieuwsgierigen, hoe werkt dat nou zo'n oneindige verzameling? </summary>
Bijvoorbeeld een verzameling van alle gehele getallen tot in het oneindige:

    def all_positive_numbers():
        number = 0
        while true:
            yield number
            number += 1

    for number in all_positive_numbers():
        print(number)

        if number > 100:
            break

Bovenstaande werkt via een zogenaamde `generator`. Deze wordt hier aangemaakt door de functie `all_positive_numbers` en het speciale keyword `yield`. Zie het als een functie die tijdelijk returned bij `yield`, en bij een volgende aanroep weer verder gaat waar deze gebleven was. De functie `all_positive_numbers` genereert op die manier alle getallen vanaf 0 tot in het oneindige.

De for-loop zorgt ervoor dat de `generator` de getallen gaat genereren. Omdat de generator nooit stopt, hebben we zelf maar een `break` in de loop gezet.
</details>
</details>