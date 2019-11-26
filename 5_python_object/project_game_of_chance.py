########################################

import random
money = 100
bet = 0

#Write your game of chance functions here

def check_input (bet):
    if bet == "Heads" or bet == "heads":
        bet = 1
        return bet
    elif bet == "Tails" or bet == "tails": 
        bet = 2
        return bet 
    else :
        bet = 0
        return "Wrong input."
        
def roll_dice():
  num = random.randint(1, 10)
  return "The dice roll is " + str(num) + ", motherfucker!\n"

def roll_dice_cho():
    num = random.randint(1, 6)
    return num

def odd_even(cast1, cast2):
    sum1 = cast1 + cast2
    if sum1%2 == 0:
        return 1
    else:
        return 2

def check_win(pair_impair):
    if pair_impair == cast_user:
        return "You win!"
    else :
        return "You loose!"

def heads_tails(bet):
  num = random.randint(1, 2)
  if num == 1:
      print ("It's head !")
  elif num == 2:
      print ("It's tail !")

  if num == bet :
      return "You win !"
  else :
      return "You loose..."

def check_input_pair (bet):
    if bet == "Pair" or bet == "pair":
        bet = 1
        return bet
    elif bet == "Impair" or bet == "impair": 
        bet = 2
        return bet 
    else :
        bet = 0
        return "Wrong input."

#Call your game of chance functions here

#print (roll_dice())
#bet = input("Enter your bet (Heads or Tails) : ")
#bet = check_input(bet)
#print (heads_tails(bet))

cast_user = input("Enter your bet (Pair or Impair) : ")
cast_user = check_input_pair (cast_user)
cast1 = roll_dice_cho()
cast2 = roll_dice_cho()
print (cast1, cast2)
pair_impair = odd_even (cast1,cast2)
print (check_win(pair_impair))

