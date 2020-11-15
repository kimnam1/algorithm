import sys

n = int(sys.stdin.readline())
cmdList = []

for i in range(n):
    cmdList.append(sys.stdin.readline().split())

stack = []

for i in cmdList:
    if i[0] == 'push':
        stack.append(int(i[1]))
    elif i[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])