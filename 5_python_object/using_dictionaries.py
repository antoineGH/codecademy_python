# Get A Key
# You can access the values in it by providing the key
# print(dictionary_name[key]
# >>> value

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
#>>> ['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])
#>>> ['Aries', 'Leo', 'Sagittarius']

# Get an Invalid Key
# If a Key does not exist in the dictionary  > throw a KeyError
# Best practice is to check if the key exists

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])
else:
    print("Not in the dictionary")

# Try/Except to Get a Key

building_heights = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

key_to_check = "lol"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")

# Example 
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level ["matcha"] = 30
try :
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

# Safely Get a Key
# Dictionaries have a .get() method to search for a value. If the key does not exist : return None or Arg2
# print(caffeine_level.get("LOL""We don't have this coffee..."))

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

print(caffeine_level.get("espresso", "We don't have this coffee..."))
# >>> 64
print(caffeine_level.get("LOL", "We don't have this coffee..."))
# >>> We don't have this coffee...
print(caffeine_level.get("LOL"))
# >>> None

# Example 
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# Delete a Key
# .pop() works to delete items from a dictionary, when you know the key value.

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

# Print Value and delete Key/Value pair
raffle.pop(320291, "No Prize")
# >>>"Gift Basket"
print(raffle)
# >>> {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

# Nothing to delete return "No Prize"
raffle.pop(100000, "No Prize")
# >>>"No Prize"
print(raffle)
# >>> {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}

# Example

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# add the value of "stamina grains" to health_points and remove the item from the dictionary. 
# If the key does not exist, add 0 to health_points
health_points += available_items.pop("stamina grains", 0)

# add the value of "power stew" to health_points and remove the item from the dictionary. 
# If the key does not exist, add 0 to health_points
health_points += available_items.pop("power stew", 0)

# add the value of "mystic bread" to health_points and remove the item from the dictionary. 
# If the key does not exist, add 0 to health_points
health_points += available_items.pop("mystic bread", 0)

print(health_points)
print(available_items)

# Get All Keys
# dictionary_name.keys()

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# assign users to be all of the keys of the user_ids list
users = user_ids.keys()

# Print users keys to the console
for user in user_ids.keys():
  print(user)

 # assign lessons to be all of the keys of the num_exercises list
lessons = num_exercises.keys()

# Print lessons keys to the console
for chapters in num_exercises.keys():
  print(chapters)

# Get All Value
# dictionary_name.values()
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

# Print lessons values to the console
for scores in test_scores.values():
    print(scores)

# Get all of the values as a list
list(test_scores.values())

# Example 

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

# Iterate through the values in the num_exercises list and add each value to the total_exercises
for values in num_exercises.values():
  print(values)
  total_exercises += values
  
print(total_exercises )

# Get All Items
# dictionary_name.items()
# return tuple of (key, value)

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for key_brand, value_money in biggest_brands.items():
  print(key_brand + " has a value of " + str(value_money) + " billion dollars. ")

# Example 

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out
for key_job, value_pct in pct_women_in_occupation.items():
  print("Women make up {value} percent of {key}s.".format(value = value_pct, key = key_job))

# Review

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

# Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread
spread ["past"] = tarot.pop(13)
print(spread)

# Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.
spread ["present"] = tarot.pop(22)
print(spread)

# Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread
spread ["future"] = tarot.pop(10)
print(spread)

# Iterate through the items in the spread dictionary and for each key: value pair, print out 
for key_time, value_tarot in spread.items():
  print("Your {key} is the {value} card.".format(key = key_time, value = value_tarot))