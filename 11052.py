import sys

n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))

maxPrice = [price[0]]+[0 for i in range(n-1)]

def max_price_finder(x:int):
    global maxPrice, price, n
    ans = price[x]
    for i in range((x+1)//2):
        ans = max(ans, maxPrice[x-i-1] + maxPrice[i])
    return ans

for i in range(1, n):
    maxPrice[i] = max_price_finder(i)

print(maxPrice[n-1])