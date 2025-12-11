# Mini-meesterproef

Je kunt deze opgave bestuderen om je voor te bereiden op de meesterproef. Alle stappen die je hier neemt moet je ook tijdens de meesterproef doen, maar het zal wel méér zijn. We houden deze oefening klein zodat je het format alvast begrijpt, maar het echte oefenen doe je door de huiswerkopgaven in het vak te maken.

**De complexiteit van de opgave in de meesterproef is dus hoger dan onderstaande, maar je volgt wel een soortgelijk stappenplan.**

## Aan de slag

Open deze pagina in een tweede tab, en druk dan op de knop om de tentamen-omgeving te starten. Tijdens de meesterproef krijg je de opgaven op papier.

[Start de mini-meesterproef](exam_button:minimeesterproef)

## Casus

We willen een klein systeem maken voor het bijhouden van metingen van temperatuur in een huis. Elke meting heeft een tijdstip en een gemeten temperatuur. Je moet:

1. Een data class maken die één meting representeert.
2. Een collection class maken die meerdere metingen kan opslaan en eenvoudige analyses kan doen.

## Eisen

* De focus ligt niet op het geheel afmaken van alle opdrachten. Begin bij stap 1 en maak die helemaal netjes. Daarna stap 2.
* Het schrijven van tests is verplicht per stap, en essentieel: zonder zinvolle tests kan er geen eindgesprek plaatsvinden en moet je een nieuwe meesterproef maken.
* Gebruik waar gepast encapsulation (_private attributen/methoden met logische types).
* Schrijf samenvattende docstrings bij je klassen en methoden, ook verplicht.
* Vermeld types voor methodes en parameters, zodanig dat `mypy` tevreden is.

## Metingen representeren

Definieer een klasse `Measurement` die één temperatuurmeting voorstelt.
De klasse moet in ieder geval:

*	een constructor hebben die twee waarden opslaat:
    *	timestamp (string, bijvoorbeeld `"2025-11-19 13:45"`)
    *	temperature (`float`)
        * controleer in de constructor dat temperature een float is, of maak deze automatisch float via float()

*	een `__repr__()` implementeren die een duidelijke tekstuele representatie geeft, zoals:

        Measurement(2025-11-19 13:45, 21.5°C)

Vergeet niet om direct tests te schrijven vóórdat je doorgaat met de volgende stap!

## Analyse van metingen

Definieer een klasse `MeasurementSeries` die meerdere Measurement-objecten kan bevatten.

De klasse moet minimaal:

* Een lege lijst bevatten waarin metingen worden opgeslagen.
* Een methode `add(measurement)` die een Measurement toevoegt.
* Een methode `count()` die teruggeeft hoeveel metingen er zijn.
* Een methode `average_temperature()` die de gemiddelde temperatuur van alle metingen berekent.
    * Als er geen metingen zijn, retourneer `None`.

Vergeet niet om direct tests te schrijven vóórdat je doorgaat met de volgende stap!

## Verantwoording (doe dit in de laatste 15 minuten)

Lever een kort tekstbestand `verantwoording.txt` in met daarin:

* Een korte uitleg van je ontwerpkeuzes/beslissingen.
* Wat de big-O-complexiteit is van de belangrijkste operaties van de classes.
* Wat je getest hebt en waarom.

## Inleveren

Dit gaat automatisch als je op Submit drukt in de tentamen-editor.

1. Een Python-bestand `opdracht.py` met je implementatie.
2. Een testbestand `test_opdracht.py` met pytest-tests.
3. Een kort tekstbestand `verantwoording.txt` met je toelichting.

Het is OK als iets niet lukt! We hebben wel code nodig om een goed eindgesprek te kunnen voeren, maar de meesterproef hoeft niet perfect!
