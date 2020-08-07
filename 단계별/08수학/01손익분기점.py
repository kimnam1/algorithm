numberlist = list(map(int, input().split(' ')))

a = numberlist[0]
b = numberlist[1]
c = numberlist[2]

if b >= c:
    break_even_point = -1
else:
    break_even_point = (a // (c-b)) + 1


print(break_even_point)