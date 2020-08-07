#https://www.acmicpc.net/problem/2579

def stairs_up(l):
    length = len(l)
    position = 0
    counter = 0
    while position < len(l) - 3:
        forward_four = [l[position+1], l[position+2], l[position+3], l[position+4]]
        if forward_four[0] + forward_four[1] + forward_four[2] > 

