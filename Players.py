from Hands import Hand

class Player:

    player_count = 0

    def __init__(self, name, hands=[]):
    
        self.name = name
        self.hands = hands
        self.wallet = 100

    def place_bet(self, bet, i):
    
        bet = int(bet)
        if self.wallet > bet:
            self.hands[i].bet = bet
            self.wallet -= bet
    
    def split(self):
        
        new_hand = Hand()
        self.hands.append(new_hand)
    
    def double_down(self, hand):

        i = self.hands.index(hand)
        bet = self.hands[i].bet
        self.wallet -= bet
        self.hands[i].bet += bet