### lists

age = [18, 19, 20, 18, 20]
name = ['kevin', 'alphonse', 'martin', 'thomas', 'jean']
surname = ['dupont', 'durand', 'martille', 'bouli', 'tolle']

print(age,name,surname)

combined = zip(age, name, surname)
print(list(combined))
print(age)
age.append(120)
print(age)

range_100 = range(0,101,10)
print(list(range_100))

# Gradebook

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = zip(subjects, grades)
print(list(gradebook))

# Select last element / list lenght / select index

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]

print(last_element, element5)

# Sliced 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sliced = letters[1:6]
print(sliced)

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase [len(suitcase)-2:]

# Counting elements in a list

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
laurie_votes = votes.count('Laurie')
print(jake_votes)

# Sort elements in list

names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
names.sort()
print(names)

numbers = []
numbers = range(0,100,8)
print(list(numbers))
numbers.sort()
print(list(numbers))

# Exercise sort

# Functions
def sort(list):
  list.sort()
  return list

# List
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

print(sort(addresses))
print(sort(names))
print(sort(cities))

### OR ###

names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
sorted_names = sorted(names)
print(sorted_names)

### Review ###

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
 
inventory_len = len(inventory) # Get list lengh
first = inventory[0] # Get list 1st index
last = inventory[-1] # Get list last index
inventory_2_6 = inventory[2:6] # Get list from index start to index end
first_3 = inventory[:3] # get list 3rd first indexes
twin_beds = inventory.count('twin bed') # count how many times twin bed appears in the list
inventory.sort() # sort the list
sorted_inventory = sorted(inventory)
print(sorted_inventory)