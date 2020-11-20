import sys

n = sys.stdin.readline()
stack = list(map(int, sys.stdin.readline().split()))

resList = []
res = -1

for key, value in enumerate(stack):
    for i in stack[key+1:]:
        if i > value:
            res = i
            break
    resList.append(str(res))
    res = -1

print(' '.join(resList))