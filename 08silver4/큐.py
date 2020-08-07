#https://www.acmicpc.net/problem/10845
import sys


class Queue(object):
    def __init__(self):
        self.item = []

    def push(self, x):
        self.item.append(x)
        return x

    def pop(self):
        if self.item:
            res = self.item.pop(self, 0)
        else:
            res = -1
        return res

    def size(self):
        return len(self.item)

    def empty(self):
        if not self.item:
            return 1
        else:
            return 0

    def front(self):
        if self.item:
            return self.item[0]
        else:
            return -1

    def back(self):
        if self.item:
            return self.item[len(self.item)-1]
        else:
            return -1

queue = Queue()
N = int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        print(queue.push(int(order[1])))
    elif order[0] == "pop":
        print(queue.pop)
    elif order[0] == "size":
        print(queue.size())
    elif order[0] == "empty":
        print(queue.empty())
    elif order[0] == "front":
        print(queue.front())
    elif order[0] == "back":
        print(queue.back())
