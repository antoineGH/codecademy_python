### VARIABLES -------------------------------------------------------------
menu_brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
menu_early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
menu_dinner = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
menu_kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
menu_arepas = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
menus = [brunch, early_bird, dinner, kids]

### CLASS DECLARATION -----------------------------------------------------
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

    def calculate_bills(self, purchased_items):
            total_price = 0
            for item, price in self.items.items():
                for i in purchased_items:
                    if i == item:
                        total_price += price
            return total_price

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __str__(self):
        return "{}".format(self.address)

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu.name)
                print(menu)
        return available_menus

class Business:
    def __init__(self, name, franchise):
        self.name = name 
        self.franchise = franchise

### CLASS INSTANTIATION ---------------------------------------------------

brunch = Menu("Brunch", menu_brunch, 1100, 1600)
early_bird = Menu("Easly Bird", menu_early_bird, 1500, 1800)
dinner = Menu("Dinner", menu_dinner, 1700, 1100)
kids = Menu("Kids", menu_kids, 1100, 2100)
arepas_menu =  Menu("Take a’ Arepa", menu_arepas, 1000, 2000)

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepas_place = Franchise("189 Fitzgerald Avenue", menu_arepas)

business1 = Business("Basta Fazoolin' with my Heart", {flagship_store, new_installment})
business2 = Business("Take a' Arepa", menu_arepas)


### CALLS -----------------------------------------------------------------

brunch.calculate_bills({"pancakes","home fries", "coffee"})
early_bird.calculate_bills({"salumeria plate","mushroom ravioli (vegan)"})

print(flagship_store)
print(new_installment)

flagship_store.available_menus(1200)