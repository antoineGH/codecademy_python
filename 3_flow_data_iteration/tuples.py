# Create a Tuple (Immuable list)
my_info = ('Antoine', 28, 'IT')
my_info
my_info[1]
my_info[-2]

# Load Variables with Tuple (Unpacking a Tuple)
name, age, profession = my_info
name
age
profession

# Create a one element Tuple (use a comma after first element)
my_info = ('Antoine') # Creates a STR
print(type(my_info))
my_info = ('Antoine',) # Creates a Tuple
print(type(my_info))