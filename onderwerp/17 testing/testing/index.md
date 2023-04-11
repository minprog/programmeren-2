# Testing

Discovering bugs isn't easy, but it sure is easy to introduce bugs! Up to this point you've likely dabbled with manual testing to uncover any faults and bugs in your code. By quickly running your code with various inputs like so perhaps:

    $ python3 foo.py 4
    4
    $ python3 foo.py 5
    1
    $ python3 foo.py -1
    Sorry, can't handle negative numbers!

Makes sense right, because while you are working on a problem or assignment you are the expert right then and there. You'll know what the output should be and how the code should behave at that point. So quickly call your function, see what it does and if all looks good, well, submit it, done.

That is, until assignments grow a little. Maybe there's some teamwork involved. Maybe your code is part of a bigger program that is used for many years. That's where things start to get tricky. As more code is added, there's more room for bugs to hide and even more to test. Quickly it becomes impossible to test everything by hand.


### Automatic testing

Let's automate this. Now there are many things to test when it comes to software. Here's a quick overview:

* Does the program do what we want it to do? Testing for this is called functional testing.
* But we might also be interested in performance metrics or security concerns. Things that aren't directly tied to functionality. Unsurprisingly, this is called non-functional testing.

There exists several strategies to go about testing:

* We can test the system as a whole. In other words, run the entire program and see if it does what it should do. This is called system testing. While useful, it is often difficult to test every part of the program this way.
* Zooming in, whatever you write is likely part of a bigger program, and well, it needs to fit into this bigger program. This is called integration testing.
* Finally, there's the code you write, the smaller functions and modules. Testing these individually is called unit testing.

For this module we will narrow our scope to unit testing. Testing small individual units of a program. These could be functions, classes, modules, you name it. The goal of this type of testing is ensuring, or rather re-assuring, that each unit of the program functions as desired.


### Unit testing

Effectively unit testing does not need to be much more than writing a script that calls your unit of code, and checks that it does what it's expected to do. Let's get started with an example, `get_median()`. There's a list of things of which we need the median.


    def get_median(items: list[int]) -> int:
        size = len(items)
        middle = size // 2
        return items[middle]
    

Now we could write a seperate script to automatically test this for us. Let's say we create a file called `test_median.py`:

    from median import get_median
    
    items = [1,2,3,4,5]
    expected_median = 3
    assert get_median(items) == expected_median

There we go, one unit test. Running this file will either succeed silently or you'll find an `AssertionError`. But, there's probably more to test. Does this function work with various numbers of items? What about an empty list of items? We could append more assertions, but it does get unwieldy fast. Not only because if one assertion fails, everything stops running. But also because we are likely going to be writing the same code over and over for our tests.


## pytest

In comes `pytest`, one of many unittesting frameworks for Python, but arguably a popular and easy to use one. You do need to install it through `pip`:

    pip3 install pytest

Here's how it works. Every test file needs to start with the `test_` prefix, so `test_median.py` above will do just fine. Then, every test itself is a function also prefixed with `test_`. For instance, to pytest-ify our unit test above we can write:

    from median import get_median

    def test_odd_length():
        items = [1,2,3,4,5]
        expected_median = 3
        assert get_median(items) == expected_median

Once saved in a file called `test_median.py`, you can simply run `pytest` like so:

    $ pytest
    ========================= test session start =========================
    platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/foo
    collected 1 item

    test_median.py .                                                [100%]

    ========================== 1 passed in 0.02s =========================

A few things happened here. `pytest` went looking in the current directory for any test files, those starting with `test_`. Then ran each of those files looking for functions starting with `test_`. This process is generally called test discovery and different testing frameworks will have different ways of doing this. This is just how `pytest` does it.

Then, with our one test discovered, `pytest` will run the test. For convenience, `pytest` uses Python's built-in `assert` statements. Other frameworks might have their own assertion methods. So all `pytest` does here is run the function and if an assertion fails, the test fails and otherwise it succeeds. In this case 100%, all of 1 test succeeded!

### Testen van foute input

Soms wil je in je test controleren of een functie of programma een fout geeft in plaats van een juist antwoord. Stel dat we de volgende functie hebben:

    def get_median(items: list[int]) -> int:
        size = len(items)
        assert size > 0, "Cannot get a median from an empty list."
        middle = size // 2
        return items[middle]

Je kunt dan testen of de functie inderdaad stopt als er sprake is van een foute input:

    import pytest
    from median import get_median

    def test_empty():
        with pytest.raises(AssertionError):
            get_median([])

De test slaagt als nu de `assert` triggert en een `AssertionError` geeft. Als je de `assert` weglaat dan zal de test nogal hard falen (probeer het eens uit!).

### Exceptions

Naast assertions zijn er ook exceptions in Python. Eén manier om exceptions te gebruiken is om **foute user-input** af te vangen. Als een gebruiker iets fout doet dan wil je niet dat het programma crasht maar dat het probeert er toch maar het beste van te maken. In dit voorbeeld zie je dat we om input vragen, graag een gewoon getal, maar we weten natuurlijk niet helemaal zeker of de gebruiker zich daar aan gaat houden. Daarom gebruiken we een exception om dit mogelijke probleem "af te vangen" (catchen). Daarvoor is de `try`-`except`-constructie.

    text = input("give me a number")
    try:
        number = int(text)
    except ValueError:
        number = 0

