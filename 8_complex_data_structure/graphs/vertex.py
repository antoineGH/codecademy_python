class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def get_edges(self):
        return list(self.edges)

    def add_edge(self, vertex, weight = 0):
        print("Adding edge to {}".format(vertex))
        self.edges[vertex] = weight