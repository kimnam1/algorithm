#https://www.acmicpc.net/problem/1934
import sys


def LCM(x, y):
    bigNumb = max(x, y)
    smallNumb = min(x, y)
    res = bigNumb
    while True:
        if res % smallNumb == 0:
            break
        else:
            res += bigNumb
    return res

T = int(sys.stdin.readline())
for i in range(T):
    numbs = list(map(int, sys.stdin.readline().split()))
    print(LCM(numbs[0], numbs[1]))
