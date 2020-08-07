def findingfraction(n:int):
    nowlevel = 1

    level = 1
    while level < 5000:
        if ((level*(level-1)/2)+1) <= n < ((level*(level+1)/2)+1):
            nowlevel = level
            break
        else:
            level += 1

    if nowlevel % 2 == 0:
        son = n - ((level*(level-1)/2)+1) + 1
        mom = nowlevel + 1 - son
    else:
        mom = n - ((level*(level-1)/2)+1) + 1
        son = nowlevel + 1 - mom

    return f'{int(son)}/{int(mom)}'

print(findingfraction(int(input())))