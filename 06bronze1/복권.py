#https://www.acmicpc.net/problem/1359
import math
import sys


def nCr(n, r):
    return math.factorial(n) / math.factorial(r) / math.factorial(n - r)

def lotteryChance(n:int, m:int, k:int):
    myNumb = nCr(n, k)
    numbOfCase = 0
    for i in range(k, m+1):
        numbOfCase += nCr(myNumb, i) * nCr(n-i,m-i)
    return numbOfCase / (myNumb ** 2)

# numbList = list(map(int, sys.stdin.readline().split()))
print(lotteryChance(5, 4, 3))
# print(lotteryChance(numbList[0], numbList[1], numbList[2]))
