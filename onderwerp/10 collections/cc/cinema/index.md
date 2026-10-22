# Cyclomatic Complexity: Bioscoop

Dit is een extra oefening bij de [workshop over Cyclomatic Complexity](/onderwerp/collections/cc). Heb je de opdracht over Hangman afgerond, of wil je de techniek nog eens oefenen? Dan is dit een goed vervolg. Je werkt hier met dezelfde tool (`flake8`) en hetzelfde doel: elke functie krijgt een Cyclomatic Complexity van maximaal 3.

Deze opdracht is de makkelijkste van de extra opdrachten. Er komt geen bestand of willekeur aan te pas, maar het programma zit vol met beslissingen: leeftijdscategorieën, dagen, tijdstippen en kortingen.

## De opdracht: Bioscoop

Hier vind je de code van een kassa voor een bioscoop (`cinema.py`). Je geeft de dag, het tijdstip, of het een 3D-film is en het aantal kaartjes in. Vervolgens geef je voor ieder kaartje de leeftijd van de bezoeker op en krijg je de prijs te zien. Aan het einde volgt het totaalbedrag. Dit zijn de regels:

* Een kaartje kost (in euro's) 0,00 tot en met 2 jaar (`infant`), 6,00 tot en met 11 jaar (`child`), 10,00 tot en met 64 jaar (`adult`) en 7,50 vanaf 65 jaar (`senior`).
* Een volwassene met een studentenkaart krijgt 1,50 korting (`student`).
* Kaartjes voor `infant`s zijn altijd gratis, toeslagen en kortingen gelden niet.
* Op zaterdag en zondag is een kaartje 1,00 duurder, op dinsdag 2,00 goedkoper.
* Begint de film voor 12 uur dan is een kaartje 1,00 goedkoper, vanaf 18 uur 1,50 duurder.
* Een 3D-film kost 2,00 extra per kaartje.
* Bij 4 kaartjes of meer is er 10% groepskorting op het totaalbedrag.

Zo ziet een voorbeeld eruit:

    WELCOME TO THE CINEMA
    Which day? (monday-sunday)
    saturday
    At what hour does the movie start? (0-23)
    20
    3D movie? (y/n)
    y
    How many tickets?
    2
    Age of visitor 1?
    30
    Student card? (y/n)
    n
    Ticket 1: adult 14.50
    Age of visitor 2?
    8
    Ticket 2: child 10.50
    Total: 25.00

<details markdown="1"><summary markdown="span">cinema.py</summary>

    def cinema() -> None:
        print("WELCOME TO THE CINEMA")

        # Prompt and re-prompt for the day
        day = input("Which day? (monday-sunday)\n").lower()
        while day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
                          "sunday"):
            day = input("Invalid day! Please enter monday-sunday.\n").lower()

        # Prompt and re-prompt for the hour
        hour = int(input("At what hour does the movie start? (0-23)\n"))
        while hour < 0 or hour > 23:
            hour = int(input("Invalid hour! Please enter a number between 0 and 23.\n"))

        # Prompt for 3D
        is_3d = input("3D movie? (y/n)\n")
        while is_3d != "y" and is_3d != "n":
            is_3d = input("Please answer y or n.\n")

        # Prompt and re-prompt for number of tickets
        tickets = int(input("How many tickets?\n"))
        while tickets < 1 or tickets > 10:
            tickets = int(input("Invalid amount! Please enter a number between 1 and 10.\n"))

        total = 0
        for number in range(1, tickets + 1):
            # Prompt and re-prompt for age
            age = int(input(f"Age of visitor {number}?\n"))
            while age < 0 or age > 120:
                age = int(input("Invalid age! Please enter a number between 0 and 120.\n"))

            # Base price per age group
            if age < 3:
                price = 0
                group = "infant"
            elif age < 12:
                price = 600
                group = "child"
            elif age < 65:
                price = 1000
                group = "adult"
            else:
                price = 750
                group = "senior"

            # Adults can have a student discount
            if group == "adult":
                student = input("Student card? (y/n)\n")
                while student != "y" and student != "n":
                    student = input("Please answer y or n.\n")
                if student == "y":
                    price -= 150
                    group = "student"

            # Infants always get in for free, others pay surcharges and discounts
            if price > 0:
                if day == "saturday" or day == "sunday":
                    price += 100
                elif day == "tuesday":
                    price -= 200

                if hour < 12:
                    price -= 100
                elif hour >= 18:
                    price += 150

                if is_3d == "y":
                    price += 200

            print(f"Ticket {number}: {group} {price // 100}.{price % 100:02d}")
            total += price

        # Groups of 4 or more get 10% off
        if tickets >= 4:
            discount = total // 10
            total -= discount
            print(f"Group discount: -{discount // 100}.{discount % 100:02d}")

        if total == 0:
            print("Total: free")
        else:
            print(f"Total: {total // 100}.{total % 100:02d}")


    if __name__ == '__main__':
        cinema()

