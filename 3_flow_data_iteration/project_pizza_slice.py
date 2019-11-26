# Functions
def list_lenght(list):
    list_len = len(list)
    return list_len

def merge_lists(list1, list2):
    merged_list = zip(list1,list2)
    return merged_list

def Sort(sub_li): 
    return(sorted(sub_li, key = lambda x: x[1]))    

def find_cheapest(list):
    return list[0]

def find_expensive(list):
    return list[-1]

def find_three_cheapest(list):
    return list [:3]

def search_count(list,element):
    count = list.count(element)
    return count

# Lists

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

toppings_len = list_lenght(toppings)
print("We sell " + str(toppings_len) + " different kinds of pizza!")
merged_list = list(merge_lists(toppings,prices))
sorted_merged_list = list(Sort(merged_list)) 
print(list(sorted_merged_list))

cheapest_pizza = find_cheapest(sorted_merged_list)
print(cheapest_pizza)

expensive_pizza = find_expensive(sorted_merged_list)
print(expensive_pizza)

three_cheapest = find_three_cheapest(sorted_merged_list)
print(three_cheapest)

count = search_count(prices,2)
print(count)