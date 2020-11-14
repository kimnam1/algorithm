import sys

N = int(sys.stdin.readline())
W = []
for i in range(N):
    W.append(list(map(int, sys.stdin.readline().split())))

resList = []

def recur(v:list, curPos:int, sum:int):
    global N, W
    res = sum

    for j, cost in enumerate(W[curPos]):
        if len(v) == N:
            resList.append(res)
            break
        if cost == 0 or j in v:
            pass
        else:
            v.append(j)
            res += recur(v, j, sum+cost)
            v.remove(j)

    return res

recur([], 0, 0)
print(min(resList))