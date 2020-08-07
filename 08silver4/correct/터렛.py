#https://www.acmicpc.net/problem/1002
import sys

def turret(a, b, c, d, e, f):
    dBtw = ((a-d)**2+(b-e)**2)**0.5
    if dBtw == 0 and c == f: # 같은 원일 때
        return -1
    if c >= f:
        bigCircle = [a, b, c]
        smallCircle = [d, e, f]
    else:
        bigCircle = [d, e, f]
        smallCircle = [a, b, c]
    if dBtw < bigCircle[2]: # 큰 원 안에 작은 원 중심 있을 때
        if bigCircle[2] - dBtw < smallCircle[2]:
            return 2
        elif bigCircle[2] - dBtw == smallCircle[2]:
            return 1
        else:
            return 0
    elif dBtw == bigCircle[2]: # 큰 원 위에 작은 원 중심 = 무조건 두 점에서 만남
        return 2
    else:
        if dBtw >  c + f:
            return 0
        elif dBtw == c + f:
            return 1
        elif dBtw < c + f:
            return 2


T = int(sys.stdin.readline())
cases = []
for i in range(T):
    case = list(map(int, sys.stdin.readline().split()))
    print(turret(case[0], case[1], case[2], case[3], case[4], case[5]))