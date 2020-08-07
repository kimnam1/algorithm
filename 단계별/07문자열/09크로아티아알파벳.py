b = input()
count = 0
for i in range(len(b)):
    if b[i] == 'c':
        if b[i+1] == '=':
            pass
        elif b[i+1] == '-':
            pass
        else:
            count += 1
    elif b[i] == 'd':
        if b[i+1] == 'z':
            if b[i+2] == '=':
                pass
            else:
                count += 1
        elif b[i+1] == '-':
            pass
        else:
            count += 1
    elif b[i] == 'l':
        if b[i+1] == 'j':
            pass
        else:
            count += 1
    elif b[i] == 'n':
        if b[i+1] == 'j':
            pass
        else:
            count += 1
    elif b[i] == 's':
        if b[i+1] == '=':
            pass
        else:
            count += 1
    elif b[i] == 'z':
        if b[i+1] == '=':
            pass
        else:
            count += 1
    else:
        count += 1

print(count)