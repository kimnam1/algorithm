#https://www.acmicpc.net/problem/15658
import itertools
import sys

N = int(sys.stdin.readline())
numbList = list(map(int, sys.stdin.readline().split()))
numbList.reverse()
operatorNumb = list(map(int, sys.stdin.readline().split()))
temp = []
for i in range(operatorNumb[0]):
    temp.append('+')
for i in range(operatorNumb[1]):
    temp.append('-')
for i in range(operatorNumb[2]):
    temp.append('*')
for i in range(operatorNumb[3]):
    temp.append('/')
operatorsPermu = list(dict.fromkeys(itertools.permutations(temp, N-1)))

big = int
small = int

for i, c in enumerate(operatorsPermu):
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