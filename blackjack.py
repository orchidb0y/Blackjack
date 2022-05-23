# Rules of blackjack:
# Players will place their initial bets. There might be a minimum bet.
# Dealer will deal everybody two cards, faceup.
# Dealer will give himself one card faceup and one hole card (facing down).

# Cards 2 through 9 are worth their value.
# 10, jacks, Kings and Queens are worth 10 points.
# Aces can count as 1 or 11.

# A BLACKJACK consists of ACE + 10 VALUE card on the FIRST TWO cards. Gets paid right away. It pays 3:2, that is, if someone bets $500, they get $750.

# The objective of the game is to get as close to 21 without going over.

# After the two initial cards, there are 5 possible plays:

    # HIT: take another card.
    # STAY: take no more cards.
    # DOUBLE DOWN: increase the initial bet by 100% and take only one more card.
        # A player can double down after splitting.
    # SPLIT: creates two hands from a starting hand where BOTH CARDS ARE THE SAME VALUE.
        # Each new hand gets another card, so that the player has two starting hands.
        # This requires and additional bet on the second hand.
        # The two hands are played independently, and the wager on each hand is won or lost independently.
        # For the sake of simplicity, this game will only allow splitting in the first round.
    # SURRENDER: forfeit half the bet and end the hand immediately. Only available as the first decision.
    # If the card that is showing on the table's side is an ace, any player can make an INSURANCE bet.
        # The INSURANCE bet is a side bet that the dealer has a blackjack.
        # The table asks for insurance betsbefore the first player plays.
        # The bet can only be of up to half of the player's current bet.
        # Players with blackjack can also take insurance.

# After all players have taken their turns, it's the table's turn:

    # The table will flip up their facedown card, and take a card until it is close to or over 21.

# FOR NOW, THE GAME WILL ONLY DEAL WITH SIMPLE RULES, NOT ACCOUNTING FOR RULE VARIATIONS
# Each player will start with $100 in their pocket
# No splitting for now

import random
import time
# import os


class Dealer:
    house = 0
    deck = []
    deck_and_values = {}
    hand = []

    def __init__(self):
        values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = [' of Clubs', ' of Diamonds', ' of Hearts', ' of Spades']
        for suit in suits:
            for number in numbers:
                Dealer.deck.append(number + suit)
        Dealer.deck_and_values = dict(zip(Dealer.deck, values * 4))
        random.shuffle(Dealer.deck)

    def deal_player(self, player):
        t = 1
        while t:
            print()
            dealing = dealer.deck.pop()
            player.hand.append(dealing)
            print(dealing)
            time.sleep(1)
            dealing = dealer.deck.pop()
            player.hand.append(dealing)
            print(dealing)
            t -= 1

    def deal_house(self):
        t = 1
        while t:
            print()
            dealing = dealer.deck.pop()
            dealer.hand.append(dealing)
            print(dealing)
            time.sleep(1)
            dealing = dealer.deck.pop()
            dealer.hand.append(dealing)
            print('Hidden card')
            t -= 1


class Player:
    pocket = 100
    bet = 0
    hand = []
    points = 0
    player_count = 0

    def __init__(self, name):
        self.name = name
        self.id = Player.player_count

    def place_bet(self, bet):
        self.bet = bet
        self.pocket -= bet

    def hit(self):
        pass

    def stay(self):
        pass

    def double_down(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

    def insurance(self):
        pass


def make_player(name):
    Player.player_count += 1
    globals()[f'player{Player.player_count}'] = Player(name)
    return globals()[f'player{Player.player_count}']


dealer = Dealer()

print('Welcome to Blackjack. I assume your\'re familiar with the rules.')

time.sleep(1.2)

player_num = 0
player_list = []
player_num = int(input('How many players are we dealing with? '))

while player_num == 0 or player_num > 3:
    player_num = int(input('Sorry, the game will only accept up to three players. How many players are we dealig with? '))

while player_num:
    for number in range(1, player_num + 1):
        name = input(f'What is the name of player {number}? ')
        make_player(name)
        player_num -= 1

print(globals())