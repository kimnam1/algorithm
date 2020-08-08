#https://www.acmicpc.net/problem/14888
#연산자 끼워넣기

import itertools
import sys

n = int(sys.stdin.readline())
numbList = list(map(int, sys.stdin.readline().split()))
numbList.reverse()
operatorNumbs = list(map(int, sys.stdin.readline().split()))
temp = []
for i in range(operatorNumbs[0]):
    temp.append('+')
for i in range(operatorNumbs[1]):
    temp.append('-')
for i in range(operatorNumbs[2]):
    temp.append('*')
for i in range(operatorNumbs[3]):
    temp.append('/')
operatorsOdds = list(dict.fromkeys(itertools.permutations(temp)))

big = int
small = int

for i, c in enumerate(operatorsOdds):
    numbs = numbList.copy()
    dd = numbs.pop()
    for j in c:
        dn = numbs.pop()
        if j == '+':
            dd = dd + dn
        elif j == '-':
            dd = dd - dn
        elif j == '*':
            dd = dd * dn
        elif j == '/':
            if dd < 0:
                ddabs = abs(dd)
                dd = -(ddabs // dn)
            else:
                dd = dd // dn
    if i == 0:
        big = dd
        small = dd
    else:
        big = max(big, dd)
        small = min(small, dd)

print(big)
print(small)