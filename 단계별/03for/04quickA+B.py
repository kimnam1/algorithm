import sys

testlengthstr = sys.stdin.readline()
testlng = int(testlengthstr)
for i in range(1, testlng+1):
    input = sys.stdin.readline().split(' ')
    a = int(input[0])
    b = int(input[1])
    print(a + b)