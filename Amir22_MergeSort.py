def merge(nums1, nums2):
    if not nums1:
        return nums2
    elif not nums2:
        return nums1

    res = []
    p1, p2 = 0, 0

    while p1<len(nums1) and p2<len(nums2):
        if nums1[p1] <= nums2[p2]:
            res.append(nums1[p1])
            p1 += 1
        else:
            res.append(nums2[p2])
            p2 += 1

    if p1 < len(nums1):
        res.extend(nums1[p1:])
    elif p2 < len(nums2):
        res.extend(nums2[p2:])
    return res


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


arr = [4,3,8,2,1,1,90,12,5]
print(merge_sort(arr))



