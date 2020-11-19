import sys

n = int(sys.stdin.readline())
wanted = []
for i in range(n):
    wanted.append(int(sys.stdin.readline()))

wanted.reverse()

stack = []
curNumb = 1
res = []
resres = True

while wanted:
    x = wanted.pop()
    while x >= curNumb or not stack:
        res.append('+')
        stack.append(curNumb)
        curNumb += 1
    if stack[len(stack) - 1] == x:
        res.append('-')
        stack.pop()
    else:
        resres = False
        break

if resres:
    for i in res:
        print(i)
else:
    print('NO')