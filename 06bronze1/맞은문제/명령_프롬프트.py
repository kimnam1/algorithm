# https://www.acmicpc.net/problem/1032

n = int(input())

a = [input() for i in range(n)]
firstline = a[0]
ans = ''
for i in range(len(firstline)):
    characternow = firstline[i]
    samecount = 0
    for j in range(n):
        if a[j][i] == characternow:
            samecount += 1
        else:
            pass
    if samecount == n:
        ans = ans + characternow
    else:
        ans = ans + "?"

print(ans)