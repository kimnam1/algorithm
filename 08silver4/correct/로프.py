#https://www.acmicpc.net/problem/2217
import copy
import sys


def rope(l:list):
    l.sort()
    resList = []
    for i in range(len(l)):
        resList.append((l[i]*(len(l)-i)))
    return max(resList)

N = int(sys.stdin.readline())
numbList = []
for i in range(N):
    numbList.append(int(sys.stdin.readline()))

print(rope(numbList))