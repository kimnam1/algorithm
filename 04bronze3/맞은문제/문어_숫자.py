# https://www.acmicpc.net/problem/1864
import sys

def octonumber(a:str):
    if a == "-":
        return 0
    elif a == '\\'.rstrip():
        return 1
    elif a == "(":
        return 2
    elif a == "@":
        return 3
    elif a == "?":
        return 4
    elif a == ">":
        return 5
    elif a == "&":
        return 6
    elif a == "%":
        return 7
    elif a == "/":
        return -1

while True:
    d = input()
    d = d[::-1]
    ans = 0
    if d == "#":
        break
    else:
        for i in range(len(d)):
            ans += octonumber(d[i]) * (8 ** i)
    print(ans)