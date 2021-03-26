# 1. A Tale of Two Graph Searches ---

# Broad Graph Search
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])

# Depth Graph Search 
# Pass Graph to Search, Current_Vertex to Start the search with, Target Value to find in the Graph
def dfs(graph, current_vertex, target_value, visited = None):

  # If visited is None, create an empty visited list to hold all the visited vertices.
  if visited is None:
    visited = []
  # Append current vertex in the visited list as it has been visited already
  visited.append(current_vertex)

  # Check If current vertex is the value we search in the graph
  if current_vertex is target_value:
    return visited
  
  # Retrieve value neighbor (connected vertex as value in the dictionnary for key 'current_vertex')
  for neighbor in graph[current_vertex]:
    # For each connected vertex, if not visited already
    if neighbor not in visited:
      # recurse call dfs with graph, neighbor (connected next value), searched value, and the list of already visited vertices
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path

# Graph Declaration
some_important_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

# Graph Search Functions Calls
print(bfs(some_important_graph, 'lava', 'lasers'))
print(dfs(some_important_graph, 'lava', 'lasers'))



#2. A Graph Search with Real Depth

def dfs(graph, current_vertex , target_value , visited = None):
  if not visited:
    visited = []
    visited.append(current_vertex)
    return visited
    
print(dfs(None, "bees?", None))

#3. Case of Base

def dfs(graph, current_vertex, target_value, visited=None):
  if visited == None:
    visited = []
  visited.append(current_vertex)
  # build out your base case:
  if current_vertex == target_value:
    return visited

#4. Search It Again, Sam

def dfs(graph, current_vertex, target_value, visited=None):
  if visited is None:
    visited = []
    
  visited.append(current_vertex)
  
  if current_vertex == target_value:
    return visited

  # Add your recursive case here:
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

# Call dfs() below and print the result:
print(dfs(the_most_dangerous_graph, "crocodiles" , "bees"))
#>>> ['crocodiles', 'lasers', 'sharks', 'bees']

#5. Breadth-First Search: Take My Breadth Away

# Define your breadth-first search function:
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()

#print(bfs(None, "laval!", None))

#6. Breadth-First Search 2: The Breadthening

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  # Continue the function here:
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      continue

#7. A Breadth of Fresh Neighbors

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    
    for neighbor in graph[current_vertex]:
      # Finish the function here:
      if neighbor not in visited:
        if neighbor == target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])
      
        
      

# Call bfs() below and print the result:
print(bfs(the_most_dangerous_graph, "crocodiles", "bees"))

#8. Graph Search Python: Review

def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  if current_vertex is target_value:
    return visited
  
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path
      
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])

some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
  }

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print(dfs(some_hazardous_graph, 'sharks', 'bees'))