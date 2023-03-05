class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.color = "unvisited"
        self.distance = 9999
        self.predecessor = None

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if vertex.name not in self.vertices:
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

    def display(self):
        for i in self.vertices:
            print(i, ":", self.vertices[i].neighbors, "- Distance:", self.vertices[i].distance)

    # def _bfs(self, vertex, queue):
    #     vertex.color = "visited"
    #     for _ in vertex.neighbors:
    #         i = self.vertices[_]
    #         if i.color == "unvisited":
    #             i.distance = vertex.distance + 1
    #             queue.append(_)
    #
    #     if queue:
    #         v = queue.pop(0)
    #         node_v = self.vertices[v]
    #         if node_v.distance > vertex.distance + 1:
    #             self.vertices[n].distance = vertex.distance + 1
    #         self._bfs(node_v, queue)
    #         self.vertices[v].color = "finished"
    #
    # def bfs(self, vertex):
    #     queue = []
    #     vertex.distance = 0
    #     self._bfs(vertex, queue)

    def bfs_2(self, vertex):
        vertex.color = "visited"
        vertex.distance = 0
        queue = []
        for n in vertex.neighbors:
            if self.vertices[n].color == "unvisited":
                self.vertices[n].distance = vertex.distance + 1
                queue.append(n)
        while queue:
            u = queue.pop(0)
            node_u = self.vertices[u]
            node_u.color = "visited"

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == "unvisited":
                    queue.append(v)
                    if node_v.distance > node_u.distance+1:
                        node_v.distance = node_u.distance + 1


G = Graph()

a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
g = Vertex("G")
h = Vertex("H")


G.add_vertex(a)
G.add_vertex(b)
G.add_vertex(c)
G.add_vertex(d)
G.add_vertex(e)
G.add_vertex(f)
G.add_vertex(g)
G.add_vertex(h)

# for i in range(ord("A"), ord("I")):
#     G.add_vertex(Vertex(chr(i)))


G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("A", "D")
G.add_edge("D", "B")
G.add_edge("D", "E")
G.add_edge("E", "F")
G.add_edge("E", "G")
G.add_edge("A", "H")

G.bfs_2(a)
G.display()
