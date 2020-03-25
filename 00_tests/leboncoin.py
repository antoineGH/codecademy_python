### CLASS DELCARATION

class Marketplace:
    def __init__(self):
        self.clients_dict = {}
        self.items_dict = {}

    def add_client(self, client_id, client_object):
        self.clients_dict[str(client_id)]= client_object

    def remove_client(self, client_id):
        self.clients_dict.pop(client_id, None)

    def show_clients(self):
        for value in self.clients_dict.values():
            print(value)

    def show_clients_id(self):
        for key in self.clients_dict.keys():
            print(key)

    def add_item(self, item_id, item_object):
        self.items_dict[str(item_id)]= item_object

    def remove_item(self, item_id):
        self.items_dict.pop(item_id, None)

    def show_items(self):
        for value in self.items_dict.values():
            print("{}: {} {}€.\nOwned by {} {}. Phone: {}, Mail: {}.\n".format(value.title, value.description, value.price, value.owner.name, value.owner.surname, value.owner.phone, value.owner.mail))

    def show_items_id(self):
        for key in self.items_dict.keys():
            print(key)

class Client:
 
    def __init__(self, name, surname, client_id, mail, phone, location, wallet):
        self.name = name
        self.surname = surname
        self.client_id = client_id
        self.mail = mail
        self.phone = phone
        self.location = location
        self.wallet = wallet

    def __repr__(self):
        return("{} {} (ID:{}), {}, {} @{} ({}€).".format(self.name, self.surname, self.client_id, self.mail, self.phone, self.location, self.wallet))

class Item:
    def __init__(self, title, description, price, owner, item_id):
        self.title = title
        self.description = description
        self.price = price
        self.owner = owner
        self.item_id = item_id

    def __repr__(self):
        return("{} ({}): {}, {}€ ({})".format(self.title, self.item_id, self.description, self.price, self.owner))

### FUNCTIONS

def add_client(name, surname, mail, phone, location, wallet):
    print("\n--- ADD CLIENT ---")
    client_id = name.lower() + surname.lower()
    client_object = name.lower() + surname.lower()
    client_object = Client(name, surname, client_id, mail, phone, location, wallet)
    marketplace.add_client(client_id, client_object)
    print("{} {} (ID:{}) Added.".format(name, surname, client_id))

def remove_client(name, surname):
    print("\n--- REMOVE CLIENT ---")
    client_id = name.lower() + surname.lower()
    marketplace.remove_client(client_id)
    print("{} {} (ID:{}) Removed.".format(name, surname, client_id))

def show_clients():
    print("\n--- SHOW CLIENTS ---")
    marketplace.show_clients()

def show_clients_id():
    print("\n--- SHOW CLIENTS ID ---")
    marketplace.show_clients_id()

def add_item(title, description, price, owner_name, owner_surname):
    for client in marketplace.clients_dict.values():
        if client.name + client.surname == owner_name + owner_surname:
            owner = client
    print("\n--- ADD ITEM ---")
    item_id = (title.lower()).replace(" ", "") + owner.name.lower() + owner.surname.lower()
    item_object = (title.lower()).replace(" ", "") + owner.name.lower() + owner.surname.lower()
    item_object = Item(title, description, price, owner, item_id)
    marketplace.add_item(item_id, item_object)
    print("{} (ID:{}) Added.".format(title, item_id))

def remove_item(title, name, surname):
    print("\n--- REMOVE ITEM ---")
    item_id = (title.lower()).replace(" ", "") + name.lower() + surname.lower()
    marketplace.remove_item(item_id)
    print("{} owned by {} {} Removed.".format(title, name, surname))

def show_items():
    print("\n--- SHOW ITEMS ---")
    marketplace.show_items()

def show_items_id():
    print("\n--- SHOW ITEMS ID ---")
    marketplace.show_items_id()

def buy_item(title, buyer_name, buyer_surname, owner_name, owner_surname):
    print("\n--- BUY ITEM ---")
    for item in marketplace.items_dict.values():
        item_id = item.item_id
        if (item.title == title) and (item.owner.name + item.owner.surname == buyer_name + buyer_surname):
            print("Hurray! You already own that item.")
            return
        for client in marketplace.clients_dict.values():
            if client.name + client.surname == buyer_name + buyer_surname:
                client.wallet -= item.price
                sold = True
                item.owner = client
                print("{} {} buy {} for {}€.".format(buyer_name, buyer_surname, item.title, item.price))
        if sold:
            for client in marketplace.clients_dict.values():
                if client.name + client.surname == owner_name + owner_surname:
                    client.wallet += item.price
    marketplace.remove_item(item_id)
   
### CALLS
marketplace = Marketplace()

add_client("Bastien", "Ratat", "bastien.ratat@gmail.com", "0602912777", "MARSEILLE", 20000)
add_client("Antoine", "Ratat", "antoine.ratat@gmail.com", "0601942777", "CHENGDU", 30000)
add_client("Catherine", "Ratat", "catherine.ratat@gmail.com", "0603942777", "MARSEILLE", 50000)
remove_client("Catherine", "Ratat")
show_clients()

add_item("Z650 Kawasaki", "Moto en parfait état.", 5000, "Antoine", "Ratat")
add_item("Ninja Kawasaki", "Moto un peu cassé.", 3000, "Bastien", "Ratat")
remove_item("Ninja Kawasaki", "Bastien", "Ratat")
show_items()
buy_item("Z650 Kawasaki", "Bastien", "Ratat", "Antoine", "Ratat")
show_items()
show_clients()

