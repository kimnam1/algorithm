import sys

n = int(sys.stdin.readline())
ansList = []

for i in range(1, 1001):
    if i == 1:
        ansList.append(1)
    elif i == 2:
        ansList.append(2)
    else:
        ansList.append(ansList[i-2] + ansList[i-3])

print(ansList[n-1] % 10007)