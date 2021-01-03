import sys

n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))

minPrice = [price[0]]+[0 for i in range(n-1)]

def min_price_finder(x:int):
    global minPrice, price, n
    ans = price[x]
    for i in range((x+1)//2):
        ans = min(ans, minPrice[x-i-1] + minPrice[i])
    return ans

for i in range(1, n):
    minPrice[i] = min_price_finder(i)

print(minPrice[n-1])