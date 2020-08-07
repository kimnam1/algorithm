#https://www.acmicpc.net/problem/1333
import sys

# numbList = list(map(int, sys.stdin.readline().split()))

def missed_call2(n,l,d):
    tick = 0
    ringing = False
    singing = True
    ringingTick = 0
    singingTick = 0
    while True:
        if ringing and not singing:
            return tick
        else:
            #노래 나오는 시간
            if singingTick < l:
                singingTick += 1
                singing = True
            elif singingTick < l + 5:
                singingTick += 1
                singing = False
            else:
                singingTick = 0
                singing = True
            #전화 울리는 시간
            if ringingTick < d:
                ringingTick += 1
                ringing = False
            elif ringingTick == d:
                ringing = True
                ringingTick += 1
            else:
                ringing = False
                ringingTick = 0
        tick += 1
        if tick > n*l + 5*n:
            return tick

print(missed_call2(2, 5, 7))
