class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

        self.color = "unvisited"
        self.discover = 0
        self.finish = 0

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def dfs_recursive(self, vertex):
        global time
        vertex.color = "visited"
        vertex.discover = time
        time += 1
        for i in vertex.neighbors:
            if self.vertices[i].color == "unvisited":
                self.dfs_recursive(self.vertices[i])
        vertex.color = "finished"
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self.dfs_recursive(vertex)

    def display(self):
        for v in self.vertices:
            print(v, ":", self.vertices[v].neighbors, "-- discover/finish:", self.vertices[v].discover, "/", self.vertices[v].finish)


global time
graph = Graph()
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")

graph.add_vertex(a)
graph.add_vertex(b)
graph.add_vertex(c)
graph.add_vertex(d)

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "D")

graph.dfs(a)

graph.display()