aa = input()
aaa = aa.split(' ')

a = int(aaa[0])
b = int(aaa[1])
c = int(aaa[2])

if a>=b:
    if a>=c:
        if b>=c:
            print(b)
        else:
            print(c)
    else:
        print(a)
elif b>=a:
    if b>=c:
        if a>=c:
            print(a)
        else:
            print(c)
    else:
        print(b)