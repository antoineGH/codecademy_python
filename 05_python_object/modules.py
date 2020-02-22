# A module is a collection of Python declarations intended broadly to be used as a tool. 
# from module_name import object_name
from matplotlib import pyplot

# Import datetime from datetime below:
from datetime import datetime
print(help(datetime)) # Diplay module help
print(dir(datetime)) # Display object help

current_time = datetime.now()
print(current_time)

# Datatime operations
# Load and display a datetime variable
from datetime import datetime
birthday = datetime(1990, 10, 6, 20, 30, 12)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)

# Diplay Time now
print(datetime.now())

# Calculate Delta between 2 times
delta = datetime.now() - birthday
print(delta)

delta2017_2018 = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(delta2017_2018)

delta_jesus = datetime.now() - datetime(1,1,1)
print(delta_jesus)

# Parse date and time with a specified format
# Create datetime from a string
parsed_data = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
parsed_data.year
parsed_data.month
parsed_data.day

# Format Datetime to string
# Create string from datetime
date_string = datetime.strftime(datetime.now(),'%b %d, %Y')

# Modules Python Random

# random.choice() : takes a list as an argument and returns a number from the list
# random.randint() : takes two numbers as arguments and generates a random number between the two numbers you passed in

import random

random_list = []
random_list = [ random.randint(1, 100) for number in range(101) ]

randomer_number  = random.choice(random_list)
print(randomer_number)

# Modules Python Namespaces

# Create Module Alias
# import module_name as name_you_pick_for_the_module

# Import object pyplot alias plt in the module matplotlib
from matplotlib import pyplot as plt
import random

numbers_a = range(1,13)
numbers_b = random.sample(range(1000),12)

plt.plot(numbers_a,numbers_b)
plt.show()

# Modules Python Decimals

from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction) #Returns 0.45 instead of 0.44999999999999996

# Example Decimal 

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

# Modules Python Files and Scope

# import always_three (function) from library.py (File)
# from library import always_three

# Pipenv Virtual Environment

