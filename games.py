import random

money = 100

#Write your game of chance functions here

def coin_toss(call, bet, money):
    current_bet = bet
    toss = random.randint(1, 2)
    if toss == 1 and call == "Heads":
        print("YOU WIN! The coin came up Heads. You have won ${bet}".format(bet = bet))
        money += current_bet
    elif toss == 2 and call == "Tails":
        print("YOU WIN! The coin came up Tails. You have won ${bet}".format(bet = bet))
        money += bet
    else:
        print("Sorry you lose. Please play again")
        money -= bet
    print(money)

coin_toss("Heads", 30, money)


#Call your game of chance functions here
