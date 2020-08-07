# https://www.acmicpc.net/problem/1964

def pentagon(n:int):
    # 5 + ((5 * 2) - 3) + ((5 * 3) - 5)
    ans = 0
    for i in range(1, n+1):
        ans += (5 * i) - (2 * i) + 1
    return ans + 1

a = int(input())

print(pentagon(a)%45678)