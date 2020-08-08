#https://www.acmicpc.net/problem/15649
#n과m1

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
import itertools
import sys

l = list(map(int, sys.stdin.readline().split()))
N = l[0]
M = l[1]

res = itertools.permutations([i for i in range(1, N+1)], M)

for i in res:
    print(" ".join(map(str, i)))