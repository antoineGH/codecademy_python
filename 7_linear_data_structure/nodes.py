# Creating Node class
# Add an __init__ method with "value" and "link_node" (optional)
# Nodes Getters methods to access the data and link within the node
# Nodes Setter method to update the link of the node

class Node:
    def __init__(self, value, link_node = None):
        self.value = value
        self.link_node = link_node
        
    def get_value(self):
        return self.value
        
    def get_link_node(self):
        return self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node

# Instantiate 3 nodes
yacko = Node("likes to yak",)
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# Set link from Yacko to Dot
yacko.set_link_node(dot)
# Set link from Dot to Wacko
dot.set_link_node(wacko)

# get Dot value from Yacko
dots_data = yacko.get_link_node().get_value()

# get Wacko value from Dot
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)

# get Yacko value
print(yacko.get_value())

# get from Yacko to Wacko value
print(yacko.get_link_node().get_link_node().get_value())