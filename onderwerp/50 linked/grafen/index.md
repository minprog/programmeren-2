# Grafen en bomen

We beginnen hier met de introductie van twee wiskundige manieren van beschrijven van structuren. Het gaat om "grafen" en "bomen". Het zijn heel generieke ideeën waarmee je heel veel structuren kunt beschrijven: zowel probleemstructuren (concreet) als ook datastructuren in de computer zelf (abstract).

## Grafen

Een **graaf** (Engels: graph) is een verzameling objecten waarin sommige objecten een verbinding hebben.

Hieronder tonen we een heel abstracte graaf met vijf **knopen** (Engels: nodes). We zeggen abstract omdat de knopen geen betekenis lijken te hebben. De knopen hebben namen A, B, C, D, E, F en G.

       ---(A)
      /     \
    (B)      (C)
     |         \
     |          (D)
    (E)---(F)       \
             \------(G)

Knoop A is direct verbonden met knoop C via een **zijde** (edge). Nog sterker, elke knoop in de graaf is verbonden met precies twee andere knopen.

Tegelijk zijn er ook knopen die niet verbonden zijn, zoals het paar B en E. Maar in deze graaf is er wel een **pad** van elke knoop naar elke andere. Van A kun je via C en D bij G komen.

## Taal

Zoals je hierboven ziet kunnen we een graaf vrij eenvoudig grafisch weergeven. Alles wat we in tekst erbij hebben beschreven is te zien in deze weergave. Met deze basiskennis van grafen heb je een nieuwe *taal* om bepaalde situaties of problemen efficiënt uit te drukken. Enerzijds een grafische taal, die handig is voor op het whiteboard als je samen de structuur van een probleem uitpluist. Anderzijds kunnen woorden als knoop, zijde en pad helpen om heel precies uit te leggen over welk deel van een probleem je spreekt.

## Toepassing

We tonen nog eens dezelfde graaf, maar met andere [namen](https://www.nicospilt.com/verkortingen_tabel.htm) voor de knopen:

       ---(Asdm)
      /     \
    (Asa)    (Assp)
     |         \
     |          (Dmn)
    (Dvd)-(Dmnz)    \
                \---(Wp)

Dit zijn de spoorwegstations rondom Amsterdam Science Park (de rest van het spoor negeren we). Heel globaal is het weergegeven zoals je kunt zien op een kaart van Nederland. Maar belangrijker is de essentiële informatie die wordt weergegeven: welke stations via een spoorlijn met elkaar verbonden zijn.

We kunnen nu soortgelijke uitspraken doen als hierboven. Muiderpoort (Asdm) is direct verbonden met Science Park (Assp). Maar niet alle stations zijn direct met elkaar verbonden. Toch is er wel een pad van elk station naar elk andere. Van Muiderpoort kun je bijvoorbeeld via Science Park en Diemen (Dmn) bij Weesp (Wp) komen.

Let ook op de informatie die we hier weglaten. Je kunt prima van Diemen naar Diemen Zuid (Dmnz) gaan via Weesp. Wat niet zichtbaar is in de graaf is dat het om twee aparte spoorlijnen gaat met een heel onhandige overstap in Weesp (je kunt beter de bus nemen). De graaf is dus niet erg geschikt om *efficiënte* routes te berekenen.

Kortom, deze graaf is een **model** van het spoorwegnet rondom Science Park, waarin we bepaalde eigenschappen opnemen, maar andere eigenschappen weglaten.

## Grafen in de computer

Sinds de opkomst van het vakgebied van de informatica zijn er diverse algoritmen bedacht waarmee vragen over grafen heel efficiënt doorgerekend kunnen worden. Een typische vraag is: "wat is het kortste pad van A naar G?".

Als je je probleem kunt beschrijven als een graaf, dan kun je die bekende algoritmen dus ook gebruiken om de vraag te beantwoorden. Maar: voor ons voorbeeld met het spoorwegnet zouden we dus eerst een manier moeten vinden om in een graaf op te nemen dat er verschillende spoorlijnen zijn.

Omdat we in dit vak niet verder ingaan op de algoritmiek van grafen, zullen we ook niet verder beschrijven hoe bepaalde problemen als graaf gerepresenteerd kunnen worden. Wel is er aandacht voor het representeren van een graaf in Python, en dit past goed bij de onderwerpen die we tot nu toe behandeld hebben.

## Bomen

We zullen ook nog een specifieke vorm van grafen benoemen. Een **boom** is een graaf zonder cykels (cycles). Dat betekent dat er geen paden (zeg maar rondjes) zijn van een knoop naar zichzelf. In het voorbeeld hierboven is de hele graaf één grote cykel; je kunt van elk station een reis maken langs andere stations en weer terugkomen op hetzelfde punt. Dat is dus geen boom.

Een voorbeeld van een boom is de hiërarchische structuur in een traditioneel bedrijf. Deze beschrijft de verschillende rollen die er in dat bedrijf zijn en wie de "baas" is van wie:

             CEO
            /   \
         CTO       CFO
        /   \        \
      Dev    QA       Finance
       |             /
    Intern       Analyst

In zo'n hiërarchie is meestal geen plek voor cykels. Er is geen analist die toch ook de leidinggevende is van een developer. Tenminste, dat nemen we in dit model aan.

Omdat het om een hiërarchische structuur gaat hebben we nog een aantal nieuwe termen die we kunnen introduceren. Elke knoop heeft 0 of meer **kinderen** (children). Een kind heeft altijd één **ouder** (parent). Een knoop zonder kinderen heet een **blad** (leaf). Lekker consistent.

Net als met grafen hebben bomen bepaalde eigenschappen waarvan informatici gebruik hebben gemaakt om algoritmen te ontwikkelen die toepasbaar zijn op allerlei problemen die te representeren zijn als een boom. Veel programmeerproblemen zijn te vertalen naar een boom-representatie waarna er zo'n generiek algoritme kan worden toegepast om de oplossing te berekenen.

De boom hierboven is toevallig ook een **binaire boom** (binary tree). Elke knoop in zo'n boom heeft maximaal 2 kinderen. Dat mag er dus ook ééntje zijn, zoals de intern-rol die kind is van de dev-rol.
