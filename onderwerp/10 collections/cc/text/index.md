# Cyclomatic Complexity: Tekstanalyse

In deze opdracht ga je de Cyclomatic Complexity van een bestaand programma verlagen. Je gebruikt hiervoor `flake8`, met als doel dat elke functie een Cyclomatic Complexity van maximaal 3 krijgt.

De complexiteit zit in dit programma vooral in **lussen**: lussen binnen lussen, met `if`s erin. Dat vraagt meer overzicht over welke stukken code bij elkaar horen.

## De opdracht: Tekstanalyse

Hier vind je de code van een programma dat een tekstbestand (`text.txt`) analyseert (`text.py`). Het haalt leestekens uit de tekst, telt de woorden en laat een aantal statistieken zien. Woorden die in de lijst met `stopwords` staan tellen mee in het totaal, maar worden niet meegeteld bij "Words used once" en "Most common words". Een apostrof wordt weggehaald: `cat's` wordt `cats`.

<details markdown="1"><summary markdown="span">text.py</summary>

    def analyze() -> None:
        print("TEXT ANALYZER")

        stopwords = {"the", "a", "an", "and", "of", "to", "in", "is", "it", "that", "was", "he", "she"}

        # Read the file and turn every line into a list of clean, lowercase words
        words: list[str] = []
        with open("text.txt", "r") as file:
            for line in file:
                cleaned = ""
                for character in line:
                    if character.isalpha():
                        cleaned += character.lower()
                    elif character == "'":
                        continue
                    else:
                        cleaned += " "
                for word in cleaned.split():
                    words.append(word)

        if len(words) == 0:
            print("No words found.")
            return

        # Count the words that are not stopwords
        counts: dict[str, int] = {}
        for word in words:
            if word not in stopwords:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

        # The longest word, the first one wins in case of a tie
        longest = ""
        for word in words:
            if len(word) > len(longest):
                longest = word

        # The shortest word, the first one wins in case of a tie
        shortest = words[0]
        for word in words:
            if len(word) < len(shortest):
                shortest = word

        long_words = 0
        for word in words:
            if len(word) > 6:
                long_words += 1

        unique: set[str] = set()
        for word in words:
            unique.add(word)

        print(f"Total words: {len(words)}")
        print(f"Unique words: {len(unique)}")
        print(f"Longest word: {longest}")
        print(f"Shortest word: {shortest}")
        print(f"Long words: {long_words}")

        once = 0
        for word in counts:
            if counts[word] == 1:
                once += 1
        print(f"Words used once: {once}")

        # Select the five most common words, the first counted wins a tie
        print("Most common words:")
        chosen: set[str] = set()
        for rank in range(5):
            best = ""
            best_count = 0
            for word in counts:
                if word not in chosen and counts[word] > best_count:
                    best = word
                    best_count = counts[word]
            if best == "":
                break
            chosen.add(best)
            print(f"{best:<12}{'#' * best_count}")


    if __name__ == '__main__':
        analyze()

</details>

Alles staat gepropt in één grote functie. De Cyclomatic Complexity van deze functie is:

    $ python3 -m flake8 --max-complexity 1 --select=C text.py
    text.py:1:1: C901 'analyze' is too complex (23)

Aan jou de taak om deze code te verbeteren op zo'n manier dat de Cyclomatic Complexity niet hoger dan 3 is. Dat betekent dat het volgende geen klachten meer geeft:

    $ python3 -m flake8 --max-complexity 3 --select=C text.py

## Bootstrappen

Eerst even opstarten:

Kopieer de code hierboven, maak een bestand genaamd `text.py` en plak daar de code in. Maak in dezelfde map ook een bestand `text.txt` met bijvoorbeeld de volgende tekst:

<details markdown="1"><summary markdown="span">text.txt</summary>

    The fox jumped over the fence, and the dog watched it go. "That fox is clever," said the farmer's wife.
    It was a quiet evening in the village; the fox was gone and the dog was asleep.
    Clever foxes never return to the same fence twice, she said, but this fox always did.

</details>

