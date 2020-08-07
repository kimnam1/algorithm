numlist = []

for i in range(9):
    numlist.append(int(input()))


max = numlist[0]
dd = 0

for i in range(9):
    if numlist[i] > max:
        max = numlist[i]
        dd = i
    else:
        pass

print(max)
print(dd+1)
