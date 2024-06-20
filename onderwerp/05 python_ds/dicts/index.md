# Dicts

Python heeft meerdere ingebouwde datastructuren, zo ook een `dict`. Dit is een datastructuur met een aantal bijzondere eigenschappen:

- Een dict onthoud combinaties van keys en values. Met een key kan een value worden opgehaald.
- Keys zijn allemaal uniek. Dit werkt op dezelfde manier als bij een `set`.
- Een dict kent geen volgorde en daarom zijn er ook geen plekken (indices).\*

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

<details markdown="1"><summary markdown="span">`names["Martijn"]` versus `names.get("Martijn")`</summary>
Naast de blokhaakjes kan je ook gebruik maken van de `.get()` methode. De blokhaakjes geven een error als de key niet in de dictionary zit, bijvoorbeeld: `KeyError: 'Martijn'`. De `.get()` methode geeft in het geval van een missende key de waarde `None` terug. `.get()` neemt een optioneel tweede argument, wordt de key niet gevonden, dan wordt dit tweede argument teruggeven.

    names["John"] # gooit een KeyError: 'John'
    names.get("John") # returned None
    names.get("John", "Missing") # returned "Missing"

</details>
