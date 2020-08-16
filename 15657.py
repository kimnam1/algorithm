import sys

nm = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
N = nm[0]
M = nm[1]

def recur(curIndx, result:list):
    if len(result) == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(curIndx, N):
            result.append(numbers[i])
            recur(i, result)
            result.pop()

recur(0, [])