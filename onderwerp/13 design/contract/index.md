# Documenteer je functies

Zoals beschreven in het boek kun je de **verwachtingen** van jouw functies documenteren. Wat voor soort informatie gaat erin, en wat komt eruit?

In deze module ga je op allerlei manieren je programma's Schuifpuzzel en Hangman verbeteren. De eerste bestaat uit een aantal functies, en de tweede vooral uit classes met methods. Op beide kun je de technieken uit deze module toepassen.

## Preconditions

De preconditions van een functie of method beschrijven vooral aan welke voorwaarden de parameters van de functie moeten voldoen. Dit is een harde eis. Als de parameters niet voldoen, dan is er geen enkele garantie dat de functie werkt. Het is dan aan de programmeur om te zorgen dat de functie *altijd* met parameters wordt aangeroepen die binnen deze condities vallen.

Preconditions zouden in principe ook kunnen gaan om andere "state" dan de parameters. Stel dat je een globale variabele hebt, dan kan de precondition ook daar voorwaarden aan stellen. Maar het gebruik van globale variabelen moet alleen bij hoge uitzondering plaatsvinden. Het geval wil wel dat elk *object* (als je met classes werkt) ook een soort globale state heeft: `self`.

Deze variabele `self` is vanuit elke functie beschikbaar en kan zich in verschillende toestanden (states) bevinden. Jouw code gaat uit van bepaalde voorwaarden over het object en daarom kan het soms nuttig zijn om voorwaarden voor `self` te documenteren. Stel bijvoorbeeld dat je een `Deck` class hebt. Misschien wil je wel vastleggen dat er geen kaarten gedeeld mogen worden zolang de kaarten niet geschud zijn (maar misschien ook wel, dus hierover moet je nadenken op basis van de functionaliteit die de class moet bieden!).

## Postconditions

De postconditions van een functie of method beschrijven het resultaat van de functie. In je docstring heb je het *doel* van de functie samengevat, waar ook het resultaat wordt beschreven. In de postcondition beschrijf je dit nog specifieker, bijvoorbeeld in termen van de parameters of andere variabelen. Belangrijk is ook dat je beschrijft of een functie iets `return`t of iets `print`. De meeste functies zullen één van beide doen.

Printen is één van de *side-effects* die een functie kan hebben (zie boek). Andere side-effects kunnen zijn het instellen van een globale variabele, het aanroepen van een API via internet of het aanpassen van een instance variable in een object. Alle vormen van side-effects moeten worden gedocumenteerd in de postconditions.

Om te zorgen dat de postcondition geen enorm ingewikkeld verhaal wordt is het belangrijk functies goed van elkaar te scheiden en zoveel mogelijk één operatie te laten uitvoeren. De hierboven genoemde scheiding tussen functies die returnen en die printen is een goed voorbeeld daarvan.

## Opdracht

Voor dit onderdeel is je opdracht om Schuifpuzzel en Hangman te documenteren met pre- en postconditions.

1. Voeg bovenaan elke functie of method een docstring toe (zie boek pagina 15 voor voorbeelden) met een korte omschrijving van het doel.

2. Voeg aan elke docstring een omschrijving van de preconditions toe, zoals hierboven en in het boek beschreven.

3. Voeg aan elke docstring een omschrijving van de postconditions toe, zoals hierboven en in het boek beschreven.

4. Voeg aan de functies en methods ook `assert`-statements toe die de preconditions zo goed mogelijk controleren.

Bespreek vooral de mogelijkheden met je buren. Het vraagt echt flink doordenken om interessante (en liefst complete!) pre- en postconditions te stellen.

Een `class` zelf heeft geen pre- of postconditions. Bedenk en bespreek waarom dit is.
