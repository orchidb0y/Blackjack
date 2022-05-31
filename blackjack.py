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

# Each player will start with $100 in their pocket
# No splitting

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

    def __init__(self, number_of_decks = 1):
        values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = [' of Clubs', ' of Diamonds', ' of Hearts', ' of Spades']
        for suit in suits:
            for number in numbers:
                self.deck.append(number + suit)
        self.deck_and_values = dict(zip(self.deck, values * 4))
        self.deck = self.deck * number_of_decks
        random.shuffle(self.deck)

    def deal_player(self, person):
        print('Dealing for {name}:\n'.format(name = person.name))
        time.sleep(0.5)
        if self.deck != []:
            dealing1 = self.deck.pop()
        else:
            end_game()
        if self.deck_and_values[dealing1] == [1, 11]:
            person.one_ace = True
        person.hand.append(dealing1)
        print(dealing1)
        time.sleep(0.5)
        if self.deck != []:
            dealing2 = self.deck.pop()
        else:
            end_game()
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
        if self.deck != []:
            dealing = self.deck.pop()
        else:
            end_game()
        if self.deck_and_values[dealing] == [1, 11]:
            self.one_ace = True
        else:
            self.total += self.deck_and_values[dealing]
        self.hand.append(dealing)
        print(dealing)
        time.sleep(0.5)
        if self.deck != []:
            dealing = self.deck.pop()
        else:
            end_game()
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
        if self.deck != []:
            deal = self.deck.pop()
        else:
            end_game()
        if self.one_ace == True:
            for card in self.hand:
                if self.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand.pop(i))
            for card in self.hand:
                if self.hand != []:
                    self.total += self.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            if self.deck_and_values[deal] == [1, 11]:
                self.one_ace = False
                self.two_ace = True
            else:
                self.total += self.deck_and_values[deal]
        elif self.two_ace == True:
            for card in self.hand:
                if self.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                if self.hand != []:
                    self.total += self.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            if self.deck_and_values[deal] == [1, 11]:
                self.two_ace = False
                self.three_ace = True
            else:
                self.total += self.deck_and_values[deal]
        elif self.three_ace == True:
            for card in self.hand:
                if self.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                if self.hand != []:
                    self.total += self.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            if self.deck_and_values[deal] == [1, 11]:
                self.three_ace = False
                self.four_ace = True
            else:
                self.total += self.deck_and_values[deal]
        elif self.four_ace == True:
            for card in self.hand:
                if self.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand[i])
            for card in self.hand:
                if self.hand != []:
                    self.total += self.deck_and_values[card]
            for ace in range(len(self.aces)):
                self.hand.append(self.aces.pop())
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}.')
            time.sleep(0.5)
            self.total += self.deck_and_values[deal]
        else:
            for card in self.hand:
                self.total += self.deck_and_values[card]
            self.hand.append(deal)
            time.sleep(0.5)
            print(f'\nThe dealer got a {deal}')
            time.sleep(0.5)
            if self.deck_and_values[deal] == [1, 11]:
                self.one_ace = True
            else:
                self.total += self.deck_and_values[deal]
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
                self.total += 1
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
                self.total += 12
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
                self.total += 13
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
                self.total += 14
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
        for player in list_of_players:
            if player.lost == True:
                busted_players += 1
        if busted_players == len(list_of_players):
            time.sleep(1)
            print('\nEveryone is busted!')
            time.sleep(1)
            self.end_of_turn(list_of_players)
        else:
            print(f'\nNow it\'s the dealer\'s turn.')
            time.sleep(1)
            print(f'\nThe hidden card is {self.hidden_card}')
            self.hand.append(self.hidden_card)
            self.hidden_card = ''
            time.sleep(1)
            if self.blackjack == True:
                print('The dealer has a blackjack!')
                self.total = 21
                self.end_of_turn(list_of_players)
            elif self.one_ace == True:
                self.total += 11
                print(f'The hand totals {self.total} points.')
                self.take_turn(number_of_players, list_of_players, goal)
            elif self.two_ace == True:
                self.total += 12
                print('The hand totals {self.total} points.')
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
                if person.surrended == True:
                    time.sleep(0.5)
                    print(f'\n{person.name} surrended and lost this round.')
                    person.lose_count += 1
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                elif person.blackjack == False and self.blackjack == True:
                    if person.insure == True:
                        print(f'{person.name} was insured, earning them 2:1. Adding {person.insurance * 2} to their wallet.')
                        self.house -= person.insurance * 2
                        self.house += person.bet
                        person.wallet += person.insurance * 3
                        person.money_won_lost += person.insurance * 2
                        person.money_won_lost -= person.bet
                        person.bet = 0
                        person.lose_count += 1
                        time.sleep(0.5)
                        print(f'They now have ${person.wallet} in their wallet.')
                        time.sleep(0.5)
                    else:
                        print(f'{person.name} was not insured. They lose the turn and their bet.')
                        self.house += person.bet
                        person.lose_count += 1
                        person.money_won_lost -= person.bet
                        person.bet = 0
                elif person.blackjack == True and self.blackjack == True:
                    print(f'\nIt\'s a push between {person.name} and the dealer!')
                    person.wallet += person.bet
                    person.bet = 0
                    person.tie_count += 1
                    time.sleep(0.5)
                elif person.blackjack == True and self.blackjack == False:
                    print(f'\n{person.name} has a blackjack, earning them 3:2 ! Adding ${person.bet * 0.5} to their wallet.')
                    self.house -= (person.bet * 1.5)
                    person.wallet += (person.bet * 2.5)
                    person.money_won_lost += (person.bet * 1.5)
                    person.bet = 0
                    person.win_count += 1
                    person.blackjack_count += 1
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                elif person.total > self.total and person.total <= 21:
                    print(f'\n{person.name} won over the dealer!')
                    time.sleep(0.5)
                    print(f'They got 1:1 over their bet. Adding ${person.bet} to their wallet.')
                    self.house -= person.bet
                    person.wallet += 2 * person.bet
                    person.money_won_lost += person.bet
                    person.bet = 0
                    person.win_count += 1
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
                elif person.total == self.total:
                    print(f'\nIt\'s a tie between {person.name} and the dealer!')
                    person.wallet += person.bet
                    person.bet = 0
                    person.tie_count += 1
                    time.sleep(0.5)
                elif person.total < self.total or person.total > 21:
                    print(f'\n{person.name} lost to the dealer!')
                    time.sleep(0.5)
                    print('Their money goes to the house.')
                    self.house += person.bet
                    person.money_won_lost -= person.bet
                    person.bet = 0
                    person.lose_count += 1
                    time.sleep(0.5)
                    print(f'They now have ${person.wallet} in their wallet.')
                    time.sleep(0.5)
        elif self.lost == True:
            for person in list_of_players:
                if person.lost == False:
                    if person.blackjack == True:
                        print(f'\n{person.name} has a blackjack, earning them 3:2 ! Adding ${person.bet * 1.5} to their wallet.')
                        self.house -= (person.bet * 1.5)
                        person.wallet += (person.bet * 2.5)
                        person.money_won_lost += (person.bet * 1.5)
                        person.bet = 0
                        person.win_count += 1
                        person.blackjack_count += 1
                        time.sleep(0.5)
                        print(f'They now have ${person.wallet} in their wallet.')
                        time.sleep(0.5)
                    else:
                        print(f'\n{person.name} won over the dealer!')
                        time.sleep(0.5)
                        print(f'They got 1:1 over their bet. Adding ${person.bet} to their wallet.')
                        self.house -= person.bet
                        person.wallet += 2 * person.bet
                        person.money_won_lost += person.bet
                        person.bet = 0
                        person.win_count = 1
                        time.sleep(0.5)
                        print(f'They now have ${person.wallet} in their wallet.')
                        time.sleep(0.5)
                if person.lost == True:
                    print(f'\n{person.name} was bust, so they lose their bet anyway.')
                    time.sleep(0.5)
                    print('Their money goes to the house.')
                    self.house += person.bet
                    person.money_won_lost -= person.bet
                    person.bet = 0
                    person.lose_count = 1
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
        self.insurance = 0
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
        self.first_choice = True
        self.win_count = 0
        self.lose_count = 0
        self.tie_count = 0
        self.blackjack_count = 0
        self.money_won_lost = 0
        self.doubled_down = False
        self.surrended = False
        self.insure = False
    
    def __repr__(self):
        print(self.name, 'name')
        print(self.total, 'points')
        print(self.blackjack, 'blackjack')
        print(self.one_ace, 'one ace')
        print(self.two_ace, 'two ace')
        print(self.three_ace, 'three ace')
        print(self.four_ace, 'four ace')
        print(self.tie, 'tie')
        print(self.lost, 'lost')
        print(self.first_choice, 'first choice')
        print(self.bet, 'bet')
        print(self.insurance, 'insurance')
        print(self.wallet, 'wallet')
        print(self.hand, 'hand')
        print(self.doubled_down, 'doubled down')
        print(self.surrended, 'surrended')
        print(self.insure, 'insurance')
        take_turn(self)
        return 'nul'

    def place_bet(self, bet):
        value = int(bet)
        if (self.wallet - value) > 0:
            self.bet = value
            self.wallet -= value

    def hit(self):
        self.total = 0
        if dealer.deck != []:
            deal = dealer.deck.pop()
        else:
            end_game()
        if self.first_choice == True:
            self.first_choice = False
        if self.one_ace == True:
            for card in self.hand:
                if dealer.deck_and_values[card] == [1, 11]:
                    i = self.hand.index(card)
                    self.aces.append(self.hand.pop(i))
            for card in self.hand:
                if self.hand != []:
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
                if self.hand != []:
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
                if self.hand != []:
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
                if self.hand != []:
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
            if self.doubled_down == True:
                pass
            elif (self.total + 11) > 21:
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
            if self.doubled_down == True:
                pass
            elif (self.total + 2) > 21:
                print('You\'re bust!')
                self.lost = True
            elif (self.total + 2) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 2) < 21:
                print(f'You have {self.total + 2} points.')
                take_turn(self)
        elif self.three_ace == True:
            if self.doubled_down == True:
                pass
            elif (self.total + 3) > 21:
                print('You\'re bust!')
                self.lost = True
            elif (self.total + 3) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 3) < 21:
                print(f'You have {self.total + 3} points.')
                take_turn(self)
        elif self.four_ace == True:
            if self.doubled_down == True:
                pass
            elif (self.total + 4) > 21:
                print('You\'re bust!')
                self.lost = True
            elif (self.total + 4) == 21:
                print('You have 21 points!')
                self.has_21 = True
            elif (self.total + 4) < 21:
                print(f'You have {self.total + 4} points.')
                take_turn(self)
        else:
            if self.doubled_down == True:
                pass
            elif self.total > 21:
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
            if self.hand != []:
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
        time.sleep(0.5)
        print(f'\n{self.name} doubles down!')
        time.sleep(0.5)
        self.wallet -= self.bet
        self.bet = self.bet * 2
        print(f'New bet is worth ${self.bet}.')
        time.sleep(0.5)
        self.doubled_down = True
        self.hit()
        self.total = 0
        for card in self.hand:
            if dealer.deck_and_values[card] == [1, 11]:
                i = self.hand.index(card)
                self.aces.append(self.hand.pop(i))
        for card in self.hand:
            if self.hand != []:
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

    def split(self):
        pass

    def sur(self):
        time.sleep(0.5)
        print(f'{self.name} is surrendering, therefore they forfeit half of their bet.')
        self.wallet += (self.bet / 2)
        self.bet = 0
        self.surrended = True
        time.sleep(0.5)

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
    if person.first_choice == True:
        print(f'\nWhat does {person.name} want to do first? (1-9)\n')
        time.sleep(1)
        print('''        1) Hit
        2) Stay
        3) Double down
        4) Split (not implemented)
        5) Surrender
        6) Check your hand
        7) Check the house\'s hand
        8) Check your bet and wallet
        9) Quit the game
        ''')
        opt = input()
        if opt == '1':
            person.hit()
        elif opt == '2':
            person.stay()
        elif opt == '3':
            person.double_down()
        elif opt == '4':
            print('Splitting is not implemented in the game.')
            take_turn(person)
        elif opt == '5':
            person.sur()
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
            person.wallet += person.bet
            print(f'\n{person.name} chose to leave the game with ${person.wallet} in their wallet.')
            time.sleep(0.5)
            print(f'During the game, they won {person.win_count} times, lost {person.lose_count} times, tied {person.tie_count} times and got {person.blackjack_count} blackjacks.')
            time.sleep(0.5)
            print(f'Their net gain/loss was ${person.money_won_lost}')
            remove_player(person)
            time.sleep(0.5)
        elif opt == 'quit':
            sys.exit()
        elif opt == 'debug':
            print(person)
        elif opt == 'deck length':
            print(len(dealer.deck))
        else:
            print('\nI\'m sorry, I didn\'t get that.')
            time.sleep(0.5)
            take_turn(person)
    else:
        print(f'\nWhat does {person.name} want to do now? (1-6)\n')
        time.sleep(1)
        print('''        1) Hit
        2) Stay
        3) Check your hand
        4) Check the house\'s hand
        5) Check your bet
        6) Quit the game
        ''')
        opt = input()
        if opt == '1':
            person.hit()
        elif opt == '2':
            person.stay()
        elif opt == '3':
            person.check_hand()
        elif opt == '4':
            person.check_house_hand()
        elif opt == '5':
            time.sleep(0.5)
            print(f'\nYou bet ${person.bet} and have ${person.wallet} left in your wallet.')
            time.sleep(0.5)
            take_turn(person)
        elif opt == '6':
            time.sleep(0.5)
            person.wallet += person.bet
            print(f'\n{person.name} chose to leave the game with ${person.wallet} in their wallet.')
            time.sleep(0.5)
            print(f'During the game, they won {person.win_count} times, lost {person.lose_count} times, tied {person.tie_count} times and got {person.blackjack_count} blackjacks.')
            time.sleep(0.5)
            print(f'Their net gain/loss was ${person.money_won_lost}')
            remove_player(person)
            time.sleep(0.5)
        elif opt == 'quit':
            sys.exit()
        elif opt == 'debug':
            print(person)
        elif opt == 'deck length':
            print(len(dealer.deck))
            take_turn(person)


