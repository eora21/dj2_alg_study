adder = {0: (0, 0), 1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}


def DFS(stack):
    s = 0
    w = 0
    while stack:
        row, col = stack.pop(0)

        for arrow in range(5):
            y_adder, x_adder = adder[arrow]
            y = row + y_adder
            x = col + x_adder
            if 0 <= y < R and 0 <= x < C and field[y][x] != "#":
                if field[y][x] == "o":
                    s += 1
                    
                elif field[y][x] == "v":
                    w += 1

                field[y][x] = "#"
                stack.append((y, x))
        
    return (s, 0) if s > w else (0, w)


R, C = map(int, input().split())

field = [list(input()) for _ in range(R)]

sheep = 0
wolf = 0
for r in range(R):
    for c in range(C):
        if field[r][c] != "#":
            s, w = DFS([(r, c)])
            sheep += s
            wolf += w

print(sheep, wolf)