# Lijst structuren

Je bent bezig met het ontwerp van een systeem waarin je persoonsdata (bijvoorbeeld klantgegevens) moet bijhouden. We modelleren personen met een `class` met daarin alle betreffende informatie. Voor deze opdracht is dat de volgende class:

    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

        def __repr__(self) -> str:
            return f"Person({self.name}, {self.age})"

Jouw taak is om een *container* class genaamd `PersonList` te ontwerpen waar al deze `Person` objecten in kunnen worden opgeslagen. Voor de rest van het systeem is het nodig dat jouw container class de volgende operaties ondersteunt:

- `append(person: Person) -> None` --- voegt een `Person` toe aan de collectie
- `pop() -> Person` --- verwijdert de eerste `Person` (de persoon wiens naam het eerst in het alfabet voorkomt) uit de collectie
- `lookup(name: str) -> Person` --- zoekt en geeft het object uit de collectie met de naam `name`
- `remove(name: str) -> bool` --- verwijdert een persoon uit de collectie met de naam `name`
- `as_sorted_list() -> list[Person]` --- geeft een lijst van alle personen gesorteerd op naam

In deze opdracht ga je drie verschillende versies maken die allemaal bovenstaande operaties ondersteunen, maar intern een andere structuur gebruiken om de data op te slaan.

## Implementatie 1: een gesorteerde list

Met klemtoon heb je te horen gekregen dat `as_sorted_list()` snel een gesorteerde lijst van personen moet kunnen produceren. Als het even kan in constante tijd graag (`O(1)`). Dus we gaan in `PersonList` een lijst **gesorteerd** bijhouden met alle personen erin. Als die lijst toch al bestaat is `as_sorted_list()` een eitje om te implementeren. Hier is starter code voor `PersonList`. Wij hebben `as_sorted_list()` alvast geïmplementeerd.

    class PersonList:
        def __init__(self):
            self._people: list[Person] = []

        def add(person: Person) -> None:
            raise NotImplementedError()

        def pop() -> Person:
            raise NotImplementedError()

        def lookup(name: str) -> Person:
            raise NotImplementedError()

        def remove(name: str) -> bool:
            raise NotImplementedError()
        
        def as_sorted_list() -> list[Person]:
            return self._people

Aan jou de taak om alle `raise NotImplementedError()`s weg te halen, en te implementeren. Zorg ervoor dat `self._people` altijd gesorteerd blijft op naam.


## Implementatie 2: een linked list

Niet al je collega's zijn helemaal tevreden met `PersonList`. Heel fijn dat `as_sorted_list` snel is, maar dat gebruiken ze toch bijna nooit. `pop()` daarentegen, die methode wordt pas vaak gebruikt. Kan je dat niet even in constante tijd maken in plaats van `as_sorted_list`.

Van programmeren 1 herinner je misschien nog: linked lists! Die zijn goed in elementen verwijderen en toevoegen aan het begin en eind van een lijst. Hier is een recap:

![embed](https://www.youtube.com/embed/wh4TS7RJDTA)

Implementeer weer `PersonList`, maar nu met een linked list. Je kan beginnen met onderstaande code. Hou de linked list op volgorde van naam.

    class Node:
        def __init__(self, person: Person, next: "Node" | None=None):
            self.person = person
            self.next = next

    class PersonLinkedList(PersonList):
        def __init__(self):
            self._head: Node | None = None

        def add(person: Person) -> None:
            raise NotImplementedError()

        def pop() -> Person:
            raise NotImplementedError()

        def lookup(name: str) -> Person:
            raise NotImplementedError()

        def remove(name: str) -> bool:
            raise NotImplementedError()
        
        def as_sorted_list() -> list[Person]:
            raise NotImplementedError()

> Zie je dat `PersonLinkedList` overerft van `PersonList`? Zo heeft `PersonLinkedList` dezelfde eigenschappen als `PersonList` en kan je `PersonLinkedList` overal gebruiken waar eerder een `PersonList` werd gebruikt. Dit mag nu ook van `mypy` :)


## Implementatie 3: dict en een linked list

Er is nog één obstakel volgens je collega's: `lookup` kost in beide implementaties te veel tijd. Kan dat niet in constante tijd?

`dict`s! Die kunnen opzoeken in (amortized) constante tijd. Alleen is er geen manier om een `dict` op volgorde van namen te houden. Dus doen we een combo achter de schermen, zowel een `dict` bijhouden om snel op te kunnen zoeken, als een `LinkedList` om de volgorde te bewaken. Dan slaan we data dubbel op, maar wordt `lookup` een stuk sneller.

Hier is een opzet:

    class Node:
        def __init__(self, person: Person, next: "Node" | None=None):
            self.person = person
            self.next = next

    class PersonDictList(PersonList):
        def __init__(self):
            self._head: Node | None = None

            # Een dictionary met als key de naam van een persoon en als value de persoon
            self._people: dict[str, Person] = {}

        def add(person: Person) -> None:
            raise NotImplementedError()

        def pop() -> Person:
            raise NotImplementedError()

        def lookup(name: str) -> Person:
            raise NotImplementedError()

        def remove(name: str) -> bool:
            raise NotImplementedError()
        
        def as_sorted_list() -> list[Person]:
            raise NotImplementedError()

## Vergelijken

Nu bestaan er drie implementaties van `PersonList`. Om je medeprogrammeurs te helpen kiezen, vragen we je een overzicht te maken van de voor- en nadelen. Vul deze tabel aan in een bestand genaamd `vergelijking.txt`:

| Operatie       | PersonList | PersonLinkedList | PersonDictList |
| -------------- | ---------- | ---------------- | -------------- |
| add            |            |                  |                |
| pop            |            | O(1)             | O(1)           |
| lookup         |            |                  | O(1)           |
| remove         |            |                  |                |
| as_sorted_list | O(1)       |                  |                |
