#https://www.acmicpc.net/problem/1110

def plusCycle(x:int):
    start = x
    cycleCount = 0
    now = start
    while True:
        if now < 10:
            now = now * 10 + now
            cycleCount += 1
            if now == start:
                break
        else:
            now = (now % 10) * 10 + ((now // 10 + now % 10) % 10)
            cycleCount += 1
            if now == start:
                break
    return cycleCount

print(plusCycle(int(input())))