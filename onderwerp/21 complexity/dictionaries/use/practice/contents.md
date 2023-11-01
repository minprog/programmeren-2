# Practice with dictionaries

> If there is an exercise that you don't know how to solve, review the theory again. If that doesn't help, discuss the exercise with another student and/or the teacher.

Test your understanding with the following practice exercises. Use your usual code editor and create a file called `dictionaries.py`.

**Exercise 1** Similar to the video, create a dictionary called `my_class` with students and grades. Use the names Ralph, Diana, Jordi, and Michele with their respective grades: 4, 8, 7, and 5.

**Exercise 2** Add a student Gretel to the above dictionary with a grade of 9. Print the dictionary `my_class` to check if Gretel is indeed added to the dictionary.

**Exercise 3** Write a piece of code that asks the user to input a name and looks in the dictionary `my_class` if the student exists. Print the message "[name] is a student in this class, and has the grade: [grade]." or "[name] is not a student in this class.", depending on whether or not the student is in the dictionary `my_class`. Example usage:

	python dictionaries.py
	Enter a name: Jordi
	Jordi is a student in this class, and has the grade: 7.

Use the `in` operator for this exercise. Do not use `get()`.

**Exercise 4** Use the following list of students:

	students = ["Michele", "Diana", "Maria", "Ralph", "Jacobus"]

Write a loop that looks up each student from the lists in `my_class` and prints "[name]: [grade]" on a new line for each student. If the student doesn't exist in `my_class` it should print the text "n/a" for the grade. Expected output:

	Michele: 5
	Diana: 8
	Maria: n/a
	Ralph: 4
	Jacobus: n/a

Use `get()` for this. Do not use an `if`-statement.
