# https://www.acmicpc.net/problem/10250

def hotel(h:int, w:int, n:int):
    if n % h != 0:
        room = (n // h) + 1
        level = n % h
    elif n % h == 0:
        room = n // h
        level = h


    levelans = str(level)
    if len(str(room)) == 1:
        roomans = '0' + str(room)
    else:
        roomans = str(room)
    return levelans + roomans

god = int(input())
caselist = []
for i in range(god):
    caselist.append(list(map(int, input().split(' '))))
for i in range(god):
    print(hotel(caselist[i][0], caselist[i][1], caselist[i][2]))
