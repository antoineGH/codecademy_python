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

class Stack:

    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            return "Impossible to push, the stack is full"

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            return "Nothing to pop, the stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            return "Nothing to peek at, the stack is empty."

    def has_space(self):
        if self.limit > self.size:
            return True
        else:
            return False

    def is_empty(self):
        return self.size == 0

pizza_stack = Stack(5)
pizza_stack.is_empty()
pizza_stack.has_space()
pizza_stack.peek()
pizza_stack.pop()
pizza_stack.push("Pizza 1")
pizza_stack.push("Pizza 2")
pizza_stack.push("Pizza 3")
pizza_stack.push("Pizza 4")
pizza_stack.push("Pizza 5")
pizza_stack.push("Pizza 6")

print("The first pizza to deliver is " + pizza_stack.peek())

pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()