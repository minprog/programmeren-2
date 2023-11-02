# 21

In deze opdracht bouw je verder op de `Card` class van de vorige opdracht.

1.  Schrijf een niet te ingewikkelde implementatie van een `Deck` class die random kaarten kan "delen", zoals dat heet. Een instatie van `Deck` start met de 52 kaarten. Er moet een `deal()`-methode zijn die een random plek uit de lijst met kaarten kiest en deze uit de lijst popt. Maak ook een `cardsLeft()`-methode die aangeeft hoeveel kaarten nog resteren. (Een meer ingewikkelde versie van deze class staat verderop in het boek, en ongetwijfeld online, maar maak gewoon zelf een eenvoudige implementatie.)

2.  Gegeven de `Card` en `Deck` classes, schrijf een programma `21.py` dat het spel [21](https://en.wikipedia.org/wiki/Twenty-One_(banking_game)) met 2 spelers kan spelen (interactief, dus spelers kunnen hun beslissing invoeren op het toetsenbord). De regels:

    > "Whilst there are numerous variants of twenty-one, the following general rules apply. The game has a banker and a variable number of punters. The role of banker rotates around the players, except for casino games where the banker's role is held permanently by a member of the casino staff. The banker deals two cards, face down, to each punter. Bets are placed either before receiving the cards or after receiving and viewing the first card. The punters, in turn, having picked up and examined both cards announce whether they will stay with the cards they have or receive another card from the banker free. Some games also allow a punter to raise his stake and 'buy' another card. The aim is to score exactly twenty-one points or, failing that, to come as close to twenty-one as possible, based on the card values dealt. If a player exceeds twenty-one, they lose their stake. Once every punter has either announced they will stay with their cards or exceeded twenty-one, the dealer takes his turn. Anyone who achieves twenty-one in his first two cards has a 'natural vingt-un', 'pontoon' or 'blackjack', depending on the game variant, which wins double."

Deze module gaat voornamelijk over het gebruik van ADTs, dus je hoeft geen tests te schrijven voor het 21-programma. Het programma hoeft zelf niet in OOP geschreven te zijn maar gebruikt bij voorkeur wel verschillende functies.

## Inleveren

Lever hieronder de implementatie in.
