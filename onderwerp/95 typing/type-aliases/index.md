# Aliases and generics

## Generics

How do you write your own generic functions? In Python that requires type variables. There is a special syntax for adding these type variables to a function:

    def first[T](items: list[T]) -> T:
        return items[0]

`first` will return the first item in the list, but what type is returned is dependent on the list. For instance, if `first` is called like so:

    n = first([1,2,3])

Then `n` will be of type `int`. Because a `list[int]` is passed in and `T` will take on the form of `int`. `T` is what is ultimately returned from `first` and that is then why `n` is an `int`.

Type variables can be used outside generic data structures too, for instance:

    def longest[T](a: T, b: T) -> T:
        return a if len(a) >= len(b) else b

This function will work for any type T, and it will return that same type.

**Question**

Annotate the generic function below with a type variable:

    def repeat(x, n):
        return [x] * n

<textarea name="form[q3]" rows="2" required=""></textarea>
