# Kalender, revisited

Deze opdracht ken je van Programmeren 1, maar je gaat 'm nu helemaal vanaf het begin uitwerken in Python. Nog even wat de bedoeling is:

    $ python kalender.py 9 2022
              Sep 2022
    ---------------------------
    Zon Maa Din Woe Don Vri Zat
                      1   2   3
      4   5   6   7   8   9  10
     11  12  13  14  15  16  17
     18  19  20  21  22  23  24
     25  26  27  28  29  30

## Individuele opdracht

Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

## Werkproces documenteren

Zorg dat je je werkproces en ontwerpstappen goed beschrijft in een documentje. Dit lever je hieronder ook in.

## Specificatie

De basis van je uitwerking is een programma dat een kalender kan weergeven, exact zoals hierboven zichtbaar is.

Dit is algoritmisch een aardige uitdaging, want de datums moeten op de juiste weekdag geprint worden. Om dit correct te kunnen doen moet je weten op welke dag de eerste van de maand valt. En dat kun je berekenen als je van een willekeurige historische datum week op welke weekdag deze viel. Zo weten we bijvoorbeeld dat 1 januari 1800 een woensdag was.

De weekdagen gaan we nummeren. In de kalender hierboven zien we zondag als de eerste dag en zaterdag als de laatste; daarmee heeft zondag index 0 en zaterdag index 6. Woensdag is dus index 3 en daarmee kunnen we declareren dat 1 januari 1800 eveneens de index 3 heeft. We definiëren daarvoor een constante genaamd `START_DAY`.

Om te weten welke op welke weekdag 1 september 2022 is, moeten we dus weten hoeveel dagen er tussen 1 januari 1800 en 1 september 2022 zitten (`days_from_1800`), en
wat de dag van de week op 1 januari 1800 is (`START_DAY`).
Samen geeft dit de formule `(days_from_1800 + START_DAY) % 7` voor de index van de eerste dag van de maand.

Vergeet niet dat er schrikkeljaren kunnen zijn! Een jaar is een schrikkeljaar als het deelbaar is door 4. Maar wegens kalenderhervorming zijn jaren die deelbaar zijn door 100 geen schrikkeljaren, behalve als het ook nog eens deelbaar is door 400, dan is het juist wel weer een schrikkeljaar.

Je mag er bij deze opdracht vanuit gaan dat de **eindgebruiker** (niet programmeur) jaartallen >= 1800 invult en valide maandnummers.

Voor het werken met command line arguments gebruik je in Python de variabele `sys.argv`:

    import sys

    print(len(sys.argv)) # is bijvoorbeeld 1 of 2
    print(sys.argv[0])

Zie de [documentatie over sys.argv](https://docs.python.org/3.10/library/sys.html?highlight=argv#sys.argv) voor de precieze werking.


## Main

Zorg dat je het verwerken van de command-line arguments, met daarbij het eventueel printen van errors, isoleert in de `if __name__ == '__main__'`-sectie.


## Opdracht

Implementeer het bovenstaande programma, waarbij je je houdt aan de volgende aanwijzingen:

- Je werkt volgens de principes van top-down design. Voordat je begint met programmeren ga je definiëren wat het doel van het programma is. Dan ga je dat doel opsplitsen in kleinere stappen. Je blijft dit verfijnen tot je relatief eenvoudig te implementeren onderdelen hebt.

    - Beschrijf je ontwerp-stappen die je hebt gemaakt in een documentje. Denk aan zinnen als: "Dit is het doel van het hoofdprogramma:", "Daardoor werd de functie te ingewikkeld dus die heb ik opgesplitst in ... en ...".

    - Dit ontwerpen is meer een kunst dan een wetenschap. Blijf dus puzzelen en verfijnen tot het logisch lijkt. Kijk niet naar de oude opdracht en maak je eigen opdeling.

    - Probeer goede namen te verzinnen voor de onderdelen en gebruik dit als feedback voor je design: wordt de naam te ingewikkeld of te lang? Dan is de functie misschien op te splitsen---of je moet meerdere functies aanpassen om alles simpeler te krijgen.

    - Schrijf als je klaar bent met ontwerpen voor alle functies een docstring met korte samenvatting van het doel.

- Schrijf voor alle functies expliciete specificatie van de preconditions en postconditions in de docstrings, zoals voorgeschreven in het boek.

    - Documenteer van alle functies eventuele side-effects in de docstrings. Geef ook aan als er géén side-effects zijn.

    - Gebruik het aanwezig zijn van side-effects als feedback voor je design. Je wil namelijk dat functies met side effect verder zo weinig mogelijk doen, en dat functies die een berekening maken liefst geen side effects hebben. Zo krijgt elke functie een duidelijk doel.

    - Schrijf assertions in de functies voor de preconditions die snel te verifiëren zijn.

- Vermeld type hints voor alle parameters en return values.

    - Controleer zelf de typing in je programma met `mypy --strict`.

- Schrijf in een apart bestand unit tests voor de kalender-functionaliteit.

    - Controleer zelf je tests met `pytest`.
    
    - Denk goed na over de tests die je voor elke functie zou kunnen schrijven. Vanuit de preconditions weet je welke waarden "geldig" zijn als invoer voor een functie. Je kunt en wilt geen test schrijven voor *álle* mogelijke combinaties van parameters. Kun je wellicht verschillende *soorten* waarden ontdekken, en tests bedenken voor elke combinatie van *soorten* waarden?

- Beschrijf in je ontwerpdocument ook eventuele debug-stappen die je hebt genomen. Als het goed is gaat het debuggen op een andere, preciezere manier als je je pre- en postconditions goed gedefinieerd hebt en ook assertions en tests gebruikt.

- Geef voor elke functie de complexiteit van de functie aan in de docstring. De complexiteitsmaat big-O ken je van eerdere oefeningen.

## Submit

Je kunt hieronder je uitwerkingen opsturen.

Je kunt 1 punt extra verdienen als je programma's zichtbaar uitblinken in bijvoorbeeld toepassing van Python-achtige constructies en in het ontwerp van je tests. Als je hiervoor specifieke dingen hebt gedaan die we misschien over het hoofd zien, geef het dan hier aan.

<textarea name="form[extra_punt]" rows="5"></textarea>
