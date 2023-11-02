
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
