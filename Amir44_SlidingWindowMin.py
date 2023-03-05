def running_min(nums, k):
    res = []

    for i in range(k, len(nums)+1):
        res.append(min(nums[i-k:i]))
    return res


def running_min2(nums, k):
    stack = []
    res = []
    for i in range(len(nums)):
        while stack and stack[0] <= i-k:
            stack.pop(0)
        while stack and nums[i] < nums[stack[-1]]:
            stack.pop()
        stack.append(i)
        # print('stack:', stack)
        if i >= k-1:
            res.append(nums[stack[0]])
    return res


#
# 1) for interval i-j, remove any index in stack smaller than i
# 2) remove any mamber in stack which has values larger than arr[i]
# 2) add arr[i]
#     :

arr = [1, 2, 3, 1, 2, 1, -1, -10, 1, 5]
k = 3
print('arr:', arr)
print(running_min(arr, k))
print(running_min2(arr, k))