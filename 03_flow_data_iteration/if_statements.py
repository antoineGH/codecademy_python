# IF Statements Basic
def dave_check(username):
    if username == "dave":
        return "Get off my computer Dave!"

def angela_check(username):
    if username == "angela":
        return "Get off my computer Angela"

username = "angela"
print(dave_check(username))
print(angela_check(username))

# IF Statements Operator 
def greater_than (x,y):
  if x > y:
    return x
  if x < y:
    return y
  if x == y:
    return "These numbers are the same"

greater_than(5,3)

def graduation_reqs (credits):
  if credits >= 120:
      return "You have enough credits to graduate!"
    
print(graduation_reqs(120))

# IF Statements + AND
def graduation_reqs(credits,gpa):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"
  
graduation_reqs(120,2.0)

# IF Statements + OR
def graduation_mailer (credits, gpa):
  if credits>=120 or gpa>=2.0:
    return True
  
print (graduation_mailer(120,2.0))

# IF Statements + NOT
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  
  if (gpa >= 2.0) and (credits < 120):
    return "You do not have enough credits to graduate."
  
  if (gpa < 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  
  if (gpa < 2.0) and (credits < 120):
    return "You do not meet either requirement to graduate!"
  
print(graduation_reqs(2.0,120))
print(graduation_reqs(2.0,119))
print(graduation_reqs(1.9,120))
print(graduation_reqs(1.9,119))

def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  else:
    return "You do not meet the GPA or the credit requirement for graduation." 
  
graduation_reqs(0.0,120)

def applicant_selector(gpa,ps_score,ec_count):
  if (gpa >= 3.0) and (ps_score >= 90) and ( ec_count >= 3):
    return "This applicant should be accepted."
  elif (gpa >= 3.0) and (ps_score >= 90) :
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."


# MOVIE REVIEW 
# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif (rating > 5) and (rating < 9):
    return "This one was fun."
  else :
    return "Outstanding!"
  
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"


print(movie_review(6))
# should print "This one was fun."


# TWICE AS LARGE 
# Write your twice_as_large function here:
def twice_as_large(num1,num2):
  if num1 > (num2 * 2):
    return True
  else : 
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False


print(twice_as_large(11, 5))
# should print True

# EXPONENT
# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else :
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# MODULO
# Write your divisible_by_ten function here:

def divisible_by_ten(num):
  if num%10==0:
    return True
  else:
    return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# COMPARE NUMBER TIE
# Write your max_num function here:
def max_num(num1, num2, num3):
  if ( num1 > num2 ) and ( num1 > num3 ):
    return num1
  elif ( num2 > num1 ) and ( num2 > num3 ):
    return num2
  elif ( num3 > num2 ) and ( num3 > num1 ):
    return num3
  else:
    return "It's a tie!"
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

# Budget 
# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < (food_bill + electricity_bill + internet_bill + rent)):
    return True
  else: 
    return False
# Uncomment these function calls to test your over_budget function:
#print(over_budget(100, 20, 30, 10, 40))
# should print False
#print(over_budget(80, 20, 30, 10, 30))
# should print True

# ALWAYS FALSE
# Write your always_false function here:
def always_false(num):
  if (num > 0) or (num < 0) or (num == 0):
    return False
  
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# not sum to 10
# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if (num1 + num2 != 10):
    return True
  else : 
    return False
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False

# COMPARE NAME
# Write your same_name function here:
def same_name(your_name,my_name):
  if (your_name == my_name):
    return True
  else :
    return False
  
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))


