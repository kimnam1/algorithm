#https://www.acmicpc.net/problem/1672

def dna_test(s:str):
    nowLength = len(s)
    res = s
    while len(s) != 1:
        if res[nowLength-2] == res[nowLength-1]:
            temp = res[nowLength-1]
            res.rstrip()
            res.rstrip()
            res = res + temp
        elif res[nowLength-2] == "A":
            if res[nowLength-1] == "G":
                res.strip()
                res.strip()
                res = s + "C"
            elif res[nowLength-1] == "C":
                res.rstrip()
                res.rstrip()
                res = res + "A"
            elif res[nowLength-1] == "T":
                res.rstrip()
                res.rstrip()
                res = res + "G"
        elif res[nowLength-2] == "G":
            if res[nowLength-1] == "A":
                res.rstrip()
                res.rstrip()
                res = res + "C"
            elif res[nowLength-1] == "C":
                res.rstrip()
                res.rstrip()
                res = res + "T"
            elif res[nowLength-1] == "T":
                res.rstrip()
                res.rstrip()
                res = res + "A"
        elif res[nowLength-2] == "C":
            if res[nowLength-1] == "A":
                res.rstrip()
                res.rstrip()
                res = res + "A"
            elif res[nowLength-1] == "G":
                res.
                res.strip()
                res = res + "T"
            elif res[nowLength-1] == "T":
                res.rstrip()
                res.rstrip()
                res = res + "G"
        elif res[nowLength-2] == "T":
            if res[nowLength-1] == "A":
                res.rstrip()
                res.rstrip()
                res = res + "G"
            elif res[nowLength-1] == "G":
                res.rstrip()
                res.rstrip()
                res = res + "A"
            elif res[nowLength-1] == "C":
                res.rstrip()
                res.rstrip()
                res = res + "G"
    return res

print(dna_test("AAGTCG"))