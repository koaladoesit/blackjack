import game_logic
#A game of blackjack has a maximum of 3 players per dealer.
#The game begins by asking how many players are at the table.
#This functions at the minute instantiates 3 players and only uses the
#amount specified. However, doesn't that keep memory occupied with
#the empty seat(s)?
def get_active_players():

    player1 = game_logic.Player()
    player2 = game_logic.Player()
    player3 = game_logic.Player()
    active_players = [player1, player2, player3]
    #get attributes only for active players
    number_players =0
    while number_players not in range(1,4):
        number_players = int(input("How many players (up to 3) are in today? "))
    pop_player = number_players

    for i in range(1, number_players+1):
        active_players[i].get_name(i)
        active_players[i].place_bet()
        active_players[i].deal_first_hand()
    while pop_player < 3:
        active_players.pop()
        pop_player+=1
    return active_players




active_players = get_active_players()


print(active_players[0].hand)
print(active_players[1].hand)

####refactor deal_first_hand to avoid gotcha!!!