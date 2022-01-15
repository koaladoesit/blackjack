import random


# There are 52 cards in a deck, ranks containing 10 numbers and 4 faces,
# each of them available in 4 different suits:
ranks = [r for r in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']

suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']

def get_deck():
#Return a new deck of cards.
    deck =[]
    for rank in ranks:
        for suit in suits:
            deck.append([rank, suit])
    return deck

'''
- A shoe is a shuffled pack of 6 decks
- A blank card is a red plastic card inserted in a shoe at a random position so that when the blank
is drawn, the current game becomes the last
- I prefer to insert the blank at a random position < middle, so that, drawing from the end of the
pack, I can have longer games going.
'''
#create shoe:
def shuffled_shoe(deck=get_deck()):
    shoe =[]
    for i in range(6):
        shoe += deck
    random.shuffle(shoe)
    middle = len(shoe)/2
    red_card_position = random.randint(0, middle)
    shoe.insert(red_card_position, [0,'BLANK'])
    return shoe

'''
- Cards marked 2-10 will score the value they show, for example a 2 will score a 2.
- Cards that have “faces” or “ranks” (Jack, Queen, King)  will score a 10
- Ace will score 1 or 11, depending on the current hand:
- If the current hand score <= 10, player decides Ace value (1 or 11).
- If the current score >10, Ace = 1
'''

# calculate the score of the current hand
# TO DO: implement player decision:
def score(hand):
    score = 0
    has_ace = False
    has_face = False
    blackjack =  False
    for card in hand:
        if type(card[0])== int:
            score+=card[0]
        elif card in ['JACK', 'QUEEN', 'KING']:
            score+=10
            has_face = True
        else: has_ace = True
    if has_ace and has_face:
        has_blackjack = True
    if has_ace and not has_face:
        if score <= 10:
            score += 11
        else:
            score+=1
    return (score, blackjack)

def check_if_busted(score):
    busted = False
    if score > 21:
        busted = True
    return busted

shoe = shuffled_shoe()