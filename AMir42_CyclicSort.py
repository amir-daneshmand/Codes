def cyclic_sort(nums):
    i = 0

    while i<len(nums):
        if nums[i] != i:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            i += 1

    return nums


nums = [4,2,1,5,0,3]
print(cyclic_sort(nums))