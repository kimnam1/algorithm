a = input().split(' ')
n = int(a[0])
x = int(a[1])
list = input().split(' ')
answer = ""

for i in range(0, n):
    temp = int(list[i])
    if temp < x:
        answer = answer + str(temp) + " "

print(answer)