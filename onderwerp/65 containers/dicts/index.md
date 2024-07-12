# Dictionary structuren

Python heeft een ingebouwde datastructuur genaamd `dict` om keys en values op te slaan. Handig, want zo kan je informatie aan elkaar koppelen:

    achternamen = {"Martijn": "Stegeman", "Nina": "van der Meulen"}
    print("Martijn {achternamen['Martijn']}")

In deze opdracht ga je zelf een `dict` implementeren. Op meerdere manieren, allereerst als een `dict` die alle types kan opslaan, maar die een stuk minder snel is. Daarna op basis van een hash table, zodat waardes ook snel kunnen worden opgehaald.

## 1. Nieuwe implementatie: ListDict

In de basis houdt een dictionary keys en values bij elkaar. Vervolgens kan op basis van een key een value worden opgezocht, toegevoegd, aangepast of worden verwijderd. Dit ga je implementeren in de vorm van een nieuwe class: `ListDict`. Om precies te zijn implementeer je de volgende methodes:

- `add(key: K, value: V) -> None` --- voegt een key en value toe
- `contains(key: K) -> bool` --- kijkt of een key in de datastructuur zit
- `get(key: K, default_value: V | None=None) -> V | None` --- haalt de bijbehorende value op
- `remove(key: Any) -> bool` --- haalt een key en value weg, als deze bestaat

Om de keys en values op te slaan gebruiken we een `list[tuple[K, V]]`. Het idee is om ieder key-value paar op te slaan in een `tuple[K, V]` en alle paren bij te houden in een `list`.

**TODO** Implementeer `ListDict` in `dicts.py`. Je kan met de volgende opzet beginnen:

    class ListDict[K, V]:
        def __init__(self):
            self._pairs: list[tuple[K, V]] = []

        def add(self, key: K, value: V) -> None:
            """
            Adds a new key-value pair to the dictionary. If the key already exists,
            its value is updated.

            Complexity: ...
            """
            raise NotImplementedError()

        def contains(self, key: K) -> bool:
            """
            Checks if the key exists in the dictionary.

            Complexity: ...
            """
            raise NotImplementedError()

        def get(self, key: K, default_value: V | None=None) -> V | None:
            """
            Returns the value associated with the key.

            Complexity: ...
            """
            raise NotImplementedError()

        def remove(self, key: K) -> bool:
            """
            Removes the key-value pair associated with the key. Returns True if the key was found and removed, otherwise returns False.

            Complexity: ...
            """
            raise NotImplementedError()


**TODO** De implementatie op basis van een lijst van paren is niet per se efficiënt. Geef in de docstring van elke methode de computationele complexiteit aan. Bijvoorbeeld:

   def add(self, key: Any, value: Any) -> None:
        """
        Complexity: O(n)
        """

## 2. StrDict

Het idee van een dictionary draait om het ophalen en opzoeken van een key. Praktisch alle operaties werken daarmee. Dat maakt de keuze voor een `list[tuple[K, V]]` wat ongelukkig, want dan moet continu de `list` worden doorzocht. Grote kans dat je bij `ListDict` een boel for-loops hebt gebruikt.

Nu een beter idee, stel we gebruiken nog steeds een `list` om alle paren (`tuple[K, V]`) op te slaan. Alleen dit keer kiezen we bewust waar ieder paar in de `list` wordt opgeslagen. Met als doel dat we deze vervolgens ook snel terug kunnen vinden. Stel, alle keys zijn tekst (van het type `str`), dan is één zo'n methode uit de echte wereld een archiefkast:

![archiefkast](file_cabinet.png)

Het idee van zo'n archiefkast is om in een la alleen documenten neer te leggen die beginnen met een bepaalde letter. Het voordeel daarvan is dat het terugvinden van een document een stuk sneller gaat, je hoeft namelijk alleen maar in één la te zoeken.

