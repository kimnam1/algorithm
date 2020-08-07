# https://www.acmicpc.net/problem/1181

n = int(input()) # 단어 개수
wordlist = []
for i in range(n):
    wordlist.append(input())

wordlist = list(set(wordlist)) # 중복 단어 삭제

wordlist.sort(key=len) # 길이로 정렬


for i in range(len(wordlist)):
    print(wordlist[i])