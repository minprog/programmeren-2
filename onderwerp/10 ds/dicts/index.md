# Dicts

Python heeft meerdere ingebouwde datastructuren, zo ook een `dict`. Dit is een datastructuur met een aantal bijzondere eigenschappen:

- Een dict onthoud combinaties van keys en values. Met een key kan een value worden opgehaald.
- Keys zijn allemaal uniek. Dit werkt op dezelfde manier als bij een `set`.
- Een dict kent geen volgorde\* en daarom zijn er ook geen plekken (indices).

Net zoals bij een `set` is het opzoeken van een key onafhankelijk van het aantal elementen in een dict. Dat is ook weer razendsnel.

Zo maak je een dict aan:

    empty_names = {}
    names = {"Martijn": "Stegeman", "Jelle": "van Assema"}

Zo haal je een value op:

    names["Martijn"] # Dit geeft: Stegeman

Zo voeg je een key en value toe aan een dict:

    names["Simon"] = "Pauw"

Zo verwijder je een key en bijbehorende value:

    names.pop("Simon")

Zo kijk je of een key in een dict zit:

    if "Martijn" in names:
        ...

Zo loop je over een dict heen:

    for first_name in names:
        last_name = names[first_name]

### get

Python dicts kennen een methode `get()`. Deze methode haalt een value op uit de dictionary op basis van een key. Er is één extra ding: zit de key niet in de dictionary, dan wordt een standaard waarde teruggeven.

**TODO** Implementeer de volgende functie in een bestand genaamd `dicts.py`

    def get[KT, VT](dictionary: dict[KT, VT], key: KT, default_value: VT | None=None) -> VT | None:
        """
        Returns a value belonging to the key. Returns default_value
        if the key is not in the dictionary.
        """

**TODO** Hier zijn pytest tests om de functie te testen. Plaats deze in `test_dicts.py`:

    from dicts import *

    def test_get():
        assert get({1: 2, 3: 4}, 1) == 2

    def test_get_missing():
        assert get({1: 2, 3: 4}, 0) == None

    def test_get_missing_default():
        assert get({1: 2, 3: 4}, 0, 0) == 0

    def test_get_empty():
        assert get({}, 1) == None

### values

Pythons dicts kennen een methode `values()`. Deze methode geeft "an object providing a view on D's values" terug. Voor deze opdracht doen we alsof dit een `list` is.

**TODO** Implementeer de volgende functie in een bestand genaamd `dicts.py`:

    def values[KT, VT](dictionary: dict[KT, VT]) -> list[VT]:
        """
        Returns all values from the dictionary as a list.
        """

**TODO** Hier zijn pytest tests om de functie te testen. Plaats deze in `test_dicts.py`:

    from dicts import *

    def test_values():
        assert values({1: 2, 3: 4}) == [2, 4]

    def test_values_empty():
        assert values({}) == []

    def test_values_duplicate():
        assert values({0: 2, 1: 2}) == [2, 2]

<details markdown="1"><summary markdown="span">\*\) Insertion ordered</summary>
Sinds python3.7 hebben dictionaries wel een volgorde: "insertion ordered". Oftewel de volgorde van het toevoegen blijft bewaard. Er is geen andere volgorde mogelijk, je kan een dictionary dus niet achteraf sorteren. Wel kan je een nieuwe dictionary aanmaken met gesorteerde keys en values door deze op volgorde toe te voegen.

Let op, sets hebben in tegenstelling tot dicts echt geen volgorde.

Zorg ervoor dat `values()` de values op volgorde van de dictionary in de lijst stopt. De volgende test moet dus slagen:

    assert values({1: 2, 3: 4}) == [2, 4]

</details>

<details markdown="1"><summary markdown="span">`keys()`</summary>
Naast values hebben dicts ook een keys methode. Deze methode geeft "a set-like object providing a view on D's keys" terug. Dit is een mogelijke implementatie:

    def keys[KT, VT](dictionary: dict[KT, VT]) -> set[VT]:
        """
        Returns all keys from the dictionary as a set.
        """
        return set(dictionary)

</details>

### count

Schrijf een functie `count` die alle waardes in een `list` telt. Het resultaat is een `dict` met de waardes van de `list` als keys en als values hoe vaak deze waardes voorkomen. Bijvoorbeeld

    >>> count(["hello", "world", "hello"])
    {"hello": 2, "world": 1}

**TODO** Implementeer de volgende functie in een bestand genaamd `dicts.py`:

    def count[V](values: list[V]) -> dict[V, int]:
        """
        Count the occurrences of each value.
        Returns a dict with the values as keys and
        the number of occurences as values.
        """

**TODO** Hier zijn alvast twee pytest tests om de functie te testen. Plaats deze in `test_dicts.py` en **voeg zelf nog twee tests toe**.

    def test_count_unique_values():
        assert count([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

    def test_count_mixed_types():
        assert count([1, 'a', 'b', 2.5]) == {1: 1, 'a': 1, 2.5: 1, 'b': 1}

<details markdown="1"><summary markdown="span">`from collections import Counter`</summary>
In Python bestaat standaard een module genaamd `collections`. Hierin vind je extra datastructuren voor wat specifiekere toepassingen. Eén van die datastructuren is [Counter](https://docs.python.org/3/library/collections.html#collections.Counter). Deze datastructuur is gemaakt om op een handige manier waardes te kunnen tellen en daar vervolgens mee te kunnen programmeren.

Achter de schermen is `Counter` zelf ook een `dict` en ook zo te gebruiken. Anders dan bij een `dict` zijn er operaties toegevoegd die handig zijn voor optellingen op tellen. Bijvoorbeeld twee tellingen bij elkaaris:

    >>> from collections import Counter
    >>> c = Counter(a=3, b=1)
    >>> d = Counter(a=1, b=2)
    >>> c + d
    Counter({'a': 4, 'b': 3})

Ook voegt `Counter` een aantal methodes toe zoals `most_common()` en `total()`.

</details>

### update

Python dicts kennen een methode `update()`. Deze methode update een dictionary met alle keys en values uit een andere dictionary.

**TODO** Implementeer de volgende functie in een bestand genaamd `dicts.py`:

    def update[KT, VT](dict_a: dict[KT, VT], dict_b: dict[KT, VT]) -> None:
        """
        Updates dict_a with all keys and values from dict_b.
        """

**TODO** Voeg minimaal vier pytest tests toe om de functie te testen. Kijk goed bij de eerdere tests voor inspiratie. Plaats deze tests ook in `test_sets.py`.
