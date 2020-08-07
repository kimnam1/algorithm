a = int(input())

for i in range(1, a+1):
    ff = "*" * i
    blk = " " * (a-i)
    print(blk + ff)