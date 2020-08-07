#https://www.acmicpc.net/problem/1476
"""
E = 15 * x + e
S = 28 * y + s
M = 19 * z + m
E가 가장 먼저 자리수가 올라갈 것이므로 x가 가장 작은 수
z가 그 다음, y가 가장 큰 수
처음에 x를 하나 높여서 ESM이 같은지 체크
그 다음 z를 하나 높여서 ESM이 같은지 체크
...


"""
import sys


def ESM(e, s, m):
    x = 0
    y = 0
    z = 0
    E = 15 * x + e
    S = 28 * y + s
    M = 19 * z + m
    while E != S or E != M:
        smallest = min(E, S, M)
        if smallest == E:
            x += 1
            E = 15 * x + e
        elif smallest == S:
            y += 1
            S = 28 * y + s
        elif smallest == M:
            z += 1
            M = 19 * z + m
    return E

numbList = list(map(int, sys.stdin.readline().split()))
print(ESM(numbList[0], numbList[1], numbList[2]))