class Client:
    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return("{}.".format(self.name))

def create_client(name):
    object_dict = {}
    for i in range(1, 6):
        client_id = name + str(i)
        client_key = name + str(i)
        print(client_key)
        client_id = Client(name)
        object_dict[str(client_key)]= client_id
    return object_dict

object_dict = create_client("antoine")

for key, value in object_dict.items():
    print(type(key))
    print(type(value))
    print(key, value)
    print(value.name)

def get_from_dict(client_key):
    for key, value in object_dict.items():
        if key == client_key:
            print(value)

get_from_dict("antoine5")


def add_client(name, surname, mail, phone, location, wallet, clients_dict):
    client_id = name.lower() + surname.lower()
    client_object = name.lower() + surname.lower()
    client_object = Client(name, surname, mail, phone, location, wallet)
    clients_dict[str(client_id)]= client_object
    return clients_dict