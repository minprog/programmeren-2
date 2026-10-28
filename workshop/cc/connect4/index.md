# Cyclomatic Complexity: Vier op een rij

In deze opdracht ga je de Cyclomatic Complexity van een bestaand programma verlagen. Je gebruikt hiervoor `flake8`, met als doel dat elke functie een Cyclomatic Complexity van maximaal 3 krijgt.

Dit is een lastige opdracht. De code is verdeeld over twee bestanden en je kan niet volstaan met het uitknippen van stukjes code in aparte functies: sommige functies vragen om een andere aanpak. Denk goed na over wat er eigenlijk gebeurt, voordat je begint met aanpassen.

## De opdracht: Vier op een rij

Hier vind je de code voor een spel Vier op een rij (`connect4.py`, `board.py`) voor twee spelers. Speler `X` en speler `O` laten om de beurt een steen in één van de zeven kolommen vallen. De eerste speler met vier stenen op een rij (horizontaal, verticaal of diagonaal) wint. Als het bord vol is zonder winnaar is het gelijkspel. Na afloop kan je nog een spel spelen, de stand wordt bijgehouden.

<details markdown="1"><summary markdown="span">board.py</summary>

    ROWS = 6
    COLUMNS = 7


    def new_board() -> list[list[str]]:
        board: list[list[str]] = []
        for row in range(ROWS):
            board.append([])
            for column in range(COLUMNS):
                board[row].append(".")
        return board


    def print_board(board: list[list[str]]) -> None:
        print()
        print("  1  2  3  4  5  6  7")
        for row in board:
            line = ""
            for cell in row:
                if cell == "X":
                    line += " X "
                elif cell == "O":
                    line += " O "
                else:
                    line += " . "
            print(line)
        print()


    def is_column_full(board: list[list[str]], column: int) -> bool:
        if board[0][column] != ".":
            return True
        else:
            return False


    def drop_piece(board: list[list[str]], column: int, player: str) -> int:
        row = ROWS - 1
        while row >= 0:
            if board[row][column] == ".":
                board[row][column] = player
                break
            row -= 1
        return row


    def is_board_full(board: list[list[str]]) -> bool:
        full = True
        for row in range(ROWS):
            for column in range(COLUMNS):
                if board[row][column] == ".":
                    full = False
        return full


    def has_won(board: list[list[str]], row: int, column: int, player: str) -> bool:
        """Check if the piece just dropped at (row, column) makes four in a row."""

        # Horizontal
        count = 1
        c = column - 1
        while c >= 0 and board[row][c] == player:
            count += 1
            c -= 1
        c = column + 1
        while c < COLUMNS and board[row][c] == player:
            count += 1
            c += 1
        if count >= 4:
            return True

        # Vertical
        count = 1
        r = row - 1
        while r >= 0 and board[r][column] == player:
            count += 1
            r -= 1
        r = row + 1
        while r < ROWS and board[r][column] == player:
            count += 1
            r += 1
        if count >= 4:
            return True

        # Diagonal, from top left to bottom right
        count = 1
        r = row - 1
        c = column - 1
        while r >= 0 and c >= 0 and board[r][c] == player:
            count += 1
            r -= 1
            c -= 1
        r = row + 1
        c = column + 1
        while r < ROWS and c < COLUMNS and board[r][c] == player:
            count += 1
            r += 1
            c += 1
        if count >= 4:
            return True

        # Diagonal, from bottom left to top right
        count = 1
        r = row + 1
        c = column - 1
        while r < ROWS and c >= 0 and board[r][c] == player:
            count += 1
            r += 1
            c -= 1
        r = row - 1
        c = column + 1
        while r >= 0 and c < COLUMNS and board[r][c] == player:
            count += 1
            r -= 1
            c += 1
        return count >= 4

</details>

