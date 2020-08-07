#https://www.acmicpc.net/problem/9012
import sys


def is_VPS(s):
    counter = 0
    index = 0
    while counter >= 0:
        if s[index] == "(":
            counter += 1
        elif s[index] == ")":
            counter -= 1
        else:
            return "NO"
        if index + 1 == len(s):
            if counter == 0:
                return "YES"
            else:
                return "NO"
        index += 1
    if counter < 0:
        return "NO"

T = int(sys.stdin.readline())
for i in range(T):
    print(is_VPS(sys.stdin.readline().strip()))
