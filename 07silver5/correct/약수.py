# https://www.acmicpc.net/problem/1037

n = int(input())
a = list(map(int, input().split(' ')))
a.sort()
if n % 2 == 0:
    print(a[0] * a[n-1])
else:
    print(a[(n //2)] ** 2)