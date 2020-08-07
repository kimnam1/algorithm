#https://www.acmicpc.net/problem/2711
def misspellman(a:int, b:str):
    post = list(b)
    post[a-1] = ''
    return ''.join(post)

T = int(input())
testcase = []
for i in range(T):
    testcase.append(list(input().split(' ')))
for i in range(T):
    print(misspellman(int(testcase[i][0]), testcase[i][1]))