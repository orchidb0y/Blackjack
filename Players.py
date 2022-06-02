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
    
    def sur(self, hand):

        i = self.hands.index(hand)
        bet = self.hands[i].bet
        self.wallet += bet / 2
        self.hands[i].bet = 0
        self.hands[i].surrended = True