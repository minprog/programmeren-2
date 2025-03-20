# Code schrijven en de standaard

Zorg dat je de opdrachten in de gegeven volgorde maakt. Ze bouwen vaak op! Een `*` betekent dat die opdracht niet nodig is om de module af te ronden. Je kan ervoor kiezen om die opdracht niet te maken in deze module en verder te gaan naar de volgende module.

# Python-code runnen

Om jouw programma's gewoon uit te proberen geef je een commando als het volgende:

    python3 hello.py         <---(of python zonder 3)

Dit voert het programma in het bestand `hello.py` uit.

    python3 -i camelcase.py
    >>> convert("hello_world")
    'helloWorld'

Dit voert het programma uit en opent daarna de Python-interpreter. Daar kan je individuele functies direct uitvoeren en testen.

# De standaard

De ingeleverde code moet niet alleen aan de opdracht voldoen maar ook aan de **standaard**. We houden diverse vaste regels aan voor je uitwerkingen. Of jouw code hieraan voldoet wordt gecontroleerd met verschillende tools die we runnen bij inleveren.

* Je code moet voldoen aan een aantal vaste stijlregels, bijvoorbeeld de maximale lengte van regels code.

    * Om te controleren gebruik je [pycodestyle](/onderwerp/intro/pycodestyle).
    
            pycodestyle --select=E101,E112,E113,E115,E116,E117,E501,E502,W505,W291 --max-line-length=99 --max-doc-length=79

* Je code moet types specificeren voor alle functies en variabelen.

    * Om te controleren gebruik je [mypy](/onderwerp/intro/mypy).
    
            mypy --strict

* Je inzending moet tests bevatten. Hoeveel tests minimaal wisselt per opdracht.

    * Om te controleren gebruik je [pytest](/onderwerp/intro/pytest).

Deze tools moet je zelf draaien voordat je inlevert. Op die manier krijg je feedback als er iets nog niet klopt. De nakijkserver draait de tools ook, maar geeft alleen aan als er iets fout gaat, maar laat meestal niet zien wat het probleem is.
