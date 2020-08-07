# https://www.acmicpc.net/problem/1246
import sys


def eggSeller(n:int, consumer:list): #n은 달걀 개수
    consumer.sort()
    maxPrice = 0
    maxPriceKey = 0
    if len(consumer) >= n:
        for i in range(-n, 0):
            price = (len(consumer[i:])*consumer[i])
            if price > maxPrice:
                maxPrice = price
                maxPriceKey = consumer[i]
            else:
                pass
    else:
        for i in range(len(consumer)):
            price = (len(consumer[i:])*consumer[i])
            if price > maxPrice:
                maxPrice = price
                maxPriceKey = consumer[i]
            else:
                pass
    return [maxPriceKey, maxPrice]

nm = list(map(int, sys.stdin.readline().split()))
consumerList = []
for i in range(nm[1]):
    consumerList.append(int(sys.stdin.readline().rstrip()))
ans = eggSeller(nm[0], consumerList)
print(ans[0], ans[1])