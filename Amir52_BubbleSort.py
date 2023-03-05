def bubble_sort(nums):
    for i in range(len(nums)):
        sorted = True
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                sorted = False
        if sorted:
            break

    return nums

nums_ = [5,3,1,9,10, -1]



print(bubble_sort(nums_))
