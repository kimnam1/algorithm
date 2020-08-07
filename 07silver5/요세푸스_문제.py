# https://www.acmicpc.net/problem/1158

def josephus(n,k):
    p = [i+1 for i in range(n)]
    ans = []
    while len(p) != 0:
        for i in range(k-1):
            p.append(p[0])
            p.remove(p[0])
        ans.append(p[0])
        p.remove(p[0])
    return ans

a = list(map(int, input().split(' ')))
ans = '<'
ansl = josephus(a[0], a[1])
for i in range(len(ansl)):
    if i+1 == len(ansl):
        ans += f'{ansl[i]}>'
    else:
        ans += f'{ansl[i]}, '

print(ans)


# 시간초과!