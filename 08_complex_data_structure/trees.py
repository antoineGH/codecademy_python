# Child nodes are held as references by another instance of TreeNode, known as the parent node.

# Defining TreeNode class 

class TreeNode:

# __init__
# self.value : Node Value
# self.children : Empty list keep track of child nodes
  
  def __init__(self, value):
    print("initializing node...")
    self.value = value
    self.children = []

# add_child
# Append a child node in self.children list from parent node
    
  def add_child(self, child_node):
      print("Adding child node \"{child_node}\" to the parent node \"{parent_node}\"".format(child_node = child_node.value, parent_node = self.value))
      self.children.append(child_node)

# remove_child
# Create an empty list and append every element from self.children which are NOT the element to remove
# Replace self.children with the newly created list.

  def remove_child(self, child_node):
      print("Remove child node \"{child_node}\" from the parent node \"{parent_node}\"".format(child_node = child_node.value, parent_node = self.value))
      new_children = []
      for item in self.children:
          if child_node != item:
              new_children.append(item)
      self.children = new_children

# remove_child_list_comprehension
# Using list comprehension to append each element except child_node in self.children

  def remove_child_lc(self, child_node):
      print("Remove child node \"{child_node}\" from the parent node \"{parent_node}\"".format(child_node = child_node.value, parent_node = self.value))
      self.children = [child != child_node for child in self.children]

# traverse
# print root node self.value and for each node in self.children print value
# while nodes_to_visit are all pop, print current_node value, increment nodes_to_visit with the current_node's children

  def traverse(self):
    print("Traversing Tree")
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

### CALLS -----------------------------------------------------------------------------------------------

root = TreeNode("Root Node")
child = TreeNode("Child Node 1")
child2 = TreeNode("Child Node 2")
child3 = TreeNode("Child Node 3")

root.add_child(child)
root.add_child(child2)
root.add_child(child3)
root.remove_child(child2)
root.traverse()