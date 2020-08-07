#https://www.acmicpc.net/problem/10973
import sys


def previousPermutation(l:list):
    if len(l) == 1:
        return [-1]
    temp = []
    while True:
        child = l.pop()
        parent = l.pop()
        if parent > child:
            temp.append(child)
            temp.sort(reverse=True)
            for i in temp:
                if i < parent:
                    l.append(i)
                    temp.remove(i)
                    break
            temp.append(parent)
            temp.sort(reverse=True)
            l += temp
            return l
        else:
            temp.append(child)
            l.append(parent)
            if len(l) < 2:
                return [-1]

T = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))
result = list(map(str, previousPermutation(test)))
print(" ".join(result))