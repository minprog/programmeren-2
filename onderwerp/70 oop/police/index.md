# Politie

Afgelopen zondagnacht is uit een museum het schilderij *De Gouden Kater* gestolen. Er zijn geen sporen van braak, geen getuigen en geen camerabeelden. Wat de politie wel heeft is een lijst met contacten tussen verdachten: wie mailde, belde of sprak met wie. Alle gegevens liggen op tafel, maar niemand heeft ze nog kunnen ordenen.

Aan jou de taak om dat te doen. Jij zoekt uit wie de sleutelpersonen zijn, welke groepen er bestaan en hoe informatie door dit netwerk reist. Onderweg verzamel je aanwijzingen. Wie zit er achter de diefstal?

Om dit te kunnen doen ga je het netwerk modelleren als een graaf. Dit is een verzameling van nodes (personen) en edges (contacten tussen personen). Met behulp van dit model kun je vervolgens analyseren wie met wie in verbinding staat, hoe informatie zich kan verspreiden, en welke personen of groepen een centrale rol spelen binnen het netwerk.

Bijvoorbeeld, gegeven de volgende informatie:

    Alice belt Bob
    Diana emailt Charlie
    Diana emailt Alice
    Diana ontmoet Charlie
    Bob ontmoet Charlie
    Bob belt Alice
    Charlie belt Eve

Zijn er 5 unieke personen en daarom 5 nodes. Deze nodes zijn verbonden via 7 edges waarvan 5 uniek. De graaf die hieruit vormt kan er zo uitzien:

       Alice
       /   \
     Bob   Diana
       \   /
       Charlie
          |
         Eve

In dit schema:

* Nodes = namen (personen).
* Edges = lijntjes (contacten).

## Stap 1: Node en Edge

Implementeer in een bestand genaamd `police.py` de class `Node` en `Edge`:

    class Node:
        def __init__(self, name: str) -> None:
            pass

        def __repr__(self) -> str:
            """
            Represent the node as a string in the form of: "Alice"
            """
            pass

        @property
        def edges(self) -> "list[Edge]":
            pass

        def add_edge(self, edge: "Edge") -> None:
            pass

Hier staat een `@property` bij de methode `edges`. Dit betekent dat de methode kan worden aangeroepen zonder gebruik van haakjes, alsof het een normale property (attribuut) is van het object.

    class Edge:
        def __init__(self, node1: Node, node2: Node) -> None:
            pass

        def __repr__(self) -> str:
            """
            Represent the edge as a string in the form of: "Alice - Bob"
            """
            pass

        @property
        def node1(self) -> Node:
            pass

        @property
        def node2(self) -> Node:
            pass

        def other(self, node: Node) -> Node:
            """
            Returns the other node in the edge.
            Raises ValueError if node is not part of this edge.
            """
            pass


## Stap 2: Graph

Implementeer nu de klasse `Graph`:

    class Graph:
        def __init__(self) -> None:
            pass

        def __repr__(self) -> str:
            """
            Represent the graph as a string in the form of:
            Alice - Bob
            Diana - Charlie
            Diana - Alice
            """

        def add_person(self, name: str) -> None:
            """
            Add a person (Node) to the Graph.
            """
            pass

        def add_contact(self, name1: str, name2: str) -> None:
            """
            Add a connection between two people (Edge) to the graph.
            """
            pass

        @property
        def all_people(self) -> list[Node]:
            pass

        @property
        def all_contacts(self) -> list[Edge]:
            pass

## Stap 3: load_from_file

Bij deze opdracht zijn er twee data bestanden:

* small_contacts.csv
* contacts.csv

