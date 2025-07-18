# Grafen en bomen

We beginnen hier met de introductie van een wiskundige manier van beschrijven genaamd "grafen".

Een **graaf** (Engels: graph) is een verzameling objecten waarin sommige objecten een verbinding hebben.

Hieronder tonen we een heel abstracte graaf met vijf **knopen** (Engels: nodes). We zeggen abstract omdat de knopen geen betekenis lijken te hebben. De knopen hebben namen A, B, C, D, E, F en G.

       ---(A)
      /     \
    (B)      (C)
     |         \
     |          (D)
    (E)---(F)       \
             \------(G)

Knoop A is direct verbonden met knoop C via een **zijde** (Engels: edge). Nog sterker, elke knoop in de graaf is verbonden met precies twee andere knopen.

Tegelijk zijn er ook knopen die niet verbonden zijn, zoals het paar B en E. Maar in deze graaf is er wel een **pad** van elke knoop naar elke andere. Van A kun je via C en D bij G komen.

## Taal

Zoals je hierboven ziet kunnen we een graaf vrij eenvoudig grafisch weergeven. Alles wat we in tekst erbij hebben beschreven is te zien in deze weergave. Met deze basiskennis van grafen heb je een nieuwe *taal* om bepaalde situaties of problemen efficiënt uit te drukken. Ook kunnen woorden als knoop, zijde en pad helpen om goed uit te leggen wat er aan de hand is.

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

We kunnen nu soortgelijke uitspraken doen als hierboven. Muiderpoort (Adsm) is direct verbonden met Science Park (Assp). Maar niet alle stations zijn direct met elkaar verbonden. Toch is er wel een pad van elk station naar elk andere. Van Muiderpoort kun je bijvoorbeeld via Science Park en Diemen (Dmn) bij Weesp (Wp) komen.

Let ook op de informatie die we hier weglaten. Je kunt prima van Diemen naar Diemen Zuid (Dmnz) gaan via Weesp. Wat niet zichtbaar is in de graaf is dat het om twee aparte spoorlijnen gaat met een heel onhandige overstap in Weesp (je kunt beter de bus nemen). De graaf is dus niet erg geschikt om *efficiënte* routes te berekenen.

Kortom, deze graaf is een **model** van het spoorwegnet rondom Science Park, waarin we bepaalde eigenschappen opnemen, maar andere eigenschappen weglaten.

## Grafen in de computer

Sinds de opkomst van het vakgebied van de informatica zijn er diverse algoritmen bedacht waarmee vragen over grafen heel efficiënt doorgerekend kunnen worden. Een typische vraag is: "wat is het kortste pad van A naar G?".

Als je je probleem kunt beschrijven als een graaf, dan kun je die bekende algoritmen dus ook gebruiken om de vraag te beantwoorden. Voor ons voorbeeld met het spoorwegnet zouden we een manier moeten vinden om in een graaf op te nemen dat er verschillende spoorlijnen zijn.

Omdat we in dit vak niet verder ingaan op de algoritmiek van grafen, zullen we ook niet verder beschrijven hoe bepaalde problemen als graaf gerepresenteerd kunnen worden. Wel is er aandacht voor het representeren van een graaf in Python, en dit past goed bij de onderwerpen die we tot nu toe behandeld hebben.

## Bomen

We zullen ook nog een specifieke vorm van grafen benoemen. Een **boom** is een graaf zonder cykels (Engels: cycles). Dat betekent dat er geen paden (zeg maar rondjes) zijn van een knoop naar zichzelf. In het voorbeeld hierboven is de hele graaf één grote cykel. Dat is dus geen boom.

Een voorbeeld van een boom is de hiërarchische structuur in een traditioneel bedrijf:

             CEO
            /   \
         CTO       CFO
        /   \        \
      Dev    QA       Finance
       |             /
    Intern       Analyst

In zo'n hiërarchie is meestal geen plek voor cykels. Er is geen analist die toch ook de leidinggevende is van een developer. Tenminste, dat nemen we nu aan.

Ook bomen hebben weer bepaalde eigenschappen waarvan informatici gebruik hebben gemaakt om algoritmen te ontwikkelen die toepasbaar zijn op problemen die te representeren zijn als een boom.
