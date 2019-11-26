def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
 
sing_song()
sing_song()
 
def loading_screen():
    print("This page is loading...")
 
loading_screen()
 
# Loose indentation > outside of the function
 
def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
print("And the world will be as one")
 
sing_song()
 
# Single Parameter
 
def mult_two_add_three(number):
    print(number*2 +3)
 
mult_two_add_three(10)
mult_two_add_three(0)
mult_two_add_three(-1)
 
# Multiple Parameters
 
def mult_x_add_y(number,x,y):
    print(number*x +y)
 
mult_x_add_y(5,2,3)
mult_x_add_y(1,3,1)
 
def create_spreadsheet(title,row_count=1000):
    print("Creating a spreadsheet called "+ title +" with " + str(row_count) + " rows")
 
create_spreadsheet("GODZILLA")
 
# Positional arguments (order 1,2,3)
create_spreadsheet("Applications",10)
 
# Keywords arguments
create_spreadsheet(row_count=10,title="Applications")
 
# Single Return Value
 
def calculate_age(current_year,birth_year):
    my_age = current_year - birth_year
    return my_age
 
my_age= calculate_age(2019,1990)
dad_age= calculate_age(2019,1975)
 
print ("I am " + str(my_age) + " years old and my dad is " + str(dad_age) + " years old")
 
# Multiple Return Value
 
def get_boundaries(target,margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
 
low, high = get_boundaries(100,20)
print("Low limit : " + str(low) + "\n High limit : " + str(high))
 
# Scope
current_year = 2019
 
def calculate_age(birth_year):
    my_age = current_year - birth_year
    return my_age
 
my_age= calculate_age(1990)
print ("I am " + str(my_age) + " years old")   
 
# Review
 
def repeat_stuff(stuff,num_repeats=10):
    return stuff*num_repeats
 
repeat_stuff("Row ",3)
 
lyrics = repeat_stuff("Row ",3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)
