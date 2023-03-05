def bubble_sort_naive(nums):
    not_sorted = True
    while not_sorted:
        not_sorted = one_pass(nums)
    return nums


def one_pass(nums):
    not_sorted = False
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            not_sorted = True
    return not_sorted


arr = [1, 7, 3, 5, 9, 2, 0]
print(arr)
print(bubble_sort_naive(arr))