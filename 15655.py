import itertools
import sys

nm = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

M = nm[1]

res = list(itertools.combinations(numbers, M))

for i in res:
    print(' '.join(map(str, i)))