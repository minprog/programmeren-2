# Priority Queue

Een normale queue (rij) houdt de volgorde van toevoegen aan. Het wat er als eerst bijkomt, gaat er ook alst eerste uit (FIFO: First In First Out). Dit kan goed worden geïmplementeerd met een linked-list, want specifiek het toevoegen aan het eind en weghalen aan het begin kan een linked-list in constante tijd. Dit idee breekt zodra er prioriteit komt kijken. Oftewel een andere volgorde niet op basis van binnenkomen, maar op basis van belangrijkheid. Want bij een linked-list zijn er dan twee opties:

1. We houden de lijst niet gesorteerd:
    1. Toevoegen gaat dan in O(1) zoals normaal.
    2. Weghalen gaat nu in O(n). Om het item te vinden met de hoogste prioriteit moet de hele lijst worden doorzocht.
2. We houden de lijst wel gesorteerd:
    1. Toevoegen gaat dan in O(n). Om de juiste plek van het nieuwe item te vinden moet de hele lijst worden doorzocht.
    2. Weghalen gaat nu wel in O(1), want de lijst is gesorteerd en het item met de hoogste prioriteit staat vooraan.

In beide gevallen gaat een operatie in lineaire tijd (O(n)). Dat kan beter.

## Heap

Een heap is een AST op basis van een gedeeltelijk geordende binaire boom structuur. Een binaire boom is een soort linked-list, waar iedere node wijst naar niet één volgende node, maar naar maximaal twee. Binnen zo'n structuur hebben we het over een ouder (parent) en kinderen (children). Iedere ouder heeft in een binaire boom potentieel twee kinderen.

In een heap zorgen we ervoor dat de hoogste waarde (of de laagste, het is maar net wat je wilt) bovenaan de boom zit, de zogenaamde "root" node. Dat doen we door er altijd voor te zorgen dat deze regel waar is:

- Iedere ouder heeft een hogere waarde dan zijn kinderen.

Hierdoor garanderen we dat de root de hoogste waarde bevat. Want het is niet mogelijk dat de waarde van de kinderen, kleinkinderen, kleinkleinkinderen, etc. groter zijn. Wel kan het zo zijn dat de broers of zussen (siblings) groter zijn dan elkaar. Daardoor kan het voorkomen dat de gehele boom niet op volgorde staat. Maar één ding is zeker, de hoogste waarde staat bovenaan.

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_xngghs4k&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_v2wiitqp)

### Toevoegen van een nieuwe node

Net zoals bij een linked list voegen we een node toe aan een uiterste, hier onderaan de boom. Na het toevoegen van een node kan het zo zijn dat de nieuwe node een hogere waarde heeft dan haar ouder. In dat geval moet er nog iets worden gefixt: de nieuwe node en haar ouder wisselen van plek. Nu kan het zo zijn dat de nieuwe node weer een hogere waarde heeft dan haar nieuwe ouder. Als dat zo is, wisselen we ze weer om. Net zolang totdat de nieuwe node een lagere of gelijke waarde heeft aan haar ouder.

Bij het toevoegen van een nieuwe node moeten er daarom potentieel evenveel omwisselingen gedaan worden als dat er lagen zijn in de boom. Maar, omdat elke node in de boom twee kinderen kan hebben, is iedere laag in de boom twee keer zo groot als de laag erboven. Sterker nog, iedere nieuwe laag heeft precies evenveel nodes als alle lagen erboven bij elkaar opgeteld plus één. Dat betekent dat de boom telkens twee keer zo groot moet worden als dat deze was, om één extra stap toe te voegen aan het algoritme om een node toe te voegen. Daardoor is de complexiteit van het toevoegen O(log(n)) (bij informatica is de log standaard met base 2).

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_0qsdfv5y&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_13ax2aki)

### Verwijderen van de eerste node

De eerste node verwijderen gaat volgens het volgende stappenplan:

1. haal de eerste node weg
2. verplaats de laatste node (onderaan de boom) naar de plek van de eerste node
3. zolang de verplaatste node kleiner is dan één van zijn kinderen, wissel ze om

Eigenlijk is het verwijderen dus hetzelfde als toevoegen, maar dan precies andersom. Toevoegen begint onderaan en de node bubbelt naar boven. Verwijderen begint bovenaan en de node zinkt naar beneden. Daardoor is ook deze operatie in O(log(n)).

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_h5ozap03&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_m57goxkp)

## Impementeer PriorityQueue

Nu is het aan jou om een priority queue te implementeren op basis van een heap. De priority queue moet de volgende operaties ondersteunen:

- `add(value: Any) -> None` --- voegt een waarde toe aan de queue
- `pop() -> Any` --- haalt de hoogste waarde uit de queue

Heaps kan je op verschillende manieren implementeren. Net zoals bij linked lists kan dat door middel van nodes die wijzen naar elkaar. Bij heaps kan dat ook door middel van een lijst en een handig trucje. Doen we als volgt, op iedere plek in de lijst staat een waarde van een node. De hoogste waarde staat op plek 0. De kinderen daarvan staan op plekken 1 en 2. De kinderen daarvan staan weer op plekken 3, 4, 5 en 6. De kinderen daarvan staan op plekken 7, 8, 9, 10, 11, 12, 13, 14. Etc. Je kan het je zo voorstellen:

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_7cjgkbko&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_eoyowtdp)

Doordat de ouders en kinderen op vaste plekken in de lijst staan kan je ook terugvinden welke kinderen bij welke ouders horen door te rekenen:

* Stel we hebben een node op plek 1, dan staan de kinderen op plekken:
    * `1 * 2 + 1 = 3`
    * `1 * 2 + 2 = 4`
* Stel we hebben een node op plek 4, dan staat haar ouder op plek:
    * `(4 - 1) / 2 = 1` (let op, dit is een integer-deling!)

In algemene zin, gegeven een node k:

* De kinderen van k staan op:
    * `k * 2 + 1`
    * `k * 2 + 2`
* De ouder van k staat op:
    * `(k - 1) / 2`

Je kan beginnen met de volgende code:

    from typing import Any

    class PriorityQueue:
        def __init__(self):
            self._heap: list[Any] = []

        def add(value: Any) -> None:
            raise notImplementedError()

        def pop() -> Any:
            raise not ImplementedError()