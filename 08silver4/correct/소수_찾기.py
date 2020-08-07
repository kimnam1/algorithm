#https://www.acmicpc.net/problem/1978
import sys


def is_primenumber(a):
    if a == 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
        else:
            pass
    return True

N = int(sys.stdin.readline())
numbList = list(map(int, sys.stdin.readline().split()))
counter = 0
for i in range(N):
    if is_primenumber(numbList[i]):
        counter += 1
    else:
        pass

print(counter)