import math
def merge_sort(nums):
    if len(nums)<2:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    elif not right:
        return left

    res = []
    n_l, n_r = len(left), len(right)

    p_l, p_r = 0, 0
    left.append(math.inf)
    right.append(math.inf)

    while p_l<n_l or p_r<n_r:
        while p_l<n_l and left[p_l]<=right[p_r]:
            res.append(left[p_l])
            p_l += 1

        while p_r < n_r and left[p_l] > right[p_r]:
            res.append(right[p_r])
            p_r += 1

    return res

a = [1,2, 7, 9]
b = [0, 2.5, 10]

print(merge_sort([100, -1, 9, 1, -100, 2, 8, 4, 7, 1, 9, 0]))

