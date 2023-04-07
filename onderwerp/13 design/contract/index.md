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

## Assertions

Je bent eerder al `assert`-statements tegengekomen. Het doel van assertions is om preconditions in het programma te laten controleren tijdens het runnen van het programma. Als een assertion "faalt" dan wordt het programma direct gestopt. Onthou dus dat assertions eisen moeten stellen waar **nooit** van mag worden afgeweken. Zo zou er echt nooit een kaart gedeeld mogen worden van een `Deck` waar helemaal (nog) geen kaarten in zitten. Je kunt nog wel beredeneren dat de method dan misschien `None` zou returnen maar aan de andere kant: waarom zou er überhaupt een stuk code zijn dat de `deal`-functie aanroept terwijl er helemaal geen kaarten in het spel zitten? Met een `assert` bepaal je dat dit nooit mag gebeuren.

Let op dat assertions geen manier zijn om fouten te communiceren naar de gebruiker van je programma. Als het programma zonder omhaal gestopt wordt met een technische foutmelding, dan gaat je gebruiker hier niks van begrijpen. Assertions zijn dus vooral belangrijk om fouten te voorkomen en vroeg te detecteren *tijdens het ontwikkelproces*.

## Functies

Om de opdrachten in deze module op een interessante manier te kunnen uitvoeren is het belangrijk om code op te delen in functies. Hoogstwaarschijnlijk zijn je opdrachten al aardig opgedeeld, maar zorg er eventueel voor dat je nog extra functies maakt als je daar mogelijkheden toe ziet. Het kan ook nog tijdens de verdere opdrachten, het hoeft niet direct.

Zet daarnaast eventuele losse testcode altijd in een "if-name-is-main". Voor `mario.py` kunt je bijvoorbeeld aan het volgende design denken:

    def good_name_for_drawing_a_pyramid(height):
        # TODO

    def awesome_name_for_drawing_a_line(width):
        # TODO

    def great_name_for_getting_height_from_the_user():
        # TODO

    if __name__ == "__main__":
        height = great_name_for_getting_height_from_the_user()
        good_name_for_drawing_a_pyramid(height)

## Wat is die if-name-is-main?

`__name__ == "__main__"` controleert of de verborgen variabele `__name__` is ingesteld op `"__main__"`. *Dit is alleen het geval als dat python-bestand rechtstreeks wordt uitgevoerd vanaf de command line.*

Bijvoorbeeld, in het geval van `foo.py`, zal Python de `__name__` instellen op `"__main__"` als je `python3 foo.py` uitvoert vanaf de opdrachtregel. Je kunt dit uitproberen door `__name__` te printen:

     $ echo "print(__name__)" > foo.py
     $ python3 foo.py
     __main__

Als je het bestand echter *indirect* uitvoert, door bijvoorbeeld `foo.py` te `import`eren in een ander Python-programma genaamd `bar.py`, staat de naam anders ingesteld:

     $ echo "import foo" > bar.py
     $ python3 bar.py
     foo

Waarom is dit belangrijk? Python zal bij het `import`eren alle code in een Python-bronbestand uitvoeren. Dit is de reden waarom we `foo` afgedrukt zien, ook al is de enige code in `bar.py` `import foo`. Nu kun je je voorstellen dat dit vaak ongewenst is. Misschien wilde `bar.py` wat functies van `foo.py` hergebruiken, maar niet zomaar alle overige code in `foo.py` uitvoeren. Daarom is het een goede gewoonte om code te "bewaken" (guard) die alleen moet worden uitgevoerd als de gebruiker het programma direct runt.

Kortom, `if __name__ == "__main__"` is het equivalent van Python voor een main-functie, zoals bekend uit talen als C en Java. Het gebruik ervan is in Python optioneel, maar over het algemeen een goede gewoonte.

## Individuele opdracht

Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand of iets anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

## Opdracht

Voor dit onderdeel is je opdracht om Schuifpuzzel en Hangman te documenteren met pre- en postconditions.

1. Voeg bovenaan elke functie of method een docstring toe (zie boek pagina 15 voor voorbeelden) met een korte omschrijving van het doel.

2. Voeg aan elke docstring een omschrijving van de preconditions toe, zoals hierboven en in het boek beschreven.

3. Voeg aan elke docstring een omschrijving van de postconditions toe, zoals hierboven en in het boek beschreven.

4. Voeg aan de functies en methods ook `assert`-statements toe die de preconditions zo goed mogelijk controleren.

Bespreek vooral de mogelijkheden met je buren. Het vraagt echt flink doordenken om interessante (en liefst complete!) pre- en postconditions te stellen.

Een `class` zelf heeft geen pre- of postconditions. Bedenk en bespreek waarom dit is.

Lever hieronder de aangepaste versies van `schuifpuzzel.py` en `hangman.py` in.
