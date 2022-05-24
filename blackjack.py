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

    def deal_player(self, person):
        print('Dealing for {name}:'.format(name = person.name))
        print()
        time.sleep(1)
        dealing = dealer.deck.pop()
        person.hand.append(dealing)
        print(dealing)
        time.sleep(1)
        dealing = dealer.deck.pop()
        person.hand.append(dealing)
        print(dealing)
        time.sleep(1)
        
    def deal_house(self):
        print('\nNow dealing for the house.')
        print()
        time.sleep(1)
        dealing = dealer.deck.pop()
        dealer.hand.append(dealing)
        print(dealing)
        time.sleep(1)
        dealer.hand.append(dealer.deck.pop())
        print('Hidden card')
        time.sleep(1)

    def hit(self):
        pass


class Player:
    player_count = 0

    def __init__(self, name):
        self.name = name
        self.id = Player.player_count
        self.hand = []
        self.points = 0
        self.bet = 0
        self.wallet = 100
        self.total = 0
        self.has_21 = False

    def place_bet(self, bet):
        self.bet = bet
        self.pocket -= bet

    def hit(self):
        card = dealer.deck.pop()
        self.hand.append(card)
        self.total = 0
        if dealer.deck_and_values[card] == [1, 11]:
            self.hand.pop()
            for value in self.hand:
                self.total += value
                print(f'Your hand has a total value of {self.total + 1} or {self.total + 11}.')
            self.hand.append(card)
        else:
            for card in self.hand:
                self.total += int(dealer.deck_and_values[card])
        print(f'\nYou got a {card}')
        time.sleep(1)
        if self.total < 21:
            print(f'Your hand now totals to {self.total} points.')
            opt = input('Continue? (y/n)\n')
            if opt == 'y':
                take_turn(self)
            else:
                pass
        elif self.total == 21:
            print('You have 21 points!')
        else:
            print('You\'re bust!')


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

    def check_hand(self):
        print('\nYou have these cards in hand:\n')
        for card in self.hand:
            print(card)
        self.total = 0
        for card in self.hand:
            if dealer.deck_and_values[card] == [1, 11]:
                i = self.hand.index(card)
                self.hand.pop(i)
                for card in self.hand:
                    self.total += dealer.deck_and_values[card]
                print(f'Your hand has a total value of {self.total + 1} or {self.total + 11}.')
                self.hand.append(card)
                break
            else:
                self.total += int(dealer.deck_and_values[card])
        print(f'\nYour hand has a total value of {self.total}')
        take_turn(self)


list_of_players = []


def make_player(name):
    Player.player_count += 1
    globals()[f'player{Player.player_count}'] = Player(name)
    list_of_players.append(globals()[f'player{Player.player_count}'])
    return list_of_players


def take_turn(person):
    print('''
    What does {name} want to do? (1-5)

    1) Hit
    2) Stay
    3) Double down
    4) Split (not implemented)
    5) Surrender
    6) Check your hand
    '''.format(name = person.name))
    opt = input()
    if opt == '1':
        person.hit()
    elif opt == '2':
        pass
    elif opt == '3':
        person.double_down()
    elif opt == '4':
        person.split()
    elif opt == '5':
        person.surrender()
    elif opt == '6':
        person.check_hand()
    else:
        print('I\'m sorry, I didn\'t get that.')
        take_turn(person)


def players_turn(number_of_players, list_of_players):
    while number_of_players:
        for player in list_of_players:
            take_turn(player)
            number_of_players -= 1
    number_of_players = len(list_of_players)


dealer = Dealer()

print('Welcome to Standard Blackjack. I assume your\'re familiar with the rules. Each player starts with $100 in their wallets. The payouts are 3:2 for Blackjack, 1:1 if you win a round and Insurance pays out 2:1.')

time.sleep(3)

number_of_players = 0
number_of_players = int(input('How many players are we dealing with? (1-3) '))

while number_of_players == 0 or number_of_players > 3:
    number_of_players = int(input('Sorry, the game will only accept up to three players. How many players are we dealig with? (1-3) '))

while number_of_players:
    for number in range(1, number_of_players + 1):
        name = input(f'What is the name of player {number}? ')
        make_player(name)
        number_of_players -= 1

number_of_players = len(list_of_players)

time.sleep(1)
print('\nAlright, we\'re ready to start. The dealer will start dealing cards to each of the players.\n')
time.sleep(1)

while number_of_players:
    for player in list_of_players:
        dealer.deal_player(player)
        number_of_players -= 1
        if number_of_players > 0:
            print()
    time.sleep(1)

number_of_players = len(list_of_players)

dealer.deal_house()

print('\nNow that the cards are dealt, it\'s time for the players to take their turns and make their first decision.')
time.sleep(1)

if dealer.deck_and_values[dealer.deck[0]] == [1, 11]:
    print('\nThe dealer is showing an Ace! Each player must decide if they want to insure their hands against a Blackjack.')
    # NOT IMPLEMENTED

players_turn(number_of_players, list_of_players)