**TODO** Implementeer `StrDict` in `dicts.py` volgens het idee van een archiefkast. Je kan beginnen met onderstaande code. Kijk goed naar de gebruikte datastructuur, dit is nu een `list[list[tuple[str, V]]]` geworden. Dat is een lijst van 26 lijsten (één voor iedere letter van het alfabet). Ieder van deze lijsten moet vervolgens alleen key-values bevatten waarvan de key begint met dezelfde letter.

    class StrDict[V]:
        def __init__(self):
            self._filing_cabinet: list[list[tuple[str, V]]] = []

            # Add a drawer for every letter of the alphabet
            for i in range(26):
                self._filing_cabinet.append([])

        def add(self, key: str, value: V) -> None:
            """
            Adds a new key-value pair to the dictionary. If the key already exists,
            its value is updated.
            """
            raise NotImplementedError()

        def contains(self, key: str) -> bool:
            """
            Checks if the key exists in the dictionary.
            """
            raise NotImplementedError()

        def get(self, key: str, default_value: V | None=None) -> V | None:
            """
            Returns the value associated with the key.
            """
            raise NotImplementedError()

        def remove(self, key: str) -> bool:
            """
            Removes the key-value pair associated with the key. Returns True if the key was found and removed, otherwise returns False.
            """
            raise NotImplementedError()

> Je mag bij deze opdracht aannemen dat iedere key begint met een alfabetische letter.

<details markdown="1"><summary markdown="span">`ord("a")` geeft 97</summary>
In Python zijn karakters `str`s en daar kan je in tegenstelling tot C niet direct mee rekenen. Wel bestaat er de functie `ord`:

    ord(c)
        Return the Unicode code point for a one-character string.

Je kan deze zo gebruiken:

    >>> ord('A')
    65
    >>> ord('a')
    97

</details>

**TODO** Om het verschil in performance te zien draai je het onderstaande script `time_dicts.py`. Dat doe je met `python3 time_dicts.py`. Dit script voert al jouw geïmplementeerde dictionary methodes uit en meet de tijd die het kost. Je kan `NUM_ELEMENTS` en `REPEAT` aanpassen om te kijken wat de impact is van grotere en kleinere datastructuren.

<details markdown="1"><summary markdown="span">time_dicts.py</summary>
    from typing import Any, Protocol

    import copy
    import dicts
    import random
    import string
    import sys
    import time

    class DictLike[K, V](Protocol):
        def add(self, key: K, value: V) -> None: ...
        def contains(self, key: K) -> bool: ...
        def get(self, key: K, default_value: V | None=None) -> V | None: ...
        def remove(self, key: K) -> bool: ...

    # The number of elements in each Dict
    NUM_ELEMENTS = 10000

    # The number of times each timing function is run
    REPEAT = 10

    # Setup keys and values for testing
    KEYS = []
    for i in range(NUM_ELEMENTS):
        # Sample 5 random letters
        letters = random.sample(string.ascii_lowercase, 5)

        # Create a key of 5 letters and a unique index, ensuring each key is unique
        key = "".join(letters[:5]) + str(i)

        KEYS.append(key)

    VALUES = [f"value{i}" for i in range(NUM_ELEMENTS)]

    # Timing functions
    def time_add(d: DictLike[str, str]):
        for key, value in zip(KEYS, VALUES):
            d.add(key, value)

    def time_contains(d: DictLike[str, Any]):
        for key in KEYS:
            d.contains(key)

    def time_get(d: DictLike[str, Any]):
        for key in KEYS:
            d.get(key)

    def time_remove(d: DictLike[str, Any]):
        for key in KEYS:
            d.remove(key)

    if __name__ == "__main__":
        for dict_version in ["ListDict", "StrDict", "HashStrDict", "HashDict"]:
            # Test only the implemented dict versions
            if not hasattr(dicts, dict_version):
                continue

            # Create a Dict with all KEYS and VALUES
            dict_type = getattr(dicts, dict_version)
            dict_instance = dict_type()
            for key, value in zip(KEYS, VALUES):
                dict_instance.add(key, value)
            
            # Time each function
            for operation, time_function in [
                ("add", time_add),
                ("contains", time_contains),
                ("get", time_get),
                ("remove", time_remove)
            ]:
                print(f"Measuring {dict_version} {operation} time ({REPEAT} runs, {NUM_ELEMENTS} elements):", end="")
                sys.stdout.flush()

                times: list[float] = []

                for i in range(REPEAT):
                    # Setup a new dictionary with all KEYS and VALUES
                    d = copy.deepcopy(dict_instance)

                    # Shuffle the keys such that order of keys does not impact performance
                    random.shuffle(KEYS)

                    # Time the function
                    start_time = time.time()
                    time_function(d)
                    measured_time = time.time() - start_time

                    times.append(measured_time)

                print(f" {sum(times):.6f} seconds")
