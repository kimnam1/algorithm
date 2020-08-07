b = input()
count = 0
for i in range(len(b)):
    count += 1
    if b[i] == '=':
        count += -1
        if (b[i-1] == 'z') and (b[i-2] == 'd'):
            count += -1
    elif b[i] == '-':
        count += -1
    elif (b[i] == 'j') and ((b[i-1] == 'l') or (b[i-1] == 'n')):
        count += -1


print(count)