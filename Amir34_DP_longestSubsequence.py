def longest_length(nums):
    N = len(nums)
    lengths = [1]*N
    counts = [1]*N
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengths[j] >= lengths[i]:
                    lengths[i] = lengths[j]+1
                    counts[i] = counts[j]
                elif lengths[j] < lengths[i]:
                    counts[i] += counts[j]
    print(lengths)
    print(counts)
    return max(lengths)




nums = [1, 2, 3, 5, 4, 7]
nums2 = [1, 3, 2, 4, 6, 5, 7]
res = longest_length(nums2)
print(res)

print("----------")

for i in range(5):
    if i and nums[i-1]:
        print(nums[i-1])