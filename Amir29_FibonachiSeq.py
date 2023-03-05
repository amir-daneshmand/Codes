f0 = 0
f1 = 1

N = 40


def fibonachi(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N > 1:
        return fibonachi(N-1)+fibonachi(N-2)



print(fibonachi(N))
