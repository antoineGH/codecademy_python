# Functions Even / Odd numbers in a list
def even_nums(list):
    for item in list:
        if item%2 == 0:
            print(item)

def odd_nums(list):
    for item in list:
        if item%2 == 0:
            continue
        print(item)

even_nums([4, 7, 9, 10, 13])
odd_nums([4, 7, 9, 10, 13])

# Divisible by Ten
def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0 :
            count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# Greetings
# List Comprehension
def add_greetings(names):
    greeting = ["Hello, "+ name for name in names]
    return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

# Normal Way
def add_greetings(names):
    greeting=[]
    for name in names:
        greeting.append("Hello, "+name)
    return greeting

print(add_greetings(["Owen", "Max", "Sophie"]))

# Delete Starting Even Numbers
def delete_starting_evens(lst):
  while (len(lst) > 0) and (lst[0] % 2 == 0):
    lst = lst[1:]
    return lst
      
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# Odd Indices
def odd_indices(list):
    new_list= []
    for index in range (1, len(list) ,2):
        new_list.append(list[index])
    return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# Exponents
def exponents(list1, list2):
    new_list= []
    for item in list1:
        for item2 in list2:
            new_list.append(item**item2)
    return new_list

print(exponents([2, 3, 4], [1, 2, 3]))

# Larger Sum 
def larger_sum(list1, list2):
    count1=0
    count2=0
    for num1 in list1:
        count1 += num1
    for num2 in list2:
        count2 += num2
    if count1 >= count2:
        return list1
    else:
        return list2

print(larger_sum([1, 9, 5], [2, 3, 11]))

# Over 9000
def over_nine_thousand(list):
    sum = 0
    for num in list:
        sum += num
        if sum > 9000:
            break
            return sum
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))