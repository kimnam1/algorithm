#https://www.acmicpc.net/problem/2577

def number_counter(a, b, c):
    multiplied = a * b * c
    multiplied_str = str(multiplied)
    multiplied_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    for i in range(len(multiplied_str)):
        multiplied_dict[multiplied_str[i]] = multiplied_dict[multiplied_str[i]] + 1
    return multiplied_dict

A = int(input())
B = int(input())
C = int(input())
ans = number_counter(A, B, C)

for i in range(10):
    print(ans[str(i)])
