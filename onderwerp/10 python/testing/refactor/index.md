# Once more with tests

Refactor your code from `mario`, `readability` and `dna` with `pytest` unit tests. Write these tests in a file called `test_mario.py` for each assignment respectively. It is up to you design the tests for each assignment, but you can take inspiration from the various test cases supplied with each assignment.

Upon submission we will run your test cases against various buggy and correct submissions. You can download all these submissions like so:

> **IMPORTANT** Do not download or look at these submissions before you have implemented and submitted your own implementation of `mario`, `readability` and `dna`. Needless to say, these submissions are full of spoilers!

    TODO DOWNLOAD LINK
    

## Testing without side effects

Testing a so called "pure" function, that is a function without any side effects, is a relatively straight forward task. For instance, take this function:
 
    def is_divisible(numerator: int, denumerator: int) -> bool:
        """Returns True if denumerator divides numerator, False otherwise.""
        if denumerator == 0:
            return False
        return int / denumerator == 0

We could test this function by calling it with different inputs and by expecting various outputs. Perhaps something like the following:

    from wherever_divisible_is_defined import is_divisible

    def test_divisible():
        assert is_divisible(9, 3) == True

    def test_is_not_divisible():
        assert is_divisible(8, 5) == False

    def test_dividing_by_zero():
        assert is_divisible(4, 0) == False

As you are about to find out, testing code with side effects is quite a bit more difficult and messy than the above. This is why it is good practice to separate things like prompts for input and prints for output to small separate functions. That way you can more easily test all your other code using short and simple tests like the above.

That said, you can't always avoid IO (input-output). Below you'll find how you can still test your functions even if they do contain IO side effects.


### Testing with print statements (stdout)

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

> Note that you don't have to check for exact output. Python comes with a bunch of useful string functions that allow for rough comparisons . For instance, maybe you are satisfied with just the word "divides" being printed. You could test for this with `assert "divides" in captured.out`. Or perhaps you don't want to check with capitalization like so: `assert captured.out.lower() == "9 divides 3!\n"`. Or maybe it's fine that a newline is omitted? `assert captured.out.strip() == "9 divides 3!"`


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

> For the technically curious, `sys.stdin` is how you'd access `stdin` in Python. Don't forget to `import sys` first. `io` is a Python module for dealing with input-output streams. You can find the docs [here](https://docs.python.org/3/library/io.html).
