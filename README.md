# Blackjack Rules:

1. __Cards__

- There are 52 cards in a deck
- Cards marked 2-10 will score the value they show, for example a 2 will score a 2.
- Cards that have “faces” (Jack, Queen, King)  will score a 10
- Ace will score 1 or 11, depending on the current hand:
- If the current hand score <= 10, player decides Ace value (1 or 11). If the current score >10, Ace = 1 (decision not yet implemented)
- A shoe is a shuffled pack of 6 decks
- A blank card is a red plastic card inserted in a shoe at a random position so that when the blank is drawn, the current game becomes the last
- Note for testing: the game is played from the end of the shoe, not the beginning (a higher position of the blank means fewer games)

2. __Players__

- There is a maximum of 3 players in a game, and one dealer
- Each player is dealt a two - cards hand at the beginning of the game, face-up.
- The dealer gets 2 cards as well, but one of them is face-down(hidden)
- Players place their bets on the hand they were given.

3. __Objective (game_logic)__

- Each player plays against the dealer, and NOT against each other
- Players try to have a better “score” than the dealer, without going over 21.
- The score is the total of point accumulated in a hand. 
- IF a player goes over 21 with their hand, then the player goes “bust” which means they lose the game.
- A “Blackjack” or a “natural” is a 21 composed of a “face” + an Ace, dealt in the first hand (which comprises of two cards)
- If any player, including the dealer, has Blackjack, then their hand wins, even if the opponent has 21.
- If the dealer has BlackJack, they win the game against anyone who doesn't, and tie with those who do.
- Dealer is not allowed to hit if they have a “hard 17”, which is a 17 that does not include an Ace. A soft 17 can still hit. 

4. __Game decisions__

- After the first hand is dealt including to the dealer, players have 4 choices of which only two have been included in the script, see Gambling for the other two:
- “Hit” = ask for another card
- “Stay” = forfeit their turn

5. __Game play:__

- When all the players, including the dealer, have stayed or doubled, the dealer will reveal their own cards and announce the wins/losses, also take or give the wins according to the rules above.
# How the script works:
- Run game_play.py in terminal and follow the instructions. 
- Your hand will be shown as a list and your decisions will be taken as user input
- To be continued...

# Gambling - to be implemented
1. __Blackjack__

- If a player wins against a dealer by having a Blackjack gets 3:1 of the bets they've placed (a 2 chips bet will get a 6 chips win)

2. __Game decisions:__

- “Double Down” = add 100% of the bet to the table and get one last card (placed layterally to show he is not to hit again)
- “Split” = if the player has two cards of the same value and rank (e.g., two 8s or two kings), he can play two separate hands and bet on the two separately, be dealt on them separately as well.



