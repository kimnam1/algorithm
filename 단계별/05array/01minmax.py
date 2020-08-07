import sys

n = int(input())
numlist = list(map(int, sys.stdin.readline().split(' ')))

first = numlist[0]
min = first
max = first
for i in numlist: # minfunction
    if i < min:
        min = i
    else:
        pass

for i in numlist: # maxfunction
    if i > max:
        max = i
    else:
        pass

print(f'{min} {max}')