#Game = War
#


class Card:
    # Two class variables defined, suits and values
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]
    #Two 'None' items so that the value matches the index for convenience
    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    #Magic method __less than__, a rich comparison method. This is what called when you write something < something else
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    #Magic method __greater than__, a rich comparison method.
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    #__represent__ represents the object of a card, using our values as indexes for the class variables in our list
    #This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.
    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v


from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        #randomises items in a list by changing index?
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return      # if len card is 0, the code end here and nothing gets returned.
        return self.cards.pop()     #if not true, a 'popped' card (drawn from the top of the deck) is returned


class Player:
    def __init__(self, name):
        self.wins = 0       #starts as the integer 0 and can be incremented
        self.card = None    #starts as None as a placeholder, will change as game goes on
        self.name = name

class Game:
    def __init__(self):
        name1 = input("Player 1 name: ")
        name2 = input("Player 2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):     #just prints out who won to user
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Let the games begin!")
        while len(cards) >=2:
            m = "Type q to quit. Type any key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Tie game."


    



