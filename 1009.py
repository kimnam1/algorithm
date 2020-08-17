import sys

T = int(sys.stdin.readline())

recur2 = [2, 4, 8, 6]
recur3 = [3, 9, 7, 1]
recur4 = [4, 6]


recur7 = [7, 9, 3, 1]
recur8 = [8, 4, 2, 6]
recur9 = [9, 1]


for i in range(T):
    ans = 0
    n, m = map(int, sys.stdin.readline().split())
    d = n % 10
    if d == 0:
        ans = 10
    elif d == 1 or d == 5 or d == 6:
        ans = d
    elif d == 2:
        ans = recur2[(m % 4) - 1]
    elif d == 3:
        ans = recur3[(m % 4) - 1]
    elif d == 4:
        ans = recur4[(m % 2) - 1]
    elif d == 7:
        ans = recur7[(m % 4) - 1]
    elif d == 8:
        ans = recur8[(m % 4) - 1]
    elif d == 9:
        ans = recur9[(m % 2) - 1]
    print(ans)