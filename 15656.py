import sys

nm = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
N = nm[0]
M = nm[1]

def recur(counter, result):
    if counter == M:
        print(" ".join(map(str, result)))
    else:
        for i in numbers:
            result.append(i)
            recur(counter+1, result)
            result.pop()

recur(0, [])