def groupword(s: str):
    list = []
    for i in range(len(s)):
        list.append(s[i])

    ans = True
    checker = ''
    checkedlist = []
    for i in range(len(list)):
        if list[i] == checker:
            pass
        elif (not inlist(checkedlist, list[i])) and list[i] != checker:
            checker = list[i]
            checkedlist.append(checker)
        elif inlist(checkedlist, list[i]) and list[i] != checker:
            ans = False
    return ans

def inlist(a:list, b): # list a 안에 b가 없으면 True, 있으면 False
    ans = False
    for i in range(len(a)):
        if a[i] == b:
            ans = True
        else:
            pass
    return ans

n = int(input())
wordlist = []
for i in range(n):
    wordlist.append(input())

count = 0
for i in range(len(wordlist)):
    if groupword(wordlist[i]):
        count += 1

print(count)