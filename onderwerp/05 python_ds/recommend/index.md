# Recommend

Een vaak voorkomend probleem binnen zoekmachines en aanbevelingssystemen is resultaten vinden die lijken op wat je zoekt, of op wat je hebt bezocht/gekocht. Daar zijn veel technieken voor, maar in de basis is er een maat nodig om overeenkomst in uit te drukken.

Hebben we het over tekst, dan is één zo'n maat het aantal overeenkomende woorden tussen twee teksten. Dit ga je bij deze opdracht gebruiken om films aan te bevelen aan een gebruiker op basis van het script van een andere film.

### 1. convert_to_words

Implementeer allereerst onderstaande functie in een bestand genaamd `recommend.py`. Deze functie moet een `set` van woorden teruggeven. We kiezen hier voor een `set` omdat we enkel geïnteresseerd zijn in de verschillende woorden in een tekst, en niet of ze meerdere keren voorkomen.

    def convert_to_words(text: str) -> set[str]:
        """
        Returns a set of words from the text.

        This uses a simple language-independent definition of a word
        as groups of consecutive letters.
        """

> <b>Let op!</b> Deze functie wordt straks onderdeel van een groter programma. Daarvoor is het belangrijk dat deze functie goed werkt, dat scheelt je straks veel zorgen. Schrijf daarom nu in een bestand genaamd `test_recommend.py` een aantal tests voor `convert_to_words`. Test tenminste een tekst met interpunctie, een tekst met meerdere woorden, en een tekst met interpunctie en meerdere woorden zoals: "Hello, world.-How is it going?".

### 2. compute_jaccard_index

Deze maat van overeenkomende woorden heeft een naam, de zogenaamde "Jaccard index". Kort gezegd, hoeveel <b>unieke</b> woorden komen er overeen tussen twee stukken tekst? Zou dit alleen een optelsom zijn, dan word dit getal van nature hoger voor langere teksten. Daarom wordt de optelsom genormaliseerd, teruggebracht naar een getal tussen de 0 en 1. Dit doen we door te delen door het totaal aantal unieke woorden in de twee teksten. Dit ziet er zo uit:

    jaccard_index = aantal_unieke_overeenkomende_woorden / totaal_aantal_unieke_woorden

    def compute_jaccard_index(text1: str, text2: str) -> float:
        """
        Returns a text similarity score of 0-1.

        This uses the Jaccard similarity measure. That is the number
        of shared unique words divided by the total number of unique words.
        """

Maak handig gebruik van `convert_to_words` bij het implementeren van deze functie.

<details markdown="1"><summary markdown="span">set union</summary>
De union van twee sets geeft een nieuwe set met daarin alle unieke items van de twee sets. Dit kan op twee manieren:

    set3 = set1.union(set2)
    set3 = set1 | set2

</details>

<details markdown="1"><summary markdown="span">set intersection</summary>
De intersection van twee sets geeft een nieuwe set met daarin alle overeenkomende items van de twee sets. Dit kan op twee manieren:

    set3 = set1.intersection(set2)
    set3 = set1 & set2

</details>

> Deze functie geeft een getal terug dat voor grotere teksten moeilijk na te gaan is. Een groot deel van het programma gaat erop vertrouwen dat dit getal klopt. Dus schrijf nu weer gelijk een aantal tests. Test tenminste twee teksten zonder overlap, twee teksten met totale overlap, en twee teksten met gedeeltelijke overlap.

### 3. get_scripts

Nu we een overeenkomstmaat hebben, hebben we film scripts nodig. Deze kun je zo downloaden:

> # TODO change adventure -> scripts

    curl -LO https://github.com/minprog/adventure/raw/2022/more/adventure.zip
    unzip scripts.zip
    rm scripts.zip

Dit geeft je een folder met 10 filmscripts: Elvis, Frozen, Her, Interstellar, Joker, Killers of the Flower Moon, Lalaland, Magnolia, Tenet en Up. Implementeer onderstaande functie om alle scripts in te lezen. De functie moet een `dict` returnen met de titel van het script als key (bijvoorbeeld `her.txt`) en de gehele inhoud van het script als value.

    def get_scripts(scripts_directory_path: str) -> dict[str, str]:
        """
        Returns a dictionary of movie script names and their contents.

        This will read all files inside scripts_directory_path.
        """

<details markdown="1"><summary markdown="span">Bestandsnamen ophalen</summary>
Gebruik de functie [listdir](https://docs.python.org/3/library/os.html#os.listdir) om alle bestandsnamen binnen een folder (directory) op te halen. Hiervoor moet je de module `os` importeren met `import os`.
</details>

<details markdown="1"><summary markdown="span">Bestand openen en inlezen</summary>
Gebruik hiervoor de functie `open` om een bestand te openen en de methode `read` om uit het bestand te lezen. Zie [Python's documentatie](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files). **Let op** gebruik de `with` statement als je met bestanden werkt. Op die manier kan je niet vergeten een bestand te sluiten.
</details>

> Deze functie leest bestanden in en dat maakt het testen anders. Om dit goed te testen zou je verschillende folders kunnen klaarzetten om mee te testen. Voor deze opdracht is het voldoende om alleen één test toe te voegen dat test of alle 10 scripts correct worden teruggegeven.

### 4. recommend

Nu het moment om alles samen te laten komen. Implementeer onderstaande functie om een film aan te bevelen op basis van het script van een andere film.

    def recommend(script_name: str) -> str:
        """
        Recommend another movie based on one movie script.

        Takes the name of a script, and returns the name of another script.
        """

<details markdown="1"><summary markdown="span">Aanbeveling-spoilers</summary>
Dit zijn een aantal aanbevelingen:

- `interstellar.txt` geeft `tenet.txt`
- `tenet.txt` geeft `interstellar.txt`
- `frozen.txt` geeft `up.txt`
- `elvis.txt` geeft `joker.txt`
- `joker.txt` geeft `magnolia.txt`
</details>

### 5. user interaction

Als kers op de taart, maak er een echt programma van dat een film aanneemt en een andere film teruggeeft:

    python3 recommend.py frozen.txt
    up.txt

<details markdown="1"><summary markdown="span">sys.argv</summary>
Net zoals in de programmeertaal C bestaat er een waarde genaamd `argv`. Dit is de zogenaamde "argument vector". Daarin staan alle meegegeven command-line arguments. In Python is `argv` een `list` en deze staat opgeslagen in een module genaamd `sys`. Zo kom je eraan:

    import sys

    print(sys.argv)

</details>

<details markdown="1"><summary markdown="span">`if __name__ == "__main__":`</summary>
Maak gebruik van `if __name__ == "__main__":` om ervoor te zorgen dat bepaalde Python code niet draait als deze wordt geïmporteerd in een ander Python-bestand. Zo wil je bijvoorbeeld nog steeds je eigen functies kunnen importeren in `test_jaccard.py`, maar niet dat de code draait om `argv` uit te lezen of het resultaat uit te printen.

    # rest van het bestand

    if __name__ == "__main__":
        # check argv
        # recommend new movie

</details>

Je hoeft voor deze opdracht geen foutafhandeling te doen. Je mag er vanuitgaan dat de gebruiker van je programma altijd een bestaand script invoert.

## Testen

Zorg ervoor dat iedere functie is getest met aparte test functies in een apart bestand genaamd `test_jaccard.py`.