</details>

Alles staat gepropt in één grote functie. De Cyclomatic Complexity van deze functie is:

    $ python3 -m flake8 --max-complexity 1 --select=C cinema.py
    cinema.py:1:1: C901 'cinema' is too complex (21)

Aan jou de taak om deze code te verbeteren op zo'n manier dat de Cyclomatic Complexity niet hoger dan 3 is. Dat betekent dat het volgende geen klachten meer geeft:

    $ python3 -m flake8 --max-complexity 3 --select=C cinema.py

## Bootstrappen

Kopieer de code van de bioscoop hierboven, maak een bestand genaamd `cinema.py` en plak daar de code in. Draai `python3 -m flake8 --max-complexity 3 --select=C cinema.py` om te kijken of de tool werkt. Je hoort het volgende te zien:

    cinema.py:1:1: C901 'cinema' is too complex (21)

Draai het programma met `python3 cinema.py` en probeer een paar verschillende kaartjes uit, zodat je een gevoel krijgt voor de regels.

## What to do

Het doel is de Cyclomatic Complexity onder de 3 te krijgen voor het gehele programma. Dat kan je doen door:

1. De code op te breken in kleinere functies
2. De code zelf eenvoudiger te maken waardoor er minder paden mogelijk zijn.

Kijk goed naar wat er in de code vaak terugkomt. Er zijn een paar stukjes code die op elkaar lijken. Ook staan er beslissingen in die eigenlijk een opzoektabel zijn. Doe het stap voor stap, één functie per keer, en blijf goed testen tussendoor.

<details markdown="1"><summary markdown="span">hint: herhaalde code</summary>

Het programma vraagt een paar keer om een getal binnen een bereik, en een paar keer om een ja/nee-antwoord. Zoek de herhaling op en maak er functies van die je meerdere keren kan gebruiken, bijvoorbeeld `ask_int(prompt, error, low, high)`. Let op dat de teksten van de prompts precies hetzelfde blijven.

</details>

<details markdown="1"><summary markdown="span">hint: if/elif-ketens</summary>

Een lange `if`/`elif`-keten die een waarde uitkiest op basis van een andere waarde, kan vaak veel korter met een `dict` of een tuple met tuples. Een `dict` heeft bovendien `.get(key, default)`, waarmee je zelfs de 'anders'-situatie niet met een `if` hoeft op te lossen.

</details>

<details markdown="1"><summary markdown="span">hint: stap voor stap rekenen</summary>

Het uitrekenen van de prijs van één kaartje is een apart stukje werk: leeftijd erin, prijs eruit. Hetzelfde geldt voor het bepalen van de toeslag voor het tijdstip. Als functies maar één ding doen, hoeven ze ook niet veel keuzes te maken.

</details>

## Spelregels

* De output van het programma moet exact hetzelfde blijven. Bij het inleveren checken de checks dit ook.
* Alle code moet in één bestand staan: `cinema.py`.
* Alle code mag worden gewijzigd.
* De Cyclomatic Complexity mag voor geen enkele functie hoger zijn dan 3.
* De type hints moeten blijven kloppen: de checks draaien ook `mypy` en `pycodestyle`.

## Tips

* Hou een tweede bestand bij, bijvoorbeeld `cinema_old.py`, met de originele versie van de code. Dan kan je beide versies met dezelfde invoer uitvoeren en makkelijker zien of het programma nog steeds precies hetzelfde doet.
* Maak een bestand `invoer.txt` met per regel één antwoord, en draai `python3 cinema.py < invoer.txt`. Dan hoef je niet steeds alles opnieuw in te typen.
* Test ook de randgevallen: een ongeldige dag, een uur dat net op de grens zit (11, 12, 17, 18), en een leeftijd die precies op de grens tussen twee categorieën zit.
* Lever je code ook eens vroegtijdig in. De checks geven feedback als de output niet helemaal klopt.
