#https://www.acmicpc.net/problem/10872
import sys


def factorial(x):
    if x == 0:
        return 1
    result = 1
    for i in range(1, x+1):
        result *= i
    return result

n = int(sys.stdin.readline())
print(factorial(n))