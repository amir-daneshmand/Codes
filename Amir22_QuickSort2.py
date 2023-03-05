def quick_sort(nums):
    left, p, right = partition(nums)
    sorted_array = []
    if len(left) <= 1 and len(right) <= 1:
        sorted_array.extend(left)
        sorted_array.extend(p)
        sorted_array.extend(right)
    else:
        left = quick_sort(left)
        right = quick_sort(right)
        sorted_array.extend(left)
        sorted_array.extend(p)
        sorted_array.extend(right)
    return sorted_array


def partition(nums):
    if not nums:
        return [], [], []

    left, p, right = [], nums[0], []
    for num in nums:
        if num < p:
            left.append(num)
        elif num > p:
            right.append(num)

    return left, [p], right

arr = [4,2,6,7,9,1,6,8,0,1]

print(quick_sort(arr))