Deze bestanden download je [hier](https://github.com/minprog/programmeren-2/raw/refs/heads/2026/onderwerp/70%20oop/police/contacts.zip). Kijk even goed in de bestanden om te zien hoe het in elkaar steekt.

Implementeer nu de methode `load_from_file`:

    @staticmethod
    def load_from_file(filename: str) -> Graph:
        """
        Reads contacts from file and creates a graph.
        """
        graph = Graph()

        with open(filename) as f:
            pass

`load_from_file` is een `staticmethod`. Dit is een methode die geen instantie (object) van de class nodig heeft. Er is dus ook geen `self`. Wel zo logisch, want wat deze methode juist gaat doen is een nieuwe `Graph` aanmaken.

Eenmaal geïmplementeerd zou het volgende moeten werken:

    $ python -i police.py
    >>> graph = Graph.load_from_file("small_contacts.csv")
    >>> graph
    Alice - Bob
    Bob - Charlie
    Charlie - Alice
    >>> graph.all_people
    [Alice, Bob, Charlie]
    >>> graph.all_contacts
    [Alice - Bob, Alice - Charlie, Bob - Charlie]

## Vraagstukken

### Wie heeft de meeste contacten en wie zijn die contacten?

*Aanwijzing 1: een meesterbrein houdt de touwtjes in handen, en heeft dus contact met bijna iedereen. Wie is dat, en met wie praat diegene?*

Voeg de volgende twee methodes toe aan Graph om je te helpen bij deze vraag.

    def get_most_contacts(self) -> Node:
        """
        Returns the person with the most contacts.
        If there are multiple, returns one of them.
        """
        pass

    def get_direct_contacts(self, name: str) -> list[Node]:
        """
        Returns a list of direct contacts for the given person.
        Raises a ValueError if name is not in graph.
        """
        pass

### Is er indirect contact?

*Aanwijzing 2: slimme criminelen laten zich niet met elkaar zien. Toch moet informatie ergens doorheen zijn gegaan. Wie zijn de tussenpersonen?*

Implementeer hiervoor de methode:

    def get_indirect_contacts(self, name: str) -> list[Node]:
        """
        Returns all nodes with which the given name has indirect contact (not direct).
        """

### Welke criminele groepen zijn er?

*Aanwijzing 3: niet iedereen op de lijst is betrokken. Welke groepen horen bij de bende, en welke zijn alleen toevallig in beeld gekomen?*

Een groep is een afgesloten stuk van de graaf. Zo kent de volgende graaf twee groepen:

       Alice
       /   \
     Bob   Diana
       \   /
       Charlie   George
          |        |
         Eve      Fred - Hope

Implementeer hiervoor:

    def get_groups(self) -> list[set[Node]]:
        """Returns the groups (set[Node]) of the graph."""
        pass

### Tot welke driehoeken hoort Luca?

*Aanwijzing 4: de kern van een bende is meestal een kleine kring die elkaar blind vertrouwt. Wie zit er bij Luca in de binnenste kring?*

Een driehoek is een groep van drie personen die allemaal contact met elkaar hebben. Hieronder bijvoorbeeld zijn er twee driehoeken (Alice, Bob, Diana) en (Bob, Diana, Charlie).

       Alice
       /   \
     Bob - Diana
       \   /
       Charlie
          |
         Eve

Implementeer:

    def get_triangles(self, name: str) -> list[set[Node]]:
        """
        Returns all groups consisting of three connected
        persons of which name is a part.
        """

## Stap 4: Zaak gesloten

Je hebt nu alle aanwijzingen. Tijd om ze te combineren en de dader aan te wijzen. Implementeer:

    def find_culprit(self) -> Node:
        """
        Returns the person who stole the painting.
        """
        pass

De dader is als volgt te herkennen:

* Het **brein** achter de diefstal is de persoon met de meeste contacten.
* De dader heeft **geen direct contact** met het brein, maar zit wel in **dezelfde groep**.
* Het brein laat alles lopen via de **binnenste kring**: de personen die met het brein in een **driehoek** zitten.
* Van alle personen die aan bovenstaande eisen voldoen, is de dader degene met de meeste directe contacten in die binnenste kring.

Gebruik voor de oplossing de methodes die je eerder hebt gemaakt: `get_most_contacts`, `get_direct_contacts`, `get_indirect_contacts`, `get_groups` en `get_triangles`. Roep je `find_culprit` aan op de graaf van `contacts.csv`, dan krijg je de dader terug.

<details markdown="1"><summary markdown="span">Onthul de dader (spoilers!)</summary>

Alleen kijken als je de code hebt ingeleverd! Het brein is **Luca**, met 14 contacten de spil van het netwerk. De dader is **Wiebe**: geen direct contact met Luca, maar wel contact met vijf personen uit Luca's binnenste kring (Alejandro, Jelle, Nikolai, Peter en Rick). Rik, Roger, Sien, Kim, Marit, Jonathan en Sjoerd zitten in kleine losse groepjes en hebben er niets mee te maken.
</details>
