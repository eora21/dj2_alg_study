from typing import Deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
field = [list(map(int, input().rstrip("\n"))) for _ in range(N)]
check = [[[N * M + 1] * M for _ in range(N)] for _ in range(2)]

check[0][0][0] = 1
check[1][0][0] = 1

queue = Deque()
queue.append((0, 0, 1, 1))

while queue:
    row, col, step, power = queue.popleft()
    for to in range(0, 4):
        y = row + dy[to]
        x = col + dx[to]

        if 0 <= y < N and 0 <= x < M:
            if field[y][x] == 1 and power and check[0][y][x] > step + 1:
                check[0][y][x] = step + 1
                queue.append((y, x, step + 1, 0))

            elif field[y][x] == 0:
                if check[power][y][x] > step + 1:
                    check[power][y][x] = step + 1
                    queue.append((y, x, step + 1, power))

    if check[0][-1][-1] != N * M + 1 or check[1][-1][-1] != N * M + 1:
        print(min(check[0][-1][-1], check[1][-1][-1]))
        break
else:
    print(-1)
