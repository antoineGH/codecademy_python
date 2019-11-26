#A radix is the base of a number system. For the decimal number system, the radix is 10.
#Radix sort has two variants - MSD and LSD
#Numbers are bucketed based on the value of digits moving left to right (for MSD) or right to left (for LSD)
#Radix sort is considered a non-comparison sort
#The performance of radix sort is O(n)

#1. Finding the Max Exponent

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  maximum_value = str(maximum_value)
  max_exponent = len(maximum_value)
  return max_exponent
  
list_to_sort = [1, 3333, 2]
print(radix_sort(list_to_sort))

# >>> 4

#2. Setting Up For Sorting

#Create a copy of to_be_sorted and save the copy into a new list called being_sorted

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for digit in range(10)]
  return digits

#3. Bucketing Numbers

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for i in range(10)]

  for number in being_sorted:
    number_as_a_string = str(number)
    digit = number_as_a_string[-1]
    digit = int(digit)
    digits[digit].append(number)
    print(digits[digit])
  return digits

list_to_sort = [1, 3333, 2]
print(radix_sort(list_to_sort))

#4. Rendering the List

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))

  being_sorted = to_be_sorted[:]
  digits = [[] for i in range(10)]

  for number in being_sorted:
    number_as_a_string = str(number)
    digit = number_as_a_string[-1]
    digit = int(digit)
    digits[digit].append(number)

  # reassign being_sorted here:
  being_sorted = []
  for numeral in digits:
    being_sorted.extend(numeral)
  return being_sorted

list_to_sort = [1, 3333, 2]
print(radix_sort(list_to_sort))
    
#5. Iterating through Exponents

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    digits = [[] for i in range(10)]
    position = exponent + 1
    index = -position 

    for number in being_sorted:
      number_as_a_string = str(number)
      digit = number_as_a_string[index]
      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)
  return being_sorted

#6. Review (and Bug Fix!)

#Takes numbers in an input list.
#Passes through each digit in those numbers, from least to most significant.
#Looks at the values of those digits.
#Buckets the input list according to those digits.
#Renders the results from that bucketing.
#Repeats this process until the list is sorted.

def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
      	digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)

      digits[digit].append(number)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted

unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
print(radix_sort(unsorted_list))