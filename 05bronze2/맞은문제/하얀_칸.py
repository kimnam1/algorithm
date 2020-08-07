# https://www.acmicpc.net/problem/1100

a = [input() for i in range(8)]
count = 0
for i in range(len(a)):
    currentLine = a[i]
    if i % 2 == 0:
        for j in range(8):
            if currentLine[j] == "F" and j % 2 == 0:
                count += 1
            else:
                pass
    else:
        for j in range(8):
            if currentLine[j] == "F" and j % 2 == 1:
                count += 1
            else:
                pass

print(count)