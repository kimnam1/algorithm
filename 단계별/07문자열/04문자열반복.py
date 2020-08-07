T = int(input())
Slist = []
for i in range(T):
    case = input().split(' ')
    Slist.append(case)

for i in range(T):
    R = int(Slist[i][0])
    S = Slist[i][1]
    P = []
    for j in range(len(S)):
        P.append(S[j]*R)
    print(''.join(P))