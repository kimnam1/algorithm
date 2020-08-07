def chartonumb(s: str):
    ans = []
    a = s
    for i in range(len(a)):
        if (a[i] == 'A') or (a[i] == 'B') or (a[i] == 'C'):
            ans.append('2')
        elif (a[i] == 'D') or (a[i] == 'E') or (a[i] == 'F'):
            ans.append('3')
        elif (a[i] == 'G') or (a[i] == 'H') or (a[i] == 'I'):
            ans.append('4')
        elif (a[i] == 'J') or (a[i] == 'K') or (a[i] == 'L'):
            ans.append('5')
        elif (a[i] == 'M') or (a[i] == 'N') or (a[i] == 'O'):
            ans.append('6')
        elif (a[i] == 'P') or (a[i] == 'Q') or (a[i] == 'R') or (a[i] == 'S'):
            ans.append('7')
        elif (a[i] == 'T') or (a[i] == 'U') or (a[i] == 'V'):
            ans.append('8')
        elif (a[i] == 'W') or (a[i] == 'X') or (a[i] == 'Y') or (a[i] == 'Z'):
            ans.append('9')
    return int(''.join(ans))

def timecount(a: int):
    s = str(a)
    count = 0
    for i in range(len(s)):
        if s[i] == '2':
            count += 3
        elif s[i] == '3':
            count += 4
        elif s[i] == '4':
            count += 5
        elif s[i] == '5':
            count += 6
        elif s[i] == '6':
            count += 7
        elif s[i] == '7':
            count += 8
        elif s[i] == '8':
            count += 9
        elif s[i] == '9':
            count += 10
    return count

print(timecount(chartonumb(input())))