</details>

## 3. HashStrDict

Met `StrDict` heb je zonet een efficiëntere dictionary geïmplementeerd, maar wel met twee kanttekeningen:

* De computationele complexiteit van iedere operatie blijft hetzelfde als bij `ListDict`. In termen van big O, is alleen de hoogste factor relevant. Dat betekent dat `O(n)` gelijk is aan `O(n / 26)`. Want, als `n` gigantisch groot wordt, maakt het delen door 26 eigenlijk niet meer uit.
* De datastructuur werkt nu alleen nog maar voor strings, voorheen werkte het voor alle types.

Eerst de complexiteit, want in tegenstelling tot een fysieke archiefkast is het in een computer een stuk makkelijker om extra lades toe te voegen. Dus in plaats van 26 lades, laten we 26 x 26 = 676 lades gebruiken. Dan sorteren we niet alleen op eerste letter, maar op de eerste twee letters van iedere key. Zo wordt de datastructuur potentieel 676x sneller. Waarom daar stoppen, waarom niet:

* 26 x 26 x 26 = 17576 lades
* 26 x 26 x 26 x 26 = 456976 lades
* 26 x 26 x 26 x 26 x 26 = 11881376 lades
* ...

Je ziet het aantal lades hierboven exploderen. Hierin zit een afweging. Want hoe meer lades er zijn, hoe sneller de datastructuur, maar ook hoe meer geheugen er gebruikt wordt. Dus ergens zit een goede balans tussen snelheid en geheugen, tussen tijd en ruimte.

Daarnaast wordt niet iedere la evenveel gebruikt. Sterker nog, sommige lades zullen waarschijnlijk nooit gebruikt worden op de manier dat we ze nu indelen. Vrij weinig teksten beginnen met de letter combinaties als `xyz` of `qxv`. Zonde eigenlijk om daar een la voor te reserveren. Andersom worden sommige lades te veel gebruikt, bijvoorbeeld teksten die beginnen met `een` of `het`. Dat betekent dat die overvolle lades doorzocht moeten worden en dat gaat niet snel. Het zou beter zijn als we de gehele lading evenwichtiger kunnen verdelen.

In het geval van een dictionary zijn we op zoek naar een indelingsmethode die:

* Zo evenwichtig mogelijk verdeeld (zo uniform mogelijk)
* Zo min mogelijk botsingen veroorzaakt, oftewel zo min mogelijk waardes die in dezelfde la belanden
* Op zichzelf ook nog snel is. Want het doel is een snelle datastructuur, dus als deze methode dat in de weg zit schiet het niet op.

We zijn dus op zoek naar een goede functie die een `str`, onze key, omzet naar de index van een bepaalde la. Op zo'n manier dat diezelfde `str` door middel van diezelfde functie weer kan worden teruggevonden. In de informatica heet dit een hash-functie. Voor `StrDict` hierboven heb je eigenlijk de volgende hash functie geïmplementeerd:

    def hash_key(self, key: str) -> int:
        return ord(key[0].lower()) - ord('a') 

