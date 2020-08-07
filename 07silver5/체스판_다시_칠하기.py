# https://www.acmicpc.net/problem/1018

def colorchangecheck(a:list): # 8길이짜리 8줄 list 들어오면 w시작과 b시작으로 가장 작은 change값 return
    countstartW = 0
    countstartB = 0
    for i in range(8): # w로 시작하는 8*8로 만들기
        linenow = a[i]
        for j in range(8):
            charnow = linenow[j]
            if i % 2 == 0:
                if j % 2 == 0:
                    if charnow == "W":
                        pass
                    else:
                        countstartW += 1
                else:
                    if charnow == "W":
                        countstartW += 1
                    else:
                        pass
            else:
                if j % 2 == 1:
                    if charnow == "W":
                        pass
                    else:
                        countstartW += 1
                else:
                    if charnow == "W":
                        countstartW += 1
                    else:
                        pass
    for i in range(8): # b로 시작하는 체스판 만들기
        linenow = a[i]
        for j in range(8):
            charnow = linenow[j]
            if i % 2 == 0:
                if j % 2 == 0:
                    if charnow == "B":
                        pass
                    else:
                        countstartB += 1
                else:
                    if charnow == "B":
                        countstartB += 1
                    else:
                        pass
            else:
                if j % 2 == 1:
                    if j % 2 == 0:
                        if charnow == "B":
                            pass
                        else:
                            countstartB += 1
                    else:
                        if charnow == "B":
                            countstartB += 1
                        else:
                            pass
    return min(countstartB, countstartW)

def pickboard(m:int, n:int, a:list):
    ans = []
    



nm = input().split(' ')
checkerboard = []
for i in range(nm[0]):
    checkerboard.append(input())

chessboardcount = 0



