from shoe import get_score, check_if_busted

'''
Dealer won't hit if they have a “hard 17”, which is a 17 that
does not include an Ace. A soft 17 can still hit.

Decisions:
After the first hand is dealt including to the dealer, players have 4 choices:
- “Hit” = ask for another card
- “Stay” = forfeit their turn
- “Double Down” = add 100% of the bet to the table and get one last card (placed layterally to show he is not to hit again)
- “Split” = if the player has two cards of the same value and rank (e.g., two 8s or two kings), he can play two separate hands and bet on the two separately, be dealt on them separately as well.

'''
def decide(player):
    if player.name == "Dealer":
        has_blank = get_score(player.hand)[3]
        score = get_score(player.hand)[0]
           #if dealer, check if has ace and 17 (soft 17) or less than 17 score
        if score < 17 or (score == 17 and get_score(player.hand)[2]==True):
            player.deal()
            print("Dealer hits")
            if player.hand[-1][0] == "BLANK":
                has_blank = True # this seems a bit redundant since we'll check anyway while scoring...
                player.deal() # deal again if blank
            score = get_score(player.hand)[0]
            if score>21:
                print("Game Over, all hands win against Dealer! ")
                player.busted = True
        #to do , function to make all other hands win
        elif score >= 17 and score < 21:
            print("Dealer stays.")
            player.stay = True
        else:
            print("Game Over, all hands win against Dealer! ")
            player.busted = True

        #to do , function to make all other hands win
    #check if dealer and if so, use the 17 strategy to take a decision. Otherwise let user decide
    else:
        score = get_score(player.hand)[0]
        has_blank = get_score(player.hand)[3] # checks if we drew the blank
        if check_if_busted(score) :
            print("This player is busted! ")
            player.busted = True
        elif player.tie:
            print("This player has tied!")
        else:  #doing just the "hit" and"stay" implementation, for starters:
            decision = input(" Hit or stay? ")
            if decision.lower()== "hit":
                player.deal()
                if player.hand[-1][0] == "BLANK":
                    has_blank = True # this seems a bit redundant since we'll check anyway while scoring...
                    print("BLANK was drawn, this is the last game")
                    player.deal() # deal again if blank
                score = get_score(player.hand)[0]
                if score > 21:
                    print("This player is busted! ")
                    player.busted = True
            elif decision.lower()== "stay":
                print("Player stays!")
                player.stay = True
            else:
                print("Unable to prevent you from being a smart...jack, forfeating turn! :D")

    return  has_blank # returns True if a blank card was drawn

def compare_hands(player, dealer):
    if get_score(dealer.hand)[1]: #checks if dealer has blackjack
        if get_score(player.hand)[1]: #checks if player has blackjack
            player.tie = True
            print("Player {} tie!".format(player.name))
        else:
            player.loss = True
            print("Player {} lost".format(player.name))
    else: # compare hands with the dealer's and decide the outcome of the current game
        if get_score(dealer.hand)[0] > get_score(player.hand)[0]:
            player.loss = True
            print("Player {} lost".format(player.name))
        elif get_score(dealer.hand)[0] < get_score(player.hand)[0]:
            player.win = True
            print("Player {} won".format(player.name))
        else:
            player.tie = True
            print("Player {} tie".format(player.name))

def reset_game(player, number):  # reset the player's attributes to default values, to start a new game
    if player.win: player.wins+=1
    if player.lost: players.losses+=1
    player.hand = []
    player.__init__(number)
    player.win = False
    player.lost = False
    player.tie= False
    player.busted = False









