# https://www.acmicpc.net/problem/1064

def distance(a, b):
    (ax, ay) = a
    (bx, by) = b
    dx = ax - bx
    dy = ay - by
    return ((dx**2)+(dy**2))**0.5

def parallelogram(a, b, c):
    (ax, ay) = a
    (bx, by) = b
    (cx, cy) = c

    ans1 = (ax+(bx-ax)+(cx-ax)), (ay+(by-ay)+(cy-ay))
    ans2 = (bx+(cx-bx)+(ax-bx)), (by+(cy-by)+(ay-by))
    ans3 = (cx+(ax-cx)+(bx-cx)), (cy+(ay-cy)+(by-cy))

    if True: # 벡터가 같을 때 = 한 직선 위에 있을 때 ???????????????
        return -1
    else:
        sq1 = (distance(a, b) + distance(a, c)) * 2
        sq2 = (distance(b, c) + distance(b, a)) * 2
        sq3 = (distance(a, c) + distance(b, c)) * 2
        return max(sq1, sq2, sq3) - min(sq1, sq2, sq3)

x = list(map(int, input().split(' ')))

a = (x[0], x[1])
b = (x[2], x[3])
c = (x[4], x[5])

print(parallelogram(a, b, c))