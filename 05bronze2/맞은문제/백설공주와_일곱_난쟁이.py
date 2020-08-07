#https://www.acmicpc.net/problem/3040
import copy


def dwarfs_finder(a, b, c, d, e, f, g, h, i):
    ans = [a, b, c, d, e, f, g, h, i]
    for i in range(8):
        for j in range(8-i):
            test = copy.deepcopy(ans)
            test.remove(ans[i])
            test.remove(ans[i+j+1])
            hundredtester = 0
            for k in range(len(test)):
                hundredtester += test[k]
            if hundredtester == 100:
                return test
            else:
                pass

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

ans = dwarfs_finder(a, b, c, d, e, f, g, h, i)
for i in range(7):
    print(ans[i])