# Using Loop to display elements from a list
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for i in dog_breeds:
    print(i)

#for <temporary variable> in <list variable>:
#    <action>

# Using Range in Loops

for i in range(3):
  print("WARNING!")


# Loop that goes through each student in students_period_A and adds it to the end of students_period_B
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for i in students_period_A:
  students_period_B.append(i)
  print(i)

# Using Break to stop looping
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")

## Dog Example

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog_breed_I_want == dog:
    print("They have the dog I want!")
    break

# Continue 
# Let’s say we want to print out all of the numbers in a list, unless they’re negative. 
# We can use continue to move to the next i in the list

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
    if i < 0:
        continue
    print(i)

# Bar example allow only if above 21

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)

# While Loops
# list.pop remove 

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students[-1])
  all_students.pop()
  
print(students_in_poetry)

# Nested Loops
#
project_groups = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for groups in project_groups:
    for students in groups:
        print(students)

# Ice Cream Nested Loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for ice_cream in location:
    scoops_sold = scoops_sold + ice_cream
    
print(scoops_sold)

# List comprehension
# Loop in the words list and check every first letter of the world, if it matches if an @ add it to list username

words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == "@":
    usernames.append(word)
  
print(usernames)

usernames= [word for word in words if word[0]=="@"]
print(usernames)

# List comprehension - Shortcut to write 
# usernames = [word for word in words if word[0] == '@'] 

# Ride coaster
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = []

for height in heights:
  if height > 161:
    can_ride_coaster.append(height)
  
print(can_ride_coaster)

### OR (list comprehension way)

can_ride_coaster = [high for high in heights if high>161]
print(can_ride_coaster)

# List Comprehension 2 
# messages = [user + " please follow me!" for user in usernames]
# Takes a string in usernames
# Assigns that number to a variable called user
# Adds “ please follow me!” to user
# Appends that concatenation to the new list called messages
# Repeats steps 1-4 for all of the strings in usernames

# Celsius to Farenheit

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temperature_in_celsius * 9/5 + 32 for temperature_in_celsius in celsius]

print(fahrenheit)

# Review

squares = []
single_digits = range(0,10)
for digits in single_digits:
  print(digits)
  squares.append(digits**2)

print(squares)

cubes = [digits **3 for digits in single_digits ]

print(cubes)

