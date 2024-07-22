# Duck typing

So far we have looked at concrete types, such as integers, strings and lists. These types are expressive, you know exactly what you are working with. But, often these concrete types limit design. Take for instance this function:

    def sum(items: list[int]) -> int:
        total = 0
        for item in items:
            total += item
        return item

There is no reason this implementation cannot work with other types of data structures. A tuple of integers or a set of integers should work just fine, but the type hint `list[int]` will only accept a concrete `list`. This is quite un-pythonic!

Looking at the implementation of `sum`, all that is needed from `items` is that it works with a for-loop. Or more precisely, the data structure needs to be iterable.

We could say that we only care about a property of the type of data structure, namely that it is iterable. We are not not necessarily interested in the concrete thing. Rather, if the type we insert into the function is somewhat list-like, the function should work just fine. In comes duck typing:

> if it walks like a duck, swims like a duck, and quacks like a duck... it's a duck.

We need a type that can swim, or in our case a data structure that is iterable. Whether that happens to be a swimming duck or a swimming fish in the end, that is irrelevant here. Luckily Python's `typing` module comes with a bunch of "duck types" built-in, one of which is `Iterable` that we can use like so:

    from typing import Iterable

    def sum(items: Iterable[int]) -> int:
        total = 0
        for item in items:
            total += item
        return item

Now any calls to `sum`, whether that'd be with a `tuple` or `set`, will all pass type checks. As all of these data structures are iterable! This form of abstract types is called structural subtyping. Alternatively, and probably easier to remember: **static duck typing**. This is done through creating a subtype that only contains some structural aspect of the original type. For instance, `Iterable` is a subtype with only the method `__iter__` (Python's hidden method for iterable things). So as long as the actual type implements `__iter__` any type check will pass.

The `typing` module provides more duck types, most notably: `Sequence` and `Mapping`. `Sequence` is a duck type for anything that keeps an order and is index-able. Lists and tuples are `Sequence`s, but a `set` for instance is not.

    from typing import Sequence

    a: Sequence[int] = [1, 2, 3]  # All good
    b: Sequence[int] = (1, 2, 3)  # All good
    c: Sequence[int] = {1, 2, 3}  # Incompatible types in assignment (expression has type "Set[int]", variable has type "Sequence[int]")

`Mapping` is a generic type for structures that map one value to another, such as dictionaries for instance.

    from typing import Mapping

    a: Mapping[str, int] = {"foo": 1}  # All good

<details markdown="1"><summary  markdown="span">For the technically curious...</summary>

These abstract data types are implemented as so called `Protocols`. See this [Python Enhancement Proposal](https://www.python.org/dev/peps/pep-0544/). Through these Protocols you can define your own duck types too. For instance:

    from typing import Iterable, Protocol

    class SupportsAdd(Protocol):
        def __add__(self, other):
            pass

    def sum(items: Iterable[SupportsAdd]) -> SupportsAdd:
        total = None
        for item in items:
            if total is None:
                total = item
            else:
                total += item
        return item

    sum([1, 2, 3]) # all good
    sum([1.5, None]) # error: List item 1 has incompatible type "None"; expected "SupportsAdd"

</details>

**Question**

Annotate the code below with duck types instead:

    T = TypeVar("T")

    def reverse(items: list[T]) -> list[T]:
        new = []
        for item in items:
            new.insert(0, item)
        return new

<textarea name="form[q4.1]" rows="5" required=""></textarea>

    T = TypeVar("T")

    def select(items: list[T], indices: list[int]) -> list[T]:
        selection = []
        for index in indices:
            selection.append(items[index])
        return selection

<textarea name="form[q4.2]" rows="5" required=""></textarea>

    T = TypeVar("T")

    def filter(items: list[T], allowed: dict[T, bool]) -> list[T]:
        new = []
        for item in items:
            if allowed[item]:
                new.append(item)
        return new

<textarea name="form[q4.3]" rows="6" required=""></textarea>
