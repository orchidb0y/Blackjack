from random import randint


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
            if self.value + (count * 11) > 21:
                self.value += count
            else:
                self.value += 11
    
    def renew_hand(self):

        self.hand = []
        self.value = 0
        self.aces = 0
        self.bust = False
        self.blackjack = False
        self.played = False
        self.bet = 0
        self.insurance = 0