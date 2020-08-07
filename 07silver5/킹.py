# https://www.acmicpc.net/problem/1063

def movement(now, move):
    ansV = now[0]
    ansH = int(now[1])
    if move == "R":
        if ansV == "H":
            pass
        else:
            ansV = chr(ord(ansV) + 1)
    elif move == "L":
        if ansV == "A":
            pass
        else:
            ansV = chr(ord(ansV) - 1)
    elif move == "B":
        if ansH == 1:
            pass
        else:
            ansH = ansH - 1
    elif move == "T":
        if ansH == 8:
            pass
        else:
            ansH = ansH + 1
    elif move == "RT":
        if ansV == "H" or ansH == 8:
            pass
        else:
            ansV = chr(ord(ansV) + 1)
            ansH = ansH + 1
    elif move == "LT":
        if ansV == "A" or ansH == 8:
            pass
        else:
            ansV = chr(ord(ansV) - 1)
            ansH = ansH + 1
    elif move == "RB":
        if ansV == "H" or ansH == 1:
            pass
        else:
            ansV = chr(ord(ansV) + 1)
            ansH = ansH - 1
    elif move == "LB":
        if ansV == "A" or ansH == 1:
            pass
        else:
            ansV = chr(ord(ansV) - 1)
            ansH = ansH - 1
    return ansV + str(ansH)

a = input().split(' ')
kingLocation = a[0]
pawnLocation = a[1]
n = int(a[2])

move = []
for i in range(n):
    move.append(input())

for i in range(n):
    kingExpected = movement(kingLocation, move[i])
    pawnExpected = movement(pawnLocation, move[i])
    if (kingLocation == kingExpected) or (pawnLocation == pawnExpected):
        pass
    else:
        kingLocation = kingExpected
        pawnLocation = pawnExpected

print(kingLocation)
print(pawnLocation)