def start_game(number_of_players):
    print('Welcome to Standard Blackjack. Each player starts with $100 in their wallets. The payout for a blackjack is 3:2. The payout for a successful insurance is 2:1.')
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
    print()
    while number_of_players:
        for person in list_of_players:
            bet = input(f'How much does {person.name} want to bet? ')
            person.place_bet(bet)
            number_of_players -= 1
    number_of_players = len(list_of_players)
    num_of_decks = int(input('\nHow many decks do you want to play with? The more decks, the longer the game can run. '))
    globals()['dealer'] = Dealer(num_of_decks)
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
    if dealer.deck_and_values[dealer.hand[0]] == [1, 11]:
        print('\nThe dealer is showing an Ace. Players will have to decide if they want to insure their hands against a blackjack.')
        time.sleep(1)
        for person in list_of_players:
            insure = input(f'Does {person.name} want to make an insurance? (y/n)\n')
            if insure == 'y':
                person.insure = True
                person.wallet -= (person.bet / 2)
                person.insurance = (person.bet / 2) 
                time.sleep(0.5)
                print(f'{person.name} took an insurance of ${person.insurance} against a blackjack.')
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
    print('Reshuffling.')
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
        person.first_choice = True
        person.hand = []
        person.doubled_down = False
        person.surrended = False
        person.insure = False
    dealer.total = 0
    dealer.blackjack = False
    dealer.has_21 = False
    dealer.one_ace = False
    dealer.two_ace = False
    dealer.three_ace = False
    dealer.four_ace = False
    dealer.lost = False
    dealer.hand = []
    time.sleep(3)
    print('\nThe next turn starts now. The dealer will deal the cards after each player places a new bet.\n')
    time.sleep(2)
    for person in list_of_players:
        bet = input(f'How much does {person.name} want to bet? ')
        person.place_bet(bet)
    print()
    deal_players(number_of_players, list_of_players)

