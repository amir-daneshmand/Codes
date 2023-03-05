'''
Problem statement can be found at

https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

'''


def compute_cost(S, X, Y):
    cost_C = 0 if S[0] == 'C' or S[0] == '?' else math.inf
    cost_J = 0 if S[0] == 'J' or S[0] == '?' else math.inf

    for i in range(1, len(S)):
        cost_C_new = min(cost_C, cost_J + Y) if S[i] == 'C' or S[i] == '?' else math.inf
        cost_J_new = min(cost_J, cost_C + X) if S[i] == 'J' or S[i] == '?' else math.inf

        cost_C = cost_C_new
        cost_J = cost_J_new

    return min(cost_C, cost_J)


import math

T = int(input())

for t in range(T):
    X, Y, S = [x for x in input().split(' ')]
    X, Y, S = int(X), int(Y), list(S)
    print('Case #{}: {}'.format(t + 1, compute_cost(S, X, Y)))