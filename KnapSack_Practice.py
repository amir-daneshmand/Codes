def Knapsack(W, V, k, val = 0, i = 0, comb = []):
    if i == len(W)-1:
        return val if k>=0 else 0

    return max(Knapsack(W,V,k-W[i], val+V[i], i+1, comb+[i]), Knapsack(W,V,k, val, i+1, comb))

def Knapsack_DP(W,V,k):
    dp = [[0]*(k+1) for _ in range(len(W)+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if j>=W[i-1]:
                dp[i][j] = max(dp[i-1][j], V[i-1]+dp[i-1][j-W[i-1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]




W = [20, 25, 10, 35, 45, 60]
V = [30, 32, 11, 40, 12, 70]
k = 100

print(Knapsack(W,V,k))

print(Knapsack_DP(W,V,k))