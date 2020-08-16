import sys

nm = list(map(int, sys.stdin.readline().split()))
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

ret = []

def recur(curIdx, result:list):
    if len(result) == nm[1]:
        ret.append(" ".join(map(str, result)))
    else:
        for i in range(curIdx, nm[0]):
            result.append(numbers[i])
            recur(i+1, result)
            result.pop()

recur(0, [])

ret = list(dict.fromkeys(ret))
for i in ret:
    print(i)