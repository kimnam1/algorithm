# https://www.acmicpc.net/problem/1145

def least_multi(a, b, c, d, e): # 들어가는 인자는 5개의 자연수
    ans = 1
    while True:
        dlist = [ans % a, ans % b, ans % c, ans % d, ans % e]
        dlist.sort()
        if dlist[0] + dlist[1] + dlist[2] == 0:
            break
        else:
            ans += 1
    return ans

print(least_multi(30, 42, 70, 35, 90))

# 왜틀리지??