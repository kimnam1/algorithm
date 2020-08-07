# https://www.acmicpc.net/problem/1065

def hansucheck(a: int):
    list = []
    if (len(str(a)) == 1) or (len(str(a)) == 2): # 한자리수나 두자리수일 때 무조건 한수
        return True
    elif len(str(a))==3:
        for i in range(3):
            list.append(int(str(a)[i]))
        if (list[0]-list[1])==(list[1]-list[2]):
            return True
        else:
            return False
    elif a == 1000:
        return False


n = int(input())

count = 0
for i in range(1, n+1):
    if hansucheck(i) == True:
        count += 1
    else:
        pass

print(count)