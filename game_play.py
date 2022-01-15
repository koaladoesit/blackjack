import game_logic
from players import Player

'''
- There is a maximum of 3 players in a game, and one dealer
- Each player is dealt a two - cards hand at the beginning of the game, face-up.
- The dealer gets 2 cards as well, but one of them is face-down(hidden)
- Players place their bets on the hand they were given.'''

# This was a function that instantiated 3 players and only used the
# number specified. However, I don't like wasting memory,
# so let's write some ugly code!



number_of_players = 0
# The game begins by asking how many players are at the table.
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

for i in range(0, number_of_players):
    active_players[i].place_bet()

#TO DO: instantiate the dealer as a player:
dealer = Player(4)




print(player1.hand)
print(player2.hand)
print(dealer.hand[0])