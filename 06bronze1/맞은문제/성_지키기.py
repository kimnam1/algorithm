# https://www.acmicpc.net/problem/1236

a = list(map(int, input().split(' ')))
castle = []
for i in range(a[0]):
    castle.append(input())

vcount = 0
hcount = 0

# 행 체크
for i in range(len(castle)):
    vnow = castle[i]
    xcount = 0
    for j in range(len(vnow)):
        if vnow[j] == "X":
            xcount += 1
        else:
            pass
    if xcount == 0:
        vcount += 1
    else:
        pass

# 열 체크
for i in range(a[1]):
    hnow = i
    xcount = 0
    for j in range(a[0]):
        if castle[j][hnow] == "X":
            xcount += 1
        else:
            pass
    if xcount == 0:
        hcount += 1
    else:
        pass

print(max(vcount, hcount))