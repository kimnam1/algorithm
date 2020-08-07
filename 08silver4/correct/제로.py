#https://www.acmicpc.net/problem/10773
import sys

N = int(sys.stdin.readline())
numbList = []
for i in range(N):
    x= int(sys.stdin.readline())
    if x == 0:
        numbList.pop()
    else:
        numbList.append(x)

print(sum(numbList))