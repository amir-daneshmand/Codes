a, b = 1, 1

res = [1, 1]
while b <= 40:
    a, b = b, a+b
    res.append(b)

print(res)

print(any([1, 1, 1, 1, 0]))
print(all([1, 1, 1, 1, 0]))


a = [0, 1, 2, 3, 4, 5]
b = [2, 3, 4]

a_set = set(a)
b_set = set(b)
print('b is a subset of a: ', b_set.issubset(a_set))
print('a is a subset of b: ', a_set.issubset(b_set))


print(a[2:5])
print(b)
print(a[2:5] == b)
import collections
print(collections.Counter(a[2:5]))
print(collections.Counter(b))
print(collections.Counter(a[2:5]) == collections.Counter(b))

a = [2, 4, 7,2, 1]
# import heapq
# heapq.heapify(a)
print(a[-len(a)])

