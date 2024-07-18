# Cyclomatic Complexity: Hangman

[Cyclomatic Complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity), of ook McCabe's complexity, is een metriek waarmee de fundamentele complexiteit van stukjes code (functies) zichtbaar kan worden gemaakt. We gaan daarbij uit van de "routes" die je door de code kunt lopen als je deze traceert vanaf de start.

In de basis is het idee vrij simpel: elke **beslissing** maakt een functie complexer. Zo zorgt een "control-structure" zoals een if/else-statement of een for/while-loop voor een splitsing in de weg. Het maakt een extra route mogelijk waarmee je door de code kunt doorlopen. Hoe meer van zulke verschillende routes bestaan, hoe ingewikkelder het wordt om de code te begrijpen.

Cyclomatic complexity meet het aantal verschillende routes door een stuk code. Het resultaat is een getal van 1 of meer. Neem bijvoorbeeld onderstaande code:

    def join(string: str, items: list[str]) -> str:
        """
        Return a string which is the concatenation of the strings in items.
        The separator between elements is the string.
        """
        if len(items) == 0:
            return ""

        result = items[0]

        for item in items[1:]:
            result += string + item

        return result

In deze functie zitten twee controle structuren, twee keuzepunten. Dat maakt drie mogelijke unieke routes:

* De conditie van de if-statement is `true`, dan zijn we direct klaar.
* De conditie van de if-statement is `false`, `items[1:]` is leeg en de for-loop wordt daarom niet uitgevoerd, dan ook klaar.
* De conditie van de if-statement is `false`, `items[1:]` is niet leeg, dan wordt de for-loop uitgevoerd en vervolgens klaar.

De Cyclomatic Complexity voor deze functie is daarom 3.

<details markdown="1"><summary markdown="span">relatie Cyclomatic Complexity en testen</summary>
Naast een maat voor complexe code geeft de Cyclomatic Complexity ook een maat voor testbare code. Want de score laat zien hoeveel unieke routes er door de code mogelijk zijn. Dat vertaalt zich ook naar hoeveel testcases er minimaal moeten zijn om alle code uit te voeren. Oftewel, een hoge Cyclomatic Complexity is een teken van lastig te testen code.

</details>

## flake8

De Cyclomatic Complexity is een berekenbare metriek en er bestaan tools om deze te berekenen voor jou. Eén zo'n tool is de style checker `flake8`. Deze kan net zoals `pycodestyle` allerlei style regels checken, maar `flake8` heeft ook een ingebouwde Cyclomatic Complexity module. In deze opdracht ga je die module gebruiken om de Cyclomatic Complexity van een bestaand programma te berekenen en vervolgens te verbeteren. Daarvoor moet je `flake8` eerst installeren, dat doe je zo:

    python3 -m pip install flake8

Vervolgens kan je met het volgende commando de cyclomatic complexity van iedere functie in een bestand berekenen.

    python3 -m flake8 --max-complexity 1 --select=C mijn_programma.py

Probeer bovenstaande maar eens uit op één van je eigen programma's. Als het goed is wijst het de ingewikkelde punten in je programma aan.

## De opdracht: Hangman

Hier vind je de code voor een spelletje Hangman (`galgje`).

