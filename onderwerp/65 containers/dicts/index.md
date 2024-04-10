# Dictionary structuren

Python heeft een ingebouwde datastructuur genaamd `dict` om keys en values op te slaan. Heel handig, want zo kan je informatie aan elkaar koppelen, en ook zeer snel opzoeken en ophalen:

    achternamen = {"Martijn": "Stegeman", "Nina": "van der Meulen"}
    print("Martijn {achternamen['Martijn']}")

Achter de schermen gebruikt Python een hash-table om deze waardes op te slaan en op te zoeken. Hier is een korte recap:

![embed](https://www.youtube.com/embed/btT4bCOvqjs)

Een hash table gebruikt een hash-functie om waardes op een bepaalde plek op te slaan. In het filmpje hierboven is dat de eerste letter van ieder woord (de key). Python's `dict` werkt op dezelfde manier. Er is een namelijk ingebouwde functie genaamd `hash` die bepaald waar een waarde wordt opgeslagen. 

    $ python3
    >>> hash("hello")
    1904666118889457047

Alleen deze functie heeft limitaties, want deze werkt niet voor types die kunnen veranderen. Zoals bijvoorbeeld `list`s:

    $ python3
    >>> hash([1, 2, 3])
    -1904666118889457047
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

Dit is een ontwerpkeuze binnen Python zelf. Want veranderbare waardes zoals een `list` zouden na een verandering een andere `hash` waarde opleveren. Zou je in het voorbeeld van het filmpje de eerste letter van iemands naam veranderen, dan kan je die persoon niet meer terugvinden in de hash table.


## 1. Nieuwe implementatie: AnyDict

Stel we willen toch een dictionary die alle types als keys accepteert: `AnyDict`. Aan jou de taak om deze te maken. De concrete implementatie moet een **lijst van paren** zijn, ieder paar is een tuple van een key en een value. De AST moet de volgende operaties implementeren:

- `add(key: Any, value: Any) -> None` --- voegt een key en value toe
- `contains(key: Any) -> bool` --- kijkt of een key in de datastructuur zit
- `lookup(key: Any) -> Any` --- haalt de bijbehorende value op
- `remove(key: Any) -> bool` --- haalt een key en value weg, als deze bestaat

Je kan met de volgende opzet beginnen:

    from typing import Any

    class AnyDict:
        def __init__(self):
            self._pairs: list[tuple[Any, Any]] = []

        def add(key: Any, value: Any) -> None:
            raise notImplementedError()

        def contains(key: Any) -> bool:
            raise notImplementedError()

        def lookup(key: Any) -> Any:
            raise notImplementedError()

        def remove(key: Any) -> bool:
            raise notImplementedError()


## 2. Efficientie?

Deze implementatie op basis van een lijst is niet per se efficiënt. Een hash table zou veel efficiënter zijn. Geef in de docstring van elke methode een analyse van de efficiëntie. 


## 3. Tests

Schrijf in een apart bestand `pytest` tests voor `AnyDict`. 
