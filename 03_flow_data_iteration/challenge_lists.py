### DOUBLE INDEX

# Functions
def double_index(list, index):
    if (index > 0) and (index < len(list)):
        list[index] = list[index] * 2
        return list
    else: 
        print("Invalid index")
    

# List 
my_list = [3, 8, -10, 12]
print(my_list)
my_list = double_index(my_list, 3)
print(my_list)

### REMOVE MIDDLE

# Functions
def remove_middle(list,start,end):
    list = list[:start] + list[end+1:]
    return list

# Call
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


### MORE THAN N
# Functions
def more_than_n(list, item, n):
    if list.count(item) > n:
        return True
    else: 
        return False
# Call
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

### MORE FREQUENT ITEM
# Functions
def more_frequent_item(list, item1, item2):
    if list.count(item1) >= list.count(item2):
        return item1
    else:
        return item2
# Call
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

### MIDDLE ITEM
# Functions
def middle_element(list):
    if len(list)%2 == 0:
        sum= list[int(len(list)/2)] + list[int(len(list)/2)]-1
        return sum/2
    else:
        return list[int(len(list)/2)]

# Call
print(middle_element([5, 2, -10, 4, 5,10]))

### APPEND SUM
# Functions
def append_sum(list):
    for i in range(3):
        list.append(list[-1]+list[-2])
    return list

# Call
print(append_sum([1, 1, 2]))

### LARGER LIST
# Functions
def larger_list(list1, list2):
    if len(list1) >= len(list2):
        return list1[-1]
    else:
        return list2[-1]

# Call
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10,4]))

### COMBINE SORT
# Functions
def combine_sort(list1, list2):
    list_combined = list1 + list2
    list_combined.sort()
    return list_combined
# Call
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

### APPEND SIZE
# Functions
def append_size(list):
    list.append(len(list))
    return list
# Call
print(append_size([23, 42, 108]))

### EVERY THREE NUMBS
# Functions
def every_three_nums(start):
    if start > 100:
        list_range = []
        return list_range
    else:
        list_range = range(start,101,3)
        return list_range

# Call
print(list(every_three_nums(91)))