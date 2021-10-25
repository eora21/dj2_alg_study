from typing import Deque


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, Q = map(int, input().split())
size = 2 ** N
field = [list(map(int, input().split())) for _ in range(size)]
L = list(map(int, input().split()))

for magic in range(Q):
    fs = 2 ** L[magic]
    if fs > 1:
        rotate = [[0] * size for _ in range(size)]
        cnt = 0
        
        for r in range(0, size, fs):
            for c in range(0, size, fs):
                for row in range(r, r + fs):
                    for col in range(c, c + fs):
                        rotate[r + col - c][c + fs - 1 - (row - r)] = field[row][col]
        field = rotate

    melt = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if field[i][j] > 0:
                ice = 0
                for to in range(4):
                    y = i + dy[to]
                    x = j + dx[to]
                    if 0 <= y < size and 0 <= x < size and field[y][x] > 0:
                        ice += 1

                melt[i][j] = field[i][j] - 1 if ice < 3 else field[i][j]
    field = melt

queue = Deque()
check = [[True] * size for _ in range(size)]
total_ice = 0
max_link = 0
for i in range(size):
    for j in range(size):
        if check[i][j] and field[i][j] > 0:
            check[i][j] = False
            total_ice += field[i][j]
            link = 1
            queue.append((i, j))
            while queue:
                row, col = queue.popleft()
                for to in range(4):
                    y = row + dy[to]
                    x = col + dx[to]
                    if 0 <= y < size and 0 <= x < size and check[y][x] and field[y][x] > 0:
                        check[y][x] = False
                        total_ice += field[y][x]
                        link += 1
                        queue.append((y, x))
            if max_link < link:
                max_link = link
            
print(total_ice, '\n', max_link, sep="")