# Python

Het doel van deze module is jouw programmeerkennis over te dragen naar een nieuwe taal, Python. Dat doe je door veel kleine programma's en functies uit te werken. Je kan vaak beginnen met de gedachte, "hoe zou ik dat doen in C?" en vervolgens, "hoe ziet dat eruit in Python?".

De verschillende opdrachten zijn bewust kort en praktisch zonder uitleg. Dat betekent dat je zelf en *het liefst samen* op onderzoek uit moet gaan. Daag jezelf en elkaar hierbij uit, want de opdrachten zijn zo gekozen dat er vaak slimmere, zogenaamd meer Pythoneske manieren zijn om ze op te lossen.

De assistenten zijn minder behulpzaam bij deze module. Het is echt aan jou en je mede-studenten om uit te vogelen hoe Python in elkaar steekt. Natuurlijk mag je wel altijd om hulp vragen, maar doe dit altijd eerst bij je medestudenten. 

> Bij deze module is samenwerken dus de bedoeling. Er is geen sprake van plagiaatcontrole. Wel is het essentieel dat je aan het eind van de week kunt staan voor je eigen uitwerkingen en dat je onafhankelijk je ingeleverde code in detail kunt uitleggen.

## Leerdoelen

Je gaat in deze module:

- De basis van Python onder de knie krijgen
- Oefenen met lists, dicts en sets
- Kleine programmeeropdrachten in Python uitwerken
- Tests schrijven voor je eigen code
- Werken met tools die kwaliteit checken

## Puntentelling

Je krijgt de volledige 6 punten als je minstens de tweederde van de opgaven goedwerkend hebt ingeleverd. Maak dus tijd voor deze module!

## De norm

De ingeleverde code moet niet alleen aan de opdracht voldoen maar ook aan "de norm". Dat wordt gecontroleerd met verschillende tools die we runnen bij inleveren:

* [pycodestyle](/onderwerp/intro/pycodestyle): `pycodestyle --select=E101,E112,E113,E115,E116,E117,E501,E502,W505,W291 --max-line-length=99 --max-doc-length=79`
* [mypy](/onderwerp/intro/mypy): `mypy --strict`
* [pytest](/onderwerp/intro/pytest): Er zijn minimaal X tests geschreven in `pytest` en `pytest` zelf slaagt. Hoeveel tests minimaal wisselt per opdracht.

Deze tools moet je zelf draaien voordat je inlevert. Op die manier krijg je feedback als er iets nog niet klopt. De nakijkserver draait de tools ook, maar geeft alleen aan als er iets fout gaat, maar vaak niet wat.

## Python-code runnen

    python3 hello.py         <---(of python zonder 3)

Voert het programma hello.py uit.

    python3 -i camelcase.py
    >>> convert("hello_world")
    'helloWorld'

Voert het programma uit en opent de Python interpreter. Daar kan je individuele functies direct uitvoeren en testen.

## De opdrachten

Zorg dat je de opdrachten in de gegeven volgorde maakt. Ze bouwen vaak op. Een `*` betekent dat die opdracht niet nodig is om de module af te ronden. Je kan ervoor kiezen om die opdracht niet te maken in deze module en verder te gaan naar de volgende module.
