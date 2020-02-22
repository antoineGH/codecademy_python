import random
import sys 

# VARIABLES ----------------------------

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
player_to_words  = {"CPU1": ["BLUE", "TENNIS", "EXIT"], "CPU2": ["EARTH", "EYES", "MACHINE"], "CPU3": ["ERASER", "BELLY", "HUSKY"], "CPU4": ["ZAP", "COMA", "PERIOD"],}
player_to_points = {}

# FUNCTIONS ----------------------------

def create_dictionary(list1, list2, dictionary_name):
    # Create dictionary 'dictionary_name' from list1 and list2 using list comprehension with zip()
    dictionary_name = {key:value for key, value in zip(list1, list2)}
    return dictionary_name

def add_dictionary_value(key, value, dictionary):
    # Add key/value pair in dictionary
    dictionary.update({key.upper(): value})
    print("Adding key \'{key}\', value \'{value}\' in dictionary.\n".format(key=key, value=value))

def generate_random_letters():
    # Generate a list of 7 random letters (random_letters) from the list (letters)
    random_letters = []
    for number in range (0,7):
        randomer_number  = random.choice(letters)
        random_letters.append(randomer_number)
    return random_letters

def input_player_word(random_letters):
    # Get the list of random letters
    # Input player 
    # Append new words into word_list, press 0 to stop input words
    # Check if the letters used are in the list of letters
    # Return Tuple player(str), word_list(list)

    word_list = []
    exit = 0
    player = input("Enter new player: ")
    print("Please use {letters}".format(letters=random_letters))
    while (exit != 1):
        word = input("Enter new word (0 to finish): ")
        if word == "0":
            exit = 1
        else:
            word = word.upper()
            acceptable = True
            for i in range(0,len(word)):
                if word[i] not in random_letters:
                    acceptable = False
            if acceptable == True :                             
                word_list.append(word)
                print(word_list)
            else:
                print("Not in the list !")
                print("Please use {letters}".format(letters=random_letters))
    return player, word_list;

def check_already_existing(word_list):
    # Check if one word exist more than 1 time in the list (word_list)
    for word in word_list:
        if (word_list.count(word) > 1):
            print("Cheater you used multiple time the same word !")
            return sys.exit(0)  

def play_word(player, word):
    # If player already exists browse the list of word
        # For each word in list words if the player = player_key(existing player) append the new word at the end of the words list.
    # If player doesn't exists
        # Update dictionary with player(key) and list of word(value)
    if player in player_to_words:
        for w in word:  
            for player_key, words in player_to_words.items():
                if player == player_key:
                    words.append(w)
        return player_to_words
    else :
        player_to_words.update({player: word})
        return player_to_words    
    
def score_word(word):
    # Browse letter in word and increment point_total with letter_to_points(letter (key)) to get the points(value)
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total

def player_score_word(dictionary_player_word):
    # Browse players and words from dictionary with nested for 
    # Increment player_points with the return of score_word(word) 
    # Update player_to_points dictionary with player(key) and player_points(value)
    for player, words in dictionary_player_word.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points.update({player: player_points})
    return player_to_points

def print_word_points(word):
    # Print letters in word and their corresponding points
    # Print total points for letter using the score_word function to calculate points.
    for letter in word:
        print("{letter}: {point}".format(letter=letter, point=letter_to_points.get(letter, 0)))
    print("TOTAL {word}:{total_point}\n".format(word=word, total_point= score_word(word)))

def print_player_score_word(dictionary_player_word):
    # Browse players and words from dictionary with nested for 
    # Print player_to_points.get(player) to get the total_points (value) for the player (key)
    for player, words in dictionary_player_word.items():
        print("---- {player} ----\n".format(player=player.upper()))
        for word in words :
            print_word_points(word)
        print("TOTAL {player}: {point_player}\n".format(player=player.upper(), point_player=player_to_points.get(player)))
   
def check_winner(player_to_points):
    # Convert Dictionary to list, Sorted the list, Create list[-1] (winner), Print winner name and points
    player_to_words_list = [ [value, key] for key,value in player_to_points.items()]
    player_to_words_list_sorted = sorted(player_to_words_list)
    winner = player_to_words_list_sorted[-1]
    print("\nWINNER \'{winner}\': {points} points.".format(winner=winner[1] , points=winner[0]))

# CALLS --------------------------------

letter_to_points = create_dictionary(letters, points, "letter_to_points")

add_dictionary_value("", 0, letter_to_points)

random_letters = generate_random_letters()

player, word_list = input_player_word(random_letters)

check_already_existing(word_list)

play_word(player, word_list)

player_to_points = player_score_word(player_to_words)

print_player_score_word(player_to_words)

check_winner(player_to_points)