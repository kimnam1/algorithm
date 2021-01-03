import sys

n = int(sys.stdin.readline())

ansList = [1, 3]

for i in range(2, 1000):
    ansList.append(ansList[i-1] + (2*ansList[i-2]))

print(ansList[n-1] % 10007)