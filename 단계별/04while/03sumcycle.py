import sys

start = int(sys.stdin.readline())
if start < 10:
    start10 = start * 10
else:
    start10 = start

cycle = start10
count = 0
while True:
    a = cycle // 10
    b = cycle % 10

    sum = a + b

    if sum >= 10:
        sum = sum % 10
    else:
        sum = sum

    cycle = (b*10) + sum
    if (start < 10) and (count == 0):
        cycle = start * 10 + start

    count = count + 1

    if cycle == start:
        break

print(count)