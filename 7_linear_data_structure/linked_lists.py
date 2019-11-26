# Linked Lists:

# Adding a new node
# Adding a new node to the beginning of the list requires you to link your new node to the current head node. 

# Removing a node
# Adjust the link on the previous node so that it points to the following node.

# Are comprised of nodes
# The nodes contain a link to the next node (and also the previous node for bidirectional linked lists)
# Can be unidirectional or bidirectional
# Are a basic data structure, and form the basis for many other data structures
# Have a single head node, which serves as the first node in the list
# Require some maintenance in order to add or remove nodes

# Each linked list is a sequential chain of nodes
# So before we start building out the LinkedList itself, 
# We want to build up a Node class in Python that we can use to build our data containers.

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    self.next = None
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
    def __init__(self, value = None):
        new_node = Node(value)
        self.head_node = new_node

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else :
                    current_node = next_node

weekdays = LinkedList("Sunday")
weekdays.insert_beginning("Saturday")
weekdays.insert_beginning("Friday")
weekdays.insert_beginning("Thursday")
weekdays.insert_beginning("Wednesday")
weekdays.insert_beginning("Tuesday")
weekdays.insert_beginning("Monday")

list_weekdays = weekdays.stringify_list()
print(list_weekdays)

weekdays.remove_node("Wednesday")
list_weekdays = weekdays.stringify_list()
print(list_weekdays)
