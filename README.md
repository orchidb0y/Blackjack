# Blackjack
Blackjack terminal game as the final project for CS101 at Codeacademy

The code has been rewritten to be simpler, shorter, faster and more readable. It also now supports multiple hands.
The necessary modules for the new version are Cards.py, Decks.py, Hands.py, Players.py and Game.py.
The game runs on Game.py.

Enjoy!

## Purpose
This terminal-based program was developed as the final project for CS101 at Codecademy. It is intended to be an effort to utilize and apply all basic knowledge of Python such as classes.

## Instructions
To run the game, cd into the directory where you have cloned this repo, and run the Game.py file with
the command `python3 Game.py`.

## How to play
### Object of the game
The game is played in a five-deck fashion (meaning there are five decks of 52 cards). Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

### Cards values
Cards from 2 to 10 are worth their face value. Jacks, Queens and Kings are also worth 10 points. Aces are worth 1 or 11, it depends on what other cards you have in hand.

### Betting
Before each game beings, each player (starting with $100 in their wallets) places a bet on their one hand.

### The deal
When all the players have placed their bets, the dealer gives one card face up to each player in rotation clockwise, and then one card face up to themselves. Another round of cards is then dealt face up to each player, but the dealer takes the second card face down. Thus, each player except the dealer receives two cards face up, and the dealer receives one card face up and one card face down.

### Naturals
If a player's first two cards are an ace and a "ten-card" (a picture card or 10), giving a count of 21 in two cards, this is a natural or "blackjack." At the end of the turn, when it is time for the dealer to play, they will reveal their face down card. If they also have a "blackjack", it's a push (tie), and the player receives their bet back. If the dealer has a natural, they immediately collect the bets of all players who do not have naturals, (but no additional amount).

If the dealer's face up card is an ace, each player who does not have a blackjack will have an opportunity to place an insurance during their turn. An insurance is a side bet to the ammount of half of their original bet. If the dealer ends up having a "blackjack", they lose their original bet, but the insurance pays 2:1, meaning that they end up having lost no money.

### The play
Player 1 goes first, and for the **first** choice of their turn they must decide wheter to "stay" (not ask for another card), "hit" (ask for another card), "double down" (double their bet and get **only one** more card from the deck), "insure" (insure their bet against a dealer natural) or "slit" (split their hand into two hands). If they chose to "hit" and are not "bust" (going over 21), they may keep hitting until bust or until they decide to stay. After the first choice of their turn, they may only choose to "hit" or "stay".

The combination of an ace with a card other than a ten-card is known as a "soft hand," because the player can count the ace as a 1 or 11, and either draw cards or not. For example with a "soft 17" (an ace and a 6), the total is 7 or 17. While a count of 17 is a good hand, the player may wish to draw for a higher total. If the draw creates a bust hand by counting the ace as an 11, the player simply counts the ace as a 1 and continues playing by standing or "hitting" (asking the dealer for additional cards, one at a time). (The program does this calculation by itself, meaning that aces are automatically worth 1 point if counting it as an 11 creates a bust. However, they may still go bust with aces worth 1 point if they keep drawing)

### The dealer's play
When the dealer has served every player, the dealers face-down card is turned up. If the total is 17 or more, it must stand. If the total is 16 or under, they must take a card. The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace, and counting it as 11 would bring the total to 17 or more (but not over 21), the dealer must count the ace as 11 and stand. The dealer's decisions, then, are automatic on all plays, whereas the player always has the option of taking one or more cards.

### Splitting pairs
If a player's first two cards are of the same denomination, such as two jacks or two sixes, they may choose to treat them as two separate hands when their turn comes around. The amount of the original bet then goes on one of the cards, and an equal amount must be placed as a bet on the other card. The player first plays the hand to their left by standing or hitting one or more times; only then is the hand to the right played. The two hands are thus treated separately, and the dealer settles with each on its own merits.

### Doubling down
Another option open to the player is doubling their bet. When the player's turn comes, they place a bet equal to the original bet, and the dealer gives the player just one card.

### Insurance
When the dealer's face-up card is an ace, any of the players may make a side bet of up to half the original bet that the dealer's face-down card is a ten-card, and thus a blackjack for the house. Once all such side bets are placed, the dealer looks at the hole card. If it is a ten-card, it is turned up, and those players who have made the insurance bet win and are paid double the amount of their half-bet - a 2 to 1 payoff. When a blackjack occurs for the dealer, of course, the hand is over, and the players' main bets are collected - unless a player also has blackjack, in which case it is a push. Insurance is invariably not a good proposition for the player, unless they are quite sure that there are an unusually high number of ten-cards still left undealt.

### Settlement
A bet once paid and collected is never returned. Thus, one key advantage to the dealer is that the player goes first. If the player goes bust, they have already lost their wager, even if the dealer goes bust as well. If the dealer goes over 21, the dealer pays each player who has stood the amount of that player's bet. If the dealer stands at 21 or less, the dealer pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total. If there is a tie or a push (a player having the same total as the dealer), no money is paid out or collected.