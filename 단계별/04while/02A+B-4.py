import sys
r = sys.stdin
while True:
    line = r.readline()
    rr = line.strip().split(' ')
    if rr[0] == '':
        break
    a = int(rr[0])
    b = int(rr[1])

    print(a+b)
    r = sys.stdin