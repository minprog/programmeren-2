# Oefenen met testen

Herschrijf je code voor **Schuifpuzzel** en **Hangman** en voeg unit tests toe in aparte bestanden.

## Individuele opdracht

Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand of iets anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

## Wat moet je testen?

Stel, we hebben de volgende functie:

    def is_divisible(numerator: int, denominator: int) -> bool:
        """Returns True if denominator divides numerator, False otherwise.""
        if denominator == 0:
            return False
        return numerator / denominator == 0

We kunnen dan bijvoorbeeld de volgende tests schrijven, waarin we drie verschillende combinaties van input beschrijven, met hun bijbehorende output:

    from wherever_divisible_is_defined import is_divisible

    def test_divisible():
        assert is_divisible(9, 3) == True

    def test_is_not_divisible():
        assert is_divisible(8, 5) == False

    def test_dividing_by_zero():
        assert is_divisible(4, 0) == False

Wat maakt dit nu een goede verzameling tests voor deze functie? Het is ondoenlijk om alle mogelijke inputs te gaan nalopen en controleren, zeker als dat voor een heleboel functies moet. Daarom is het belangrijk om een zo **representatief** mogelijke verzameling tests te kiezen voor elke functie. Dat is zowel ambacht, die je opbouwt met ervaring, als wetenschap, waarin kritisch onderscheid maken tussen te testgevallen belangrijk is. Hier kijken we bijvoorbeeld naar de volgende ideeën:

- Je wilt in ieder geval een aantal gevallen testen waar de getallen inderdaad "divisible" zijn. In het voorbeeld hierboven is sprake van de combinatie `9` en `3`. Voor deelbaarheid is het misschien ook handig om naar een noemer van `1` te kijken en ook als de teller en noemer hetzelfde getal zijn. Allemaal bijzondere gevallen die je kunt bedenken met kennis van het probleem.

- Dan wil je waarschijnlijk diverse gevallen testen waar de getallen *niet* "divisible" zijn. Hierboven is sprake van de combinatie `8` en `5`. Wat is er nog meer? Er zijn niet zoveel bijzondere gevallen te bedenken. Misschien is dit voldoende. Als je echt op dreef bent kun je kijken of er grenzen zijn aan hoe groot integers mogen zijn in Python en of dit nog invloed heeft op de werking van `is_divisible`.

- Tot slot is er een speciale "edge case" in de functie, die ook expliciet terugkomt in de definitie. Er staat dat als de noemer `0` is, er sowieso `False` wordt gegeven. Die moet je dan zeker testen. Misschien is het zelfs goed om de combinatie `0` en `0` te testen. Overigens: niet alle edge cases staan zo duidelijk in functies! Soms zijn edge cases bijvoorbeeld gevolg van het gekozen datatype. Dus het is ook een kwestie van goed kijken wat er mis zou kunnen gaan.

Kortom, het is al een redelijke verzameling tests, maar misschien moeten er nog een paar bij.

Nu is een belangrijke vraag om in gedachten te houden: waarom test je eigenlijk? Je doet dat onder andere om goede afspraken te kunnen hebben over de verwachtingen van de uitkomst van de functie. Dat klinkt logisch, maar stel nu dat een medeprogrammeur jouw `is_divisible` ziet en denkt "better to ask for forgiveness" en de hele `if` weggooit. Vanaf nu zal je functie een exception geven zodra in de laatste regel een `/ 0` wordt uitgevoerd.

Dus als de noemer `0` is komt er voortaan een exception, in plaats van het antwoord `False`. Dat is een wezenlijk andere uitkomst dan voorheen, en misschien heeft dat wel invloed op andere delen van de code (daar moet je nu bijvoorbeeld een `try` toevoegen?). Goed dus om die verwachting van `return False` in de verzameling tests te hebben, want dan ziet je medeprogrammeur dat hier een bewuste keuze was gemaakt en dat zo'n wijziging niet zomaar gedaan moet worden. Tijd voor een goed gesprek dus!

## Comments

Zorg dat je in de comments bij een testcase altijd vermeld waarom je die testcase hebt gekozen.


<!--
As you are about to find out, testing code with side effects is quite a bit more difficult and messy than the above. This is why it is good practice to separate things like prompts for input and prints for output to small separate functions. That way you can more easily test all your other code using short and simple tests like the above.

That said, you cannot always avoid IO (input-output). Below you will find how you can still test your functions even if they do contain IO side effects.
 -->

<!--### Testing with print statements (stdout)

What if a function is built around side effects? For instance, a function that prints output instead of returning a value. Something like the following:

    def is_divisible(numerator: int, denumerator: int) -> bool:
        """Tells the user whether denumerator divides the numerator.""
        if denumerator == 0 or int / denumerator != 0:
            print(f"{denumerator} does not divide {numerator}!")
        else:
            print(f"{denumerator} divides {numerator}!")

