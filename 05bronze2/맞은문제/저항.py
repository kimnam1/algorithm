# https://www.acmicpc.net/problem/1076
def colorToNumber(color:str):
    if color == "black":
        return 0
    elif color == "brown":
        return 1
    elif color == "red":
        return 2
    elif color == "orange":
        return 3
    elif color == "yellow":
        return 4
    elif color == "green":
        return 5
    elif color == "blue":
        return 6
    elif color == "violet":
        return 7
    elif color == "grey":
        return 8
    elif color == "white":
        return 9

a = [input() for i in range(3)]
first = colorToNumber(a[0])
second = colorToNumber(a[1])
third = colorToNumber(a[2])
print(((first * 10) + second) * (10 ** third))