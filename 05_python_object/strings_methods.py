# Formatting Methods 
# upper()| title()

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
poem_author_fixed = poem_author.upper()

print(poem_title_fixed)
print(poem_author_fixed)

# Splitting Strings
# string_name.split(delimiter)

string="Antoine, Kevin, Bryan, Bastien, Yann"
print (string.split(","))

string="Antoine| Kevin| Bryan| Bastien| Yann"
print (string.split("|"))

string="Antoine Kevin Bryan Bastien Yann"
print (string.split())

# Split Author's name on "," and create a list only with last name
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
author_temp = [] 
for i in author_names:
  author_temp.append(i.split())
author_last_names = []

for i in author_temp:
  author_last_names.append(i[1])
print(author_last_names)

# We can also split strings using escape sequences string.split('\n')

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

# Joining Strings
# .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.
# 'delimiter'.join(list_you_want_to_join)

my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
string = ' '.join(my_munequita)
print(string)

# We could join this list together with ANY string. One often used string is a comma ,

santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)

# Join list with \n
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
print(smooth_fifth_verse)

# .strip()
# Python provides a great method for cleaning strings: .strip(). 
# Stripping a string removes all whitespace characters from the beginning and end
featuring = "           rob thomas                 "
clean = featuring.strip()
print(clean)

# By including the argument '!' we are able to strip all of the ! characters from either side of the string
featuring = "!!!       rob thomas       !!!!!"
clean = featuring.strip('!')
clean = clean.strip()
print(clean)

# Strip and join
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
    
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# Replace
# Replace takes two arguments and replaces all instances of the first argument in a string with the second argument
# string_name.replace(character_being_replaced, new_character)

with_spaces = "You got the kind of loving that can be so smooth"
with_underscores  = with_spaces.replace(' ','_')
print(with_underscores)

# Exemple Replace
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

# .find()
# .find() takes a string as an argument and searching the string it was run on for that string and return its index.
'smooth'.find('t')
'4'

# Exemple Find
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# .format()
# .format() takes variables as an argument and includes them in the string that it is run on. 
def poem_title_card (poet, title):
  return  "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

# Format 2 - Other way to display don't have to respect order when give variable to the function.
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")
print(my_beard_description)

# Review
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

titles=[]
poets=[]
dates=[]

highlighted_poems_list=highlighted_poems.split(',')
highlighted_poems_stripped = [line.strip() for line in highlighted_poems_list]
print(highlighted_poems_stripped)

for i in highlighted_poems_stripped:
    split = i.split(':')
    
    titles.append(split[0])
    poets.append(split[1])
    dates.append(split[2])

print("Titles are {}".format(titles))
print("Poets are {}".format(poets))
print("Dates are {}".format(dates))

for i in range(0,len(highlighted_poems_stripped)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

