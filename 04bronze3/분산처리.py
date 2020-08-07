# https://www.acmicpc.net/problem/1009
import sys

T = int(sys.stdin.readline())
for i in range(T):
    ab = list(map(int, sys.stdin.readline().split(' ')))
    print(ab[0]**ab[1] % 10)

#시간 초과
