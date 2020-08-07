S = list(map(str, input().upper()))

dict = {}

for i in range(ord('A'), ord('Z')+1):
    dict[chr(i)] = 0

for i in range(len(S)):
    dict[S[i]] += 1
maxcount = 0
max = ''
for i in range(ord('A'), ord('Z')+1):
    if dict[chr(i)] > maxcount:
        maxcount = dict[chr(i)]
        max = chr(i)
    elif dict[chr(i)] == maxcount:
        max = '?'

print(max)