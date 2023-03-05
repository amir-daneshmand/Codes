class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


uf = UF(6)
uf.union(1, 2)
uf.union(1, 3)
uf.union(1, 0)
uf.union(4, 5)

print("parents = ", uf.parent)
print("parent of 0 = ", uf.find(0))
print("parent of 1 = ", uf.find(1))
print("parent of 2 = ", uf.find(2))
print("parent of 3 = ", uf.find(3))
print("parent of 4 = ", uf.find(4))
print("parent of 5 = ", uf.find(5))

print(uf.parent)
import collections
dic = collections.defaultdict(list)
s = "vdkges"

for i in range(len(s)):
    dic[uf.find(i)].append(s[i])

print(list(dic.keys()))
print(list(dic.values()))