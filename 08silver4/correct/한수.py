#https://www.acmicpc.net/problem/1065
import sys


def oneNumber(a):
    if a < 100:
        return True
    else:
        aAsStr = str(a)
        diff = int(aAsStr[0]) - int(aAsStr[1])
        for i in range(len(aAsStr)-1):
            if int(aAsStr[i]) - int(aAsStr[i+1]) == diff:
                pass
            else:
                return False
        return True

N  = int(sys.stdin.readline())
counter = 0
for i in range(1, N+1):
    if oneNumber(i):
        counter += 1
    else:
        pass
print(counter)
