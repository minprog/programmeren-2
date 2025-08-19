# Politie

De politie is een onderzoek gestart naar een potentieel crimineel netwerk. Daarbij is in kaart gebracht welke personen contact onderhouden met elkaar via e-mail, telefoon en persoonlijke ontmoetingen. Aan jou de taak om dit netwerk te analyseren en ervoor te zorgen dat de politie hun aandacht richt op de juiste verdachten. Jij onderzoekt wie de sleutelpersonen zijn in het netwerk, welke groepen er bestaan en hoe informatie of invloed zich door dit netwerk verspreidt.

Om dit te kunnen doen ga je het netwerk modelleren als een graaf. Dit is een verzameling van nodes (personen) en edges (contacten tussen personen). Met behulp van dit model kun je vervolgens analyseren wie met wie in verbinding staat, hoe informatie zich kan verspreiden, en welke personen of groepen een centrale rol spelen binnen het netwerk.

Bijvoorbeeld, gegeven de volgende informatie:

    Alice belt Bob
    Diana emailt Charlie
    Diana emailt Alice
    Diana ontmoet Charlie
    Bob ontmoet Charlie
    Bob belt Alice
    Charlie belt Eva

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

### Stap 1: Node en Edge

Implementeer in een bestand genaamd `politie.py` de volgende klasses:

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


### Stap 2: Graph

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

### Stap 3: load_graph

Bij deze opdracht zijn er een drietal data bestanden:

    * small_contacts.csv
    * medium_contacts.csv
    * large_contacts.csv

> TODO fix DL

Deze bestanden download je [hier](/). Kijk even goed in de bestanden om te zien hoe het in elkaar steekt.

Implementeer nu de functie `load_graph`:

    def load_graph(filename: str) -> Graph:
        """
        Reads contacts from file and creates a graph. 
        """

Eenmaal geïmplementeerd zou het volgende moeten werken:

    $ python -i politie.py
    >>> graph = load_graph("small_contacts.csv")
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

Hebben de volgende verdachten contact gehad?

* Luca en Akira
* Roel en Ivan
* Marco en Peter
* Hugo en Erik

Implementeer hiervoor de methode:

    def has_indirect_contact(self, name1: str, name2: str) -> bool:
        """
        Returns True if name1 has had contact with name2
        """

### Hoeveel criminele groepen zijn er?

Een groep is een afgesloten stuk van de graaf. Zo kent de volgende graaf twee groepen:

       Alice
       /   \
     Bob   Diana
       \   /
       Charlie   George
          |        |
         Eve      Fred - Hope

Implementeer hiervoor:

    def count_groups(self) -> int:
        """Return the number of groups in the graph."""
        pass

### Criminele driehoeken

Tot welke driehoeken hoort Luca? Een driehoek is een groep van drie personen wie allemaal contact met elkaar hebben.

Implementeer:

    def get_triangles(self, name: str) -> list[set[Node]]:
        """
        Returns all groups consisting of three connected
        persons of which name is a part.
        """

### Welke maximale cliques zijn er?

Een clique is een verzameling van personen die allemaal contact met elkaar hebben. Een maximale clique is een clique waaraan niemand kan worden toegevoegd. Zo kent de volgende graaf drie maximale cliques (Alice, Bob en Diana), (Bob, Diana en Charlie) en (Charlie en Eve).

       Alice
       /   \
     Bob - Diana
       \   /
       Charlie
          |
         Eve

Om dit uit te zoeken kan je gebruik maken van het volgende algoritme:

1. Begin met een groep voor elke persoon.
2. Voor elke groep, kijk naar alle personen die contact hebben met iemand in de groep.
    * Heeft deze persoon contact met alle personen in de groep?
        * Maak een nieuwe groep met iedereen uit de originele groep plus deze persoon.
3. Stop als je niemand meer kunt toevoegen: Als je geen nieuwe mensen meer kunt toevoegen aan je groep, dan heb je een groep gevonden waarin iedereen met elkaar praat.
4. Kon je wel iemand toevoegen aan de groep? Dan is de groep niet maximaal en kun je deze verwijderen.
5. Herhaal voor alle groepen: Herhaal dit proces totdat al je groepen maximaal zijn.
6. Verwijder duplicate cliques.

> Bovenstaand algoritme is geïnspireerd door het [Bron-Kerbosch algoritme](https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm)