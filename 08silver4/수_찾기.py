#https://www.acmicpc.net/problem/1920
import sys


def finding_number(l:list, x:int):
    res = 0
    for i in range(len(l)):
        if l[i] == x:
            res = 1
            break
        else:
            pass
    return res


N = int(sys.stdin.readline())
pool = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbs = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    print(finding_number(pool, numbs[i]))

#시간초과
