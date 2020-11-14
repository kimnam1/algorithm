import sys

n, s = map(int, sys.stdin.readline().split())
numbList = list(map(int, sys.stdin.readline().split()))
resList = []

def recur(sum:int, curIdx:int):
    global numbList, resCount

    if curIdx == len(numbList):
        resList.append(sum)
    else:
        recur(sum, curIdx+1)
        recur(sum + numbList[curIdx], curIdx + 1)

recur(0, 0)
resCnt = 0
resList.remove(0)
for i in resList:
    if i == s:
        resCnt += 1
    else:
        pass

print(resCnt)