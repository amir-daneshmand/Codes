class Node:
    def __init__(self, val):
        self.val = val
        # self.effort = math.inf
        self.neighbors = set()
        # self.visited = False

    def add_neighbor(self, coord):
        if coord not in self.neighbors:
            self.neighbors.add(coord)


class Graph:
    def __init__(self, A):
        self.vertices = {}
        self.A = A

    def add_node(self, node, coord):
        if coord not in self.vertices:
            self.vertices[coord] = node

    # def add_edge(self, node1, node2):
    #     node1.add_neighbor(node2)
    #     node2.add_neighbor(node1)

    def construct(self):
        A = self.A
        row_len = len(A)
        col_len = len(A[0])
        for i in range(row_len):
            for j in range(col_len):
                node = Node(A[i][j])
                self.add_node(node, (i, j))
                if i > 0:
                    node.add_neighbor((i - 1, j))
                if i < row_len - 1:
                    node.add_neighbor((i + 1, j))
                if j > 0:
                    node.add_neighbor((i, j - 1))
                if j < col_len - 1:
                    node.add_neighbor((i, j + 1))

    def disp(self):
        for i in self.vertices:
            print("vetices:", i, " - ", self.vertices[i].neighbors)

    def dijk(self, source, end):
        unvisited = {i: math.inf for i in self.vertices}
        efforts_nodes = {i: math.inf for i in self.vertices}

        efforts_nodes[source] = 0
        unvisited[source] = 0
        while unvisited:
            current = min(unvisited, key=lambda k: efforts_nodes[k])
            unvisited.pop(current)
            a = self.vertices[current]
            for b in self.vertices[current].neighbors:
                # effort = max(efforts_nodes[current], abs(a.val - self.vertices[b].val))
                effort = efforts_nodes[current] + abs(a.val - self.vertices[b].val)
                # the effort is the same distance and the differnce of two nodes values give the distance
                if effort < efforts_nodes[b]:
                    efforts_nodes[b] = effort
                    if b in unvisited:
                        unvisited[b] = effort

        print(efforts_nodes)
        return efforts_nodes[end]


class Solution:
    def minimumEffortPath(self, heights):
        G = Graph(heights)
        G.construct()
        G.disp()
        source = (0, 0)
        end = (len(heights) - 1, len(heights[0]) - 1)
        return G.dijk(source, end)

import math

S = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]

print(S.minimumEffortPath(heights))