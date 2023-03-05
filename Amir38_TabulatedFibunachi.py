def fib_tabulated(n):
    elements = [0]*(n+1)
    elements[1] = 1
    for i in range(2, n+1):
        elements[i] = elements[i-1]+elements[i-2]
    return elements[n]

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)


print(fib(16))
print(fib_tabulated(16))