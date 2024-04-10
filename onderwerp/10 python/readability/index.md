# Readability

Schrijf een programma dat bij benadering het niveau berekent dat nodig is om tekst te begrijpen, zoals hieronder beschreven.

    $ python3 readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3


## Samenwerkopdracht

Bij deze opdracht is het helemaal prima om samen te werken met één of twee medestudenten. Zorg dat je gezamenlijk op één scherm kunt kijken en echt samen het probleem probeert op te lossen. Heeft iemand een goed idee, dan moet die zorgen dat de anderen het ook begrijpen. De bedoeling is dat alle samenwerkers evenveel hebben bijgedragen aan de opdracht. Iedereen levert uiteindelijk een eigen versie in.


## Specification

*   Schrijf in een bestand met de naam `readability.py` een programma dat de gebruiker eerst vraagt ​​om wat tekst in te typen en vervolgens het cijferniveau voor de tekst uitvoert, volgens de Coleman- Liau-formule.

    *   Bedenk dat de Coleman-Liau-index wordt berekend als 0,0588 * L - 0,296 * S - 15,8, waarbij 'L' het gemiddelde aantal letters per 100 woorden in de tekst is en 'S' het gemiddelde aantal zinnen is per 100 woorden in de tekst.

*   Gebruik `input` om de invoer van de gebruiker te krijgen, en `print` om het berekende antwoord terug te geven.

*   Je programma moet het aantal letters, woorden en zinnen in de tekst tellen. Je mag aannemen dat een letter een kleine letter is van `a` tot `z` of een hoofdletter van `A` tot `Z`, elke reeks tekens gescheiden door spaties moet tellen als een woord, en dat elk voorkomen van een punt, uitroepteken of vraagteken geeft het einde van een zin aan.

*   Je programma moet als uitvoer `"Grade X"` afdrukken, waarbij `X` het niveau is dat is berekend met de Coleman-Liau-formule, afgerond op het dichtstbijzijnde gehele getal.

*   Als het resulterende indexnummer 16 of hoger is (gelijk aan of hoger dan een leesniveau van een senior undergraduate), moet uw programma `"Grade 16+"` weergeven in plaats van het exacte indexnummer te geven. Als het indexnummer kleiner is dan 1, moet uw programma `"Before Grade 1"` printen.


## Voorbeeld

Je programma zou zich moeten gedragen volgens het onderstaande voorbeeld.

    $ python3 readability.py
    Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
    Grade 3

Op sommige systemen moet je `python readability.py` geven om je programma te starten.

## Testen

Hoewel `check50` beschikbaar is voor dit probleem, word je aangemoedigd om in plaats daarvan uw code zelf te testen voor elk van de volgende gevallen.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `One fish. Two fish. Red fish. Blue fish.` and press enter. Your program should output `Before Grade 1`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` and press enter. Your program should output `Grade 2`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `Congratulations! Today is your day. You're off to Great Places! You're off and away!` and press enter. Your program should output `Grade 3`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` and press enter. Your program should output `Grade 5`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` and press enter. Your program should output `Grade 7`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` and press enter. Your program should output `Grade 8`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` and press enter. Your program should output `Grade 8`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` and press enter. Your program should output `Grade 9`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` and press enter. Your program should output `Grade 10`.

*   Run your program as `python readability.py`, and wait for a prompt for input. Type in `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` and press enter. Your program should output `Grade 16+`.
