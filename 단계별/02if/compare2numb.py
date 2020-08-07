aa = input()
aaa = aa.split(' ')
a = int(aaa[0])
b = int(aaa[1])

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")