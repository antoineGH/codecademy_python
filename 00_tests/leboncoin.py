### VARIABLES DECLARATION

clients_list = []

### CLASS DELCARATION

class Marketplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, item_id):
        for item in marketplace.listings:
            if item_id == item.item_id:
                self.listings.remove(item)
                print("\nRemove {} from Marketplace.".format(item_id))

    def show_listings(self):
        print("\n--- ALL ITEMS ---\n")
        for list in self.listings:
            print("{}: {} {}€ (ID:{}).\nOwned by {} {}. Phone: {}, Mail:{}.\n".format(list.item_title, list.item_description, list.item_price, list.item_id, list.item_owner.name, list.item_owner.surname, list.item_owner.phone, list.item_owner.mail))
        print("\n")

class Client:
    def __init__(self, name, surname, mail, phone, location, wallet):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.phone = phone
        self.location = location
        self.wallet = wallet

    def __repr__(self):
        return("{} {}, {}, {} @{} ({}€).".format(self.name, self.surname, self.mail, self.phone, self.location, self.wallet))

    def debit_wallet(self, amount):
        self.wallet -= amount

    def credit_wallet(self, amount):
        self.wallet += amount

class Item:
    def __init__(self, item_title, item_description, item_id, item_price, item_owner):
        self.item_title = item_title
        self.item_description = item_description
        self.item_id = item_id
        self.item_price = item_price
        self.item_owner = item_owner

    def __repr__(self):
        return("{}: {}({})".format(self.item_title, self.item_description, self.item_owner))

### FUNCTIONS

def add_client(name, surname, mail, phone, location, wallet):
    name_surname = name + surname
    name_surname = Client(name, surname, mail, phone, location, wallet)
    clients_list.append(name_surname)
    print("\nAdd {} {} to Clients.".format(name_surname.name, name_surname.surname))

def delete_client(name, surname):
    for client in clients_list: 
        if client.name + client.surname == name + surname:
            clients_list.remove(client)
            print("\nRemove {} {} from Clients.".format(name, surname))

def show_clients():
    print("\n--- ALL CLIENTS ---\n")
    for client in clients_list:
        print(client)
    print("\n")

def add_item(item_title, item_description, item_price, owner_name, owner_surname):
    for client in clients_list:
        if (owner_name == client.name) and (owner_surname == client.surname):
            item_owner = client
    item_id = item_title[:3].upper() + owner_name[:3].upper()
    item_id = Item(item_title, item_description, item_id, item_price, item_owner)
    marketplace.add_listing(item_id)
    print("\nAdd {}(ID:{}) for {}€ to Marketplace.".format(item_title, item_id.item_id, item_price))

def buy_item(item_id, client_name, client_surname):
    
    item_listing = None
    for item in marketplace.listings:
        if item.item_id == item_id:
            item_listing = item
            price_moto = item.item_price
            title_moto = item.item_title
    if item_listing != None:
        client_id = client_name + client_surname
        for client in clients_list:
            if client_id == client.name + client.surname:
                if client.wallet >= item.item_price:
                    client.debit_wallet(item.item_price)  
                    item_price_old = item.item_price
                    old_client = item_listing.item_owner.name + item_listing.item_owner.surname
                    item_listing.item_owner = client
                    print("{} {} buy {} for {}€.".format(client.name, client.surname, title_moto, price_moto))
                    print("{} {}'s wallet has been debited of {}: TOTAL WALLET: {}".format(client.name, client.surname, item.item_price, client.wallet))
                    marketplace.remove_listing(item_id)
                    flag = True
                else:
                    print("Can't purchase, Not enough money.")
                    return
    if flag:
        for client in clients_list:
            if old_client == client.name + client.surname:
                client.credit_wallet(item_price_old)  
                print("{} {}'s wallet has been credited of {}: TOTAL WALLET: {}".format(client.name, client.surname, item_price_old, client.wallet))
                
### CALLS
marketplace = Marketplace()

add_client("Bastien", "Ratat", "bastien.ratat@gmail.com", "0602912777", "MARSEILLE", 20000)
add_client("Antoine", "Ratat", "antoine.ratat@gmail.com", "0601942777", "CHENGDU", 20000)
add_client("Catherine", "Ratat", "catherine.ratat@gmail.com", "0605942777", "MARSEILLE", 12000)
delete_client("Catherine", "Ratat")
show_clients()

add_item("Z650 Kawasaki", "Moto en parfait état.", 5000, "Antoine", "Ratat")
add_item("Ninja Kawasaki", "Moto un peu cassé.", 3000, "Bastien", "Ratat")
add_item("Z1000 Kawasaki", "Moto sympa.", 9000, "Antoine", "Ratat")

marketplace.remove_listing("Z10ANT")
marketplace.show_listings()
buy_item("Z65ANT", "Bastien", "Ratat")
marketplace.show_listings()

