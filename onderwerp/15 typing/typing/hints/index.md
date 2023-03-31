# Type hints in Python




## Abstract types

<details markdown="1"><summary  markdown="span">Structural subtyping aka duck typing</summary>



<details markdown="1"><summary  markdown="span">Nominal subtyping aka subclassing </summary>

Duck typing is great and all, but what if we actually do want a duck, not something that happens to act like a duck. For instance, let's say we are building a grading app and we have three user roles, `Teacher`, `Assistant` and `Student`. Implemented like so:

    class User:

    class Staff(User): pass

    class Teacher(Staff): pass

    class Assistant(Staff): pass

    class Student(User): pass

Through this we can write functions that only accept specific types of users. For instance:

    def view_grade(user: User) -> int: pass
    def add_grade(user: Staff) -> None: pass

This way the type checker will allow all three roles to view grades, but only the `Staff` roles can add a grade. This form of abstract types is called nominal subtyping, where that type or any subclass of that type is accepted.

</details>

<details markdown="1"><summary  markdown="span">Special types</summary>



