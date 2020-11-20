import sys

s = sys.stdin.readline().rstrip()

stack = []

for i in s:
    stack.append(i)

res = []
tag = ''
word = ''
tagOn = False

while stack:
    x = stack.pop()
    if tagOn:
        if x == '<':
            tag += x
            tagReverse = list(tag)
            tagReverse.reverse()
            res.append(''.join(tagReverse))
            tag = ''
            word = ''
            tagOn = False
        else:
            tag += x
    else:
        if x == ' ':
            res.append(word)
            res.append(' ')
            word = ''
        elif x == '>':
            if len(word) != 0:
                res.append(word)
                word = ''
            tag = ''
            tag += x
            tagOn = True
        else:
            word += x

if len(word) != 0:
    res.append(word)

res.reverse()
print(''.join(res))