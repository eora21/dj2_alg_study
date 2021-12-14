from typing import Deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS():
    while queue:
        r, c = queue.popleft()
        for to in range(4):
            y = r + dy[to]
            x = c + dx[to]

            if 0 <= y < N and 0 <= x < N and field[y][x] - h > 0 and check[y][x]:
                check[y][x] = False
                queue.append((y, x))


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

heights = set()
for i in range(N):
    heights |= set(field[i])

queue = Deque()
max_total = 1

for h in heights:
    check = [[True] * N for _ in range(N)]
    total = 0
    for row in range(N):
        for col in range(N):
            if field[row][col] - h > 0 and check[row][col]:
                check[row][col] = False
                queue.append((row, col))
                BFS()
                total += 1
    
    if max_total < total:
        max_total = total

print(max_total)