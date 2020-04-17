
def gen_list_dict(keys, pizzas, prices, spices):
    list_dict = []
    for index in range(len(pizzas)):
        list_elem = list([pizzas[index], prices[index], spices[index]])
        merged_dict = dict(zip(keys, list_elem))
        list_dict.append(merged_dict)
    return list_dict
        
keys = ['name', 'price', 'spices']
pizzas = ['mexicano', 'american', 'jamaican', 'spicy pepperoni', 'pepperoni']
prices = [5,6,5,8,9,7]
spices = ['very spicy', 'medium spicy', 'not spicy', 'very spicy', 'spicy']

list_dict = gen_list_dict(keys, pizzas, prices, spices)
print(list_dict)