In this case we need our testing code to be able read from stdout. That is the output stream that Python's `print()` dumps its output to. `mypy` manages this with a special fixture called `capsys`. You can find the official docs [here](https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function). This is how you could use `capsys` to test the function `is_divisible` above:

    def test_myoutput(capsys):
        # execute the function is_divisible
        is_divisible(9, 3)

        # have capsys read from stdout (and stderr)
        captured = capsys.readouterr()

        # assert that exactly "9 divides 3!\n" was printed
        assert captured.out == "9 divides 3!\n"

> Note that you do not have to check for exact output. Python comes with a bunch of useful string functions that allow for rough comparisons. For instance, maybe you are satisfied with just the word "divides" being printed. You could test for this with `assert "divides" in captured.out`. Or perhaps you do not want to check with capitalization like so: `assert captured.out.lower() == "9 divides 3!\n"`. Or maybe it is fine that a newline is omitted? `assert captured.out.strip() == "9 divides 3!"`


### Testing with user input (stdin)

In Python you can prompt a user for input with the function `input`. This function will wait until the user has typed something and hit Enter. Underneath the hood `input` reads its input from another stream called `stdin`. `input` waits until it can read anything from `stdin`.

This waiting behavior of `input` is almost always unwanted in an automated testing environment. After all nobody wants their tests to hang indefinitely. That is why the creators of `pytest` disable the `input` function by default. This is what you'll see if you run tests while the code contains a call to `input`:

    $ echo "input()" >> foo.py
    $ echo "def test_foo():\n    import foo" >> "test_foo.py"
    $ pytest
    ...
    OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.
    ...

But what if we do want to test code with a call to input? Perhaps the following function:

    def get_positive_number():
        number = -1
        while number < 0:
            number = int(input("Enter a positive number: "))
        return number

If we want to test this function, we are going to have to mock `stdin`. In other words, change `stdin` to something else that closely resembles the `stdin` and does what we want it to do for the tests. Mocking is a common practice in software testing, especially in larger projects with various components. For instance, if our program works with a live database, we probably want to create a mock database that contains just the items we want for our tests.

Mocking or otherwise changing code while the code is running is called [monkey patching](https://en.wikipedia.org/wiki/Monkey_patch). `pytest` provides a `monkeypatch` fixture for this that we can use like so:

    from wherever_get_positive_number_is_defined import get_positive_number
    import io

    def test_get_positive_number(monkeypatch):
        # Mock stdin with another file-like object containing just the string 10
        mock_stdin = io.StringIO("10")

        # Monkey patch sys.stdin (stdin) to our new mock_stdin
        monkeypatch.setattr("sys.stdin", mock_stdin)

        # Test whether get_positive_number reads our input correctly
        assert get_positive_number() == 10

> For the technically curious, `sys.stdin` is how you would access `stdin` in Python. Do not forget to `import sys` first. `io` is a Python module for dealing with input-output streams. You can find the docs [here](https://docs.python.org/3/library/io.html).

-->
