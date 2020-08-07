'''자료구조 책 212쪽'''
'''stack 이용해서 문자열 반전'''

def reversing_str(s):
    origin = [c for c in s]
    res = []
    for i in range(len(origin)):
        res.append(origin.pop())
    return  "".join(res)

print(reversing_str("vkldslkneninsvosvdio"))