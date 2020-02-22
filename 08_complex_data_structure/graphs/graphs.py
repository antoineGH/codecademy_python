class Graph:
    def __init__(self, directed = False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        print("Adding {} to graph".format(vertex.value))
        self.graph_dict[vertex.value] = vertex

    def add_edges(self, from_vertex, to_vertex, weight = 0):
        print("Adding edge from {} to {}".format(from_vertex.value, to_vertex.value))
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        print("Searching from {} to {}".format(start_vertex, end_vertex))
        start = [start_vertex]
        seen = {}
        while start:
            current_vertex = start.pop(0)
            seen[current_vertex] = True
            print("Current vertex : {}".format(current_vertex))
            if current_vertex == end_vertex:
                return True
                break
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]
                start += next_vertices
        return False
