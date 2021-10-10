dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def larva():
    global head, tail
    while head < tail - 1:
        head += 1
        r, c = queue[head]
        for to in range(4):
            y = r + dy[to]
            x = c + dx[to]
            if 0 <= y < N and 0 <= x < M:
                if field[y][x] == 1:
                    field[y][x] = 0
                    queue[tail] = (y, x)
                    tail += 1


for case in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    queue = [0] * (M * N)
    head = -1
    tail = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    cnt = 0

    for row in range(N):
        for col in range(M):
            if field[row][col] == 1:
                field[row][col] = 0
                queue[tail] = (row, col)
                tail += 1
                larva()
                cnt += 1

    print(cnt)