# https://www.acmicpc.net/problem/1085

def rectangle(x, y, w, h):
    vertical = [(w-x), x]
    horizontal = [(h-y), y]
    return min(min(horizontal), min(vertical))

a = list(map(int, input().split(' ')))
print(rectangle(a[0], a[1], a[2], a[3]))