import sys
from math import gcd

n, s = map(int, sys.stdin.readline().split())
dots = list(map(int, sys.stdin.readline().split()))

dist = [abs(i-s) for i in dots]

res = min(dist)
for i in dist:
    res = gcd(res, i)
print(res)