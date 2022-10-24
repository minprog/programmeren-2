# Once more with functions and type hints

> **Individueel.**
>
> Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Refactor your code from `mario`, `readability` and `dna` with type hints. You can check for any missing types or type errors by running:

    mypy --strict mario.py

Or to check all python files in the current directory:

    mypy --strict .


## Functions first

If you have not already done so, make sure your most of your code resides inside functions and that any other code is run only when `__name__ == "__main__"`. For instance you might refactor `mario.py` to something resembling the following:

    def good_name_for_drawing_a_pyramid(height):
        # TODO

    def awesome_name_for_drawing_a_line(width):
        # TODO

    def great_name_for_getting_height_from_the_user():
        # TODO

    if __name__ == "__main__":
        height = great_name_for_getting_height_from_the_user()
        good_name_for_drawing_a_pyramid(height)


## What's up with `if __name__ == "__main__"`?

`__name__ == "__main__"` checks whether the hidden variable `__name__` is set to `"__main__"`. This will only be the case if that python file is run directly. 

For instance, in case of `foo.py`, Python will set its `__name__` to `"__main__"` if you run `python3 foo.py` from the command-line. You can check this by simply printing out `__name__` from `foo.py` like so:

    $ echo "print(__name__)" >> foo.py
    $ python3 foo.py
    __main__

However, if you run the file indirectly, by perhaps `import`ing `foo.py` in another python program called `bar.py`. And then by running `python3 bar.py` from the command-line. `foo.py`'s `__name__` would be `"foo"` instead of `"__main__"`. To see for yourself:

    $ echo "import foo" >> bar.py
    $ python3 bar.py
    foo

So why is this important? Well, Python will run any code in a Python source file upon importing. This is why we see `foo` printed even though the only code in `bar.py` is `import foo`. Now you can imagine that this is often unwanted. For instance, `bar.py` might want to reuse some code from `foo.py`, but not needlesly run all of the code inside `foo.py` and end up with prints on the screen. This is why it is good practice to "guard" any code that should only run if the user decides to run that file directly with `if __name__ == "__main__":`.  


> In short, `if __name__ == "__main__"` is Python's equivalent for a main function similar to languages like C & Java. Its use is optional, but generally good practica.
