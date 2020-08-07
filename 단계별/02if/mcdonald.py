a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

s1 = a + d - 50
s2 = a + e - 50
s3 = b + d - 50
s4 = b + e - 50
s5 = c + d - 50
s6 = c + e - 50

print(min(s1, s2, s3, s4, s5, s6))