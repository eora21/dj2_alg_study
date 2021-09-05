def snowball(turn=0, i=-1, size=1):
    global max_size

    if turn == M or i == N - 1:
        if max_size < size: max_size = size
        return
    snowball(turn + 1, i+1, size + road[i+1])
    if i + 2 < N:
        snowball(turn + 1, i+2, size // 2 + road[i+2])
    return max_size

N, M = map(int, input().split())
road = list(map(int, input().split()))

max_size = 0

print(snowball())