Nu is het jouw taak om een betere hash functie te schrijven. Eén die zoveel mogelijk spreidt en zo uniek mogelijke waardes genereert. Dat doe je door zoveel mogelijk informatie uit de invoer te halen en dit allemaal mee te nemen in de berekening. Denk bijvoorbeeld aan:

* De volgorde van de letters
* Het aantal letters
* De verschillende gebruikte letters
* ...

**TODO** Implementeer `HashStrDict` in `dicts.py`. Gebruik hierbij jouw nieuwe implementatie van `hash_key`. Kijk goed naar `self.number_of_drawers`. Bij deze implementatie is het aantal lades niet altijd `26`, maar wordt dit bepaald door deze variabele. Het staat je vrij om deze waarde te verhogen of te verlagen.

    class HashStrDict[V]:
        def __init__(self):
            self._filing_cabinet: list[list[tuple[str, V]]] = []
            self.number_of_drawers = 8192

            # Add all the drawers
            for i in range(self.number_of_drawers):
                self._filing_cabinet.append([])

        def hash_key(self, key: str) -> int:
            """
            Hashes the key and returns a number between 0 and self.number_of_drawers - 1.
            """
            raise NotImplementedError()

        def add(self, key: str, value: V) -> None:
            """
            Adds a new key-value pair to the dictionary. If the key already exists,
            its value is updated.
            """
            raise NotImplementedError()

        def contains(self, key: str) -> bool:
            """
            Checks if the key exists in the dictionary.
            """
            raise NotImplementedError()

        def get(self, key: str, default_value: V | None=None) -> V | None:
            """
            Returns the value associated with the key.
            """
            raise NotImplementedError()

        def remove(self, key: str) -> bool:
            """
            Removes the key-value pair associated with the key. Returns True if the key was found and removed, otherwise returns False.
            """
            raise NotImplementedError()

> **Tip:** gebruik `% self.number_of_drawers` (modulo) om ervoor te zorgen dat de uitkomst van `hash_key` nooit groter kan zijn dan het aantal lades.

<details markdown="1"><summary markdown="span">Extra achtergrond: cryptografische hash functies</summary>
Een hash functie wordt o.a. gebruikt voor een `dict` in Python, maar kent nog andere toepassingen. Zo bestaan er ook cryptografische hash-functies. Dat zijn functies die bedoeld zijn om informatie om te zetten op zo'n manier, dat de informatie nog wel te herkennen is, maar niet terug te leiden.

Dat zit zo. Een hash functie neemt een variërende hoeveelheid informatie binnen en geeft een vaste hoeveelheid informatie terug. Bij `HashStrDict` gaan we van een `str` van onbekende grootte naar een `int` van bekende grootte (niet groter dan `self.number_of_drawers`). Dat betekent dat we van veel informatie, veel 0-en en 1-en, naar een vast aantal 0-en en 1-en gaan. Hierbij gaat dus sowieso informatie verloren. Omdat die informatie verloren gaat, kunnen we niet meer terug. Het valt niet te herleiden wat de input van de hash-functie was op basis van de output. In zekere zin heb je zo éénrichtingsverkeer, je kan wel van input naar output, maar niet van output naar input.  

Dat is een handige eigenschap als je bijvoorbeeld moet omgaan met gevoelige informatie, zoals wachtwoorden van mensen. Je wilt wel het wachtwoord kunnen herkennen, zodat een persoon kan inloggen in jouw systeem bijvoorbeeld, maar het wachtwoord zelf sla je liever niet op. Want zodra je het wachtwoord opslaat, loop je ook het risico dat deze wordt buitgemaakt. Hier kun je ervoor kiezen om het wachtwoord te hashen en alleen de hash te onthouden. Probeert een gebruiker later in te loggen, dan hash je het ingevoerde wachtwoord opnieuw en kijk je of het overeenkomt. Zo weet je of het wachtwoord correct was, of niet. Om deze reden zie je vaak dat je een wachtwoord wel kan resetten op een website, maar dat je nooit je eigen wachtwoord kan opvragen.

