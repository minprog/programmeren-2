# index

Python strings en lists kennen negatieve indices. Hier vind je de [officiële documentatie](https://docs.python.org/3/faq/programming.html#what-s-a-negative-index).

Implementeer de volgende functie in een bestand genaamd `index.py`:

    def value_at(string: str, index: int) -> str:
        """
        Returns the character at index in string.
        index can be any number between -len(string) and len(string) - 1
        """

> Implementeer de functie **zonder gebruik te maken van negatieve indices**. Je hoeft geen rekening te houden met een te grote of te kleine index.

## Testen

Schrijf in een apart bestand `test_index.py` minimaal vijf tests in totaal (vijf aparte test functies) voor de functie `value_at`. Gezien te grote of te kleine indices (illegale input) niet worden afgehandeld, hoeft er alleen te worden getest op kloppende indices (legale input). Kijkend naar de twee parameters en wat we daarvoor kunnen invoeren:

De parameter `string` is een `str` waaruit één karakter wordt opgehaald. Dan moet `string` tenminste één karakter hebben in de tests.

De parameter `index` moet een geldige index zijn, maar dit is een heel bereik van "-len(string) and len(string) - 1". Dat geeft een aantal interessante waardes om te testen:

- Een positieve index (bijvoorbeeld `2`)
- Een negatieve index (bijvoorbeeld `-2`)
- Een randgeval: index `0`
- Een extreem positief randgeval: index `len(string) - 1`
- Het andere extreme negatieve randgeval: index `-len(string)`