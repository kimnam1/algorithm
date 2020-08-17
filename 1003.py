import sys

N = int(sys.stdin.readline())
numbers = []
for i in range(N):
    numbers.append(int(sys.stdin.readline()))

zeroList = [1, 0] + [1] * 39
oneList = [0, 1] + [1] * 39

for i in range(41):
    if i == 0:
        pass
    elif i == 1:
        pass
    else:
        zeroList[i] = zeroList[i-1] + zeroList[i-2]
        oneList[i] = oneList[i-1] + oneList[i-2]

for i in numbers:
    print(zeroList[i], oneList[i])