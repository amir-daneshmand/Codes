"""
In this code snippet we generate all 2**n combinations of [0, 1, ... , n-1] integers
We also modify the code to generate k-combinations of the list
"""
def combinations(N, elements=[], i=0):
    if i == N:
        results.append(elements[:])
        return
    elements.append(i)
    combinations(N, elements, i+1)
    elements.pop()
    combinations(N, elements, i+1)

def k_combinations(N, k, elements=[], i=0):
    if len(elements) == k:
        results.append(elements[:])
        return
    elif i == N:
        return
    elements.append(i)
    k_combinations(N, k, elements, i+1)
    elements.pop()
    k_combinations(N, k, elements, i+1)

def permutations(N, elements, i = 0):
    if i == N-1:
        results.append(elements[:])
        return
    for j in range(i, len(elements)):
        elements[i], elements[j] = elements[j], elements[i]
        permutations(N, elements, i+1)
        elements[i], elements[j] = elements[j], elements[i]


#
# results = []
# combinations(3)
# print(results)
# print(len(results))


# results = []
# k_combinations(5,3)
# print(results)
# print(len(results))

results = []
N = 3
permutations(N, list(range(N)))
print(results)
print(len(results))

