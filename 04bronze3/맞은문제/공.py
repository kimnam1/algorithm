# https://www.acmicpc.net/problem/1547
import sys

def cupchange(cup1:int, cup2:int, ballcup:int):
    ans = ballcup
    if cup1 == cup2:
        pass
    elif cup2 == ballcup:
        ans = cup1
    elif cup1 == ballcup:
        ans = cup2
    else:
        pass
    return ans

n = int(input())

ballcup = 1

for i in range(n):
    a = list(map(int, sys.stdin.readline().split(' ')))
    ballcup = cupchange(a[0], a[1], ballcup)

print(ballcup)