Draai `python3 -m flake8 --max-complexity 3 --select=C text.py` om te kijken of de tool werkt. Je hoort het volgende te zien:

    text.py:1:1: C901 'analyze' is too complex (23)

Draai vervolgens `python3 text.py`. Als alles goed is, zie je dit:

    TEXT ANALYZER
    Total words: 53
    Unique words: 35
    Longest word: watched
    Shortest word: a
    Long words: 4
    Words used once: 20
    Most common words:
    fox         ####
    fence       ##
    dog         ##
    clever      ##
    said        ##

Let goed op hoe de output eruit ziet, ook als er weinig of geen woorden in `text.txt` staan. Dit is ook hoe jouw aangepaste programma moet gaan werken.

## What to do

Het doel is de Cyclomatic Complexity onder de 3 te krijgen voor het gehele programma. Dat kan je doen door:

1. De code op te breken in kleinere functies
2. De code zelf eenvoudiger te maken waardoor er minder paden mogelijk zijn.

Lees de code eerst goed door en ga vervolgens op zoek naar punten om de code op te breken in functies. Doe dit stap voor stap, één functie per keer, en blijf goed testen tussendoor.

<details markdown="1"><summary markdown="span">hint: een pijplijn</summary>

Het programma doet eerst een aantal dingen achter elkaar: het bestand lezen, de tekst schoonmaken, tellen, en dan pas printen. Elke stap heeft een invoer en een uitvoer. Denk aan functies als `read_words(filename)` die een lijst woorden teruggeeft en `count_words(words)` die een `dict` teruggeeft.

</details>

<details markdown="1"><summary markdown="span">hint: een lus per functie</summary>

Een lus binnen een lus telt dubbel. Als je elke lus in een eigen functie zet, met een duidelijke naam (`find_longest`, `count_long`, ...), blijft elke functie klein. Met `return` midden in een lus kan je een functie vaak ook korter maken.

</details>

<details markdown="1"><summary markdown="span">hint: tellen met een dict</summary>

Het stukje `if word in counts: ... else: ...` kan korter. Kijk naar wat de methode `get` van een `dict` doet als je een tweede argument meegeeft.

</details>

## Spelregels

* De output van het programma moet exact hetzelfde blijven. Bij het inleveren checken de checks dit ook.
* Alle code moet in één bestand staan: `text.py`.
* Alle code mag worden gewijzigd.
* De Cyclomatic Complexity mag voor geen enkele functie hoger zijn dan 3.
* De type hints moeten blijven kloppen: de checks draaien ook `mypy` en `pycodestyle`.

## Tips

* Hou een tweede bestand bij, bijvoorbeeld `text_old.py`, met de originele versie van de code. Dan kan je beide versies uitvoeren en makkelijker zien of het programma nog steeds precies hetzelfde doet.

  <details markdown="1"><summary markdown="span">vergelijken met het unix-programma diff</summary>

  Met `diff` laat je de computer de vergelijking doen. Dit programma leest alleen `text.txt` en vraagt niets om invoer, dus je kan beide versies direct laten draaien en de output vergelijken:

      python3 text_old.py > oud.txt
      python3 text.py > nieuw.txt
      diff oud.txt nieuw.txt

  Geeft `diff` geen uitvoer, dan is de output van de twee bestanden identiek. Anders laat `diff` precies zien welke regels verschillen. Het kan ook in één keer, zonder tussenbestanden:

      diff <(python3 text_old.py) <(python3 text.py)

  Herhaal dit voor verschillende varianten van `text.txt`, zie de tips hieronder.

  </details>

* Probeer verschillende tekstbestanden: een leeg bestand, een bestand met alleen stopwoorden, en een bestand met minder dan vijf verschillende woorden.
* Let op gelijke aantallen. Als twee woorden even vaak voorkomen, dan staat het woord dat het eerst in de tekst voorkwam bovenaan. Hetzelfde geldt voor het langste en het kortste woord.
* Lever je code ook eens vroegtijdig in. De checks geven feedback als de output niet helemaal klopt.
