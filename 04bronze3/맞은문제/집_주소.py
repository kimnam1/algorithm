# https://www.acmicpc.net/problem/1284
import sys

def address(a:int):
    figure = len(str(a))
    numberlist = []
    sum = 0
    for i in range(figure):
        numberlist.append(int(str(a)[i]))
    for i in range(figure):
        d = numberlist[i]
        if d == 0:
           sum += 4
        elif d == 1:
            sum += 2
        else:
            sum += 3
    return sum + (figure-1) * 1 + 2

while True:
    d = int(sys.stdin.readline())
    if d == 0:
        break
    else:
        print(address(d))