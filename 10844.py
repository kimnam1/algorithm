import sys

n = int(sys.stdin.readline())

ansList0 = [0, 0] + [0]*(n-1)
ansList1 = [0, 1] + [0]*(n-1)
ansList2 = [0, 1] + [0]*(n-1)
ansList3 = [0, 1] + [0]*(n-1)
ansList4 = [0, 1] + [0]*(n-1)
ansList5 = [0, 1] + [0]*(n-1)
ansList6 = [0, 1] + [0]*(n-1)
ansList7 = [0, 1] + [0]*(n-1)
ansList8 = [0, 1] + [0]*(n-1)
ansList9 = [0, 1] + [0]*(n-1)

for i in range(2, n+1):
    ansList0[i] = ansList1[i-1] % 1000000000
    ansList1[i] = (ansList0[i-1] + ansList2[i-1]) % 1000000000
    ansList2[i] = (ansList1[i-1] + ansList3[i-1]) % 1000000000
    ansList3[i] = (ansList2[i-1] + ansList4[i-1]) % 1000000000
    ansList4[i] = (ansList3[i-1] + ansList5[i-1]) % 1000000000
    ansList5[i] = (ansList4[i-1] + ansList6[i-1]) % 1000000000
    ansList6[i] = (ansList5[i-1] + ansList7[i-1]) % 1000000000
    ansList7[i] = (ansList6[i-1] + ansList8[i-1]) % 1000000000
    ansList8[i] = (ansList7[i-1] + ansList9[i-1]) % 1000000000
    ansList9[i] = ansList8[i-1] % 1000000000


print((ansList0[n]+ansList1[n]+ansList2[n]+ansList3[n]+ansList4[n]+ansList5[n]+ansList6[n]+ansList7[n]+ansList8[n]+ansList9[n])%1000000000)