# https://www.acmicpc.net/problem/10974
import sys

ret = []

def recur(remain, result):
    if not remain:
        ret.append(" ".join(result))
    for i, item in enumerate(remain):
        remain.remove(item)
        recur(remain, result + item)
        remain.insert(i, item)

numbList = [str(i) for i in range(1, int(sys.stdin.readline())+1)]
recur(numbList, '')

for i in ret:
    print(i)