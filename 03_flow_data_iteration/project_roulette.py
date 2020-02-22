import random


# Functions 
def roulette():
    num = random.randint(1, 36)
    return num

def odd_even(bet_odd_even):
    odd_even = bet_odd_even%2
    if odd_even == 0:
        return "odd"
    else:
        return "even"

def check_win(bet_number,bet_odd_even,number,odd_even,bet):
    if (bet_number == number) and (bet_odd_even == odd_even):
        print("You win !!!")
        bet = bet*10
        return bet
    elif (bet_number == number) or (bet_odd_even == odd_even):
        print("Half win !")
        bet = bet*2
        return bet
    else :
        print("You loose...")   
        bet = bet*-1
        return bet
    
# Code

money = 100
bet = int(input ("Welcome to Roulette Game, How much would you like to bet : "))
bet_number = input("Please Enter your bet (1-36) : ")
bet_odd_even = input("Please Enter your bet (odd/even) : ")
number = roulette()
odd_even = odd_even(number)
print("Roulette stopped on "+ str(number)+", it's a " + odd_even +".\n")
bet = check_win(bet_number,bet_odd_even,number,odd_even,bet)
print(bet)
money = money + bet
print(money)
