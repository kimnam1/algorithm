# https://www.acmicpc.net/problem/1075
import sys


def dividable(n, f):
    n = n // 100 * 100
    for i in range(100):
        if n % f == 0:
            return str(n)[-2:]
        else:
            n += 1

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())
print(dividable(N, F))