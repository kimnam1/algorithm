#https://www.acmicpc.net/problem/1676
import math
import sys


def zeros_of_factorial(n):
    factorialN = math.factorial(n)
    counter = 0
    for i in range(len(str(factorialN))):
        if factorialN % 10 == 0:
            counter += 1
            factorialN = factorialN // 10
        else:
            break
    return counter
print(zeros_of_factorial(int(sys.stdin.readline())))