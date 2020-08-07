#https://www.acmicpc.net/problem/10972
import sys


def nextPermutation(l:list):
    if len(l) == 1:
        return [-1]
    temp = []
    while True:
        child = l.pop()
        parent = l.pop()
        if child < parent:
            temp.append(child)
            l.append(parent)
            if len(l) < 2:
                return [-1]
        else:
            temp.append(child)
            temp.sort()
            for i in temp:
                if i > parent:
                    l.append(i)
                    temp.remove(i)
                    break
            temp.append(parent)
            temp.sort()
            l += temp
            return l

T = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))

result = list(map(str, nextPermutation(test)))
print(" ".join(result))