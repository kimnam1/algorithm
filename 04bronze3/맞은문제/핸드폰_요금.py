# https://www.acmicpc.net/problem/1267
import sys


def y_phone_bill(x):
    return (x // 30 + 1) * 10

def m_phone_bill(x):
    return (x // 60 + 1) * 15

N = int(sys.stdin.readline())
numbList = list(map(int, sys.stdin.readline().split()))
y_total = 0
m_total = 0
for i in range(N):
    y_total += y_phone_bill(numbList[i])
    m_total += m_phone_bill(numbList[i])

if y_total > m_total:
    print("M", m_total)
elif m_total > y_total:
    print("Y", y_total)
else:
    print("Y M", y_total)
