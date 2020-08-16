#https://www.acmicpc.net/problem/15652

import sys

nlist = list(map(int, sys.stdin.readline().split()))
N = nlist[0]
M = nlist[1]

res = []

def recur(counter, curNumb, result):
    if counter == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(curNumb, N+1):
            result += [i]
            recur(counter+1, i, result)
            result.pop()

recur(0, 1, [])