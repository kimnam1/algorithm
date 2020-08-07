#https://www.acmicpc.net/problem/10819
import itertools
import sys

T = int(sys.stdin.readline())
numblist = list(map(int, sys.stdin.readline().split()))

permu = list(itertools.permutations(numblist, T))

maxi = 0

for item in permu:
    sum = 0
    for index in range(len(item)-1):
        sum += abs(item[index] - item[index + 1])
    maxi = max(maxi, sum)

print(maxi)
