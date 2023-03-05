# In this code we are going to implement cycle detection using
# union-find algorithm with rank and path compression.

class Graph:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1

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
            return True, graph
        graph.union(x, y)
    return False, graph

# G = Graph(3)
# G.union(1,2)
# G.union(2,3)
# G.union(3,1)

n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 0]]

res, G = is_cyclic(edges, n)
print('Graph is cyclic' if res else 'Graph is not cyclic.')
print(G.parent, G.rank)

'''
Computational Complexity of UF with path compression and rank is O(alpha(n)) wwhere alpha(n) is inverse Ackerman 
Function and is almost constant.

'''