n = int(input())
numbers = str(input())

list = []
for i in range(n):
    list.append(int(numbers[i]))

sum = 0
for i in range(len(list)):
    sum = sum + list[i]

print(sum)