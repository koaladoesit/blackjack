from players import Player
from game_logic import decide, compare_hands, reset_game
from shoe import get_score

'''
- There is a maximum of 3 players in a game, and one dealer
- Each player is dealt a two - cards hand at the beginning of the game, face-up.
- The dealer gets 2 cards as well, but one of them is face-down(hidden)
- Players place their bets on the hand they were given.'''


def play_game(active_players, dealer): # function to play one game in a sitting
    all_hands_done = True # set to True to hunt down the 'black swan' of players still having
                            #moves left
    all_hands_busted = True
    game_restart = False
    has_blank = False
    while not game_restart:
        for player in active_players:
            if dealer.busted:
                player.win = True
                break # if the dealer is busted, we need to restart the game
            else:
                print("{}, you have this hand: {} and the dealer has one {} of {}".format(player.name, player.hand, dealer.hand[0][0], dealer.hand[0][1]))
                print("{} decide:".format(player.name))
                has_blank = decide(player)
            if not player.busted: all_hands_busted ==False
            if player.busted == False or player.stay == False:
                all_hands_done == False
            else:
                break
        if not all_hands_busted: #checking whether all players busted, which would make dealer's decision useless
            has_blank = decide(dealer)
        if dealer.busted or all_hands_done:
            game_restart = True
    return has_blank



# This was a function that instantiated 3 players and only used the
# number specified. However, I don't like wasting memory,
# so let's write some ugly code!
has_blank = False # The game will continue until someone draws the blank card
number_of_players = 0
# The session begins by asking how many players are at the table.
while number_of_players not in range(1,4):
    print("There is a maximum of 3 players in a game")
    number_of_players = int(input("How many players are in today? "))
if number_of_players == 3:
    player1 = Player(1)
    player2 = Player(2)
    player3 = Player(3)
    active_players = [player1, player2, player3]
elif number_of_players == 2:
    player1 = Player(1)
    player2 = Player(2)
    active_players = [player1, player2]
elif number_of_players == 1:
    player1 = Player(1)
    active_players = [player1]

#for i in range(0, number_of_players):
#    active_players[i].place_bet()

#dealer is a player who doesn't use all his attributes nor shows all his cards during gameplay:
dealer = Player(4)

#let's play the game:
while has_blank == False:
    has_blank = play_game(active_players, dealer)
    for player in active_players:
#also checking if the player is not busted, cuz the compare tool won't care and a busted hand could win
        if not player.busted:
            compare_hands(player, dealer)
        print(" Hand for {}".format(player.name), player.hand)
    print("Dealer's hand: ", dealer.hand) # show dealer's hand
    for i in range(0, number_of_players):
        print (i)
        reset_game(active_players[i], i)
    reset_game(dealer, 4)



