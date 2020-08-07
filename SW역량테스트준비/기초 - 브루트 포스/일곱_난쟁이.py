#https://www.acmicpc.net/problem/2309
import sys
from itertools import combinations

midgetList = []
for i in range(9):
    midgetList.append(int(sys.stdin.readline()))

midgetCombination = list(combinations(midgetList, 7))

res = []
for l in midgetCombination:
    if sum(l) == 100:
        res = sorted(l)
        break
    else:
        pass

for i in range(len(res)):
    print(res[i])