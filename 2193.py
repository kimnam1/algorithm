import sys

n = int(sys.stdin.readline())

ansList = [0, [0, 1], [1, 0]] + [[]]*(n-2) #sublist에서 0번째 숫자는 0으로 끝나는 숫자 개수, 1번째 숫자는 1로 끝나는 숫자 개수

for i in range(3, n+1):
    ansList[i] = [ansList[i-1][0] + ansList[i-1][1], ansList[i-1][0]]


print(sum(ansList[n]))