def remove_player(person):
    global list_of_players
    list_of_players.remove(person)
    if list_of_players == []:
        print('All players have left the game.')
        sys.exit()
    return list_of_players

def end_game():
    print('\nLooks like the 52 card deck is over. End of the game!')
    for person in list_of_players:
        person.wallet += person.bet
        time.sleep(1)
        print(f'\nDuring the game, {person.name} won {person.win_count} times, lost {person.lose_count} times, tied {person.tie_count} times and got {person.blackjack_count} blackjacks.')
        time.sleep(0.5)
        print(f'Their net gain/loss was ${person.money_won_lost}')
        time.sleep(1)
    sys.exit()

os.system('cls')
number_of_players = 0
dealer = Dealer()
print('''
#######    #              #       ##########  #     #    ##########       #       ##########  #     #
#      #   #             # #      #           #    #              #      # #      #           #    #
#       #  #             # #      #           #   #               #      # #      #           #   #
#       #  #            #   #     #           #  #                #     #   #     #           #  #
#      #   #            #   #     #           # #                 #     #   #     #           # #
#     #    #           #     #    #           ##                  #    #     #    #           ##
#      #   #           #######    #           ##                  #    #######    #           ##
#       #  #          #       #   #           # #         #       #   #       #   #           # #
#       #  #          #       #   #           #  #        #       #   #       #   #           #  #
#      #   #         #         #  #           #   #       #       #  #         #  #           #   #
#######    ########  #         #  ##########  #    #      #########  #         #  ##########  #    #
 
 ----------------------------------------------------------------------------------------------------
 
 ''')
start_game(number_of_players)