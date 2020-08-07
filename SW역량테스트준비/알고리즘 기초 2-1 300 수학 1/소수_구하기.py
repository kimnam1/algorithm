#https://www.acmicpc.net/problem/1929
import sys


def eratosthenes(x, y):
    trueFalse = [False, False] + [True] * (y - 1)
    primes = []

    for i, t in enumerate(trueFalse):
        if t:
            primes.append(i)
            for j in range(2, y // i + 1):
                trueFalse[j * i] = False
        else:
            pass
    for i, c in enumerate(primes):
        if c < x:
            pass
        else:
            start = i
            break

    return primes[start:]

T = list(map(int, sys.stdin.readline().split()))
result = eratosthenes(T[0], T[1])

for c in result:
    print(c)