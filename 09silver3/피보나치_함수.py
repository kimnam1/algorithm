#https://www.acmicpc.net/problem/1003
import collections
import sys


def fibonacci_function(x):
    if x == 0:
        return collections.Counter({0:1, 1:0})
    elif x == 1:
        return collections.Counter({0:0, 1:1})
    else:
        return fibonacci_function(x-1) + fibonacci_function(x-2)

T = int(sys.stdin.readline())
for i in range(T):
    x = int(sys.stdin.readline())
    print(fibonacci_function(x).get(0), fibonacci_function(x).get(1))

#맞는 거 같은데 시간초과
