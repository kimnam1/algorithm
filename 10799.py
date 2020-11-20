import sys

stack = list(sys.stdin.readline())

stickCounter = 0
res = 0
pre = ''

while stack:
    cur = stack.pop()
    if cur == ')':
        stickCounter += 1
        pre = ')'
    elif cur == '(':
        stickCounter -= 1
        if pre == ')':
            res += stickCounter
        else:
            res += 1
        pre = '('

print(res)