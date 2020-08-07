#https://www.acmicpc.net/problem/6588
import sys

a = [False, False] + [True] * (1000000)
primes = []
for i in range(2, 1000000):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 1000000, i):
            a[j] = False

def goldbachs_conjecture(x):
    for i in primes:
        if a[x - i]:
            return f"{x} = {i} + {x - i}"
        elif i >= x//2:
            return "Goldbach's conjecture is wrong."
        else:
            pass

case = int(sys.stdin.readline())
while case != 0:
    print(goldbachs_conjecture(case))
    case = int(sys.stdin.readline())