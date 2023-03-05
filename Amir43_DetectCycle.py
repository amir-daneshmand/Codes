# In this code we are going to implement cycle detection using
# union find.

class Graph:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


def is_cyclic(edges, n):
    graph = Graph(n)
    for e1, e2 in edges:
        x = graph.find(e1)
        y = graph.find(e2)
        if x == y:
            return True
        graph.union(x, y)
    return False

# G = Graph(3)
# G.union(1,2)
# G.union(2,3)
# G.union(3,1)

n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0]]

res = is_cyclic(edges, n)
print('Graph is cyclic' if res else 'Graph is not cyclic.')
