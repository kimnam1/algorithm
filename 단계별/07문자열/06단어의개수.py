S = list(map(str, input().split(' ')))
blank_yn = 0
for i in range(len(S)):
    if S[i] == '':
        blank_yn += 1
    else:
        pass

for i in range(blank_yn):
    S.remove('')

print(len(S))