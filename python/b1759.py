aeiou = set(("a", "e", "i", "o", "u"))


def make_password(repeat=0, index=-1):
    global cnt
    if cnt > L - 2:
        return

    if repeat == L:
        if cnt > 0:
            print(''.join(li))
        return
    
    for i in range(index + 1, C):
        li.append(alp[i])
        if alp[i] in aeiou:
            cnt += 1
        make_password(repeat+1, i)
        if li.pop() in aeiou:
            cnt -= 1
    return


L, C = map(int, input().split())

alp = sorted(input().split())

li = []
cnt = 0

make_password()