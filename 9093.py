import sys

t = int(sys.stdin.readline())
caseList = []
for i in range(t):
    caseList.append(sys.stdin.readline().split())

resList = []

for i in caseList:
    res = ''
    for j in i:
        resres = ''
        if len(j) > 1:
            temp = list(j)
            for k in range(len(temp)):
                resres += temp.pop()
        else:
            temp = list(j)
            resres += temp.pop()
        res += resres
        res += ' '
    resList.append(res.rstrip())

for i in resList:
    print(i)