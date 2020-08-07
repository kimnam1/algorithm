# https://www.acmicpc.net/problem/1598
import sys

def location(a:int):
    if a % 4 == 0:
        return (a//4, 4)
    else:
        return ((a//4)+1, (a % 4))

def monkeynumber(a: int, b: int):
    x = location(a)[0] - location(b)[0]
    y = location(a)[1] - location(b)[1]
    return abs(x) + abs(y)

a = list(map(int, sys.stdin.readline().split(' ')))

print(monkeynumber(a[0], a[1]))