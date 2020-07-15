import random

money = 100

#Write your game of chance functions here

def coin_toss(call, bet, money=money):
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
    print("Your new total is: ${money}.".format(money = money))

#Test for Coin Toss
#coin_toss("Heads", 30)

def cho_han(call, bet, money=money):
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    if (die_one + die_two)%2 == 0 and call == "Even":
        print("YOU WIN! The dice fell as {die_one} and {die_two}. The total is {total}. You win {bet}.".format(die_one = die_one, die_two = die_two, total = (die_one + die_two), bet = bet))
        money += bet
    elif (die_one + die_two)%2 != 0 and call == "Odd":
        print("YOU WIN! The dice fell as {die_one} and {die_two}. The total is {total}. You win {bet}.".format(die_one = die_one, die_two = die_two, total = (die_one + die_two), bet = bet))
        money += bet
    else:
        print("Sorry, you lose. Better luck next time.")
        money -= bet
    print("Your new total is: ${money}".format(money = money))

#Testing Cho Han game
#cho_han("Odd", 40)

def pick_a_card(bet, money=money):
    player_one = random.randint(1,10)
    player_two = random.randint(1,10)
    if player_one > player_two:
        print("Congratulations. You win ${bet}.".format(bet=bet))
        money += bet
    elif player_two > player_one:
        print("Sorry. You Lose. Try again.")
        money -= bet
    else:
        print("It was a tie!")
    print("Your new total is: ${money}".format(money = money))

#Testing out Pick a Card Game
#pick_a_card(15)

#Call your game of chance functions here
