#https://www.acmicpc.net/problem/4344



c = int(input())
cases = []

for i in range(c):
    cases.append(input())

for i in range(len(cases)):
    case = cases[i]
    case = list(map(int, case.split(' ')))
    n = int(case[0])
    over_the_average_count = 0
    average = (sum(case) - n) / n
    for j in range(1, (len(case))):
        if case[j] > average:
            over_the_average_count = over_the_average_count + 1
        else:
            pass
    ratio = over_the_average_count/n
    print("%0.3f%%" % (ratio*100))
