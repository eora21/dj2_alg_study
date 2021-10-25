def muscle(step=0, m=0):
    if step == N:
        if m >= 0:
            global cnt
            cnt += 1
        return

    for i in range(N):
        if check[i]:
            check[i] = False
            if m - K + exercise[i] >= 0:
                muscle(step + 1, m - K + exercise[i])
            check[i] = True


N, K = map(int, input().split())
exercise = list(map(int, input().split()))
check = [True] * N
cnt = 0
muscle()

print(cnt)
