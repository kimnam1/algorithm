#https://www.acmicpc.net/problem/11723

import sys

result = []

T = int(sys.stdin.readline())
for i in range(T):
    commandX = sys.stdin.readline().split()
    command = commandX[0]
    if command == "add":
        x = int(commandX[1])
        if x in result:
            pass
        else:
            result.append(x)
    elif command == "remove":
        x = int(commandX[1])
        if x in result:
            result.remove(x)
        else:
            pass
    elif command == "check":
        x = int(commandX[1])
        if x in result:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        x = int(commandX[1])
        if x in result:
            result.remove(x)
        else:
            result.append(x)
    elif command == "all":
        result = [i for i in range(1, 21)]
    elif command == "empty":
        result = []

