import sys

N = int(sys.stdin.readline())
nlist = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))

for i in checkList:
    if i in nlist:
        print(1)
    else:
        print(0)