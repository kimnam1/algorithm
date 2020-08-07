s = input()

list = []
for i in range(len(s)):
    list.append(s[i])

for k in range(ord('a'), ord('z')+1):
    for i in range(len(list)):
        checking = -1
        if chr(k) == list[i]:
            checking = i
            break
        else:
            pass
    print(checking, end=' ')