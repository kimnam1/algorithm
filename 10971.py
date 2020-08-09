#https://www.acmicpc.net/problem/10971

import sys

N = int(sys.stdin.readline())
cityList = []
for i in range(N):
    cityList.append(list(map(int, sys.stdin.readline().split())))

mini = 999999999

def TSP(startCityIdx, visitedIdx, curCityIdx, res):
    global mini
    for i, c in enumerate(cityList[curCityIdx]):
        if i in visitedIdx:
            continue
        elif i == startCityIdx:
            if len(visitedIdx) == (N - 1):
                if c == 0:
                    pass
                else:
                    res += c
                    mini = min(mini, res)
            else:
                continue
        elif c == 0:
            continue
        else:
            res += c
            visitedIdx.add(i)
            TSP(startCityIdx, visitedIdx.copy(), i, res)
            visitedIdx.remove(i)

for i, c in enumerate(cityList):
    visitedIdx = set()
    TSP(i, visitedIdx, i, 0)

print(mini)