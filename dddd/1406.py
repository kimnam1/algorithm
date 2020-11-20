import sys

ll = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())

cmdList = []
for i in range(m):
    cmdList.append(list(sys.stdin.readline().split()))

cursor = len(ll)

for i in cmdList:
    if i[0] == 'L':
        if cursor == 0:
            pass
        else:
            cursor -= 1
    elif i[0] == 'D':
        if cursor == (len(ll) + 1):
            pass
        else:
            cursor += 1
    elif i[0] == 'B':
        lll = ll[0:cursor]
        llr = ll[cursor:]
        if lll:
            lll.pop()
        else:
            pass
        ll = lll + llr
        if cursor == 0:
            pass
        else:
            cursor -= 1
    elif i[0] == 'P':
        lll = ll[0:cursor]
        llr = ll[cursor:]
        lll.append(i[1])
        ll = lll + llr
        cursor += 1

print(''.join(ll))