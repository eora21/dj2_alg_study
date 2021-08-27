N = int(input())

cards = [True] * N
ping = 0
cnt = False
while True:
    check = 0
    for i in range(N):
        if cards[i]:
            cnt = not cnt
            check += 1
            ping = i
            if cnt:
                cards[i] = False
    if check == 1:
        break

print(ping + 1)