</details>

## 4. HashDict

Met `HashStrDict` heb je een implementatie die, gegeven genoeg buckets, een constante computationele complexiteit heeft*. Kort gezegd, het opzoeken van een key is nu onafhankelijk van hoeveel keys er in de datastructuur zitten. Deze datastructuur heeft een eigen naam: een hash table. Dit is tabel waarin waardes worden opgeslagen en opgehaald op basis van een hash-functie. 

Nu knaagt er nog één ding, want de datastructuur werkt nog steeds alleen voor strings. Om de datastructuur te laten werken voor andere types zijn er hash functies nodig voor die types, en hoe doe je dat dan voor alle mogelijke types? Het antwoord is: niet. 

Omdat hash-functies moeten werken met de eigenschappen van de data, moeten deze toegespitst zijn op die data. Daarom zitten hash functies in Python ingebakken voor de meeste datastructuren. Zodat je zelf het wiel niet opnieuw hoeft uit te vinden voor iedere datastructuur. In Python bestaat er een functie `hash()` die je zo kan gebruiken:

    >>> hash("hello")
    930135635216851552
    >>> hash((1, 2, 3))
    529344067295497451
    >>> hash(42.9)
    2075258708292321322
    >>> hash(42)
    42

**TODO** Implementeer `HashDict` in `dicts.py`.

    class HashDict[K, V]:
        def __init__(self):
            self._filing_cabinet: list[list[tuple[K, V]]] = []
            self.number_of_drawers = 8192

            # Add all the drawers
            for i in range(self.number_of_drawers):
                self._filing_cabinet.append([])

        def hash_key(self, key: K) -> int:
            """
            Hashes the key and returns a number between 0 and self.number_of_drawers - 1.
            """
            return abs(hash(key)) % self.number_of_drawers

        def add(self, key: K, value: V) -> None:
            """
            Adds a new key-value pair to the dictionary. If the key already exists,
            its value is updated.
            """
            raise NotImplementedError()

        def contains(self, key: K) -> bool:
            """
            Checks if the key exists in the dictionary.
            """
            raise NotImplementedError()

        def get(self, key: K, default_value: V | None=None) -> V | None:
            """
            Returns the value associated with the key.
            """
            raise NotImplementedError()

        def remove(self, key: K) -> bool:
            """
            Removes the key-value pair associated with the key. Returns True if the key was found and removed, otherwise returns False.
            """
            raise NotImplementedError()

**TODO** Draai weer het script `time_dicts.py` om de performance van alle implementaties te zien. Hoe veel sneller is `HashDict` t.o.v. `ListDict`?

<details markdown="1"><summary markdown="span">!!!Performance spoilers!!!</summary>

Onderstaande output is het resultaat van onze implementatie van `dicts.py` gedraaid op een laptop uit het jaar 2022. Het precieze aantal secondes zal verschillen per laptop en per implementatie.

    Measuring ListDict add time (10 runs, 10000 elements): 12.143245 seconds
    Measuring ListDict contains time (10 runs, 10000 elements): 12.554064 seconds
    Measuring ListDict get time (10 runs, 10000 elements): 6.366691 seconds
    Measuring ListDict remove time (10 runs, 10000 elements): 6.021173 seconds
    Measuring StrDict add time (10 runs, 10000 elements): 0.454954 seconds
    Measuring StrDict contains time (10 runs, 10000 elements): 0.650468 seconds
    Measuring StrDict get time (10 runs, 10000 elements): 0.351192 seconds
    Measuring StrDict remove time (10 runs, 10000 elements): 0.233366 seconds
    Measuring HashStrDict add time (10 runs, 10000 elements): 0.074487 seconds
    Measuring HashStrDict contains time (10 runs, 10000 elements): 0.100431 seconds
    Measuring HashStrDict get time (10 runs, 10000 elements): 0.061881 seconds
    Measuring HashStrDict remove time (10 runs, 10000 elements): 0.068862 seconds
    Measuring HashDict add time (10 runs, 10000 elements): 0.037003 seconds
    Measuring HashDict contains time (10 runs, 10000 elements): 0.058676 seconds
    Measuring HashDict get time (10 runs, 10000 elements): 0.020885 seconds
    Measuring HashDict remove time (10 runs, 10000 elements): 0.027347 seconds

