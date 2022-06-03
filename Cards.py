class Card:


    def __init__(self, card, value, is_ace = False):
    
        self.card = card
        self.value = value
        self.is_ace = is_ace
        self.hidden = False
    
        if self.value == [1, 11]:
            self.is_ace = True