Een dergelijk gebruik van exceptions gaan we niet testen (omdat er sprake is van user input, wat erg lastig is om te simuleren in een test), maar exceptions kunnen op meer manieren gebruikt worden.

### Ask for forgiveness

In Python is het principe "it's often easier to ask forgiveness than to get permission" één van de leidraden bij het schrijven van code. In het bovenstaande voorbeeld is het moeilijk om elk geval voor te stellen waarin we een string kunnen omzetten in een geheel getal. De string mag alleen uit cijfers bestaan, maar een `.` is ook toegestaan. Maar niet meer dan één `.` hoor! Voor je het weet ben je allerlei if-statements aan het schrijven om de input te valideren vóór je deze durft om te zetten naar een integer.

Wat nou als we proberen er een integer van te maken en kijken wat er gebeurt?

Dat is het idee van de code hierboven: je probeert het, en als het fout blijkt, dan probeer je dat probleem op een goede wijze op te lossen. Dat is het "asking for forgiveness"-deel.

### Exceptions vs assertions

Exceptions vervullen in Python vaak dezelfde functie als assertions. Je zult ze door elkaar tegenkomen. We raden je voor nu aan om `assert`-statements te schrijven met een korte goede foutmelding, waardoor jij als programmeur snel kan achterhalen wat er mis is. Later kun je ook exceptions gaan schrijven volgens de Python-filosofie.

Voor nu is het vooral belangrijk dat je weet hoe je functies moet testen die ook exceptions kunnen geven. Stel dat we het programma van hierboven herschrijven met een excetpion:

    def get_median(items: list[int]) -> int:
        size = len(items)

        if size == 0:
            raise ValueError("Cannot get a median from an empty list.")

        middle = size // 2
        return items[middle]

Ook deze kunnen we testen:

    import pytest
    from median import get_median

    def test_empty():
        with pytest.raises(ValueError):
            get_median([])

Net als bij de `AssertionError` zal de test slagen als er een `ValueError` wordt gegeven.

### Exceptions vs assertions

In eerdere opdrachten heb je kennis gemaakt met assertions die je in je eigen code plaatst, die het programma stoppen als er iets onmogelijks gebeurt.


In een later stadium kun je ook exceptions gebruiken op de manier waarop deze in Python vaak gebruikt worden. Dit vereist wat meer ervaring met het schrijven van Python-code, zodat je ruimte hebt om na te denken over wanneer je wel en niet exceptions moet gebruiken. In deze cursus wordt niet beoordeeld op het gebruik van exceptions, wel op het gebruik van assertions.

<!--
## Fixtures

Earlier we tested `get_median` with an input namely `[1,2,3,4,5]`. Odds are that almost every test you'll write needs some input, or rather some constant or fixed things that we are going to test with. Or in testing terminology, fixtures.

`pytest` has a simple way of handling fixtures. You mark a function as a fixture and can then use it as input of tests. Here's what it looks like:


    import pytest
    from median import get_median

    @pytest.fixture()
    def odd5():
        return [1,2,3,4,5]

    def test_odd_length(odd5):
        expected_median = 3
        assert get_median(odd5) == expected_median


Note a couple things, a fixture is marked with the `@pytest.fixture()` decorator. If you haven't seen this `@` syntax before, not to worry. All you need to know is, this marks the function below as a fixture. Then note `test_odd_length` accepts a parameter with the exact same name as the fixture above. That's how `pytest` knows what to pass in to your test.

But hang on, this is more lines of code than what we had before. Why should we want this? Several reasons actually. Perhaps the obvious reason is re-use of fixtures. If we're writing multiple tests, we can now easily use `odd5` as input for those tests. In this case the input is simply a list of numbers, but you can imagine this could be a very complex datastructure of several objects too. Perhaps more interestingly for our usecase, fixtures can be parameterized. Here's what that looks like:


    import pytest
    from median import get_median

    @pytest.fixture(params=[1, 3, 5, 7])
    def odd(request):
        return list(range(1, request.param + 1))

    def test_odd_length(odd):
        expected_median = odd[len(odd) // 2]
        assert get_median(odd) == expected_median


Now we're not just testing for 5 items, but rather 4 different odd lengths. The syntax is a little weird, with `params=`, `request` as a parameter to `odd()` and `request.param` as a way to access the parameter. But that's what it is.

If we run pytest with this code in `test_median.py` we'll see:

    $ pytest
    ========================= test session start =========================
    platform linux -- Python 3.9.0, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/foo
    collected 4 items                                                     

    test_median.py ....                                             [100%]

    ========================== 4 passed in 0.02s =========================

Even though the file contains 1 test function, 4 tests are run. One for each version of the fixture. In fact, any test function taking the fixture `odd` will now be called 4 times. This is a very quick way to test for many different inputs, without needing to write a lot of code!
-->
