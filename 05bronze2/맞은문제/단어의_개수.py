#https://www.acmicpc.net/problem/1152
import sys

def word_counter(sentence:str):
    wordlist = sentence.split(' ')
    blank_cnt = 0
    for i in range(len(wordlist)):
        if wordlist[i] == "":
            blank_cnt =+ 1
        else:
            pass
    for i in range(blank_cnt):
        wordlist.remove('')
    return len(wordlist)

sentence = str(input())
print(word_counter(sentence))