Grof gezegd is op deze ene test case `HashDict` maar liefst ~300x sneller dan `ListDict`.

</details>

<details markdown="1"><summary markdown="span">unhashable type: list, set and dict</summary>
De ingebouwde `hash` functie werkt voor bijna ieder ingebakken datastructuur, behalve datastructuren die kunnen veranderen zoals `list`, `set` en `dict`. Dan krijg je deze error te zien:

    >>> hash([1, 2, 3])
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'

Omdat een hash-functie een berekening doet over alle informatie in de datastructuur, werkt dit idee niet goed voor datastructuren die kunnen veranderen. Want stel, we zijn eigenwijs en maken toch een hash functie voor een list, bijvoorbeeld:

    def hash_list(values: list) -> int:
        hash_value = 0
        for value in values:
            hash_value += hash(value)
        return hash_value

Dan gebeurt er iets eigenaardigs:

    >>> values = [1, 2, 3]
    >>> hash_list(values)
    6
    >>> values.append(4)
    >>> hash_list(values)
    10

Dezelfde lijst in dezelfde variabele levert na het toevoegen van de waarde `4` een andere hash waarde op. Zou deze lijst eerder zijn toegevoegd aan een dictionary, dan kan diezelfde lijst nooit meer worden teruggevonden na het toevoegen van de waarde `4`. Om deze reden is er in Python besloten om veranderbare datastructuren `unhashable` te maken. Je kan ze dus ook niet gebruiken als key in een `dict`.
</details>

<details markdown="1"><summary markdown="span">Worst case versus Average case*</summary>
`HashStrDict` en `HashDict` hebben strikt genomen nog een worst case complexiteit van `O(n)`. Het is niet uit te sluiten dat er botsingen optreden en dat er daardoor alsnog lineair gezocht moet worden naar een specifieke key in een la die afhangt van `n`. 

Het grote verschil zit hem in de gemiddelde complexiteit: dat is de tijd van alle operaties opgeteld, gedeeld door het aantal operaties. Deze is nu wel O(1). De gemiddelde key zal (gegeven genoeg lades) zich niet bevinden in een la met andere keys.
</details>

<details markdown="1"><summary markdown="span">`hash` vs `__hash__`</summary>
De verschillende hash functies zijn specifiek geïmplementeerd voor iedere datastructuur d.m.v. een methode genaamd `__hash__`. Kijk maar:

    >>> hash("hello")
    930135635216851552
    >>> "hello".__hash__()
    930135635216851552

Het enige wat de `hash()` functie dus doet, is `.__hash__()` aanroepen op het argument. Eigenlijk dus:

    def hash(value):
        return value.__hash__()

De reden dat dit zo werkt is zodat jij als programmeur nieuwe datastucturen ook hashable kan maken. Stel we ontwikkelen een class voor namen (`Name`), dan is deze hashable zodra we er een `__hash__()` methode voor implementeren:

    class Name:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __hash__(self):
            return hash(self.first_name) + hash(self.last_name)

Door dit te doen kan je je eigen class `Name` gebruiken in een `dict`:

    >>> name = Name("John", "Doe")
    >>> names_age_dict: dict[Name, int] = {}
    >>> names_dict[name] = 27

</details>
