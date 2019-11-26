# 2. Implement Linear Search
def linear_search(search_list, target_value):
    for number in range(len(search_list)):
        if target_value == search_list[number]:
            return number
    raise ValueError("{} not in the list".format(target_value))

list = [22,5,10,15,46,87,8,7,5,4,54,123]
print(linear_search(list, 8))

# 3. Using Linear Search

number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 100

def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))

try:
  result = linear_search(number_list, target_number)
  print("{} index in the list is {}".format(target_number, result))

except ValueError as error_message:
  print("{0}".format(error_message))

# 4. Finding Duplicates

tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if len(matches) != 0:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))

tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)

# 5. Finding the Maximum Value

test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

highest_score = linear_search(test_scores)
print("Highest Score : {}".format(highest_score))

# 6. Review