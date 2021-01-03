import sys

n = int(sys.stdin.readline())

ansList = [0 for i in range(n+1)]

def making_one(x:int):
    global ansList
    ans = 1000000
    if x == 0:
        return 0
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    elif x == 3:
        return 1
    if x % 3 == 0:
        ans = min(ans, 1 + ansList[x//3])
    if x % 2 == 0:
        ans = min(ans, 1 + ansList[x//2])
    ans = min(ans, 1 + ansList[x-1])
    return ans

for i in range(n+1):
    ansList[i] = making_one(i)

print(ansList[n])