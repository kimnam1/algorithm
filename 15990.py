import sys

t = int(sys.stdin.readline())
nList = []
for i in range(t):
    nList.append(int(sys.stdin.readline()))

ansList1 = [0, 1, 0, 1] + [0]*(max(nList)-3)
ansList2 = [0, 0, 1, 1] + [0]*(max(nList)-3)
ansList3 = [0, 0, 0, 1] + [0]*(max(nList)-3)

for i in range(4, max(nList)+1):
    ansList1[i] = (ansList2[i-1] + ansList3[i-1]) % 1000000009
    ansList2[i] = (ansList1[i-2] + ansList3[i-2]) % 1000000009
    ansList3[i] = (ansList1[i-3] + ansList2[i-3]) % 1000000009

for n in nList:
    print((ansList1[n] + ansList2[n] + ansList3[n])%1000000009)