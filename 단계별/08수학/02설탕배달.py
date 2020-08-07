def sugardelivery(a:int):
    pack5 = a // 5
    found = False
    while pack5 != -1:
        pack3 = 0
        if a == (3 * pack3) + (5 * pack5):
            found = True
            return pack3 + pack5
        else:
            while a > (3 * pack3) + (5 * pack5):
                pack3 += 1
                if a == (3 * pack3) + (5 * pack5):
                    found = True
                    return pack3 + pack5
                else:
                    pass
        pack5 -= 1

    if found == False:
        return -1

print(sugardelivery(int(input())))