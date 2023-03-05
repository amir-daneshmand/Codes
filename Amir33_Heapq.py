import heapq

nums = [5, 3, 10, 55, 24, 2]

print(nums)
heapq.heapify(nums)
print(nums)

heapq.heappush(nums, 4)
print(nums)

t = heapq.heappop(nums)
print(nums)
print(t)

print(heapq.nsmallest(2, nums))


##############################

import heapq
nums = [7,1,2,5,4]

print(nums)
heapq.heapify(nums)
print(nums)

print(heapq.heappop(nums))
print(nums)

heapq.heappush(nums, 1)
print(nums)

while nums:
    print(heapq.heappop(nums))

