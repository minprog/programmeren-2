# Refactoring

Deze module gaat over werken met bestaande code en deze te verbeteren:

- Allereerst door de complexiteit van de code zelf te verbeteren en daarmee het design van de te verbeteren. Deze complexiteit ga je analyseren met een metric genaamd `Cyclomatic Complexity` en de code zodanig aanpassen dat het design beter wordt.

- Dan hebben we **tests** waarmee je de functionaliteit van je eigen code kunt controleren, maar hier ga je juist tests schrijven voor andermans code. In tegenstelling tot je eigen code is het een stuk lastiger te achterhalen wat er allemaal fout zou kunnen gaan, en dus ook wat je zoal moet testen.  

- Tot slot focussen we op performance en ga je de runtime van code analyseren met een zogenaamde profiler. Hier ga je onderzoeken wat een programma nou echt doet zodra je deze uitvoert en wat de impact van de verschillende stukken code op het geheel is. Daarna ga je aan de slag om stap voor stap de performance te verbeteren.

Bij al deze onderdelen gebruik je tools die worden toegepast in de professionele software-ontwikkeling.

## Leerdoelen

Je gaat in deze module:

- Bekend worden met een metriek voor code design complexity: Cyclomatic Complexity
- Oefenen met code refactoren voor beter code design
- Tests leren schrijven voor code die je niet zelf hebt geschreven: black-box testen
- De runtime performance van code analyseren
- Op basis van de analyse gericht de performance van een bestaand programma verbeteren

## Puntentelling

Voor ieder complete en goedwerkende opdracht:

- Cyclomatic Complexity: 2 punten
    - Alle tests moeten slagen en de Cyclomatic Complexity 3 of lager. Er zijn hier geen deelpunten mogelijk.
- Cash: 2 punten in totaal
    - Bij deze opdracht krijg je 1/6 punt per goede oplossing, met een maximum van 2 punten.
- Profiling: 2 punten in totaal
    - Bij deze opdracht krijg je 1/3 punt per goed onderbouwde concrete optimalisatie, met een maximum van 2 punten.
