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
# No insurance for now

import random
import time
import os
import sys


class Dealer:
    house = 500
    deck = []
    deck_and_values = {}
    hand = []
    aces = []
    hidden_card = ''
    total = 0
    blackjack = False
    has_21 = False
    one_ace = False
    two_ace = False
    three_ace = False
    four_ace = False
    lost = False

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
        time.sleep(0.5)
        dealing1 = dealer.deck.pop()
        if self.deck_and_values[dealing1] == [1, 11]:
            person.one_ace = True
        person.hand.append(dealing1)
        print(dealing1)
        time.sleep(0.5)
        dealing2 = dealer.deck.pop()
        if self.deck_and_values[dealing2] == [1, 11] and person.one_ace == True:
            person.one_ace = False
            person.two_ace = True
        elif self.deck_and_values[dealing2] == [1, 11] and person.one_ace == False:
            person.one_ace = True
        person.hand.append(dealing2)
        print(dealing2)
        if person.one_ace == True and self.deck_and_values[dealing1] == [1, 11] and self.deck_and_values[dealing2] == 10:
            time.sleep(1)
            person.blackjack = True
            print(f'{person.name} got a Blackjack!.')
        elif person.one_ace == True and self.deck_and_values[dealing2] == [1, 11] and self.deck_and_values[dealing1] == 10:
            time.sleep(1)
            person.blackjack = True
            print(f'{person.name} got a Blackjack!.')
        time.sleep(1)
        
        
    def deal_house(self, number_of_players, list_of_players):
        print('\nNow dealing for the house:')
        print()
        time.sleep(0.5)
        dealing = dealer.deck.pop()
        if self.deck_and_values[dealing] == [1, 11]:
            self.one_ace = True
        else:
            self.total += self.deck_and_values[dealing]
        dealer.hand.append(dealing)
        print(dealing)
        time.sleep(0.5)
        dealing = dealer.deck.pop()
        if self.deck_and_values[dealing] == [1, 11] and self.one_ace == False:
            self.one_ace = True
        elif self.deck_and_values[dealing] == [1, 11] and self.one_ace == True:
            self.one_ace = False
            self.two_ace = True
        else:
            self.total += self.deck_and_values[dealing]
        if self.one_ace == True and self.total == 10:
            self.blackjack = True
        self.hidden_card = dealing
        print('Hidden card')
        time.sleep(1)
        number_of_players = len(list_of_players)
        first_turn(number_of_players, list_of_players)

    def hit(self, number_of_players, list_of_players, goal):
        self.total = 0
        deal = self.deck.pop()
        if self.one_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand.pop(i))
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.one_ace = False
                self.two_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        elif self.two_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.two_ace = False
                self.three_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        elif self.three_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.three_ace = False
                self.four_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        elif self.four_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            self.total += dealer.deck_and_values[deal]
        else:
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.one_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        if self.one_ace == True:
            if (self.total + 1) > 21:
                print('The dealer is bust!')
                self.lost = True
                self.end_of_turn(list_of_players)
            elif (self.total + 1) == 21:
                print('The dealer has 21 points!')
                self.has_21 = True
                self.end_of_turn(list_of_players)
            elif (self.total + 1) < 21 and self.total < goal:
                print(f'The dealer has {self.total + 1} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.total >= goal:
                print(f'The dealer has {self.total} points.')
                self.end_of_turn(list_of_players)
        elif self.two_ace == True:
            if (self.total + 2) > 21:
                print('The dealer is bust!')
                self.lost = True
                self.end_of_turn(list_of_players)
            elif (self.total + 2) == 21:
                print('The dealer has 21 points!')
                self.has_21 = True
                self.end_of_turn(list_of_players)
            elif (self.total + 2) < 21 and self.total < goal:
                print(f'The dealer has {self.total + 2} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.total >= goal:
                print(f'The dealer has {self.total} points.')
                self.end_of_turn(list_of_players)
        elif self.three_ace == True:
            if (self.total + 3) > 21:
                print('The dealer is bust!')
                self.lost = True
                self.end_of_turn(list_of_players)
            elif (self.total + 3) == 21:
                print('The dealer has 21 points!')
                self.has_21 = True
                self.end_of_turn(list_of_players)
            elif (self.total + 3) < 21 and self.total < goal:
                print(f'The dealer has {self.total + 3} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.total >= goal:
                print(f'The dealer has {self.total} points.')
                self.end_of_turn(list_of_players)
        elif self.four_ace == True:
            if (self.total + 4) > 21:
                print('The dealer is bust!')
                self.end_of_turn(list_of_players)
                self.lost = True
            elif (self.total + 4) == 21:
                print('The dealer has 21 points!')
                self.has_21 = True
                self.end_of_turn(list_of_players)
            elif (self.total + 4) < 21 and self.total < goal:
                print(f'The dealer has {self.total + 4} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.total >= goal:
                print(f'The dealer has {self.total} points.')
                self.end_of_turn(list_of_players)
        else:
            if self.total > 21:
                print('The dealer is bust!')
                self.lost = True
                self.end_of_turn(list_of_players)
            elif self.total == 21:
                print('The dealer has 21 points!')
                self.end_of_turn(list_of_players)
                self.has_21 = True
            elif self.total < 21 and self.total < goal:
                print(f'The dealer has {self.total} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.total >= goal:
                print(f'The dealer has {self.total} points.')
                self.end_of_turn(list_of_players)

    def dealers_turn(self, number_of_players, list_of_players):
        players_totals = [player.total for player in list_of_players]
        goal = max(players_totals)
        busted_players = 0
        print(f'\nNow it\'s the dealer\'s turn. They will try to reach {goal} points or more.')
        time.sleep(1)
        print(f'\nThe hidden card is {self.hidden_card}')
        self.hand.append(self.hidden_card)
        self.hidden_card = ''
        time.sleep(1)
        for player in list_of_players:
            if player.lost == True:
                busted_players += 1
        if busted_players == len(list_of_players):
            print('Everyone is busted!')
            time.sleep(1)
            self.end_of_turn(list_of_players)
        else:
            if self.blackjack == True:
                print('The dealer has a blackjack!')
                self.end_of_turn(list_of_players)
            elif self.one_ace == True:
                self.total += 11
                print(f'The hand totals {self.total} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.two_ace == True:
                print('The hand totals 2 points.')
                self.take_turn(number_of_players, list_of_players, goal)
            else:
                print(f'The hand totals {self.total} points.')
                self.take_turn(number_of_players, list_of_players, goal)
        
    def take_turn(self, number_of_players, list_of_players, goal):
        if self.total < goal:
            self.hit(number_of_players, list_of_players, goal)
            time.sleep(0.5)
        elif self.total >= goal:
            self.end_of_turn(list_of_players)
        elif self.lost == True:
            self.end_of_turn(list_of_players)
  
    def end_of_turn(self, list_of_players):
        if self.lost == False:
            for person in list_of_players:
                if person.blackjack == True and self.blackjack == True:
                    print(f'\nIt\'s a push between {person.name} and the dealer!')
                    person.wallet += person.bet
                    person.bet = 0
                    time.sleep(0.5)
                elif person.blackjack == True and self.blackjack == False:
                    print(f'\n{person.name} has a blackjack! Adding ${person.bet * (3/2)} to their wallet.')
                    self.house -= (person.bet * (3/2))
                    person.wallet += (person.bet * (3/2))
                    person.bet = 0
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                elif person.total > self.total and person.total <= 21:
                    print(f'\n{person.name} won over the dealer!')
                    time.sleep(0.5)
                    print('They got 2:1 over their bet. Adding ${person.bet * 2} to their wallet.')
                    self.house -= person.bet
                    person.wallet += 2 * person.bet
                    person.bet = 0
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                elif person.total == self.total:
                    print(f'\nIt\'s a tie between {person.name} and the dealer!')
                    person.wallet += person.bet
                    person.bet = 0
                    time.sleep(0.5)
                elif person.total < self.total or person.total > 21:
                    print(f'\n{person.name} lost to the dealer!')
                    time.sleep(0.5)
                    print('Their money goes to the house.')
                    self.house += person.bet
                    person.bet = 0
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
        elif self.lost == True:
            for person in list_of_players:
                if person.lost == False:
                    print(f'\n{person.name} won over the dealer!')
                    time.sleep(0.5)
                    print('They got 2:1 over their bet. Adding ${person.bet * 2} to their wallet.')
                    self.house -= person.bet
                    person.wallet += 2 * person.bet
                    person.bet = 0
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                if person.lost == True:
                    print(f'\n{person.name} lost to the dealer!')
                    time.sleep(0.5)
                    print('Their money goes to the house.')
                    person.bet = 0
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                    
        end_turn(list_of_players)


class Player:
    player_count = 0

    def __init__(self, name):
        self.name = name
        self.id = Player.player_count
        self.hand = []
        self.aces = []
        self.bet = 0
        self.wallet = 100
        self.total = 0
        self.blackjack = False
        self.one_ace = False
        self.two_ace = False
        self.three_ace = False
        self.four_ace = False
        self.tie = False
        self.has_21 = False
        self.lost = False

    def place_bet(self, bet):
        value = int(bet)
        if (self.wallet - value) > 0:
            self.bet = value
            self.wallet -= value

    def hit(self):
        self.total = 0
        deal = dealer.deck.pop()
        if self.one_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand.pop(i))
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nYou got a {deal}.')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.one_ace = False
                self.two_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        elif self.two_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nYou got a {deal}.')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.two_ace = False
                self.three_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        elif self.three_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nYou got a {deal}.')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.three_ace = False
                self.four_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        elif self.four_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nYou got a {deal}.')
            time.sleep(0.5)
            self.total += dealer.deck_and_values[deal]
        else:
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nYou got a {deal}')
            time.sleep(0.5)
            if dealer.deck_and_values[deal] == [1, 11]:
                self.one_ace = True
            else:
                self.total += dealer.deck_and_values[deal]
        if self.one_ace == True:
            if (self.total + 11) > 21:
                if (self.total + 1) > 21:
                    print('You\'re bust!')
                    self.lost = True
                elif (self.total + 1) == 21:
                    print('You have 21 points!')
                    self.has_21 = True
                elif (self.total + 1) < 21:
                    print(f'You have {self.total + 1} points.')
                    take_turn(self)
            elif (self.total + 11) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 11) < 21:
                print(f'You have {self.total + 11} points.')
                take_turn(self)
        elif self.two_ace == True:
            if (self.total + 2) > 21:
                print('You\'re bust!')
                self.lost = True
            elif (self.total + 2) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 2) < 21:
                print(f'You have {self.total + 2} points.')
                take_turn(self)
        elif self.three_ace == True:
            if (self.total + 3) > 21:
                print('You\'re bust!')
                self.lost = True
            elif (self.total + 3) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 3) < 21:
                print(f'You have {self.total + 3} points.')
                take_turn(self)
        elif self.four_ace == True:
            if (self.total + 4) > 21:
                print('You\'re bust!')
                self.lost = True
            elif (self.total + 4) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 4) < 21:
                print(f'You have {self.total + 4} points.')
                take_turn(self)
        else:
            if self.total > 21:
                print('You\'re bust!')
                self.lost = True
            elif self.total == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif self.total < 21:
                print(f'You have {self.total} points.')
                take_turn(self)

    def stay(self):
        self.total = 0
        time.sleep(0.5)
        print(f'\n{self.name} stays.')
        time.sleep(0.5)
        for card in self.hand:
            if dealer.deck_and_values[card] == [1, 11]:
                i = self.hand.index(card)
                self.aces.append(self.hand.pop(i))
        for card in self.hand:
            self.total += dealer.deck_and_values[card]
        for ace in range(len(self.aces)):
            self.hand.append(self.aces.pop())
        if self.one_ace == True:
            if (self.total + 11) > 21:
                self.total += 1
            if (self.total + 11) < 21:
                self.total += 11
        elif self.two_ace == True:
            self.total = 2
        elif self.three_ace == True:
            self.total = 3
        elif self.four_ace == True:
            self.total = 4
        print(f'They ended the turn with {self.total} points.')
        time.sleep(0.5)

    def double_down(self):
        pass

    def split(self):
        pass

    def surrender(self):
        pass

    def insurance(self):
        pass

    def check_hand(self):
        self.total = 0
        time.sleep(1)
        print('\nYou have these cards in hand:\n')
        for card in self.hand:
            time.sleep(0.5)
            print(card)
        for card in self.hand:
            if dealer.deck_and_values[card] == [1, 11]:
                i = self.hand.index(card)
                self.aces.append(self.hand.pop(i))
        if self.hand != []:
            for card in self.hand:
                self.total += dealer.deck_and_values[card]
        for ace in range(len(self.aces)):
            self.hand.append(self.aces.pop())
        time.sleep(0.5)
        if self.one_ace == True:
            if (self.total + 11) > 21:
                self.total += 1
            if (self.total + 11) < 21:
                self.total += 11
        elif self.two_ace == True:
            self.total = 2
        elif self.three_ace == True:
            self.total = 3
        elif self.four_ace == True:
            self.total = 4
        print(f'Your hand totals {self.total}.')
        time.sleep(1)
        take_turn(self)       


    def check_house_hand(self):
        time.sleep(0.5)
        print(f'\nThe house has a {dealer.hand[0]}.')
        time.sleep(1)
        take_turn(self)


list_of_players = []


def make_player(name):
    Player.player_count += 1
    globals()[f'player{Player.player_count}'] = Player(name)
    list_of_players.append(globals()[f'player{Player.player_count}'])
    return list_of_players


def take_turn(person):
    print(f'\nWhat does {person.name} want to do? (1-10)\n')
    time.sleep(1)
    print('''    1) Hit
    2) Stay
    3) Double down (not implemented)
    4) Split (not implemented)
    5) Surrender (not implemented)
    6) Check your hand
    7) Check the house\'s hand
    8) Check your bet
    9) Check your wallet
    10) Quit the game
    ''')
    opt = input()
    if opt == '1':
        person.hit()
    elif opt == '2':
        person.stay()
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
        time.sleep(0.5)
        print(f'\nYou bet ${person.bet} and have ${person.wallet} left in your wallet.')
        time.sleep(0.5)
        take_turn(person)
    elif opt == '9':
        time.sleep(0.5)
        print(f'\nYou have ${person.wallet} in your wallet.')
        time.sleep(0.5)
        take_turn(person)
    elif opt == '10':
        time.sleep(0.5)
        person.wallet += person.bet
        print(f'\n{person.name} chose to leave the game with ${person.wallet} in their wallet.')
        remove_player(person)
        time.sleep(0.5)
    elif opt == 'quit':
        sys.exit()
    else:
        print('\nI\'m sorry, I didn\'t get that.')
        time.sleep(0.5)
        take_turn(person)


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
    while number_of_players:
        for person in list_of_players:
            bet = input(f'How much does {person.name} want to bet? ')
            person.place_bet(bet)
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
    time.sleep(2)
    players_turn(number_of_players, list_of_players)

def players_turn(number_of_players, list_of_players):
    while number_of_players:
        for player in list_of_players:
            if player.blackjack == True:
                number_of_players -= 1
            else:
                take_turn(player)
                number_of_players -= 1
    if number_of_players == 0:
        dealer.dealers_turn(number_of_players, list_of_players)

def end_turn(list_of_players):
    number_of_players = len(list_of_players)
    print('\nEnd of turn!')
    time.sleep(1)
    for person in list_of_players:
        if person.wallet == 0:
            print(f'\n{person.name} is broke! They\'re out of the game.')
            time.sleep(0.5)
            list_of_players.remove(person)
    print('Returning all cards to the deck and reshuffling.')
    for person in list_of_players:
        for card in person.hand:
            dealer.deck.append(card)
            person.hand.remove(card)
    for card in dealer.hand:
        dealer.deck.append(card)
        dealer.hand.remove(card)
    random.shuffle(dealer.deck)
    for person in list_of_players:
        person.total = 0
        person.blackjack = False
        person.one_ace = False
        person.two_ace = False
        person.three_ace = False
        person.four_ace = False
        person.tie = False
        person.has_21 = False
        person.lost = False
    dealer.total = 0
    dealer.blackjack = False
    dealer.has_21 = False
    dealer.one_ace = False
    dealer.two_ace = False
    dealer.three_ace = False
    dealer.four_ace = False
    dealer.lost = False
    time.sleep(0.5)
    print('\nThe next turn starts now. The dealer will deal the cards.\n')
    time.sleep(2)
    deal_players(number_of_players, list_of_players)

def remove_player(person):
    global list_of_players
    list_of_players.remove(person)
    if list_of_players == []:
        print('All players have left the game.')
        sys.exit()
    return list_of_players


number_of_players = 0
dealer = Dealer()
start_game(number_of_players)