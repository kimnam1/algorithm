a = int(input())

for i in range(1,a+1):
    r = input()
    rr = r.split(' ')
    r1 = int(rr[0])
    r2 = int(rr[1])
    sum = r1 + r2
    print(f"Case #{i}: " + str(sum))