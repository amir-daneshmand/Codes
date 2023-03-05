# Enter your code here. Read input from STDIN. Print output to STDOUT

def quick_sort(arr):
    sorted_seq = []
    left, p, right = partition(arr)
    if len(left) <= 1 and len(right) <= 1:
        sorted_seq.extend(left)
        sorted_seq.extend(p)
        sorted_seq.extend(right)
        return sorted_seq
    else:
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        sorted_seq.extend(sorted_left)
        sorted_seq.extend(p)
        sorted_seq.extend(sorted_right)
        return sorted_seq


def partition(arr):
    if len(arr) > 0:
        p = arr[0]
        left = []
        right = []
        for i in arr:
            if i < p:
                left.append(i)
            elif i > p:
                right.append(i)
        return left, [p], right
    else:
        left = []
        right = []
        p = []
        return left, p, right


arr = [i for i in map(int, input().strip().split())]
sorted_arr = quick_sort(arr)
# print(sorted_arr)
print(' '.join(map(str, sorted_arr)))
