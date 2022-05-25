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
import os
import sys
from tracemalloc import start


class Dealer:
    house = 0
    deck = []
    deck_and_values = {}
    hand = []
    total = 0
    blackjack = False
    has_21 = False

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
        print('Dealing for {name}:\n'.format(name = person.name))
        time.sleep(1)
        dealing1 = dealer.deck.pop()
        if self.deck_and_values[dealing1] == [1, 11]:
            person.one_ace = True
        person.hand.append(dealing1)
        print(dealing1)
        time.sleep(1)
        dealing2 = dealer.deck.pop()
        if self.deck_and_values[dealing2] == [1, 11] and person.one_ace == True:
            person.two_ace = True
        elif self.deck_and_values[dealing2] == [1, 11] and person.one_ace == False:
            person.one_ace = True
        person.hand.append(dealing2)
        print(dealing2)
        if person.one_ace == True and self.deck_and_values[dealing1] == [1, 11] and self.deck_and_values[dealing2] == 10:
            time.sleep(1)
            person.blackjack = True
            print('You got a Blackjack!\nYou\'ll receive your payout when all players have taken their turns.')
        elif person.one_ace == True and self.deck_and_values[dealing2] == [1, 11] and self.deck_and_values[dealing1] == 10:
            time.sleep(1)
            person.blackjack = True
            print('You got a Blackjack!\nYou\'ll receive your payout when all players have taken their turns.')
        time.sleep(1)
        
        
    def deal_house(self, number_of_players, list_of_players):
        print('\nNow dealing for the house:')
        print()
        time.sleep(1)
        dealing = dealer.deck.pop()
        dealer.hand.append(dealing)
        print(dealing)
        time.sleep(1)
        dealer.hand.append(dealer.deck.pop())
        print('Hidden card')
        time.sleep(1)
        number_of_players = len(list_of_players)
        first_turn(number_of_players, list_of_players)

    def hit(self):
        pass


class Player:
    player_count = 0

    def __init__(self, name):
        self.name = name
        self.id = Player.player_count
        self.hand = []
        self.bet = 0
        self.wallet = 100
        self.total = 0
        self.has_21 = False
        self.blackjack = False
        self.one_ace = False
        self.two_ace = False

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
            print(f'Your hand totals {self.total} points.')
            time.sleep(1)
            take_turn(self)
        elif self.total == 21:
            self.has_21 = True
            print('You have 21 points!\nYou\'ll receive your payout when all players have taken their turns.')
            time.sleep(1)
        else:
            print('You\'re bust!')
            time.sleep(1)
            print('The table will take the money you bet when all players have taken their turns.')
            time.sleep(1)

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
            if self.one_ace == True or self.two_ace == True:
                i = self.hand.index(card)
                self.hand.pop(i)
                for card in self.hand:
                    self.total += int(dealer.deck_and_values[card])
                print(f'Your hand has a total value of {self.total + 1} or {self.total + 11}.')
                self.hand.append(card)
                take_turn(self)
            else:
                self.total += int(dealer.deck_and_values[card])
        if self.one_ace == False or self.two_ace == False:
            print(f'\nYour hand has a total value of {self.total}')
            take_turn(self)
        # debug
        # for card in self.hand:
        #     print(card)
        # take_turn(self)


    def check_house_hand(self):
        print('\nThe house has these cards in hand:\n')
        for card in dealer.hand:
            print(card)
        for card in dealer.hand:
            if dealer.deck_and_values[card] == [1, 11]:
                i = dealer.hand.index(card)
                dealer.hand.pop(i)
                for card in dealer.hand:
                    dealer.total += int(dealer.deck_and_values[card])
                print(f'The dealer\'s hand has a total value of {dealer.total + 1} or {dealer.total + 11}.')
                dealer.hand.append(card)
            else:
                dealer.total += int(dealer.deck_and_values[card])
        take_turn(self)


list_of_players = []


def make_player(name):
    Player.player_count += 1
    globals()[f'player{Player.player_count}'] = Player(name)
    list_of_players.append(globals()[f'player{Player.player_count}'])
    return list_of_players


def take_turn(person):
    print('''
    What does {name} want to do? (1-8)

    1) Hit
    2) Stay
    3) Double down (not implemented)
    4) Split (not implemented)
    5) Surrender (not implemented)
    6) Check your hand
    7) Check the house\'s hand (not implemented)
    8) Quit the game
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
    elif opt == '7':
        person.check_house_hand()
    elif opt == '8':
        sys.exit()
    else:
        print('I\'m sorry, I didn\'t get that.')
        take_turn(person)


def players_turn(number_of_players, list_of_players):
    while number_of_players:
        for player in list_of_players:
            take_turn(player)
            number_of_players -= 1
    if number_of_players == 0:
        time.sleep(1)
        dealers_turn()

def start_game(number_of_players):
    os.system('cls')
    print('Welcome to Standard Blackjack. Each player starts with $100 in their wallets. The payouts are 3:2 for Blackjack, 1:1 if you win a round and Insurance pays out 2:1.')
    time.sleep(3)
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
    deal_players(number_of_players, list_of_players)

def deal_players(number_of_players, list_of_players):
    while number_of_players:
        for player in list_of_players:
            dealer.deal_player(player)
            number_of_players -= 1
            if number_of_players > 0:
                print()
    time.sleep(1)
    number_of_players = len(list_of_players)
    dealer.deal_house(number_of_players, list_of_players)

def first_turn(number_of_players, list_of_players):
    time.sleep(1)
    print('\nNow that the cards are dealt, it\'s time for the players to take their turns and make their first decision.')
    time.sleep(3)
    if dealer.deck_and_values[dealer.deck[0]] == [1, 11]:
        print('\nThe dealer is showing an Ace! Each player must decide if they want to insure their hands against a Blackjack.')
        # NOT IMPLEMENTED
    players_turn(number_of_players, list_of_players)

def dealers_turn():
    print('dealer')

number_of_players = 0
dealer = Dealer()
start_game(number_of_players)