<details markdown="1"><summary markdown="span">hangman.py</summary>

    import random

    def hangman_game() -> None:
        print("WELCOME TO HANGMAN ツ")

        # Prompt and re-prompt for word length
        word_length = int(input("What length of word would you like to play with?\n"))
        while word_length > 44 or word_length <= 0:
            word_length = int(input("Invalid word length! Please enter a length between 1 and 44.\n"))

        # Load words
        words: set[str] = set()
        with open('dictionary.txt', "r") as file:
            for line in file:
                word = line.rstrip()
                if len(word) == word_length:
                    words.add(word)

        # Prompt and re-prompt for number of guesses
        number_guesses = int(input("How many guesses are allowed?\n"))
        while number_guesses <= 0:
            number_guesses = int(input("Negative or zero guesses make no sense.\n"))

        # Run an infinite number of games
        while True:
            # Game set-up
            print(f"I have a word in my mind of {word_length} letters.")
            word = random.choice(list(words))
            guesses: set[str] = set()
            correct_guesses: set[str] = set()
            current_guesses = number_guesses

            # Allow guessing and provide guesses to the game
            while current_guesses > 0:
                guessed_all = True
                for letter in word:
                    if letter not in correct_guesses:
                        guessed_all = False
                        break
                if guessed_all:
                    break

                # Prompt and re-prompt for single letter
                letter = input(f"Guess a letter ({current_guesses} left): ")
                if len(letter) != 1 or not letter.isalpha() or letter in guesses:
                    continue

                guesses.add(letter)
                if letter in word:
                    correct_guesses.add(letter)
                    print("It's in the word! :)")
                else:
                    current_guesses -= 1
                    print("That's not in the word :(")

                current_pattern = ''
                for letter in word:
                    if letter in correct_guesses:
                        current_pattern += letter
                    else:
                        current_pattern += '_'
                print(current_pattern)

            # After game ends, present the conclusion
            guessed_all = True
            for letter in word:
                if letter not in correct_guesses:
                    guessed_all = False
                    break

            if guessed_all:
                print("Whoa, you won!!!")
                break
            else:
                print(f"Sad, you lost ¯\\_(ツ)_/¯. This was your word: {word}")
                break

    if __name__ == '__main__':
        hangman_game()

</details>

Alles staat gepropt in één grote functie. De Cyclomatic Complexity van deze functie is:

    $ python3 -m flake8 --max-complexity 1 --select=C hangman.py
    hangman.py:3:1: C901 'hangman_game' is too complex (17)

Aan jou de taak om deze code te verbeteren op zo'n manier dat de cyclomatic complexity niet hoger dan 3 is. Dat betekent dat het volgende geen klachten meer geeft:

    $ python3 -m flake8 --max-complexity 3 --select=C hangman.py

## Bootstrappen

Eerst even opstarten:

1. Kopieer de code van hangman hierboven, maak een bestand genaamd `hangman.py` en de plak daar de code in.
2. Download een woordenboek (`dictionary.txt`) en zorg dat deze in dezelfde map staat als `hangman.py`:

    curl -LO https://github.com/minprog/hangman/raw/2020/classic/dictionary.zip
    unzip dictionary.zip
    rm -f dictionary.zip

3. Draai `python3 -m flake8 --max-complexity 3 --select=C hangman.py` om te kijken of de tool werkt. Je hoort het volgende te zien:

    hangman.py:3:1: C901 'hangman_game' is too complex (17)

Speel vervolgens even een spelletje Hangman om gevoel te krijgen voor het programma via:

    $ python3 hangman.py

Let goed op hoe de output eruit ziet. Dit is ook hoe jouw aangepaste programma moet gaan werken.

## What to do

Het doel is de Cyclomatic Complexity onder de 3 te krijgen voor het gehele programma. Dat kan je doen door:

1. De code op te breken in kleinere functies
2. De code zelf eenvoudiger te maken waardoor er minder paden mogelijk zijn.

Lees de code eerst goed door en ga vervolgens op zoek naar punten om de code op te breken in functies. Doe dit stap voor stap, één functie per keer, en blijf goed testen tussendoor.

## Spelregels

* De output van het programma moet exact hetzelfde blijven. Bij het inleveren checken de checks dit ook.
* Alle code moet in één bestand staan: `hangman.py`.
* Alle code mag worden gewijzigd.
* De Cyclomatic Complexity mag niet hoger zijn dan 3.

## Tips

* Hou een tweede bestand bij, bijvoorbeeld `hangman_old.py`, met de originele versie van de code. Dan kan je beide versies uitvoeren en makkelijker zien of het programma nog steeds precies hetzelfde doet.
* Maak een kleinere `dictionary.txt` aan, bijvoorbeeld een woordenboek met maar één woord. Zo haal je tijdens het ontwikkelen de willekeur van het spel er even uit en is het daardoor makkelijker testen.
* Lever je code ook eens vroegtijdig in. De checks geven feedback als de output niet helemaal klopt.