import itertools
import sys

nm = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
N = nm[0]
M = nm[1]

res = list(dict.fromkeys(itertools.permutations(numbers, M)))

for i in res:
    print(" ".join(map(str, i)))