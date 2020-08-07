a = int(input())
b = int(input())
c = int(input())

mult = a * b * c

list = str(mult)
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count0 = 0

for i in range(len(list)):
    if int(list[i]) == 0:
        count0 = count0 + 1
    elif int(list[i]) == 1:
        count1 = count1 + 1
    elif int(list[i]) == 2:
        count2 = count2 + 1
    elif int(list[i]) == 3:
        count3 = count3 + 1
    elif int(list[i]) == 4:
        count4 = count4 + 1
    elif int(list[i]) == 5:
        count5 = count5 + 1
    elif int(list[i]) == 6:
        count6 = count6 + 1
    elif int(list[i]) == 7:
        count7 = count7 + 1
    elif int(list[i]) == 8:
        count8 = count8 + 1
    elif int(list[i]) == 9:
        count9 = count9 + 1

print(count0)
print(count1)
print(count2)
print(count3)
print(count4)
print(count5)
print(count6)
print(count7)
print(count8)
print(count9)