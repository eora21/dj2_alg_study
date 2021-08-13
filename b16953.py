A, B = map(int, input().split())

cnt = 1
while True:

    if A == B:
        break

    if B % 2 == 0:
        B = int(B / 2)
    elif B != 1 and str(B)[-1] == "1":
        B = int(str(B)[:-1])
    else:
        cnt = -1
        break

    cnt += 1

print(cnt)