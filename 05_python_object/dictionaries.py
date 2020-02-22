#1. What is a Dictionary?
# A dictionary begins and ends with curly braces { }
# Each item consists of a key and a value 
# Each key/value pair  is separated by a comma 

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

#2. Make a Dictionary
# Possible to map number to number
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

# Possible to map string to list
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

# Possible to mix types
person = {"name": "Shuri", "age": 18, "siblings": ["T'Chaka", "Ramonda"]}

translations = {'mountain': 'orod', 'bread': 'bass', 'friend':	'mellon', 'horse':	'roch'}
    
#3. Invalid Keys
# We cannot use a list or a dictionary as keys of the dictionary.
# We can use a list or a dictionary as a value in a dictionary, 
children = {"von Trapp" : ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

#4. Empty Dictionary
# Create an empty dictionary.
empty_dict = {}

#5. Add A Key
# To add a single key : value pair to a dictionary, we can use the syntax:
#my_dict["new_key"] = "new_value"

# Create Empty Dictionnary
animals_in_zoo = {}
# Add a single key / value pair
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)

#6. Add Multiple Keys
# Add multiple key : value pairs to a dictionary at once with .update() method

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# Add two new users to the user_ids dictionary
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#7. Overwrite Values
# If the entry already exist in our dictionary, it would be overwritten
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
print(oscar_winners)

oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

#8. List Comprehensions to Dictionaries
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}

print(students)

# Remember that zip() combines two lists into a list of pairs. This list comprehension:

# Takes a pair from the zipped list of pairs from names and heights
# Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# Creates a key : value item in the students dictionary
# Repeats steps 1-3 for the entire list of pairs

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(type(zipped_drinks))
print(zipped_drinks)

# Create 'drinks_to_caffeine' dictionary with a list comprehension with zipped_drinks list and turns each pair into a key:value item
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(type(drinks_to_caffeine))
print(drinks_to_caffeine)

#9. Review

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Llist comprehension to create 'plays 'dictionary that zip(songs, playcounts) and creates a song:playcount pair
plays = {song : playcounts for song, playcounts in zip(songs, playcounts)}
print(plays)

# Add a new entry to plays
plays["Purple Haze"]= 1
print(plays)

# Update the value of "Respect" in plays
plays.update({"Respect": 94})
print(plays)

# Create dictionary with key "The Best Songs" with a value of plays, key "Sunday Feelings" with a value of an empty dictionary
library = {"The Best Songs": plays , "Sunday Feelings": {}}
print(library)
