# https://www.acmicpc.net/problem/1094

def stick(a): #a는 만들고 싶은 막대기 길이
    stick_list = [64]
    while sum(stick_list) > a:
        shortest = min(stick_list)
        stick_list.remove(shortest)
        stick_list.append(shortest/2)
        stick_list.append(shortest/2)
        if sum(stick_list) - shortest/2 >= a:
            stick_list.remove(shortest/2)
        else:
            pass
    return len(stick_list)

x = int(input())

print(stick(x))