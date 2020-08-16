#https://www.acmicpc.net/problem/15651

#1부터 N까지 자연수 중에서 M개를 고른 수열
#같은 수를 여러 번 골라도 된다
import sys

nlist = list(map(int, sys.stdin.readline().split()))
N = nlist[0]
M = nlist[1]

res = [1] * M

def recur(cur):
    if cur == M - 1:
        for i in range(N):
            print(" ".join(map(str, res)))
            res[cur] += 1
        res[cur] = 1
    else:
        for i in range(1, N+1):
            res[cur] = i
            recur(cur+1)

recur(0)