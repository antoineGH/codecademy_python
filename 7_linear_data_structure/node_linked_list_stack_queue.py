############################################### CLASS DECLARATION ########################################

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Class Node 
# .__init__(self, value, next_node)
# .get_value(self)
# .get_next_node(self)
# .set_next_node(self, next_node)


class LinkedList:

    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node

    def stringify_list(self):
        string = ""
        current_node = self.get_head_node()
        while current_node:
            string += str(current_node.get_value()) + ("\n")
            current_node = current_node.get_next_node()
        return string

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
                else:
                    current_node = next_node
                
# Class LinkedList
# .__init__(self, value)
# .get_head_node(self)
# .insert_beginning(self, value)
# .remove_node(self)


class Stack:

    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            new_item = Node(value)
            new_item.set_next_node(self.top_item)
            self.top_item = new_item
            self.size += 1
            print("Push {} to the stack.".format(new_item.get_value()))
        else:
            return "Can't push here, Stack is already full"

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1 
            print("Pop {} from stack.".format(item_to_remove.get_value()))
            return item_to_remove.get_value()
        else:
            return "Can't pop here, Stack is already empty"

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            return "Nothing to peek at, Stack is empty"

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

# Class Stack
# .__init__(self, limit=1000)
# .push(self, value)
# .pop(self)
# .peek(self)
# .has_space(self)
# .is_empty(self)


class Queue:
    
    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Enqueue {item} to the queue".format(item = item_to_add.get_value()))
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Queue is already full - Can't enqueue")

    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print("Dequeue {item} from the queue".format(item = item_to_remove.get_value()))
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        else:
            return "Nothing to peek at, Queue is empty"

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0

# Class Queue
# .__init__(self, max_size = None)
# .enqueue(self, value)
# .dequeue(self)
# .peek(self)
# .get_size(self)
# .has_space(self)
# .is_empty(self)


############################################### CLASS INSTANTIATION ######################################

### NODES ### 
node1 = Node("value1")
node2 = Node("value2")
node3 = Node("value3")

node1.set_next_node(node2)
node2.set_next_node(node3)

node1_value = node1.get_value()
node2_value = node1.get_next_node().get_value()
node3_value = node1.get_next_node().get_next_node().get_value()

print(node1_value, node2_value, node3_value)

### LINKED LISTS ###
ll_weekdays = LinkedList("sunday") # instantiate linkedlist with a sunday node
ll_weekdays.insert_beginning("saturday") # insert nodes with value "saturday" at the beginning of the linkedlist
ll_weekdays.insert_beginning("friday")
ll_weekdays.insert_beginning("thursday")
ll_weekdays.insert_beginning("wednesday")
ll_weekdays.insert_beginning("tuesday")
ll_weekdays.insert_beginning("monday")
string_ll_weekdays = ll_weekdays.stringify_list() # stringify linkedlist for display
print(string_ll_weekdays)
ll_weekdays.remove_node("wednesday") # remove node with value "wednesday"
string_ll_weekdays = ll_weekdays.stringify_list()
print(string_ll_weekdays)

### STACK ###
stack_pizza = Stack(5) # Instantiate Stack with a limit of 5 nodes
stack_pizza.peek() # peek an empty stack
stack_pizza.pop() # Try to pop an empty stack
stack_pizza.push("Pizza 1") # push nodes into the stack 
stack_pizza.push("Pizza 2")
stack_pizza.push("Pizza 3")
stack_pizza.push("Pizza 4")
stack_pizza.push("Pizza 5")
stack_pizza.push("Pizza 6") # stack full - can't push
stack_pizza.peek() # peek the top item of stack
stack_pizza.pop() # pop the stack
stack_pizza.pop()
stack_pizza.pop()
stack_pizza.pop()
stack_pizza.pop()
stack_pizza.pop() # stack empty - can't pop

### QUEUES ###

queue_line = Queue(5)
queue_line.peek()
queue_line.enqueue("Client 1")
queue_line.enqueue("Client 2")
queue_line.enqueue("Client 3")
queue_line.enqueue("Client 4")
queue_line.enqueue("Client 5")
queue_line.enqueue("Client 6")
queue_line.peek()
queue_line.dequeue()
queue_line.dequeue()
queue_line.dequeue()
queue_line.dequeue()
queue_line.dequeue()
queue_line.dequeue()
queue_line.dequeue()
queue_line.peek()