# Type hints

A type hint in the simplest form looks like this:

    foo: int

All this says is, the type of the variable `foo` should be an integer. Notice how there is no initial value here. This line of code does not create a variable `foo`, all it does is add a hint that `foo`, once it exists, should be an integer. That means this will raise a `NameError`:

    $ python3
    >>> foo: int
    >>> foo
    NameError: name 'foo' is not defined

It is possible to combine type hints and initialization on the same line, like so:

    foo: int = 3

That looks somewhat redundant, doesn't it? How can the _literal_ value `3` be anything else than an integer? This is where type inference kicks in. Tools will try to infer the types of variables from their use. It is quite safe to assume type inference is possible here, so probably best to just write:

    foo = 3

Type inference does have its limitations, for instance `mypy`, a popular static type checker for Python, will not do any type inference in functions without type hints. To understand why, let's quickly look into function type hints. In the simplest form:

    def add(a: int, b: int) -> int:
        c = a + b
        return c

The syntax above is straight forward, use the colon (`:`) for parameter type hints, and the arrow (`->`) for the return type. Notice how the type of `c` is not annotated. It can be, but it is not needed. From the types of `a` and `b` and the `+` operation, `mypy` can infer the type of `c`. But what if we did not annotate this function. Well, in that case, `a` and `b` could be anything: `str`, `float`, `list`, you name it! This is where `mypy` draws a line, if you do not annotate a function, `mypy` will not even attempt to do type inference. Instead all variables will be of type `Any`.

What is `Any`? Well, anything really. It is an escape hatch of sorts that provides no information. Once `Any` gets involved type checking becomes rather impossible. What is `Any + int`? `Any`.

**Question**

Annotate the `factorial` function below by adding as many type hints as needed:

    def factorial(num):
        total = 1
        for i in range(2, num + 1):
            total *= i
        return total

## Collection types

Integers, floats, booleans and strings are primitive data types. Built into the language, they serve as building blocks for more complex data structures. For instance, you might need a `list` to store your data.

    numbers: list = [1, 2, 3]
    number = numbers.pop()

Here is the catch, the type `list` does not tell _anything_ about what is in the `list`. So really what we have here is a `list` containing `Any`. In this case the type of `number` would be `Any` too.

A `list` is a generic data type. It can store various types, but its operation will vary based on what you store. Simply put for a `list`, if you initially store integers in the list, you will later be able to retrieve integers from that list. This can be annotated as follows:

    numbers: list[int] = [1, 2, 3]
    number = numbers.pop()

Now `numbers` is defined as a list of integers, and through that `number` will be of type `int` too.

Let's take a quick look at `dict`. Dictionaries have two types, their keys and values. This is how that can be annotated:

    grades: dict[str, int] = {"Martijn": 7, "Marleen": 8}

Tuples are an immutable data structure, once initialized it cannot be changed. So it is known up front exactly what the type of each value in the tuple is going to be. Because of this the `tuple` type can a variable amount of generic anotations with exactly as many types as there are values. Like so:

    foo: tuple[int, float] = (7, 7.2)
    bar: tuple[int, float, str] = (8, 7.9, "hello world")
    baz: tuple[int, int, int] = (1, 2, 3)

What about nested data structures?

    stats: dict[str, tuple[int, float]] = {"Martijn": (7, 7.2), "Marleen": (8, 8.1)}

Again, in most situations `mypy` can infer the types of the variables, and it is not strictly needed to annotate each data structure for type checking. That said, especially when it comes to data structures, annotations make the code easier to understand.

**Question**

Annotate the data structures below:

    foo = ["hello", "world"]

    bar = [("Martijn", 1), ("Marleen", 2)]

    baz = {1: {2: {3: "hello"}}}

## Type aliases

You can define your own type in case your type hints get too large:

    def create_structure(input: list[list[tuple[int,str]]]) -> dict[int, list[str]]

If you are using such types in your function headers, chances are that you're using such complex combinations elsewhere in your code, too. It may be better to define a type alias:

    MyStructure = dict[int, list[str]]

(This looks like a variable assignment but it is indeed used to define a new named type.)

Now you can use that alias in your code:

    def create_structure(input: list[list[tuple[int,str]]]) -> MyStructure

## Flexible typing

Sometimes your code isn't as clean as it could be and you require types to be a bit more flexible. Python provides a few mechanisms to provide this flexibility. [(Here are the official docs.)](https://docs.python.org/3/library/typing.html#special-forms)

### Any

The ultimate flexibility is provided by `Any`. It allows objects of any type to be processed by your code:

    from typing import Any

    def is_empty(thing: Any) -> bool:
        if thing == ""
            return True
        elif statement == []
            return True
        elif statement == "emptyness":
            return True
        else:
            return False

However, in most cases we consider using `Any` a form of cheating. After all, you have used strict typing in C, mustn't it be possible to keep it that way in Python, too?

### Union

For instance, in some cases a function might be able to cope with multiple types. Effectively one type or the other. `Union` handles this like so:

    from typing import Union

    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

Starting in Python 3.10, `Union[int, float]` can also be written as `int | float`

### Optional

Sometimes it is uncertain whether a function will return a value. Let's say we are looking for the location of a needle in a haystack. It might be in the haystack, it might also not be. In case it is not, it is a common (not necessarily best) practice to return `None`. That is what `Optional` captures, either a value is returned, or `None`.

    from typing import Optional

    def find_index(haystack: [int], needle: int) -> Optional[int]:
        for i, hay in enumerate(haystack):
            if hay == needle:
                return i
        return None

`Optional[int]` is equivalant to `Union[int, None]`. In that sense, it is entirely optional to use.
