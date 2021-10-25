import sys
from typing import Deque
input = sys.stdin.readline

adder = [(-1, 0), (0, 1), (1, 0), (0, -1)]

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

tomatos = N * M
good_tomatos = 0
queue = Deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == -1:
            tomatos -= 1

        elif box[i][j] == 1:
            good_tomatos += 1
            queue.append((i, j))

day = 0
while queue:
    row, col = queue.popleft()
    for arrow in range(4):
        y_adder, x_adder = adder[arrow]
        y = row + y_adder
        x = col + x_adder

        if 0 <= y < N and 0 <= x < M and box[y][x] == 0:
            queue.append((y, x))
            box[y][x] = box[row][col] + 1
            good_tomatos += 1
            if day < box[row][col]:
                day = box[row][col]

print(day if tomatos == good_tomatos else -1)
