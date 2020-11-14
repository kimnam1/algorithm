from itertools import combinations

L, C = map(int, input().split())
charList = [char for char in input().split()]
charList.sort()

def detector(x:list):
    moCounter = 0
    for i in x:
        if i in ['a', 'e', 'i', 'o', 'u']:
            moCounter += 1
        else:
            pass
    if (len(x) - moCounter) < 2 or moCounter < 1:
        return False
    else:
        return True

res = combinations(charList, L)

for i in res:
    if detector(list(i)):
        print(''.join(sorted(i)))