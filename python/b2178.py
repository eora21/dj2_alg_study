y_adder = [-1, 0, 1, 0]
x_adder = [0, 1, 0, -1]

N, M = map(int, input().split())

field = [input() for _ in range(N)]
place = [[0] * M for _ in range(N)]

queue = [(0, 0)]
place[0][0] = 1
for row, col in queue:
    for w in range(4):
        y = row + y_adder[w]
        x = col + x_adder[w]

        if 0 <= y < N and 0 <= x < M and field[y][x] == "1" and place[y][x] == 0:
            place[y][x] = place[row][col] + 1
            queue.append((y, x))

    if place[N-1][M-1] != 0:
        print(place[N-1][M-1])
        break