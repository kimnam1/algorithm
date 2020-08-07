# https://www.acmicpc.net/problem/1059

l = int(input())
luckyset = list(map(int, input().split(' ')))
luckyset.sort()
n = int(input())


ans = 0
for i in range(l-1):
    now = luckyset[i]
    nextnumb = luckyset[i+1]
    if n < luckyset[0]:
        left = n - 1
        right = luckyset[0] - n - 1
        ans = (left+1) * (right+1) - 1
        break
    if now < n < nextnumb:
        left = n - (now + 1)
        right = (nextnumb - 1) - n
        ans = (left+1) * (right+1) - 1
        break
    else:
        pass

print(ans)