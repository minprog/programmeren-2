# Weken

Schrijf in een bestand genaamd `weken.py` een functie genaamd `weeks_elapsed`. Start met onderstaande code:

    def weeks_elapsed(day1: int, day2: int) -> int:
        """
        day1 and day2 are days in the same year. Return the number of full weeks
        that have elapsed between the two days.
        """

    if __name__ == "__main__":
        day1 = int(input("Dagnummer 1: "))
        day2 = int(input("Dagnummer 2: "))
        result = ...
        print(f"Er zijn {result} volle weken verstreken.")

> Je kan het programma vervolgens runnen met `python3 weken.py`.

## Testen

Schrijf in een apart bestand `test_weken.py` minimaal drie tests (vier aparte test functies) voor de functie `weeks_elapsed`. Eentje krijg je alvast kado:

    from weken import weeks_elapsed

    def test_exactly_two_weeks_passed():
        assert weeks_elapsed(18, 4) == 2

> Je kan de tests runnen met `pytest test_weken.py`