#https://www.acmicpc.net/problem/1769
import sys


def sumOfAllDigits(n):
    nAsList = list(str(n))
    ans = 0
    for i in range(len(nAsList)):
        ans += int(nAsList[i])
    return ans

def oneDigit(n):
    sumCount = 0
    numberNow = n
    while True:
        if numberNow // 10 == 0:
            break
        else:
            numberNow = sumOfAllDigits(numberNow)
            sumCount += 1
    if numberNow == 3 or numberNow == 6 or numberNow == 9:
        return [sumCount, "YES"]
    else:
        return [sumCount, "NO"]

ans = oneDigit(int(sys.stdin.readline().rstrip()))
print(ans[0])
print(ans[1])

#시간초과
