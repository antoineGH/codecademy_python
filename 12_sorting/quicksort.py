#1. --- Quicksort Introduction

def quicksort(list, start, end):
  # Base case
  if start >= end:
    return 
  print("First element is \"{}\"".format(list[start]))
  start += 1
  quicksort(list, start, end)

colors = ["blue", "red", "green", "purple", "orange"]

print(quicksort(colors, 0, len(colors)))

# We’ll invoke quicksort 5 times in total. The last color is never printed because it is a 'single' element so we’ll go into the if statement that makes up our base case.

#quicksort(list, 0, 4) 
#>>> ["blue", "red", "green", "purple", "orange"], first element is "blue"
#quicksort(list, 1, 4)
#>>> ["red", "green", "purple", "orange"], first element is "red"
#quicksort(list, 2, 4)
#>>> ["green", "purple", "orange"], first element is "green"
#quicksort(list, 3, 4)
#>>> ["purple", "orange"], first element is "purple"
#quicksort(list, 4, 4)
#>>> ["orange"]
## start == end, base case!

#2. --- Pickin' Pivots

# [9, 3, 21, 4, 50, 8, 11]
# pick the first element, 9, as the pivot
# "lesser_than_list" becomes [3, 4, 8]
# "greater_than_list" becomes [21, 50, 11]

# use randrange to produce a random index
from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list
	# Define your pivot variables below
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  print("pivot_idx: {}\npivot_element: {}".format(pivot_idx, pivot_element))
  
  # Swap the elements in list below
  print("Swap the elements to keep pivot in last list index")
  list[-1], list[pivot_idx] = list[pivot_idx], list[-1]
  print("list[-1]: {}\nlist[pivot_idx]: {}".format(list[-1], list[pivot_idx]))
  
  print(list[start])
  start += 1
  return quicksort(list, start, end)

my_list = [10, 9]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)

#3. --- Partitioning Party

from random import randrange

def quicksort(list, start, end):
  if start >= end:
    return list

	# Define your pivot variables below
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  print("pivot_idx: {}\npivot_element: {}".format(pivot_idx, pivot_element))
  
  # Swap the elements in list below
  print("Swap the elements to keep pivot in last list index")
  list[-1], list[pivot_idx] = list[pivot_idx], list[-1]
  print("list[-1]: {}\nlist[pivot_idx]: {}".format(list[-1], list[pivot_idx]))

  # Create the lesser_than_pointer
  lesser_than_pointer = start
  
  # Start a for loop, use 'idx' as the variable
  # Check if the value at idx is less than the pivot
  # If so: 
    # 1) swap lesser_than_pointer and idx values
    # 2) increment lesser_than_pointer
    
  for idx in range(start, end):
    if list[idx] < pivot_element:
      print("List before swap: {}".format(list))
      list[lesser_than_pointer], list[idx]= list[idx], list[lesser_than_pointer]
      lesser_than_pointer += 1
      # After the loop is finished...
  		# swap pivot with value at lesser_than_pointer
      list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
      print("List after swap: {}".format(list))
    
  print("list[start]: {}".format(list[start]))
  start += 1
  return quicksort(list, start, end)

my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)

#4. --- Recurse, Rinse, Repeat

from random import randrange, shuffle 
def quicksort(list, start, end):
  # this portion of listay has been sorted
  if start >= end:
    return

  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  # swap random element with last element in sub-listay
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  
  # Call quicksort on the "left" and "right" sub-lists
  print("\n --- list: {}".format(list))
  print("pivot_idx: {}\npivot_element: {}".format(pivot_idx, pivot_element))
  print("left sub-list: {}".format(list[:less_than_pointer]))
  print("right sub-list: {}\n".format(list[less_than_pointer:]))
  
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)
    
unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
print(unsorted_list)
print(quicksort(unsorted_list, 0, len(unsorted_list)-1))

#5. --- Quicksort Review

# 1 We established a base case where the algorithm will complete when the start and end pointers indicate a list with one or zero elements
# 2 If we haven’t hit the base case, we randomly selected an element as the pivot and swapped it to the end of the list
# 3 We then iterate through that list and track all the “lesser than” elements by swapping them with the iteration index and incrementing a lesser_than_pointer.
# 4 Once we’ve iterated through the list, we swap the pivot element with the element located at lesser_than_pointer.
# 5 With the list partitioned into two sub-lists, we repeat the process on both halves until base cases are met.

from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return
  print("Running quicksort on {0}".format(list[start: end + 1]))
  # select random element to be pivot
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  print("Selected pivot {0}".format(pivot_element))
  # swap random element with last element in sub-lists
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      print("Swapping {0} with {1}".format(list[i], pivot_element))
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  print("{0} successfully partitioned".format(list[start: end + 1]))
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)

#list = [5,3,1,7,4,6,2,8]
#shuffle(list)
#print("PRE SORT: ", list)
#print(quicksort(list, 0, len(list) -1))
#print("POST SORT: ", list)

#PRE SORT:  [1, 6, 3, 8, 2, 7, 4, 5]
#Running quicksort on [1, 6, 3, 8, 2, 7, 4, 5]
#Selected pivot 3
#Swapping 1 with 3
#Swapping 2 with 3
#[1, 2, 3, 8, 6, 7, 4, 5] successfully partitioned
#Running quicksort on [1, 2]
#Selected pivot 1
#[1, 2] successfully partitioned
#Running quicksort on [8, 6, 7, 4, 5]
#Selected pivot 7
#Swapping 6 with 7
#Swapping 5 with 7
#Swapping 4 with 7
#[6, 5, 4, 7, 8] successfully partitioned
#Running quicksort on [6, 5, 4]
#Selected pivot 5
#Swapping 4 with 5
#[4, 5, 6] successfully partitioned
#None
#POST SORT:  [1, 2, 3, 4, 5, 6, 7, 8]