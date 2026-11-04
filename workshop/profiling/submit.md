# Submit

Verbeter de code op minstens **acht verschillende manieren**. Houd per verbetering bij:

- Waarom je dit deel van de code hebt gekozen.
- Waarom je denkt dat deze code beter kan.
- Wat je hebt aangepast.
- Wat de winst in snelheid is, of juist niet.

**Daarnaast** moet één van je verbeteringen zijn dat je de interne datastructuur van de Sudoku aanpast van een `list[str]` naar een geschiktere, snellere datastructuur.

## Spelregels

#### Mag

- De implementatie van functies en methodes aanpassen.
- Datastructuren in het programma aanpassen, zolang je geen andere regel breekt.
- Nieuwe attributen, functies en methodes toevoegen.

#### Mag niet

- De declaratie van bestaande functies en methodes aanpassen.
- De signatuur van bestaande functies en methodes aanpassen (types van parameters en return values).
- Testcases aanpassen of verwijderen.

## Automatische controle

Na het inleveren draait een automatische controle: stijl (pycodestyle), types (mypy) en de bestaande tests (pytest). Daarna meet hij hoeveel sneller jouw `sudoku.py` is dan het origineel en toont dat als getal, bijvoorbeeld "ongeveer 25x zo snel". Dat is een schatting: het getal kan een beetje schommelen tussen inzendingen.
