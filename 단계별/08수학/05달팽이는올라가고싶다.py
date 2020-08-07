# https://www.acmicpc.net/problem/2869

def snail(a:int, b:int, v:int): # a = 낮에 올라가는 길이, b = 밤에 내려오는 길이, v = 목표 높이
    if (v - a) % (a -b) == 0:
        return ((v - a) // (a -b)) + 1
    elif (v - a) % (a -b) != 0:
        return ((v - a) // (a -b)) + 2


iii = list(map(int, input().split(' ')))
a = iii[0]
b = iii[1]
c = iii[2]
print(snail(a, b, c))