# Installatie

Heb je geen terminal geïnstalleerd? Of werk je op Windows en heb je geen Git Bash geïnstalleerd? Dan moet je mogelijk nog de [installatie-instructies van DR](https://dr.proglab.nl/installatie) volgen.

### Eisen

<details markdown="1"><summary markdown="span">Je moet een automatisch gebackupte map hebben op je eigen computer waarin je je uitwerkingen voor deze cursus maakt.</summary>
Je moet een map hebben op je eigen computer waarin je je uitwerkingen voor deze cursus maakt. **Zorg er voor dat de directory automatisch gebackupt wordt**. Doe dit bijvoorbeeld via OneDrive, Google Drive, Surf Drive of iCloud. Maak in deze map meteen een nieuwe map "module1" voor de huidige module.
</details>

<details markdown="1"><summary markdown="span">Je gebruikt de editor Pulsar.</summary>
 Deze kan je hier downloaden: <https://pulsar-edit.dev>
</details>

<details markdown="1"><summary markdown="span">Je gebruikt `uv` om je Python installatie te beheren.</summary>

Installeren doe je als volgt, in de terminal op Mac/Linux of onder Git Bash op Windows:

    curl -LsSf https://astral.sh/uv/install.sh | sh

**Vervolgens herstart je de terminal.**

Met `uv` geinstalleerd, installeer je zo de nieuwste versie van Python:

    uv python install

Zie eventueel de verdere documentatie @ <https://docs.astral.sh/uv/getting-started/installation/>
</details>

<details markdown="1"><summary markdown="span">Je werkt in een virtual environment.</summary>
Een virtual environment is een omgeving voor Python waarin je apart modules en tools kan installeren zodat ze alleen daar bestaan. Op deze manier kan je voor verschillende projecten verschillende versies van Python tools en modules gebruiken. Omdat je later of misschien al eerder met Python hebt gewerkt, werken we binnen dit vak binnen een eigen virtual environment (venv in het kort). 

Navigeer via de terminal naar de map die je eerder hebt aangemaakt waarin je gaat werken tijdens het vak. In die map draai je:

    uv venv

Nu is er een nieuwe map aangemaakt genaamd `.venv`. Om de virtual environment te activeren doe je:

    source .venv/Scripts/activate

Nu zie je de naam van de map tussen haakjes voor je prompt staan. Controleer of onderstaande hetzelfde versienummer laat zien als net geinstalleerd via `uv`:

    python --version

</details>

<details markdown="1"><summary markdown="span">Je hebt de volgende Python packages geinstalleerd en je kunt de tools runnen: `pytest`, `pycodestyle` en `mypy`.</summary>

Allereerst, zorg ervoor dat je in de Virtual Environment zit. Dit kan je herkennen doordat de naam van de map tussen haakjes voor je prompt staat. Is dit niet het geval, dan zul je opnieuw `source .venv/Scripts/activate` moeten draaien in de map waar je de virtual environment hebt aangemaakt.

Eerst installeer je `pip` (Python installs Python) met:

    uv pip install pip

Vervolgens installeer je de tools met:

    pip install pytest pycodestyle mypy

Verifieer dat je de tools kan runnen door de volgende commando's:

    pytest --help
    pycodestyle --help
    mypy --help
</details>

> Kom je er niet uit? Vraag het in het lokaal na! :)
