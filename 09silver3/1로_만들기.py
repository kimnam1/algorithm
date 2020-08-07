#https://www.acmicpc.net/problem/1463
import sys


def making_one(x):
    counter = 0
    nowNumb = x
    while nowNumb != 1:
        if nowNumb % 3 == 0:
            nowNumb = nowNumb / 3
            counter += 1
        elif nowNumb % 2 == 0:
            if (nowNumb - 1) % 9 == 0:
                nowNumb = nowNumb - 1
                counter += 1
            else:
                nowNumb = nowNumb / 2
                counter += 1
        else:
            nowNumb -= 1
            counter += 1
    return counter

print(making_one(int(sys.stdin.readline())))