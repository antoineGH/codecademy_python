# String can be thought of as a list of characters.
my_string = "Antoine"

first = my_string[0]
second = my_string[1]
third = my_string[2]

print(first)
print(second)
print(third)

# Slice a string 
# string_name[first_index:last_index]
my_string = "Antoine"
slice1 = my_string[2:5]
slice2 = my_string[:5]
slice3 = my_string[4:]

print(slice1)
print(slice2)
print(slice3)

# Username = first letter surname + name
name = "ratat"
surname = "antoine"
username = surname[:1] + name
print(username)

# Concatenating Strings
fruit_prefix = "blue"
fruit_suffix = "berries"
favorite_fruit = fruit_prefix + fruit_suffix
fruit_sentence = "My favorite fruit is " + favorite_fruit

# Account generator 
def account_generator(first_name, last_name):
    account_name = first_name[:3] + last_name[:4]
    return account_name

new_account = account_generator("antoine", "ratat")
print(new_account)

# More and More String Slicing (How Long is that String?)
# len() returns the number of characters in a string

favorite_fruit = "blueberry"
length = len(favorite_fruit)
print(length)

# len() comes in handy when we are trying to select the last character in a string
# indices start at 0, so the final character in a string has the index of len(string_name) - 1.
favorite_fruit[length-1]

# You could also slice the last several characters of a string using len():
favorite_fruit[length-4:]

# Password Generator Function 

def password_generator (first_name , last_name ):
    concatenated = first_name[-3:] + last_name[-3:]
    return concatenated

temp_password = password_generator("antoine", "ratat")
print(temp_password)

# Negative Indices
#Negative indices count backward from the end of the string, so string_name[-1] is the last character of the string, 
# string_name[-2] is the second last character of the string, etc.

favorite_fruit = "blueberry"
favorite_fruit[-1] # 'y'
favorite_fruit[-2] # 'r'
favorite_fruit[-3] # 'r'
favorite_fruit[-3:] # sliced 'rry'

# company_motto exercice
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last= company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)

# Test Sliced / Position
def get_last(word, position):
    return word[position]

get_last("Antoine", 2) # 't'
get_last("Antoine", -2) # 'n'

def get_sliced(word, position):
    return word[position:]

get_sliced("Antoine", 2) # 'toine'
get_sliced("Antoine", -2) # 'ne'

# Strings are Immutable
# We’ve been selecting characters from strings, slicing strings, and concatenating strings. Each time we perform one of these operations we are creating an entirely new string.
# This is because strings are immutable.

first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"
fixed_first_name = "R" + first_name[1:] 
print(fixed_first_name)

# Escape Characters \
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

# Iterating through Strings
# Because strings are lists, that means we can iterate through a string using for or while loops

def print_each_letter(word):
    for letter in word:
        print(letter)

print_each_letter("Antoine")


# Get Lenght
def get_length(word):
    len = 0
    for letter in word:
        len += 1
    return len

get_length("Antoine")

# Strings and Conditionals (Part One)
# Letter check 
def letter_check(word, letter):
    for i in word:
        if i == letter:
            return True
            break
    return False

letter_check("antoine", "a")
letter_check("antoine", "c")
letter_check("strawberry", "a")

# Strings and Conditionals (Part Two)
# in checks if one string is part of another string.
# letter in word

"e" in "blueberry"
"a" in "blueberry"

# Contains
def contains(big_string , little_string ):
    return little_string in big_string

contains("watermelon", "melon")
contains("watermelon", "berry")

def common_letters(string_one , string_two):
    common_letter = []
    for letter in string_one:
        if letter in string_two and not (letter in common_letter):
            common_letter.append(letter)
    return common_letter

common_letters("banana", "cream")

crc= "INTRODUCTION TO STRINGS"
crc= crc[0] + crc[1:].lower()
print(crc)

# Review
def username_generator(first_name, last_name):
    username = first_name[0:3].lower() + last_name[0:4].lower()
    return username

username = username_generator("ANTOINE", "RATAT")

def password_generator(username):
    password = username[-1] + username[:-1]
    return password

print(password_generator(username))

# Built-in Method 

# count(item) : count(item) in string
string="antoine ratat, le roi des méchants"
string = string.count("a")
print(string)

# is a lower ? title ? digit ? alpha ? num ? space ?
string="antoine ratat, le roi des méchants"
string.isalnum()
string.isalpha()
string.isdigit()
string.islower()
string.isnumeric()
string.isspace()
string.istitle()
string.isupper()

# lower() upper() title() : convert to lower and check / convert to upper and check / convert to title and check
string="antoine ratat, le roi des méchants"
string = string.upper()
string.isupper()
print(string)

string = string.lower()
string.islower()
print(string)

string = string.title()
string.istitle()
print(string)

# replace() replace str by str in string
string="antoine ratat, le roi des méchants"
string = string.replace("antoine", "bastien")
print(string)

# swapcase() : Upper to Lower / Lower to Upper
string="antoine ratat, le roi des méchants"
string = string.swapcase()
print(string)