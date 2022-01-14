import random

ranks = [r for r in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']

suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']

def get_deck():
#Return a new deck of cards.
    deck =[]
    for rank in ranks:
        for suit in suits:
            deck.append([rank, suit])
    return deck

'''a shoe is composed of 6 shuffled decks with a blank red plastic card placed in it.
create the shoe, shuffle the cards and then insert a blank card in the first part of the
shuffled shoe, so that the game isn't boringly short (we'll pop() cards from the end)
whenever this blank card is drawn, the current game is the last one. Return the shoe'''
def shuffled_shoe(deck=get_deck()):
    shoe =[]
    for i in range(6):
        shoe += deck
    random.shuffle(shoe)
    middle = len(shoe)/2
    red_card_position = random.randint(0, middle)
    shoe.insert(red_card_position, [0,'BLANK'])
    return shoe



