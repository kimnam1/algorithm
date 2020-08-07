#https://www.acmicpc.net/problem/6603
#로또

import itertools
import sys

cases = []
inin = list(map(int, sys.stdin.readline().split()))
while inin != [0]:
    del inin[0]
    for i in itertools.combinations(inin, 6):
        print(" ".join(map(str, i)))
    print()
    inin = list(map(int, sys.stdin.readline().split()))