<details markdown="1"><summary markdown="span">connect4.py</summary>

    from board import new_board, print_board, is_column_full, drop_piece, is_board_full, has_won


    def play() -> None:
        print("WELCOME TO CONNECT FOUR")
        scores = {"X": 0, "O": 0, "draws": 0}

        # Run an infinite number of games
        while True:
            board = new_board()
            player = "X"

            # Play until somebody wins or the board is full
            while True:
                print_board(board)

                # Prompt and re-prompt for a valid column
                while True:
                    text = input(f"Player {player}, choose a column (1-7): ")
                    if not text.isdigit():
                        print("Please enter a number.")
                        continue
                    column = int(text) - 1
                    if column < 0 or column >= 7:
                        print("The column must be between 1 and 7.")
                        continue
                    if is_column_full(board, column):
                        print("That column is full.")
                        continue
                    break

                row = drop_piece(board, column, player)

                if has_won(board, row, column, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    scores[player] += 1
                    break

                if is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    scores["draws"] += 1
                    break

                if player == "X":
                    player = "O"
                else:
                    player = "X"

            print(f"Score: X {scores['X']} - O {scores['O']} ({scores['draws']} draws)")

            # Prompt and re-prompt for another game
            again = input("Play again? (y/n) ")
            while again != "y" and again != "n":
                again = input("Please answer y or n. ")
            if again == "n":
                break


    if __name__ == '__main__':
        play()

</details>

In `board.py` staat alles dat met het bord te maken heeft, in `connect4.py` staat het spel zelf, met alle `input` en `print`s. De Cyclomatic Complexity is op meerdere plekken te hoog:

    $ python3 -m flake8 --max-complexity 3 --select=C board.py connect4.py
    board.py:14:1: C901 'print_board' is too complex (5)
    board.py:47:1: C901 'is_board_full' is too complex (4)
    board.py:56:1: C901 'has_won' is too complex (12)
    connect4.py:4:1: C901 'play' is too complex (12)

Aan jou de taak om deze code te verbeteren op zo'n manier dat de Cyclomatic Complexity van alle functies in beide bestanden niet hoger dan 3 is. Dat betekent dat het volgende geen klachten meer geeft:

    $ python3 -m flake8 --max-complexity 3 --select=C board.py connect4.py

## Bootstrappen

Eerst even opstarten:

Kopieer de code hierboven en maak de bestanden `board.py` en `connect4.py` in dezelfde map. Draai `python3 -m flake8 --max-complexity 3 --select=C board.py connect4.py` om te kijken of de tool werkt. Je hoort bovenstaande vier meldingen te zien.

Speel vervolgens even een spelletje met `python3 connect4.py`. Probeer ook een paar ongeldige invoeren, een volle kolom en het spel na afloop opnieuw te starten, om gevoel te krijgen voor het programma. Zo begint het:

    WELCOME TO CONNECT FOUR

      1  2  3  4  5  6  7
     .  .  .  .  .  .  . 
     .  .  .  .  .  .  . 
     .  .  .  .  .  .  . 
     .  .  .  .  .  .  . 
     .  .  .  .  .  .  . 
     .  .  .  .  .  .  . 

    Player X, choose a column (1-7): 1
    ...

Let goed op hoe de output eruit ziet. Dit is ook hoe jouw aangepaste programma moet gaan werken.

## What to do

Het doel is de Cyclomatic Complexity onder de 3 te krijgen voor het gehele programma. Dat kan je doen door:

1. De code op te breken in kleinere functies
2. De code zelf eenvoudiger te maken waardoor er minder paden mogelijk zijn.
3. Slimmer te kijken naar de data. Waar je code kopieert en plakt met kleine verschillen, is er vaak een manier om het verschil in data (bijvoorbeeld een tuple) te stoppen en één keer code te schrijven.

Begin met het onderdeel dat je het ingewikkeldst vindt, of juist met het onderdeel dat je het snelst kan oplossen. Doe dit stap voor stap, één functie per keer, en blijf goed testen tussendoor.

<details markdown="1"><summary markdown="span">hint: de win-controle</summary>

`has_won` doet vier keer ongeveer hetzelfde: tel hoeveel stenen van de speler er achter elkaar liggen in een bepaalde richting. Het enige verschil is de *stap* die je zet: `(0, 1)` is naar rechts, `(1, 0)` is naar beneden. Zet de vier stappen in een tuple en schrijf één functie die in een gegeven richting telt. Een rij loopt in twee richtingen: je telt zowel in de stap als in de tegenovergestelde stap.

</details>

<details markdown="1"><summary markdown="span">hint: validatie van de invoer</summary>

In `play` zit een loop met drie controles en `continue`s. Maak een functie die de tekst controleert en de foutmelding teruggeeft (of een lege tekst als de invoer in orde is). De loop zelf wordt dan heel klein.

</details>

<details markdown="1"><summary markdown="span">hint: het bord</summary>

Voor een bord vol hoef je niet elke cel te bekijken: stenen vallen altijd naar beneden, dus als de bovenste rij vol is, is het hele bord vol. En een cel afdrukken is niet afhankelijk van of er `X`, `O` of `.` staat. Kijk goed of je een `if` kan vermijden.

</details>

<details markdown="1"><summary markdown="span">hint: spelers wisselen</summary>

Een `dict` die voor elke speler de andere speler vertelt kan een `if`/`else` vervangen.

</details>

<details markdown="1"><summary markdown="span">hint: meerdere bestanden</summary>

Je mag nieuwe functies toevoegen aan beide bestanden, en functies die in `board.py` staan gebruiken in `connect4.py` met `import`. Houd `connect4.py` voor de invoer en uitvoer en `board.py` voor het bord zelf.

</details>

## Spelregels

* De output van het programma moet exact hetzelfde blijven. Bij het inleveren checken de checks dit ook.
* De code staat in twee bestanden: `board.py` en `connect4.py`. Er mogen geen andere bestanden bij komen.
* Alle code mag worden gewijzigd.
* De Cyclomatic Complexity mag voor geen enkele functie hoger zijn dan 3.
* De type hints moeten blijven kloppen: de checks draaien ook `mypy` en `pycodestyle`.

## Tips

* Hou een kopie bij van de originele versie van de code, bijvoorbeeld in een map `old`. Dan kan je beide versies met dezelfde invoer uitvoeren en makkelijker zien of het programma nog steeds precies hetzelfde doet.

  <details markdown="1"><summary markdown="span">vergelijken met het unix-programma diff</summary>

  Met `diff` laat je de computer de vergelijking doen. Zet de zetten voor een heel spel in een bestand `invoer.txt`, met per regel één antwoord, en laat beide versies daarmee draaien. Heb je de oude versie in de map `old`, dan kan dat zo:

      (cd old && python3 connect4.py < ../invoer.txt) > oud.txt
      python3 connect4.py < invoer.txt > nieuw.txt
      diff oud.txt nieuw.txt

  Geeft `diff` geen uitvoer, dan is de output van de twee bestanden identiek. Anders laat `diff` precies zien welke regels verschillen. Het kan ook in één keer, zonder tussenbestanden:

      diff <(cd old && python3 connect4.py < ../invoer.txt) <(python3 connect4.py < invoer.txt)

  </details>

* Maak een bestand `invoer.txt` met per regel één zet, en draai `python3 connect4.py < invoer.txt`. Voor een snelle winst: `1`, `1`, `2`, `2`, `3`, `3`, `4` en `n` (X wint horizontaal).
* Test ook de randgevallen: een win op het laatste vakje van een rij, diagonalen aan de rand van het bord, een volle kolom en een gelijkspel.
* Lever je code ook eens vroegtijdig in. De checks geven feedback als de output niet helemaal klopt.
