# Assertions en exceptions

In deze cursus gebruiken we allerlei technieken om fouten te voorkomen, en om de oorzaak van een fout snel te kunnen vinden als die toch optreedt.

## Assertions

Eerder ben je assertions tegengekomen op twee plekken:

- Je hebt (in het boek) gezien dat je bovenin een functie `assert`-statements kan toevoegen om eisen aan de input op te geven: **preconditions**. De bedoeling is dat de programmeur bij voorbaat zorgt dat een assertion nooit optreedt --- want dat zou een bug zijn. Maar: als het gebeurt, dan is het helaas meestal "in productie", ofwel als iemand de software gebruikt. Mocht een assertion optreden dan wordt het programma daarom direct stopgezet om eventuele rampen te voorkomen. Het voordeel is dat de assert dan een stevige hint geeft over waar het mis ging, wat doorgegeven kan worden aan de programmeur die de oorzaak moet vinden.

- Je hebt (in de eerste module) ook `assert`-statements gezien in **tests**. Hier wordt met zo'n statement aangegeven wat een verwachte waarde is binnen de context van een test. De primaire taak van het Pytest-framework is jouw tests te runnen en te rapporteren hoeveel van de tests slagen. Als een assert `False` geeft dan faalt de test geheel. De ontwikkelaar (programmeur) runt tests en kan dan ook direct inspecteren waar een test faalt en waarom.

## Exceptions

Als je de woorden assertion en exception goed bestudeert mag je al concluderen dat de assertion altijd moet slagen. Een exception is anders: hiermee geven we exceptionele gebeurtenissen aan. Maar zo'n gebeurtenis kan mogelijk wel netjes ("gracefully") afgehandeld worden.

Om te beginnen heeft Python diverse ingebouwde exceptions die worden getriggerd als er iets ongebruikelijks gebeurt. Als we weten welke exception er verwacht zou kunnen worden, en we zien wel een mogelijkheid voor het programma om dan toch door te gaan, dan kunnen we het netjes afhandelen in de code.

Een typisch voorbeeld is **foute user-input**. Als een gebruiker iets fout doet dan wil je niet dat het programma crasht. In het volgende voorbeeld zie je dat we om input vragen. We willen heel graag een gewoon getal, zodat we er een integer van kunnen maken om hier berekeningen mee te doen. Maar we weten natuurlijk helemaal niet zeker of de gebruiker zich daar aan gaat houden. De functie `input` checkt namelijk helemaal niets.

    text = input("give me a number")
    try:
        # we hebben tekst, maar we proberen er gewoon een int van te maken
        number = int(text)
    except ValueError:
        number = 0

Je ziet drie actieve regels code: de regel waar om input wordt gevraagd, de regel waar de input wordt omgezet in een `int` en de regel waar de variabele op 0 wordt gesteld.

Maar we zien vooral een `try`-`except`-constructie. Hoe werkt dit?

## Ask for forgiveness

In Python is het principe "it's often easier to ask forgiveness than to get permission" één van de leidraden bij het schrijven van code. De functie `input` check zoals gezegd niks, dus we weten eigenlijk niet wat we kunnen verwachten, behalve dat het een string is.

We kunnen natuurlijk wel stap voor stap door de string loopen en controleren of elk teken een cijfer is, kijken of er één of meer `-`-tekens voor staan (maar niet ergens anders). En misschien een `.` of komma's? Maar niet meer dan één `.` hoor! Voor je het weet ben je allerlei if-statements aan het schrijven om de input te valideren vóór je deze durft om te zetten naar een integer.

En nu komt het. Wat nou als we proberen er een integer van te maken en kijken wat er gebeurt?

Dat is het idee van de code hierboven: je probeert het, en als het fout blijkt, dan probeer je dat probleem op een goede wijze op te lossen. Dat is het "asking for forgiveness"-deel. De `try`-`except` is daar precies voor gemaakt.

## Exceptions

In je eigen code kun je ook exceptions laten optreden met het commando `raise`.

![embed](https://video.cs50.io/BltXeMM96DA)

Het voorbeeld uit de video:

    def get_pace(miles, minutes):
        if not minutes > 0:
            raise ValueError("Minutes must be greater than 0.")
        return minutes / miles

Er zijn vanaf nu dus drie mogelijke uitkomsten voor elke functie-aanroep:

- Zodra Python een `return` tegenkomt zal de functie eindigen op een reguliere manier, met een returnwaarde.

- Zodra Python een `raise` tegenkomt zal de functie eindigen op een exceptionele manier, met een specifieke Exception en een eventuele hint.

- Als de functie eindigt zonder `raise` of `return` dan wordt automatisch de waarde `None` teruggegeven.

In principe kunnen al deze dingen gebeuren in één en dezelfde functie.

## Geen exceptions naar de gebruiker!

Je zou kunnen denken (zeker op basis van de video) dat exceptions met een duidelijke foutmelding misschien prima zijn om naar de gebruiker door te geven. Als programmeur ben je ook wel gewend dat de exceptions je om de oren vliegen.

Maar dat is het punt: exceptions zijn echt een programmeurstool. Als je een exception laat optreden dan zal deze, net als een assertion, het programma direct stoppen. Bij foute input is het toch normaal om de gebruiker een foutmelding te geven én nogmaals de gelegenheid geven om iets in te voeren.

Het is prima als een losse functie eindigt in een exception. Maar die exception zou je in vrijwel alle omstandigheden uiteindelijk moeten "opvangen" met een `try`-`except`-blok. Bedenk zelf hoe je het programma uit de video zó zou kunnen construeren dat er wel een exception optreedt in de functie `get_pace` (die blijft dus onveranderd) maar dat de `main` dan nog eens om input vraagt.

## Testen of exceptions optreden

Als exceptions een verwachte uitkomst van functies zijn, dan moeten we dus ook kunnen testen of ze echt optreden in zo'n exceptioneel geval!

Stel dat we een functie hebben die van een lijst getallen de *mediaan* uitrekent. Als de lijst leeg is, kan er per definitie geen mediaan bepaald worden. Dat is dus een situatie die exceptioneel is, maar wel soms kan gebeuren. In dat geval moet de uitkomst van de functie een exception zijn:

    def get_median(items: list[int]) -> int:
        size = len(items)

        if size == 0:
            raise ValueError("Cannot get a median from an empty list.")

        middle = size // 2
        return items[middle]

In een Pytest kunnen we deze uitkomst als volgt testen:

    import pytest
    from median import get_median

    def test_empty_list():
        with pytest.raises(ValueError):
            get_median([])
