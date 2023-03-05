def k_combinations(n, k, start = 0, comb = []):
    if len(comb) == k:
        res.append(comb)
        return

    for j in range(start, n):
        k_combinations(n, k, j+1, comb+[j])
#         Modify [j] to [nums[j]] to get a k-combinations of array nums

def combinations(n, start = 0, comb = []):
    if start > n:
        return
    res.append(comb)
    for j in range(start, n):
        combinations(n, j+1, comb+[j])
#         Modify [j] to [nums[j]] to get a k-combinations of array nums

res = []
n, k = 4, 2
#  Generates a k combinatiosn of array [0, 1, ... n-1]
# k_combinations(n, k)
combinations(n)
print(len(res), res)










