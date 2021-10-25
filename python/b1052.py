N, K = map(int, input().split())

buy = 0
while True:
    cnt = 0
    place = -1
    for i in range(24):
        if (N + buy) & 1 << i:
            cnt += 1
            if place == -1:
                place = i

    if cnt <= K:
        print(buy)
        break
    else:
        buy += 2 ** place

