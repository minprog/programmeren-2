# Flexible typing

Sometimes your code isn't as clean as it could be and you require types to be a bit more flexible. Python provides a few mechanisms to provide this flexibility. [(Here are the official docs.)](https://docs.python.org/3/library/typing.html#special-forms)

## Any

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

## Union

For instance, in some cases a function might be able to cope with multiple types. Effectively one type or the other. `Union` handles this like so:

    from typing import Union

    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

> Starting in Python 3.10, `Union[int, float]` can also be written as `int | float`

## Optional

Sometimes it is uncertain whether a function will return a value. Let's say we are looking for the location of a needle in a haystack. It might be in the haystack, it might also not be. In case it is not, it is a common (not necessarily best) practice to return `None`. That is what `Optional` captures, either a value is returned, or `None`.

    from typing import Optional, Sequence, TypeVar

    T = TypeVar("T")

    def find_index(haystack: Sequence[T], needle: T) -> Optional[int]:
        for i, hay in enumerate(haystack):
            if hay == needle:
                return i
        return None

> `Optional[int]` is equivalant to `Union[int, None]`. In that sense, it is entirely optional to use.

<!--

## Callable

Functions can be passed to other functions too. That is what `Callable` captures in Python.

    from typing import Callable

    def get_hashes(number: int) -> str:
        return "#" * number

    def get_stars(number: int) -> str:
        return "*" * number

    def create_pyramid(create_layer: Callable[[int], str], height) -> str:
        pyramid = ""
        for i in range(1, height + 1):
            pyramid += create_layer(i) + "\n"
        return pyramid

    print(create_pyramid(get_hashes, 5))
    print(create_pyramid(get_stars, 5))

**Question**

Annotate the code below:

    def get(items, index):
        if index >= len(items):
            return None
        return items[index]

<textarea name="form[q5.1]" rows="4" required=""></textarea>

    def pick_one(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a
        return b

<textarea name="form[q5.2]" rows="5" required=""></textarea>

    def map(function, items):
        results = []
        for item in items:
            result = function(item)
            results.append(result)
        return results

<textarea name="form[q5.3]" rows="6" required=""></textarea>

-->
