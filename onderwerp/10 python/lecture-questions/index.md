# Vragen over het college: Python

Beantwoord de volgende vragen in je eigen woorden, in Nederlands of Engels.

1.  In het college schreef David een spellingchecker in Python. Waarom kun je een spellingchecker implementeren in Python met minder regels code dan in C nodig is?

    <textarea name="form[q1]" rows="8" required></textarea>

2.  Waarom werkte de spellingchecker in Python waarschijnlijk langzamer dan de spellingchecker die in C geschreven is?

    <textarea name="form[q2]" rows="8" required></textarea>

3.  In het college heb je geleerd dat C-programma's worden gecompileerd, terwijl Python-programma's worden *geïnterpreteerd*. Wat betekent het, in je eigen woorden, dat een programmeertaal een geïnterpreteerde taal is?

    <textarea name="form[q3]" rows="8" required></textarea>

4.  Je herinnert je vast nog wel dat je in C de volgende constructie nodig hebt om een positief geheel getal tussen 1 and 8 op te vragen bij een gebruiker.

        1  int n;
        2  do
        3  {
        4      n = get_int("Height: ");
        5  }
        6  while (n < 1 || n > 8);

    In Python zijn er geen `do ... while` loops, dus we zouden het benodigde stuk code als volgt kunnen schrijven.

        1  while True:
        2      n = get_int("Height: ")
        3      if n >= 1 and n <= 8:
        4          break

    Leg uit hoe deze beide uitwerkingen *logisch equivalent* zijn, dat wil zeggen dat ze voor dezelfde invoer dezelfde resultaten opleveren. Doe dit door voor beide uitwerkingen de code regel voor regel uit te leggen en deze twee te vergelijken.

    <textarea name="form[q4]" rows="8" required></textarea>
