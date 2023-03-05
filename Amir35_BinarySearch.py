def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        middle = left + (right - left) // 2
        if nums[middle] >= target:
            right = middle
        else:
            left = middle + 1

    return left if nums[left] == target else -1






class Solution:
    def search(self, nums: List[int], target: int, index=0) -> int:
        N = len(nums)
        if N == 0:
            return -1
        if N == 1:
            if nums[0] == target:
                return index
            else:
                return -1
        left = nums[0:N//2]
        right = nums[N//2:N]
        middle = nums[N//2]
        if target >= middle:
            return self.search(right, target, N//2 + index)
        else:
            return self.search(left, target, index)