op = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def BFS(color, is_normal):
    while queue:
        r, c = queue.pop(0)
        
        for arrow in range(4):
            y_adder, x_adder = op[arrow]
            y = r + y_adder
            x = c + x_adder

            if 0 <= y < N and 0 <= x < N and check[is_normal][y][x]:
                if is_normal:
                    if art[y][x] == color:
                        check[is_normal][y][x] = False
                        queue.append((y , x))
                else:
                    if not ((color == "B") ^ (art[y][x] == "B")):
                        check[is_normal][y][x] = False
                        queue.append((y , x))


N = int(input())
art = [input() for _ in range(N)]
check = [[[True] * N for _ in range(N)] for _ in range(2)]

queue = []

cnt = [0] * 2
for mode in range(2):
    for row in range(N):
        for col in range(N):
            if check[mode][row][col]:
                check[mode][row][col] = False
                queue.append((row , col))
                BFS(art[row][col], mode)
                cnt[1 - mode] += 1
            
print(*cnt)