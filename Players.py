from Hands import Hand
from time import sleep

class Player:

    player_count = 0

    def __init__(self, name, hands=[]):
    
        self.name = name
        self.hands = hands
        self.wallet = 100

    def place_bet(self, bet, i = 0):
    
        bet = int(bet)
        if self.wallet >= bet:
            self.hands[i].bet = bet
            self.wallet -= bet
    
    def split(self, hand):
        
        i = self.hands.index(hand)
        new_hand = Hand()
        self.hands.insert(i + 1, new_hand)
        self.hands[i + 1].hand.append(self.hands[i].hand.pop())
        self.hands[i].split_possible = False
    
    def double_down(self, hand):

        i = self.hands.index(hand)
        bet = self.hands[i].bet
        self.wallet -= bet
        self.hands[i].bet += bet
    
    def sur(self):

        bet = self.hands[0].bet
        self.wallet += bet / 2
        self.hands[0].bet = 0
        self.hands[0].surrended = True
    
    def reward_bet(self, hand):

        if hand.lost == True:
            pass
        
        elif hand.won == True and hand.blackjack == True:
            self.wallet += hand.bet
            self.wallet += hand.bet * 1.5
        
        elif hand.won == True and hand.blackjack == False:
            self.wallet += hand.bet
            self.wallet += hand.bet
        
        elif hand.won == False and hand.blackjack == True:
            self.wallet += hand.bet
        
        elif hand.won == False and hand.lost == False:
            self.wallet += hand.bet

    def insure(self, hand):
        
        hand.insurance = (hand.bet / 2)
        sleep(1)
        print(f'You have placed an insurance of {hand.insurance}.')
        sleep(0.5)
    
    def reward_insurace(self, hand):

        self.wallet += (hand.insurance * 2)