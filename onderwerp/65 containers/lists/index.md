# List structures

Je bent bezig met het ontwerp van een systeem waarin je informatie moet bijhouden over een groot aantal personen (bijvoorbeeld klantgegevens). Elke persoon is in dat systeem een object met daarin de betreffende informatie.

Jouw specifieke taak is om een *container* class te ontwerpen waarin al deze objecten in kunnen worden opgeslagen. Daarbij is de vraag om de volgende operaties te ondersteunen:

- `add(person)` --- voegt een `person` toe aan de collectie
- `remove(name)` --- verwijdert een persoon uit de collectie met de naam `name`
- `lookup(name)` --- zoekt en geeft het object uit de collectie met de naam `name`
- `list_all` --- geeft een lijst van alle objecten gesorteerd op naam

Deze opdracht gaat over de keuzes die je hebt om **in een ADT-implementatie gebruik te maken van bestaande Python-classes zoals lists, dicst, sets en tuples**. Je gaat geen code schrijven maar redeneren op basis van een idee over welke Python-operaties je nodig zou hebben om je eigen structuur te implementeren.

Voor deze opdracht ga je drie opties vergelijken:

1. Je kunt de objecten opslaan in een standaard Python-lijst in de volgorde waarin ze zijn aangemaakt
2. Je kunt de objecten opslaan in een standaard Python-lijst die altijd gesorteerd is op naam
     * **"Altijd gesorteerd" betekent dat na het invoegen van een element de interne lijst nog steeds gesorteerd is, het invoegen moet dus op de "juiste" plek gebeuren.**
     * **Als je een lijst hebt met elementen `[1,4,5]` en je voegt `3` in, dan moet de lijst daarna `[1,3,4,5]` zijn, en niet `[1,4,5,3]` zoals wanneer je append gebruikt.**
3. Je kunt de objecten opslaan in een standaard Python-dictionary die de naam als key gebruikt

Alle drie de opties zijn valide: ze kunnen prima werkend gemaakt worden.

Geef nu voor elk van de drie opties een analyse van de efficientie van alle operaties die ondersteund moeten worden. Beschrijf daarbij het algoritme/de operaties die je zou gebruiken om die efficientie te bereiken. Als je bijvoorbeeld de methode `append` voor een lijst wil gebruiken is deze O(1). De theoretische Big-O efficientie voor bijna alle Python-structuren vind je op de [Python wiki over TimeComplexity](https://wiki.python.org/moin/TimeComplexity).


## Lijst 1

**Beschrijf** hier voor optie 1 de efficientie van de add, remove, lookup en list\_all-operaties, met daarbij een uitleg van hoe je elke operatie zou moeten implementeren. Geef geen code of pseudo-code, maar alleen een korte beschrijving.

Als voorbeeld:

- `add` implementeren we met de `append` operatie van de Python list; `append` voldoet aan de voorwaarde dat de objecten opgeslagen worden in de volgorde waarin ze worden aangemaakt; `append` is O(1) dus onze `add`-operatie ook
- `remove` implementeren we ...
- `lookup` implementeren we ...
- `list_all` implementeren we ...

## Lijst 2

**Beschrijf** hier voor optie 2 de efficientie van de add, remove, lookup en list\_all-operaties, met daarbij een uitleg van hoe je elke operatie zou moeten implementeren.

Een Python-lijst kan niet zelf automatisch sorteren op naam, want als je append gebruikt komt het element achteraan de lijst, in plaats van op de "juiste plek". Dus in dit geval moet je vaak enkele stappen combineren om de gewenste operatie te implementeren.

## Dictionary

**Beschrijf** hier voor optie 3 de efficientie van de add, remove, lookup en list\_all-operaties, met daarbij een uitleg van hoe je elke operatie zou moeten implementeren.

## Inzicht

Uiteindelijk zoek je voor de concrete implementatie van de ADT naar opties die het meest efficient werken. Dit hangt niet alleen af van bijvoorbeeld de keuze om `append` te gebruiken, maar ook hoe jouw ADT in de praktijk gebruikt gaat worden. Als "opzoeken" heel efficient moet zijn, dan mag het "invoegen" van een persoon in de lijst misschien wel wat meer stappen kosten (duurder zijn).

**Beschrijf** in welke gevallen je zou kiezen voor elk van de drie mogelijkheden voor implementatie. Mocht je een nog betere mogelijkheid zien die hier niet besproken is, dan kun je die ook geven.
