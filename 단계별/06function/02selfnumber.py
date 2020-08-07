# https://www.acmicpc.net/problem/4673


def d(n):
    ans = n
    for i in range(len(str(n))):
        ans = ans + int(str(n)[i])
    return ans

notselfnumber = []
for i in range(1, 10001):
    now = d(i)
    if now <= 10000:
        notselfnumber.append(now)
notselfnumber.sort()

index = 0
while index < len(notselfnumber):
    for i in range(1, 10001):
        checking = True
        while checking == True:
            if (i < notselfnumber[index]) and (checking == True):
                print(i)
                checking = False
            elif i == notselfnumber[index]:
                checking = False
                index += 1
            elif i > notselfnumber[index]:
                index += 1