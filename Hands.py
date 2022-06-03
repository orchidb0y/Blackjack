from random import randint
from Cards import Card

class Hand:


    def __init__(self):
    
        self.hand = []
        self.value = 0
        self.aces = 0
        self.bust = False
        self.blackjack = False
        self.played = False
        self.bet = 0
        self.insurance = 0
        self.surrended = False
        self.first_choice = True
        self.split_possible = False
        self.won = False
        self.lost = False

    def get_card(self, deck, debug = False, hide = False):
    
        card = deck.deck.pop(randint(0, (len(deck.deck)-1)))
        if hide == True:
            card.hidden = True
        self.hand.append(card)

        if card.is_ace == True:
            self.aces += 1

        self.calculate_value()
        
        if len(self.hand) == 2:
            self.check_blackjack()
            if self.blackjack == True:
                self.played = True
            for card in self.hand:
                card1 = card.value
                card2 = card.value
                if card1 == card2:
                    self.split_possible = True

        elif self.value == 21:
            self.played = True

        elif self.value > 21:
            self.bust = True
            self.played = True
        
        if debug == True:
            for card in self.hand:
                print(card.value, 'card value')
            print(self.value, 'value')
            print(self.bust, 'bust')
            print(self.blackjack, 'blackjack')
            print(self.is_21, 'is 21')
        

    def check_blackjack(self):
    
        if (self.hand[0].is_ace == True and self.hand[1].value == 10) or (self.hand[0].value == 10 and self.hand[1].is_ace == True):
            self.blackjack = True

    def calculate_value(self):
    
        self.value = 0
        count = self.aces

        for card in self.hand:
            if card.value != [1, 11]:
                self.value += card.value

        if count > 0:
            if count == 1 and (self.value + 11 <= 21):
                self.value += 11
            elif count == 1:
                self.value += 1
            elif count == 2 and (self.value + 11 <= 21):
                self.value += 12
            elif count == 2:
                self.value += 2
            elif count == 3 and (self.value + 11 <= 21):
                self.value += 13
            elif count == 3:
                self.value += 3
            elif count == 4 and (self.value + 11 <= 21):
                self.value += 14
            elif count == 4:
                self.value += 4

    def renew_hand(self):

        self.hand = []
        self.value = 0
        self.aces = 0
        self.bust = False
        self.blackjack = False
        self.played = False
        self.bet = 0
        self.insurance = 0
        self.surrended = False
        self.first_choice = True
        self.won = False
        self.lost = False
    
    def debug_blackjack(self):

        ace = Card('Ace', [1, 11], is_ace = True)
        ten = Card('10', 10)

        self.hand.append(ace)
        self.hand.append(ten)

        self.blackjack = True
        self.value = 21