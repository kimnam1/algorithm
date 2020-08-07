#https://www.acmicpc.net/problem/9095
import sys

T = int(sys.stdin.readline())

def f(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return f(x-1) + f(x-2) + f(x-3)

for i in range(T):
    print(f(int(sys.stdin.readline())))
