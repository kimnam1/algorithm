#https://www.acmicpc.net/problem/14501
import sys

resDict = {}

T = int(sys.stdin.readline())
for i in range(1, T+1):
    dayIncome = sys.stdin.readline().split()
    resDict[i] = (int(dayIncome[0]), int(dayIncome[1]))

print(resDict)

graph = {}
for i in range(1, T+1):
    graph[i] = [int(j) for j in range(i + resDict[i][0], T+1)]

print(graph)

def resignation(x):
    countable = []
    countable.append(x)
    result = 0
    resultList = []
