#https://www.acmicpc.net/problem/2581
import sys


def is_primenumber(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
        else:
            pass
    return True

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

primeList = []
for i in range(M, N+1):
    if is_primenumber(i):
        primeList.append(i)
    else:
        pass

if primeList:
    print(sum(primeList))
    print(primeList[0])
else:
    print(-1)