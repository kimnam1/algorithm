#https://www.acmicpc.net/problem/9613

import sys
from itertools import combinations

def GDC(x, y):
    bigNumb = max(x, y)
    smallNumb = min(x, y)
    rest = bigNumb % smallNumb
    while rest != 0:
        bigNumb = smallNumb
        smallNumb = rest
        rest = bigNumb % smallNumb
    return smallNumb

T = int(sys.stdin.readline())
for i in range(T):
    numbList = list(map(int, sys.stdin.readline().split()))
    numbList.pop(0)
    realNumbList = list(combinations(numbList, 2))
    resList = []
    for i, j in realNumbList:
        resList.append(GDC(i, j))
    print(sum(resList))


