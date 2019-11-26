# --- Rules of the Throwdown

# Recursion
def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

# Iteration
def factorial(n):
  if n < 0:
    ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1
  result = 1
  while n != 0:
    result =+ result * n
    n -= 1
  return result
 
print(factorial(3) == 6)
print(factorial(0) == 1)
print(factorial(5) == 120)

# --- Fibonacci

# Recursion
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

# Iteration
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")

  fibs = [0, 1]
  
  if n <= len(fibs) - 1:
    return fibs[n]

  while n > len(fibs) - 1:
    fibs.append(fibs[-1] + fibs[-2])
    
  return fibs[-1]

fibonacci(3)
fibonacci(7)
fibonacci(0)

# ---  Sum Digits

# Recursion
def sum_digits(n):
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n//10) + last_digit

print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)

print(552%10)
print(552//10)

# Iteration
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

# --- Find min List

# Recursion
def find_min(my_list, min=None):
  if not my_list:
    return min
  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min(my_list[1:], min)

print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) == None)
print(find_min([13, 72, 19, 5, 86]) == 5)

# Iteration
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

# --- Palindrome

# Iteration
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True

# Recursion
def is_palindrome(my_string):
  if len(my_string)<2:
    return True
  if my_string[0] != my_string[-1]:
    return False
  return is_palindrome(my_string[1:-1])

# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)

# --- Multiplication

# Iteration
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

# Recursion
def multiplication(num_a, num_b):
  if num_a == 0 or num_b == 0:
    return 0

  return num_a + multiplication(num_a, num_b - 1)

print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)

# --- How Deep Is Your Tree

def depth(tree):
  if not tree:
    return 0

  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])

  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

# HELPER VARIABLES
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
