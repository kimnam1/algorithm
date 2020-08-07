def hive(a:int):
    i = 0
    if a == 1:
        return 1
    while i < 20000:
        if (a <= ((3 * (i * i)) - (3 * i) + 1)) and (a > ((3 * (i * i)) - (9 * i) + 7)):
            break
        i += 1
    return i


n = int(input())
print(hive(n))