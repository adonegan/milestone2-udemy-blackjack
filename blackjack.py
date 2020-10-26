import random

# Declare variables

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five' , 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5 , 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Declare game state

game_on = False

# Create Card class

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit


# Create Deck class

class Deck:

    def __init__(self):
        # instantiate 52 card deck
        self.deck = [] #empty list
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank) # create card object
                
                self.deck.append(new_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


# Create Hand class

class Hand:

    def __init__(self):
        self.cards = [] # empty list
        self.value = 0 # start with zero value
        self.aces = 0 # add an attribut to keep track of aces

    def add_card(self,card):
        return self.cards.append(new_card)

    def adjust_for_ace(self):
        pass


# Create Chips class

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass
    