# List structures

Je bent bezig met het ontwerp van een systeem waarin je informatie moet bijhouden over een groot aantal personen (bijvoorbeeld klantgegevens). Elke persoon is in dat systeem een object met daarin de betreffende informatie.

Jouw specifieke taak is om een *container* class te ontwerpen waarin al deze objecten in kunnen worden opgeslagen. Daarbij is de vraag om de volgende operaties te ondersteunen:

- `add(person)` --- voegt een `person` toe aan de collectie
- `remove(name)` --- verwijdert een persoon uit de collectie met de naam `name`
- `lookup(name)` --- zoekt en geeft het object uit de collectie met de naam `name`
- `list_all` --- geeft een lijst van alle objecten gesorteerd op naam

Nu heb je de keuze uit een aantal *onderliggende* structuren om de data in op te slaan.

1. Je kunt de objecten opslaan in een standaard Python-lijst in de volgorde waarin ze zijn aangemaakt
2. Je kunt de objecten opslaan in een standaard Python-lijst die altijd gesorteerd is op naam
     * **"Altijd gesorteerd" betekent dat na het invoegen van een element de interne lijst nog steeds gesorteerd is, het invoegen moet dus op de "juiste" plek gebeuren.**
     * **Als je een lijst hebt met elementen `[1,4,5]` en je voegt `3` in, dan moet de lijst daarna `[1,3,4,5]` zijn, en niet `[1,4,5,3]` zoals wanneer je append gebruikt.**
3. Je kunt de objecten opslaan in een standaard Python-dictionary die de naam als key gebruikt

Het gaat er bij deze opdracht om dat je begrijpt hoe je een specialistische datastructuur kunt bouwen door intern een standaard Python-structuur te bouwen. Je gaat geen code schrijven maar redeneren op basis van een idee over welke Python-operaties je nodig zou hebben om je eigen structuur te implementeren.

Geef nu voor elk van de drie opties een analyse van de efficientie van alle operaties die ondersteund moeten worden. Beschrijf daarbij het algoritme/de operaties die je zou gebruiken om die efficientie te bereiken. Als je bijvoorbeeld de methode `append` voor een lijst wil gebruiken is deze O(1). De theoretische Big-O efficientie voor bijna alle Python-structuren vind je op de [Python wiki over TimeComplexity](https://wiki.python.org/moin/TimeComplexity).

Zoek uiteindelijk naar algoritmes die het meest efficient werken, gegeven de keuze voor een Python-structuur en de mogelijkheden die deze biedt.

## Lijst 1

Beschrijf hier voor optie 1 de efficientie van de add, remove, lookup en list\_all-operaties, met daarbij een uitleg van hoe je elke operatie zou moeten implementeren.

Als voorbeeld: voor `add` zou je hier de `append` operatie van de Python list gebruiken, omdat deze inderdaad op volgorde items toevoegt aan een lijst; dus O(1).

<textarea name="form[list]" rows="10"></textarea>

## Lijst 2

Beschrijf hier voor optie 2 de efficientie van de add, remove, lookup en list\_all-operaties, met daarbij een uitleg van hoe je elke operatie zou moeten implementeren.

Een Python-lijst kan niet zelf automatisch sorteren op naam **(want als je append gebruikt komt het element achteraan de lijst, in plaats van op de "juiste plek")**, dus de stappen om de operaties te implementeren zijn hier wat ingewikkelder.

<textarea name="form[listordered]" rows="10"></textarea>

## Dictionary

Beschrijf hier voor optie 3 de efficientie van de add, remove, lookup en list\_all-operaties, met daarbij een uitleg van hoe je elke operatie zou moeten implementeren.

<textarea name="form[dict]" rows="10"></textarea>
