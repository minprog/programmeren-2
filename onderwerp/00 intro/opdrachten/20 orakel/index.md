# Orakel

Schrijf een programma `orakel.py` dat controleert of een door de gebruiker ingevoerde string één van de volgende is:

* 42
* tweeenveertig
* tweeënveertig

Het programma moet niet case-sensitive (hoofdlettergevoelig) zijn. Dus TweeenVeertig is ook een goed antwoord. Wordt één van de drie antwoorden hierboven ingevoerd, dan print het programma Ja, anders Nee. Het programma moet als volgt werken:

    $ python3 orakel.py
    Wat is het antwoord op de grote vraag? 42
    Ja

    $ python3 orakel.py
    Wat is het antwoord op de grote vraag? 43
    Nee

Implementeer en gebruik in je programma de volgende functie:

    def check_answer(answer: str) -> bool:
        pass

> Vergeet niet gebruik te maken van `if __name__ == "__main__":`.

## Testen

Schrijf in een apart bestand `test_orakel.py` minimaal vier tests (vier aparte test functies) voor de functie `check_answer`.

