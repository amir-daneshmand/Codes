# # print((2 if 1 > 0 else 1)+(1 if 0 > 1 else 5))
#
#
# test = [[0]*2 for _ in range(4)]
# print(test)
# test[0][1] = 1
#
# print(test)

def knap_sack(w, v=0, i=0):
    if i == n and w >= 0:
        return v
    elif i == n:
        return 0

    res1 = knap_sack(w-wt_vec[i], v+val_vec[i], i+1)
    res2 = knap_sack(w, v, i+1)
    return max(res1, res2)

def knap_sack_memo(w, v=0, i=0):
    if i == n and w >= 0:
        return v
    elif i == n:
        return 0

    if (w-wt_vec[i], v+val_vec[i], i+1) in memo:
        res1 = memo[(w-wt_vec[i], v+val_vec[i], i+1)]
    else:
        res1 = knap_sack(w-wt_vec[i], v+val_vec[i], i+1)
        memo[(w-wt_vec[i], v+val_vec[i], i+1)] = res1

    if (w, v, i+1) in memo:
        res2 = memo[(w, v, i+1)]
    else:
        res2 = knap_sack(w, v, i+1)
        memo[(w, v, i+1)] = res2
    return max(res1, res2)


def knap_sack_dp():
    dp = [[0]*(K+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, K+1):
            if j >= wt_vec[i-1]:
                dp[i][j] = max(dp[i-1][j], val_vec[i-1]+dp[i-1][j-wt_vec[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

val_vec = [60, 100, 120]
wt_vec = [10, 20, 30]
K = 50


val_vec = [30, 32, 11, 40, 12, 70]
wt_vec = [20, 25, 10, 35, 45, 60]
K = 100


# val_vec = [5, 1, 2, 3]
# wt_vec = [4, 1, 2, 3]
# K = 6

n = len(val_vec)

print(knap_sack(K))
memo = {}
print(knap_sack_memo(K))
print(knap_sack_dp())


