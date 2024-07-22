# Many submissions of cash

We asked students to implement the following function:

    def number_of_coins(change: int, coins: list[int]) -> int:
        """
        Given an amount of change in cents, and a list of coins in cents,
            calculate how many coins are needed to fulfill the change.
        Raises a TypeError in case floats are given instead of integers.
        Raises a ValueError in case of negative values, or coins of value 0.
        """

For example:

    print(number_of_coins(41, [25, 10, 5, 1])) # prints 4

To further restrict the assignment we added:

* You may assume that a greedy strategy (exchanging as many as possible of the largest exchangable coin first) will always yield the correct answer.
* You may assume that the user will never enter any other values than integers and floats.
* You may assume that the user will always enter a `list` of integers or floats for coins.
* In case the change cannot be met exactly, give as much as possible, without exceeding the total. For instance if there are only quarters (25) as coins and the change is 97, give 3 quarters,

At the end of the day, thirteen students submitted their work. You can find all thirteen implementations in the `submissions` folder. That leaves us with a challenge: grading. Which of these thirteen submissions are incorrect and why?

## Individuele opdracht

Samenwerken bij deze opdracht is niet toegestaan; het is prima om medestudenten en anderen om hulp te vragen, als het er maar niet op neerkomt dat iemand anders een deel van het werk voor je doet. Voorbeelden van "redelijke" en "onredelijke" manieren van samenwerken vind je in de studiewijzer.

Het is **niet** erg als het niet lukt om alles op te lossen. Je verdient snel punten hier en een deel oplossen is ook prima.


## What to do

[Download the distribution code](testing_cash.zip).

Write unittests in Pytest to test this assignment. Find out which submissions are correct or incorrect. In case a submission is incorrect, write down why (see report below). Submit all your unittests in a file named `test_cash.py` on the bottom of this page. 

## A bit of help

Hold on, before you jump right in, we have added some scaffolding to get you going. You will find two additional files:

1. `conftest.py`, long story short, this file contains some pytest specific code that adds a command line option to pytest (`--path`) and uses these paths to load in the student implementations of `number_of_coins`. These implementations are passed to any unittest requesting a `number_of_coins` fixture. Through this file you will able to write tests like so:


        def test_something(number_of_coins):
            assert number_of_coins(41, [25, 10, 5, 1]) == 4


    And call them like so:

        pytest --path submissions/1/cash.py
        pytest --path submissions/1/cash.py --path submissions/2/cash.py

2. Thirteen programs is a lot to test, and it is easy to get overwhelmed by the number of tests. `run_tests.py` is here to help. This script will run pytest for each submission in the `submissions` folder and dump the output of the test to `outputs/1.txt` (for each submission respectively). Just run it like so:

        $ python3 run_tests.py
        Testing - submissions/1/cash.py => outputs/1.txt   | SUCCESS
        Testing - submissions/2/cash.py => outputs/2.txt   | FAILED
        Testing - submissions/3/cash.py => outputs/3.txt   | SUCCESS
        ...

## Some peace of mind

* You may assume all implementations are deterministic, there is no randomness in any implementation.
* You may assume infinite loops do not exist.
* You may assume the student code does not contain anything malicious, so you can safely run it on your computer.
* We are pretty sure that only **one** submission is correct, but feel free to prove us wrong!
* The `12` incorrect submissions are incorrect in fundamentally different ways. You will likely need to write at least 12 test cases.

## Report

In a report (`.pdf`), write down for each of the 13 submissions whether it is correct or incorrect. Provide reasoning for each incorrect submission: how can we know, without doubt, that that submission is indeed incorrect? For example, you probably have found a test case that very specifically shows a wrong behavior based on how the program is tested.

Keep in mind that the wrong submissions are wrong in fundamentally different ways, so each submisison should require a different reasoning. This is why you need to write tests for each separate solution, but still keep all tests in the same test file. This way you can see that each test triggers on a different solution.
