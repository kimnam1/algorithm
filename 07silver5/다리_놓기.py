# https://www.acmicpc.net/problem/1010
import math

def bridge(a, b):
    bigsite = max(a, b)
    smallsite = min(a, b)
    diff = bigsite - smallsite
    space = smallsite + 1

    return space**diff/math.factorial(diff)

T = int(input())
for i in range(T):
    nums = list(map(int, input().split(' ')))
    N = nums[0]
    M = nums[1]
    print(bridge(N, M))