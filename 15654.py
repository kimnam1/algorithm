import itertools
import sys

nm = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))

M = nm[1]

res = list(itertools.permutations(numbers, M))
res.sort()

for i in res:
    print(' '.join(map(str, i)))