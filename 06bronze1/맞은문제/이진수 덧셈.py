# https://www.acmicpc.net/problem/1252

def binaryToDecimal(a):
    r = str(a)[::-1]
    ans = 0
    for i in range(len(r)):
        ans += int(r[i]) * (2 ** i)
    return ans

def decimalToBinary(a):
    ans = ''
    divided = a
    for i in range(100):
        ans = ans + (str(divided%2))
        divided = divided // 2
        if divided == 0:
            break
    return int(ans[::-1])

a = list(map(int, input().split(' ')))

print(decimalToBinary(binaryToDecimal(a[0])+binaryToDecimal(a[1])))