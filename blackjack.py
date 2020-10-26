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
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = '' #empty string

        for card in self.deck:
            deck_comp += '\n ' + card.__str__() #add each Card object's print string
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Create Hand class

class Hand:

    def __init__(self):
        self.cards = [] # empty list
        self.value = 0 # start with zero value
        self.aces = 0 # add an attribut to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        # to aid function below
        if card.rank == 'Ace':
            self.aces += 1 # add to self.aces
        
    def adjust_for_ace(self):
        # If a hand's value exceeds 21 but it contains an Ace, reduce the Ace's value from 11 to 1 and continue playing
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Create Chips class

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# A function for taking bets

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except ValueError:
            print('Sorry, a bet must be an integer')

        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed',chips.total):
            else:
                break


# A function for taking hits

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# A function to prompt the player to Hit or Stand

def hit_or_stand(deck,hand):
    global playing # to control upcoming while loop

    while True:
        x = input('Would you like to Hit or Stand? Enter "h" or "s")

        if x[0].lower() == "h":
            hit(deck,hand) # hit function defined above

        elif x[0].lower == "s":
            print('Player stands. Dealer is playing.')

            playing = False
        
        else:
            print('Sorry, please try again.')
            continue
        break