#https://www.acmicpc.net/problem/3052




rlist = [] #나머지 배열

for i in range(10):
    rlist.append(int(input())%42)

uniquerlist = []

for j in range(len(rlist)):
    compare = rlist[j]
    compare_count = 0
    for k in range(len(uniquerlist)):
        if uniquerlist[k] == compare:
            compare_count = compare_count + 1
        else:
            pass
    if compare_count == 0:
        uniquerlist.append(compare)
    else:
        pass




print(len(uniquerlist))