# similarity

Een vaak voorkomend probleem binnen zoekmachines en aanbevelingssystemen is resultaten vinden die lijken op wat je zoekt, of op wat je hebt bezocht/gekocht. Daar zijn veel technieken voor, maar in de basis is er een maat nodig om gelijkenis in uit te drukken.

Hebben we het over tekst, dan is één zo'n maat de "Jaccard index". Kort gezegd, hoeveel woorden komen er overeen tussen twee stukken tekst? Deze optelsom wordt vervolgens genormaliseerd, teruggebracht naar een getal tussen de 0 en 1, door te delen door het totaal aantal unieke woorden in de twee teksten. Dit ziet er zo uit:

    jaccard_index = aantal_unieke_overeenkomende_woorden / aantal_unieke_woorden

Implementeer de volgende functies in een bestand genaamd `jaccard.py`:

    def convert_to_words(text: str) -> set[str]:
        """
        Returns a set of words from the text.

        This uses a simple language-independent definition of a word
        as groups of consecutive letters.
        """

    def compute_jaccard_similarity(text1: str, text2: str) -> float:
        """
        Returns a text similarity score of 0-1.

        This uses the Jaccard similarity measure. That is the number
        of shared unique words divided by the total number of unique words.
        """

## Testen

Schrijf in een apart bestand `test_jaccard.py` minimaal vier tests voor iedere functie (acht aparte test functies in totaal).