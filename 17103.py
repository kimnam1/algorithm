import sys


t = int(sys.stdin.readline())
caseList = []
for i in range(t):
    caseList.append(int(sys.stdin.readline()))

primeBool = [False, False] + [True] * 999999
for i in range(int(1000000**0.5)):
    if primeBool[i]:
        for j in range(2*i, 1000001, i):
            primeBool[j] = False

def goldbach(x:int):
    res = 0
    for i in range(1, x//2+1):
        if primeBool[i] and primeBool[x-i]:
            res += 1
    return res

for i in caseList:
    print(goldbach(i))