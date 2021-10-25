A, B = map(int, input().split())

cnt = 1
while True:

    if A == B:
        break

    if B % 2 == 0:
        B //= 2
    elif B != 1 and B % 10 == 1:
        B //= 10
    else:
        cnt = -1
        break

    cnt += 1

print(cnt)