# import math
#     if val>nums[i]:
#
#
#
# nums = [1, 2, 0, 3, 4, 5]
#            1  -2 3  1  1
# nums = [2 , -1, 0, 2, 3, 5]
#         0   8  -7 1 1 2
#         0   1

import math
def longest_increasing_subarray(nums):
    dp = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(i-1, -1, -1):
            if nums[j] <= nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)



nums = [12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
# nums = [5,4,3,2,1]
# sol = 12

# nums = [1,2,0,1]
# nums = [0, 1, 0, 2, 0, 3, 0]

# print(fn(nums))

print('Min changes to make the sequence strictly increasing = ', len(nums)-longest_increasing_subarray(nums))
