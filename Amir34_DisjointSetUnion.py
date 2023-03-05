import collections


class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        class UF:
            def __init__(self, n):
                self.p = list(range(n))

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf, res, m = UF(len(s)), [], collections.defaultdict(list)
        for x, y in pairs:
            uf.union(x, y)
        print(uf.p)

        for i in range(len(s)):
            m[uf.find(i)].append(s[i])

        print(m)
        for comp_id in m.keys():
            m[comp_id].sort(reverse=True)
        print(m)
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())
        return ''.join(res)


string = "febcda"
pairs = [[0, 1], [0, 2], [1, 3], [4, 5]]
s = Solution()
a = s.smallestStringWithSwaps(string, pairs)
print(a)

