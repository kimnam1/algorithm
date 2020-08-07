S = list(map(int, input().split(' ')))
ans = []


for i in range(len(S)):
    number = S[i]
    numberlist = list(map(str, str(number)))
    numberlist.reverse()
    a = ''.join(numberlist)
    ans.append(int(a))

print(max(ans))