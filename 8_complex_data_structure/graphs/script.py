# Import
from vertex import Vertex
from graphs import Graph

# Instantiate graphs (default not directed)
graph1 = Graph()
directed_graph1 = Graph(True)

# Instantiate vertices
vertex1 = Vertex("Value vertex 1")
vertex2 = Vertex("Value vertex 2")
vertex3 = Vertex("Value vertex 3")
vertex4 = Vertex("Value vertex 4")
vertex5 = Vertex("Value vertex 5")
vertex6 = Vertex("Value vertex 6")

# Adding vertex to graph1
graph1.add_vertex(vertex1)
graph1.add_vertex(vertex2)
graph1.add_vertex(vertex5)
graph1.add_vertex(vertex6)

# Adding vertex to directed_graph1
directed_graph1.add_vertex(vertex3)
directed_graph1.add_vertex(vertex4)

# Adding edges in graphs
graph1.add_edges(vertex1, vertex2, 5)
graph1.add_edges(vertex1, vertex5, 10)
graph1.add_edges(vertex1, vertex6, 15)
directed_graph1.add_edges(vertex3, vertex4)

print("\nVertices in non-directed Graph")
print("Edges for {}: {}".format(vertex1.value, vertex1.get_edges()))
print("Edges for {}: {}".format(vertex2.value, vertex2.get_edges()))

print("\nVertices in directed Graph")
print("Edges for {}: {}".format(vertex3.value, vertex3.get_edges()))
print("Edges for {}: {}".format(vertex4.value, vertex4.get_edges()))

print("\nPrint Weight edges for vertex 1")
print(vertex1.edges)
print("\nPrint Weight edges for vertex 2")
print(vertex2.edges)

# Finding Path
print("\nFinding Path from {} to {}".format(vertex1,vertex6))
print(graph1.find_path("Value vertex 1", "Value vertex 6"))

print("\nFinding Path from {} to {}".format(vertex1, vertex3))
print(graph1.find_path("Value vertex 1", "Value vertex 3"))


