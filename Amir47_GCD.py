import math
import collections


def factorize(a):
    res = collections.defaultdict(int)
    primes = {2}
    t = 3
    while t <= a:
        flag = True
        for prime in primes:
            if t % prime == 0:
                flag = False
                break
        if flag:
            primes.add(t)
        t += 1

    for prime in primes:
        while a % prime == 0:
            res[prime] += 1
            a /= prime
    return res


def evaluate(a):
    res = 1
    for key in a:
        res *= key ** a[key]

    return res


def intersect(a, b):
    return {key: min(a[key], b[key]) for key in a if key in b}


def gcd(a, b):
    return evaluate(intersect(factorize(a), factorize(b)))


def gcd_Euclidean(a, b):
    while a:
        a, b = b%a, a
    return b


a, b = 14, 56

print("math.gcd: ", math.gcd(a, b))
print("our gcd:", gcd(a, b))
print("Eucidean gcd:", gcd_Euclidean(a, b))