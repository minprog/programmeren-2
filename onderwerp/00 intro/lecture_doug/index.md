# Lecture Python

![embed](https://video.cs50.io/mgBpcQRDtl0)

## Correcties

Deze lecture (CS50 short) is alweer wat jaren oud. Dat betekent dat er intussen dingen zijn veranderd. Hieronder een aantal correcties.

### Onnodige terniary operator

Doug gebruikt het voorbeeld:

    all_letters = True if input().isalpha() else False

De methode `isalpha()` returned zelf al `True` of `False`, gebruik dus liever:

    all_letters = input().isalpha()

### Geen slice assignment

Doug gebruikt onderstaande om `5` toe te voegen aan een lijst genaamd `nums`.

    nums[len(nums):] = [5]

Dat kan, maar het is erg ongebruikelijk. Gebruik liever:

    nums.append(5)

Of als je twee lijsten wil samen voegen:

    nums = nums + [5]

### f-strings

Python 3.6 introduceerde f-strings en dat is nu de standaard om strings te formatten. Het filmpje gebruikt nog `.format` als volgt:

    "In {1}, {0} took office".format(president, year)

Gebruik liever:

    f"In {year}, {president} took office"

Let goed op de letter `f` voor het eerste `"`!