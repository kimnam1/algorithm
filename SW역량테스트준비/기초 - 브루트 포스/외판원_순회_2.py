#https://www.acmicpc.net/problem/10971
import sys

T = int(sys.stdin.readline())
numbList = []
for i in range(T):
    numbList.append(list(map(int, sys.stdin.readline().split())))

mini = 10000000
visited = []
def recur(remain, result):
    global mini, visited
    if not remain:
        mini = min(mini, result)
    for i, item in enumerate(remain):
        if i in visited:
            remain.remove(item)
        else:
            if item == 0:
                remain.remove(item)
                recur(numbList[i], result + item)
                remain.insert(i, item)

for i in numbList:
    recur(i, 0)

print(mini)