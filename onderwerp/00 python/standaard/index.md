# Code schrijven en de standaard

**Allereerst:** zorg dat je de opdrachten in de gegeven volgorde maakt. Ze bouwen vaak op! Een `*` betekent dat die opdracht geavanceerde onderwerpen/algoritmes behandelt. Deze steropdrachten leveren wel punten op, maar je kunt ze overslaan zonder je zorgen te maken dat je kennis mist.

# Python-code runnen

Om jouw programma's gewoon uit te proberen geef je een commando als het volgende:

    $ python3 hello.py         <---(of python zonder 3)

Met dat commando start je Python en die voert direct het programma in `hello.py` uit.

Er is ook nog een andere manier van runnen:

    $ python3 -i camelcase.py
    >>> convert("hello_world")
    'helloWorld'

Dit voert het programma uit en start dan een Python [REPL](https://en.wikipedia.org/wiki/Read–eval–print_loop). Daar kan je individuele functies uit jouw programma direct uitvoeren en testen.

# De standaard

De ingeleverde code moet niet alleen aan de opdracht voldoen maar ook aan de **standaard**. We houden diverse vaste regels aan voor het schrijven van Python-programma's. Of jouw code hieraan voldoet wordt gecontroleerd met verschillende tools die we runnen bij inleveren.

1. Je code moet voldoen aan een aantal vaste stijlregels, bijvoorbeeld de maximale lengte van regels code.

    * Om je uitwerking te controleren gebruik je [pycodestyle](/onderwerp/intro/pycodestyle).

            pycodestyle --select=E101,E112,E113,E115,E116,E117,E501,E502,W505,W291 --max-line-length=99 --max-doc-length=79

2. Je code moet types specificeren voor alle functies en variabelen.

    * Om je uitwerking te controleren gebruik je [mypy](/onderwerp/intro/mypy).

            mypy --strict

3. Je inzending moet tests bevatten. Hoeveel tests minimaal wisselt per opdracht.

    * Om je uitwerking te controleren gebruik je [pytest](/onderwerp/intro/pytest).

Deze tools moet je zelf draaien voordat je inlevert. Op die manier krijg je feedback als er iets nog niet klopt. De nakijkserver draait de tools ook, maar geeft alleen aan als er iets fout gaat, maar laat meestal niet zien wat het probleem is.
