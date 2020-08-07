#https://www.acmicpc.net/problem/2609
import sys
line = sys.stdin.readline().split()
N = int(line[0])
M = int(line[1])

def divider(x):
    res = []
    for i in range(1, x+1):
        if x % i == 0:
            res.append(i)
    return res

bigNumb = max(N, M)
smallNumb = min(N, M)

GCF = 1
for i in divider(smallNumb):
    if bigNumb % i == 0:
        GCF = i
    else:
        pass
print(GCF)

LCM = bigNumb
while True:
    if LCM % smallNumb == 0:
        break
    else:
        LCM += bigNumb
print(LCM)