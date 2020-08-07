#https://www.acmicpc.net/problem/1699

def sum_of_squares(n):
    cur = 1
    res = []
    while cur ** 2 <= n:
        if cur ** 2 == n:
            res.append(1)
            cur += 1
        else:
            res.append(1 + sum_of_squares(n-cur))
            cur += 1
    return min(res)

print(sum_of_squares(6))