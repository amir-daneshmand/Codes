class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Dict:
    def __init__(self, n=10):
        self.vals = [[]]*n
        self.n = n

    def get(self, key):
        for _key, value in self.vals[self.index(key)]:
            if key == _key:
                return value

    def index(self, key):
        return sum(ord(a) for a in key)%self.n

    def add(self, key, value):
        self.vals[self.index(key)].append((key, value))

_dict = Dict()

_dict.add('amir', 33)
_dict.add('ali', 332)
_dict.add('mehrdad', 1133)


print(_dict.get('ali'))
print(_dict.vals)

print(str('2322').split('3'))