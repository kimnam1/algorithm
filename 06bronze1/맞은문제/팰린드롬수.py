#https://www.acmicpc.net/problem/1259

def palindromeNumber(n):
    nAsList = list(str(n))
    for i in range(len(nAsList)//2):
        ch1 = nAsList[i]
        ch2 = nAsList[-i-1]
        if nAsList[i] == nAsList[-i-1]:
            pass
        else:
            return "no"
    return 'yes'

numberList = []
while True:
    number = int(input())
    if number == 0:
        break
    else:
        numberList.append(number)

for i in range(len(numberList)):
    print(palindromeNumber(numberList[i]))