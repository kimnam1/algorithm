#https://www.acmicpc.net/problem/1417
import sys

#값 받기
N = int(sys.stdin.readline())
vote = []#투표 예상 표 리스트
for i in range(N):
    vote.append(int(sys.stdin.readline()))

def senatorMaker(a:list):#투표 예상 값 받음
    candidNumb = len(a) #후보자 수
    totalVote = 0
    for i in range(candidNumb): # 전체 투표자 수
        totalVote += a[i]
    majority = totalVote//candidNumb + 1 # 과반수
    overMajorityAverage = 0 # 과반수 넘는 애들끼리 평균
    overMajorityCount = 0 # 과반수 넘는 애들 수
    for i in range(candidNumb):
        if a[i] >= majority:
            overMajorityAverage += a[i]
            overMajorityCount += 1
        else:
            pass
    overMajorityAverage = overMajorityAverage//overMajorityCount + 1

    movingCount = 0 # 총 움직이는 표 수
    for i in range(1, candidNumb):
        if a[i] >= overMajorityAverage:
            voteMoving = overMajorityAverage - a[0] # 움직이는 표 수
            a[i] -= voteMoving # 과반수보다 하나 작도록
            a[0] += voteMoving # 빠진만큼 0번째 애한테 더하기
            movingCount += voteMoving # 움직인만큼 카운트
        else:
            pass
    return movingCount

print(senatorMaker(vote))