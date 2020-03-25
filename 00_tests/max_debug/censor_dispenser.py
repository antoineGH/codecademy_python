
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("E:/git/codeacademy_python/00_tests/max_debug/email_one.txt", "r").read()
email_two = open("E:/git/codeacademy_python/00_tests/max_debug/email_two.txt", "r").read()
email_three = open("E:/git/codeacademy_python/00_tests/max_debug/email_three.txt", "r").read()
email_four = open("E:/git/codeacademy_python/00_tests/max_debug/email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censored_word(email, word):
    email_replaced = email.replace(word, "")
    return email_replaced

#print(censored_word(email_one, "Progress")

def censored_list(word):
    result = email_two.replace(word, "")
    return result

#for word in proprietary_terms:
#    email_two = censored_list(word)

#print(email_two)

def censored_list(word):
    result = email_three.replace(word, "")
    return result

def censored_list_special(word):
    result = email_three.replace(word, "")
    return result

for word in proprietary_terms:
    email_three = censored_list(word)

for word in negative_words:
    email_three = censored_list_special(word)

print(email_three)

