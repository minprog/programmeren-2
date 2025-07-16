# slice

Python strings en lists kennen ook slicing. Hier vind je een korte uitleg op [Stack Overflow](https://stackoverflow.com/a/509295).

Implementeer de volgende functie in een bestand genaamd `slice.py`:

    def slice(string: str, start: int=0, end: int|None=None) -> str:
        """
        Returns the substring of string between index start (inclusive)
        and end (exclusive).
        start is 0 if not given, and end is len(string) if not given.
        Both start and end can be any number between -len(string)
        and len(string) - 1
        """

> Implementeer de functie **zonder gebruik te maken van slicing**. Het doel is dat jouw functie precies hetzelfde doet als slicing in Python. Probeer daarom slicing wel uit om goed te begrijpen wat er moet gebeuren in verschillende gevallen. Bijvoorbeeld, wat is de uitkomst van `string[-10:-20]`?

> De functie `slice()` heeft zogenaamde optionele argumenten. Deze functie kan je met of zonder de argumenten aanroepen, bijvoorbeeld: `slice("hello")`, `slice("hello", 2)`, `slice("hello", 2, -1)`, `slice("hello", end=3)` 

> `None` is de niks waarde in Python. Gebruik de `is` operator om te vergelijken met `None`, bijvoorbeeld `if end is None:`. 

## Testen

De functie `slice` neemt maar liefst drie parameters aan. Dat geeft veel input om te testen:

De parameter `string`:

- Een string met één of meer karakters
- Een lege string

De parameter `start`:

- Een positieve index (bijvoorbeeld `2`)
- Een negatieve index (bijvoorbeeld `-2`)
- Een randgeval: index `0`
- Een extreem positief randgeval: index `len(string) - 1`
- Het andere extreme negatieve randgeval: index `-len(string)`

De parameter `end`:

- Geen `end`, de paramteter wordt niet meegegeven
- Een positieve index (bijvoorbeeld `2`)
- Een negatieve index (bijvoorbeeld `-2`)
- Een randgeval: index `0`
- Een extreem positief randgeval: index `len(string) - 1`
- Het andere extreme negatieve randgeval: index `-len(string)`

Voor een complete test zou je alle combinaties van input testen. Dat is effectief alle vormen van `string` maal alle vormen van `start` maal alle vormen van `end`: 2 x 5 x 6 = 60 test cases. Je ziet hier dat functies met veel parameters al snel niet meer compleet te testen zijn omdat het aantal test cases explodeert. Andersom, een manier om code beter testbaar te maken is functies op te hakken in kleinere functies met minder parameters.

Nu is 60 test cases met de hand schrijven niet goed doenbaar en vaak ook niet bepaald nuttig. Zowel niet als oefening als in de praktijk:

- Te veel werk t.o.v. het programmeren van de functie zelf.
- Veel test cases, dus het duurt langer om de tests te draaien, daardoor ga je de tests niet meer draaien.
- Moet er iets veranderen aan de code, mag je waarschijnlijk ook 60 test cases herschrijven.

Nu zou je verleidt kunnen worden om een ingewikkelde test case te schrijven die door middel van bijvoorbeeld loops alle 60 test cases afloopt. Bijvoorbeeld:

    def test_everything_everywhere_all_at_once():
        for string in ["foo", ""]:
            for start in [2, -2, 0, len(string) - 1, -len(string)]:
                for end in [None, 2, -2, 0, len(string) - 1, -len(string)]:
                    assert slice(string, start, end) == string[start:end]

Dit brengt wel nadelen met zich mee en is daarom vaak niet aan te raden:

- Ingewikkelde test case => ingewikkeld debuggen
- Hoe ingewikkelder de test, hoe groter de kans op een bug in de tests. En wie test de tests?
- Veel test cases, dus het duurt langer om de tests te draaien, daardoor ga je de tests niet meer draaien.
- Niet altijd goed mogelijk: In dit geval mazzel want alle combinaties van input zijn mogelijk, en bestaat er een implementatie om tegenaan te testen (Python's ingebouwde slicing).

Natuurlijk zijn er situaties te bedenken waarin de compleetheid van tests opweegt tegen alle nadelen (raket naar de maan sturen bijvoorbeeld). Maar vaker dan niet is het verstandiger om te kiezen in wat je test.

**TODO** Schrijf in een apart bestand `test_slice.py` minimaal zes tests in totaal (zes aparte test functies) voor de functie `slice`. Kies deze zes tests als volgt:

* De tests voeren gezamenlijk zoveel mogelijk code uit, het zogenaamde "test coverage". Praktisch iedere regel code wordt uitgevoerd door de tests.
* Kies voor belangrijke of wellicht verassende edge cases. Hier hebben tests ook een documentatie functie, je legt vast wat een functie moet doen met een eigennaardige input.