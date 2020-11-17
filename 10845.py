import sys

N = int(sys.stdin.readline())
cmdList = []
for i in range(N):
    cmdList.append(list(sys.stdin.readline().split()))

queue = []
for i in cmdList:
    if i[0] == 'push':
        queue.append(int(i[1]))
    elif i[0] == 'pop':
        queue.reverse()
        if len(queue) < 1:
            print(-1)
        else:
            print(queue.pop())
        queue.reverse()
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            queue.reverse()
            print(queue[len(queue) - 1])
            queue.reverse()
    elif i[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            queue.reverse()
            print(queue[0])
            queue.reverse()


