### Union

Python sets kennen een methode `union()`. Deze methode geeft een nieuwe set met alle elementen van twee andere sets.

Implementeer de volgende functie in een bestand genaamd `sets.py`:

    def union[A, B](set_a: set[A], set_b: set[B]) -> set[A | B]:
        """
        Returns a new set with all elements of set_a and set_b.
        """

Hier zijn pytest tests om de functie te testen. Plaats deze in `test_sets.py`:

    from sets import *

    def test_union():
        assert union({1, 2}, {3}) == {1, 2, 3}

    def test_union_overlap():
        assert union({1, 2}, {2, 3}) == {1, 2, 3}

    def test_union_empty():
        assert union({1, 2}, set()) == {1, 2}

    def test_union_completely_empty():
        assert union(set(), set()) == set()

    def test_union_different_types():
        assert union({"hello"}, {4, 5}) == {"hello", 4, 5}

<details markdown="1"><summary markdown="span">`set()` versus `{}`</summary>
De datastructuren `set`, `list`, `dict` en `tuple` kunnen allemaal aangemaakt worden via de gelijknamige functie, of door middel van haakjes. Alleen er zijn maar zoveel haakjes op je toetsenbord. Daarom gebruiken zowel set als dict de accolades (curly braces, `{}`). Daardoor ontstaat de vraag, is `{}` een lege set of een lege dict? In Python is `{}` een lege dict. De manier om een lege set aan te maken is via `set()`.
</details>

<details markdown="1"><summary markdown="span">generieke types A en B</summary>
De union van twee sets geeft een nieuwe set met daarin alle items van die twee sets. De resulterende set bevat dus ook alle types van de twee oorspronkelijke sets. Van te voren is niet bekend wat er in de twee sets zit, en dit kan ook verschillen van elkaar. Zo kan bijvoorbeeld `set_a` een `set[int]` zijn en `set_b` een `set[str]`. De resulterende set heeft in dit geval zowel `int` als `str`, oftewel `set[int | str]`. Maar omdat de types van te voren niet bekend zijn geven we het een generiek type, in dit geval `A` en `B`. Hierdoor kan Python en `mypy` achterhalen wat het type is van de uitkomst, op basis van waarmee de functie wordt aangeroepen.

    set1 = union({1, 2, 3}, {5.0, 2.0}) # geeft type set[int | float]
    set2 = union({1, 2, 3}, {"hello"}) # geeft type set[int | str]

Let op, om functies te maken met generieke type(s) moeten er blokhaakjes volgen na de functienaam met daarin de generieke types. Conventie is een enkele hoofdletter voor de generieke types. Deze syntax is nieuw in Python3.12.

</details>

<details markdown="1"><summary markdown="span">`set_a | set_b`</summary>
Omdat union een veelgebruikte operatie is bestaat er ook speciale syntax voor. Zo doen de volgende twee regels code precies hetzelfde:

    set_a.union(set_b)
    set_a | set_b

Let op, gebruik deze operatie natuurlijk niet bij het implementeren van deze opdracht. Dat keurt de check ook af. Na deze opdracht mag je natuurlijk wel gebruik maken van de ingebouwde union operatie.

</details>

### Intersection

Python sets kennen een methode `intersection()`. Deze methode geeft een nieuwe set met daarin alle elementen die zowel in de ene als de andere set zitten.

Implementeer de volgende functie in een bestand genaamd `sets.py`:

    def intersection[A, B](set_a: set[A], set_b: set[B]) -> set[A | B]:
        """
        Returns a new set with all elements that are both in
        set_a and set_b. In other words, this returns all the
        overlapping elements of set_a and set_b.
        """

Hier zijn pytest tests om de functie te testen. Plaats deze in `test_sets.py`:

    from sets import *

    def test_intersection():
        assert intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

    def test_no_intersection():
        assert intersection({1, 2, 3}, {4, 5, 6}) == set()

    def test_intersection_empty():
        assert intersection({2}, set()) == set()

    def test_intersection_completely_empty():
        assert intersection(set(), set()) == set()

    def test_intersection_different_types():
        assert intersection({1, "hello"}, {1}) == {1}

<details markdown="1"><summary markdown="span">`set_a & set_b`</summary>
Omdat intersection een veelgebruikte operatie is bestaat er ook speciale syntax voor. Zo doen de volgende twee regels code precies hetzelfde:

    set_a.intersection(set_b)
    set_a & set_b

Let op, gebruik deze operatie natuurlijk niet bij het implementeren van deze opdracht. Dat keurt de check ook af. Na deze opdracht mag je natuurlijk wel gebruik maken van de ingebouwde intersection operatie.

</details>

### Symmetric difference

Python sets kennen een methode `symmetric_difference()`. Deze methode geeft een nieuwe set met daarin alle elementen die alleen in één van de twee sets zitten.

Implementeer de volgende functie in een bestand genaamd `sets.py`:

    def symmetric_difference[A, B](set_a: set[A], set_b: set[B]) -> set[A | B]:
        """
        Returns a new set with all elements that are only in
        set_a or only in set_b. In other words, this returns
        all the non-overlapping elements of set_a and set_b.
        """

**TODO** Voeg minimaal vier pytest tests toe om de functie te testen. Kijk goed bij de eerdere tests voor inspiratie. Plaats deze tests ook in `test_sets.py`.

<details markdown="1"><summary markdown="span">`set_a & set_b`</summary>
Omdat symmetric_difference een veelgebruikte operatie is bestaat er ook speciale syntax voor. Zo doen de volgende twee regels code precies hetzelfde:

    set_a.symmetric_difference(set_b)
    set_a ^ set_b

Let op, gebruik deze operatie natuurlijk niet bij het implementeren van deze opdracht. Dat keurt de check ook af. Na deze opdracht mag je natuurlijk wel gebruik maken van de ingebouwde symmetric_difference operatie.

</details>

### Difference

Python sets kennen een methode `difference()`. Deze methode geeft een nieuwe set met daarin alle elementen die alleen in één set zitten (`set_a`), maar niet in de andere (`set_b`). Deze operatie is niet symmetrisch, dus alleen elementen uit `set_a` kunnen in de resulterende set komen.

    def difference[A, B](set_a: set[A], set_b: set[B]) -> set[A]:
        """
        Returns a new set with all elements that are only in
        set_a and not in set_b. In other words, this returns
        all the non-overlapping elements of set_a with set_b.
        """

**TODO** Voeg minimaal vier pytest tests toe om de functie te testen. Kijk goed bij de eerdere tests voor inspiratie. Plaats deze tests ook in `test_sets.py`.

<details markdown="1"><summary markdown="span">`-> set[A]`</summary>
Deze functie returned een set van het type `set[A]` omdat alleen elementen uit `set_a` in de resulterende set kunnen komen.
</details>

<details markdown="1"><summary markdown="span">`set_a & set_b`</summary>
Omdat difference een veelgebruikte operatie is bestaat er ook speciale syntax voor. Zo doen de volgende twee regels code precies hetzelfde:

    set_a.difference(set_b)
    set_a - set_b

Let op, gebruik deze operatie natuurlijk niet bij het implementeren van deze opdracht. Dat keurt de check ook af. Na deze opdracht mag je natuurlijk wel gebruik maken van de ingebouwde difference operatie.

</details>
