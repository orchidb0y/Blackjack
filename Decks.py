from Cards import Card


class Deck:


    def __init__(self, number_of_decks=5):
    
        self.deck = []

        suits = [' of Clubs', ' of Diamonds', ' of Hearts', ' of Spades']
        numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        cards = []
        for suit in suits:
            for number in numbers:
                cards.append(number + suit)

        values = ([[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4)
        for card, value in zip(cards, values):
            self.deck.append(Card(card, value))
        
        self.deck = self.deck * number_of_decks