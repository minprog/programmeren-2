# Programmeren voor grote "real-world" programma's

Als je dit vak volgt heb je al veel geprogrammeerd. Met de kennis en vaardigheid die je hebt kun je in theorie alle programma's schrijven die te bedenken zijn. Misschien wat omslachtig soms... maar het werkt!

We gaan nu een stap verder en leren over het schrijven van grotere programma's. Het vreemde is dat je dit, om praktische redenen, doet door toch weer kleinere programma's of delen van programma's te schrijven. Je zal je daarom weleens gaan afvragen: **waarom?!**.

Het boek helpt je telkens de context beter te begrijpen en daarmee deze waarom-vraag te beantwoorden. Bij de verschillende modules staat meestal een hoofdstuk klaar en het is belangrijk deze door te nemen vóór je aan de slag gaat.

## Doelen voor deze module

- Verschillen tussen kleine en grotere programma's voor het schrijven van code
- De noodzaak van abstractie
- Weten wat "testing" is en hoe je basistests moet schrijven
- Begrip van goede design principes
- Kennis maken met Python en snel vaardig worden

Die laatste staat niet voor niks onderaan. Python is hier niet het doel van de cursus maar alleen maar de taal die we gebruiken om je de andere onderwerpen aan te leren.

## Voorbereiding

1. Lees hoofdstuk 2 van [A First Course on Data Structures in Python](https://donsheehy.github.io/datastructures/). Dit is een review van de onderdelen van Python die nu relevant zijn.

2. Ga naar de [mededelingen](/announcements) en download hoofdstuk 1. Lees dit boek t/m 1.2.4. Hierin wordt kort beschreven waar we heen gaan met de cursus.

3. Bekijk eventueel nog de [video over Python](https://video.cs50.io/mgBpcQRDtl0) waarin Doug van CS50 veel basis-Python laat zien. Als je in het lokaal al een demo hebt bijgewoond is deze overbodig.

Bij 1 en 3 vind je ook informatie over classes, dictionaries en sets. Dat zijn standaard ingebouwde structuren in Python. Deze ga je pas in de volgende module toepassen.

## Correcties video

De CS50-video is al wat ouder en bevat een aantal ouderwetse voorbeelden. Wees je hiervan bewust:

-   **Onnodige ternary-operator**

    Doug gebruikt het voorbeeld:

        all_letters = True if input().isalpha() else False

    De methode `isalpha()` returned zelf al `True` of `False`, gebruik dus liever:

        all_letters = input().isalpha()

-   **Geen slice assignment**

    Doug gebruikt onderstaande om `5` toe te voegen aan een lijst genaamd `nums`.

        nums[len(nums):] = [5]

    Dat kan, maar het is erg ongebruikelijk. Gebruik liever:

        nums.append(5)

    Of als je twee lijsten wil samen voegen:

        nums = nums + [5]

-   **f-strings**

    Python 3.6 introduceerde f-strings en dat is nu de standaard om strings te formatten. Het filmpje gebruikt nog `.format` als volgt:

        "In {1}, {0} took office".format(president, year)

    Gebruik in plaats daarvan:

        f"In {year}, {president} took office"

    Let goed op de letter `f` voor het eerste `"`!
