import sys

n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(input())

words = list(dict.fromkeys(words))

wordsLength = []
for i in range(51):
    wordsLength.append([])

for i in words:
    wordsLength[len(i)].append(i)
    wordsLength[len(i)].sort()

for i in wordsLength:
    for j in i:
        print(j)