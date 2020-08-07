# https://www.acmicpc.net/problem/1546
import sys

n = int(input())
grades = list(map(int, sys.stdin.readline().split(' ')))

fake_grades = []
max_grade = max(grades)

for i in range(len(grades)):
    fake_grades.append((grades[i]/max_grade)*100)

fake_average = sum(fake_grades)/n

print(fake_average)