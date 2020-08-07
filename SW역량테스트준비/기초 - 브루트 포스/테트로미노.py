#https://www.acmicpc.net/problem/14500
import sys

NnM = list(map(int, sys.stdin.readline().split()))
N = NnM[0]
M = NnM[1]
coordin = {} #좌표 입력
for i in range(1, N+1):
    numbLine = list(map(int, sys.stdin.readline().split()))
    for j in range(1, M+1):
        coordin[(i, j)] = numbLine[j-1]

def tetromino1(coord):
    """
    ㅁㅁㅁㅁ
    """
    res = []
    #회전 안한 것
    for i in range(1, N + 1):
        for j in range(1, M - 3 + 1):
            res.append(coordin[(i, j)] + coordin[(i, j+1)] + coordin[(i, j+2)] + coordin[(i, j+3)])
    #회전 한 것
    for j in range(1, M + 1):
        for i in range(1, N - 3 + 1):
            res.append(coordin[(i, j)] + coordin[(i+1, j)] + coordin[(i+2, j)] + coordin[(i+3, j)])
    return max(res)

def tetromino2(coord):
    """
    ㅁㅁ
    ㅁㅁ
    """
    res = []
    for i in range(1, N - 1 + 1):
        for j in range(1, M - 1 + 1):
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)])
    return max(res)

def tetromino3(coord):
    res = []
    '''
    ㅁ
    ㅁ
    ㅁㅁ
    
      ㅁ
      ㅁ
    ㅁㅁ
    
    ㅁㅁ
      ㅁ
      ㅁ
      
    ㅁㅁ
    ㅁ
    ㅁ
    
    ㅁ
    ㅁㅁ
      ㅁ
      
      ㅁ
    ㅁㅁ
    ㅁ
    
      ㅁ
    ㅁㅁ
      ㅁ
      
    ㅁ
    ㅁㅁ
    ㅁ
    '''
    for i in range(1, N - 2 + 1):
        for j in range(1, M - 1 + 1):
            res.append(coordin[(i, j)] + coordin[(i + 1, j)] + coordin[(i + 2, j)] + coordin[(i + 2, j + 1)])
            res.append(coordin[(i, j + 1)] + coordin[(i + 1, j + 1)] + coordin[(i + 2, j)] + coordin[(i + 2, j + 1)])
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i + 1, j + 1)] + coordin[(i + 2, j + 1)])
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i + 1, j)] + coordin[(i + 2, j)])
            res.append(coordin[(i, j)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 2, j + 1)])
            res.append(coordin[(i, j + 1)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 2, j)])
            res.append(coordin[(i, j + 1)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 2, j + 1)])
            res.append(coordin[(i, j)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 2, j)])
    """
        ㅁ
    ㅁㅁㅁ
    
    ㅁ
    ㅁㅁㅁ
    
    ㅁㅁㅁ
    ㅁ
    
    ㅁㅁㅁ
       ㅁ
       
      ㅁㅁ
    ㅁㅁ
    
    ㅁㅁ
      ㅁㅁ
      
      ㅁ
    ㅁㅁㅁ
    
    ㅁㅁㅁ
      ㅁ
    """
    for i in range(1, N - 1 + 1):
        for j in range(1, M - 2 + 1):
            res.append(coordin[(i, j + 2)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 1, j + 2)])
            res.append(coordin[(i, j)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 1, j + 2)])
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i, j + 2)] + coordin[(i + 1, j)])
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i, j + 2)] + coordin[(i + 1, j + 2)])
            res.append(coordin[(i, j + 1)] + coordin[(i, j + 2)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)])
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i + 1, j + 1)] + coordin[(i + 1, j + 2)])
            res.append(coordin[(i, j + 1)] + coordin[(i + 1, j)] + coordin[(i + 1, j + 1)] + coordin[(i + 1, j + 2)])
            res.append(coordin[(i, j)] + coordin[(i, j + 1)] + coordin[(i, j + 2)] + coordin[(i + 1, j + 1)])
    return max(res)

print(max(tetromino1(coordin), tetromino2(coordin), tetromino3(coordin)))