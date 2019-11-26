#1. Separation

def merge_sort(items):
  if len(items) <= 1:
    return items

#2. Partitions

def merge_sort(items):
  if len(items) <= 1:
    return items
  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  return middle_index, left_split, right_split


#3. Creating the Merge Function

def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    return middle_index, left_split, right_split
  
def merge(left, right):
  result = []
  return result


#4. Merging

def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    return middle_index, left_split, right_split

def merge(left, right):
    result = []
    while (left and right):
      if left[0] < right[0]:
        result.append(left.pop(0))
      else:
        result.append(right.pop(0))   
    return result


#5. Finishing the Merge

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  return middle_index, left_split, right_split

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right

    return result


#6. Finishing the Sort

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
	
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)
  
  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  
  if left:
    result += left
  if right:
    result += right
  
  return result


# Testing the sort 

# merge_sort() which is called recursively breaks down an input list to smaller, more manageable pieces. merge() which is a helper function built to help combine those broken-down lists into ordered combination lists.
# merge_sort() continues to break down an input list until it only has one element and then it joins that with other single element lists to create sorted 2-element lists. Then it combines 2-element sorted lists into 4-element sorted lists. It continues that way until all the items of the lists are sorted!


def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1, ordered_list2, ordered_list3)

# Easy Example

def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  print(left_sorted)
  right_sorted = merge_sort(right_split)
  print(right_sorted)
  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

unordered_list1 = [5, 4, 6, 7]

ordered_list1 = merge_sort(unordered_list1)

print(ordered_list1)

#>>>[5]
#>>>[4]
#>>>[4, 5]
#>>>[6]
#>>>[7]
#>>>[6, 7]
#>>>[4, 5, 6, 7]