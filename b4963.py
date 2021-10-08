dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    field = [list(map(int, input().split())) for _ in range(h)]
    queue = [0] * w * h
    head = -1
    rear = -1

    cnt = 0
    for row in range(h):
        for col in range(w):
            if field[row][col]:
                field[row][col] = 0                
                cnt += 1
                rear += 1
                queue[rear] = (row, col)

                while head < rear:
                    head += 1
                    r, c = queue[head]
                    for to in range(8):
                        y = r + dy[to]
                        x = c + dx[to]
                        if 0 <= y < h and 0 <= x < w:
                            if field[y][x] == 1:
                                field[y][x] = 0
                                rear += 1
                                queue[rear] = (y, x)

    
    print(cnt)