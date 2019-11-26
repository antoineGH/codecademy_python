# Recursion 1
def sum_to_one(n):
  result = 1
  call_stack = []
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  return result, call_stack

sum_to_one(5)

# Recursion 2

def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  
  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print(type(call_stack))
    print(type(return_value))
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']
  return result, call_stack

sum_to_one(4)
print(list(sum_to_one(4)))

# Recursion 3

def sum_to_one(n):
  result = 0
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return sum_to_one(n-1) + n

print(sum_to_one(7))

# Recursion 4

def factorial(n):
  if n < 2:
    return 1
  print("Recursing with input: {0}".format(n))
  return n * factorial(n-1) 

print(factorial(12))

# Recursion 5

def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU', 'Sup\'La Rache']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)

# Recursion 6

def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print("List found!")
      flat_list = flatten(item)
      result += flat_list
    else:
      result.append(item)
  return result

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

# Recursion 7
def fibonacci(n):
  if n < 2:
    return n
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)

fibonacci_runtime = "2^N"
print("RunTime: {}".format(fibonacci_runtime))

# Recursion 8
def build_bst(my_list):
  if len(my_list)==0:
    return "No Child"
  
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  print("Middle index: {}\nMiddle value: {}".format(middle_idx, middle_value))
  
  tree_node = {"data": middle_value}
  tree_node["left_child"]= build_bst(my_list[:middle_idx ])
  tree_node["right_child"]= build_bst(my_list[middle_idx + 1 : ])
  return tree_node

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

runtime = "N*logN"

